'''
Basic Gym environment for bike model race driving learning.
'''
from track_model.track import Track
from racegame.racegame_display import RacecarDisplay
from typing import List, Tuple, Dict
from .rewards.abstract_reward_function import DynamicModel
from .rewards.checkpoint_rewards import CheckpointReward, RewardFunciton
from .rewards.sdist_reward import SDistReward
from bike_learning.training_config import TrainingConfig
from dynmodels.bicycle_model import BicycleModel
from dynmodels.bicycle_model_v2 import BicycleModel2
from dynmodels.bicycle_model_v2_tvars import BicycleModel2Tvars
from dynmodels.bicycle_model_v3 import BicycleModel3
from dynmodels.bicycle_model_kin import KinematicBicycleModel
from dynmodels.vehicle_4w import Vehicle4W
from dynmodels.bicycle_model_kin import KinematicBicycleModel
from enum import Enum
from scipy import integrate
import itertools
import torch as th
import time
import gym
import json
import numpy as np
import pandas as pd
import os

class FinishState(Enum):
    too_slow: str = 'too slow'
    lost_control: str = 'spinning out of control'
    crash: str = 'contacted boundary'
    backwards: str = 'driven backwards'
    finished: str = 'finished track'
    not_final: str = 'no terminal state'
    max_time: str = 'maximal time exceeded'


class BoundCheckMode(Enum):
    VAR: str = 'var'
    GEOM: str = 'geom' 

class BikeModelTrack(gym.Env):

    '''
    Optimisation model for a bike on an ellipse.
    '''
    def __init__(self, track: Track, delta_t: float, disp_res:int, screen_render=False, params=None):
        super().__init__()
        #self.bikedyn = BicycleDynamics(params=params)
        #self.bikedyn.init_dynamics(use_jax=False)
        # self.model = NonLinearBicycleModel()
        self.model2 = BicycleModel2()
        self._ref_model = BicycleModel2Tvars()
        #
        self.disp_res: int = disp_res
        self.display = None
        self.render_to_screen: bool = screen_render
        self.render_to_file = False
        self.render_to_ram = False
        self.render_state_infos = False
        #
        self.reward_density: float = 0.2
        #
        self.track_rotation = []
        self.track_rotation.append(track)
        self.reward_func = None
        self.set_track(track)
        print('making bike model on track of length: {:.1f}'.format(self.track.get_length()))
        self.delta_t = delta_t
        self.time = 0.0
        self.time_max = 5.0*60 # 5.0 minutes time limit
        self.near_bound_factor: float = 0.01
        self._finish_tol: float = 1.0
        # Setup the display
        self.init_display(disp_res)
        # Define race track
        self.state: np.ndarray = None
        self.init_state(max_dist=0.0)
        self.max_cond_breaks: int = 20
        self.frame_idx: int = 0
        self.draw_infos = True
        self.randomise_timestep = False
        self.randomise_init: bool = False
        self._td_rand_fac: float = 0.1
        self._show_absolute_states: bool = True
        self._use_exact_step: bool = False
        self._time_penalty: float = 0.0
        self._use_discrete_actions: bool = False
        self._show_track_vars: bool = True
        self._uniform_actions: bool = True
        self._can_multilap: bool = True
        self._total_distance: float = 0.0
        self._train_config = None
        self._bound_check_mode = BoundCheckMode.GEOM.value
        num_cp = int(round(self.track.get_length() * self.reward_density))
        self.reward_func: RewardFunciton = CheckpointReward(self.model2, self.track, num=num_cp)
        self.reward_func.cp_reward = 1.0 / self.reward_density
        # refined time step to make integration more accurate.
        self.split_timestep: int = 1
        self.verbose = False
        self.init_obs_act_spaces()
        self._record_solution: bool = True
        self.traj = []
        # self.pbar = tqdm.tqdm() 
        self.finish_state: FinishState = FinishState.not_final

    def add_track(self, track: Track):
        if not (track in self.track_rotation):
            self.track_rotation.append(track)

    def load_train_config(self, train_config: TrainingConfig):
        self._train_config = train_config
        # Load the reward function
        self._load_reward_config(train_config)
        # Load the model config
        self._load_physics_config(train_config)
        # Setup the bound checks
        self._bound_check_mode = train_config.bound_check_method
        self._show_track_vars = train_config.show_track_vars

    def _load_physics_config(self, train_config: TrainingConfig):
        print('Loading physics:', train_config.physics_name)
        if train_config.physics_name == 'bicycle_model_v2':
            self.model2 = BicycleModel2()
        elif train_config.physics_name == 'bicycle_model_v2_trackvars':
            self.model2 = BicycleModel2Tvars()
            self.model2.set_track(self.track)
        elif train_config.physics_name == 'bicycle_model_v1':
            self.model2 = BicycleModel()
            self.model2.set_track(self.track)
        else:
            print('\tunsupported physics:', train_config.physics_name)
        

    def _load_reward_config(self, train_config: TrainingConfig):
        if train_config.use_checkpoint_rewards:
            self.reward_density = train_config.reward_density
            num_cp = int(round(self.track.get_length() * self.reward_density))
            self.reward_func: RewardFunciton = CheckpointReward(self.model2, self.track, num=num_cp)
            # reward scale is 0.1
            reward_value = 0.1 / self.reward_density
            reward_dist = self.track.get_length() / num_cp
            self.reward_func.cp_reward = reward_value
            msg = '\t{} Checkpoints [{} reward every {} meters]'
            msg = msg.format(num_cp, reward_value, reward_dist)
            print(msg)
        else:
            # Use S-dist rewards
            self.reward_func: RewardFunciton = SDistReward(self.model2, self.track)

    def set_discrete_actions(self):
        self._use_discrete_actions = True
        throttle_num: int = 3
        steer_num: int = 3
        tmin, tmax = self.model2.throttle.get_bounds()
        smin, smax = self.model2.steer_angle.get_bounds()
        throttle_range = np.linspace(tmin, tmax, throttle_num)
        steer_range = np.linspace(smin, smax, throttle_num)
        self.num_actions: int = throttle_num * steer_num
        self.action_scale = np.zeros((self.num_actions, 2))
        for idx, (tval, sval) in enumerate(itertools.product(throttle_range, steer_range)):
            self.action_scale[idx, :] = np.array([tval, sval])
        self.action_space = gym.spaces.Discrete(self.num_actions)

    def get_obs_bounds(self):
        # State names:
        # pos_x, pos_y, yaw, v_x, v_y, omega, s_dist, nu, xi
        used_bounds = []
        pos_x_bounds = [-10_000.0, +10_000.0]
        pos_y_bounds = [-10_000.0, +10_000.0]
        yaw_bounds = [-10.0, +10.0]
        vx_bounds = [-10.0, +100.0]
        vy_bounds = [-20.0, +20.0]
        omega_bounds = [-10.0, +10.0]
        s_dist_bounds = [-10_000.0, +10_000.0]
        nu_bounds = [-50.0, +50.0]
        xi_bounds = [-10.0, +10.0]
        # Update: 2022_08_07 -> Always show track variables,
        # if they are not available directly in the model we extract
        # the track variables from our track position.
        if self._show_absolute_states:
            used_bounds.append(pos_x_bounds)
            used_bounds.append(pos_y_bounds)
            used_bounds.append(yaw_bounds)
            used_bounds.append(vx_bounds)
            used_bounds.append(vy_bounds)
            used_bounds.append(omega_bounds)
            if self._show_track_vars:
                used_bounds.append(s_dist_bounds)
                used_bounds.append(nu_bounds)
                used_bounds.append(xi_bounds)
        else:
            used_bounds.append(yaw_bounds)
            used_bounds.append(vx_bounds)
            used_bounds.append(vy_bounds)
            used_bounds.append(omega_bounds)
            if self._show_track_vars:
                used_bounds.append(nu_bounds)
                used_bounds.append(xi_bounds)
        return used_bounds

    def init_obs_space(self):
        self.observation_space = self.get_obs_space()

    def get_obs_space(self):
        bounds = self.get_obs_bounds()
        min_states, max_states = zip(*bounds)
        self.min_states = list(min_states)
        self.max_states = list(max_states)
        min_states = np.array(self.min_states, dtype=np.float32)
        max_states = np.array(self.max_states, dtype=np.float32)
        return gym.spaces.Box(min_states, max_states)

    def init_act_space(self):
        # Setup model parameters
        self.action_bounds = np.zeros((2, 2))
        #for cvar in self.bikedyn.get_ctrls_vars():
        #    idx = cvar.get_idx()
        #    self.action_bounds[idx, :] = cvar.get_action_bounds()
        self.action_bounds = np.zeros((self.model2.get_num_controls(), 2))
        for var in [self.model2.throttle, self.model2.steer_angle]:
            self.action_bounds[var.get_idx(), :] = var.get_bounds()
        if self._uniform_actions:
            bound_mtx = np.zeros((2, 2))
            bound_mtx[:, 0] = 0.0
            bound_mtx[:, 1] = 1.0
        else:
            bound_mtx = self.action_bounds
        self.min_actions = np.array(bound_mtx[:, 0], dtype=np.float32)
        self.max_actions = np.array(bound_mtx[:, 1], dtype=np.float32)
        # Define state and action spaces
        self.action_space = gym.spaces.Box(self.min_actions, self.max_actions)

    def init_obs_act_spaces(self):
        self.init_obs_space()
        self.init_act_space()

    def init_display(self, res:int):
        '''
        Setup the display
        '''
        if res <= 0:
            print('Resolution is negative, not initializing display')
            self.display = None
            self.frame_idx: int = 0
        else:
            if self.render_to_screen:
                os.environ["SDL_VIDEODRIVER"] = "X11"
            else:
                os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.display = RacecarDisplay(self.track, res)
            self.frame_idx: int = 0
        # Make environment difficult / slow to run, for debugging only.
        # or for presentation purposes of course :)
        self.render_to_file = False

    def init_secondary_display(self, res: int):
        self.second_display = RacecarDisplay(self.track, res)
        self.has_second_display = True

    def set_render_to_file(self, render: bool):
        self.render_to_file = render

    def init_state(self, min_dist=5.0, max_dist=5.0):
        '''
        Initialise a state vector
        '''
        #num_states = len(self.bikedyn.get_state_vars())
        #self.state_vec = np.zeros(num_states, dtype=np.float32)
        #self.state_vec[self.x_vel_idx] = 1.0
        s_dist = np.random.uniform(min_dist, max_dist)
        # s_dist = np.random.uniform(0.0, max_dist*self.track.get_length())
        self.start_position = s_dist
        init_pos = self.track.get_point(s_dist)
        x_pos, y_pos = init_pos.get_position().as_tuple()
        orientation = init_pos.get_orientation()
        # Reset the progress along the track center line:
        state_vals = np.zeros(self.model2.get_num_states())
        state_vals[self.model2.x.get_idx()] = init_pos.get_position().get_x()
        state_vals[self.model2.y.get_idx()] = init_pos.get_position().get_y()
        state_vals[self.model2.yaw.get_idx()] = init_pos.get_orientation()
        state_vals[self.model2.vx.get_idx()] = 10.0
        state_vals[self.model2.vy.get_idx()] = 0.0
        state_vals[self.model2.omega.get_idx()] = 0.0
        if self.has_model_tvars():
            state_vals[self.model2.s_dist.get_idx()] = s_dist
            state_vals[self.model2.nu_dist.get_idx()] = 0.0
            state_vals[self.model2.xi_angle.get_idx()] = 0.0
        #self.state = th.tensor(state_vals, requires_grad=False)
        self.state = state_vals

    def get_velocity(self) -> float:
        xvel = self.model2.vx.valf(self.state)
        yvel = self.model2.vy.valf(self.state)
        varr = np.array([xvel, yvel])
        return np.linalg.norm(varr)

    def get_velocity_vec(self) -> np.ndarray:
        return np.array([self.model2.vx.valf(self.state), self.model2.vy.valf(self.state)])

    def get_track_aligned_vel(self) -> float:
        dist = self.model2.s_dist.valf(self.state)
        track_vec = self.track.get_point(dist).get_direction().as_np()
        vel_vec = self.get_velocity_vec()
        return np.dot(track_vec, vel_vec)

    def get_centerline_distance(self) -> float:
        return self.get_sdist()

    def get_nu_distance(self) -> float:
        if self.has_model_tvars():
            return self.model2.nu_dist.valf(self.state)
        else:
            px, py = self.state[0:2]
            return self.track.get_nudist(px, py)

    def get_xi_angle(self) -> float:
        if self.has_model_tvars():
            return self.model2.xi_angle.valf(self.state)
        else:
            s_dist = self.get_sdist()
            track_angle = self.track.get_point(s_dist).get_orientation()
            yaw = self.model2.yaw.valf(self.state)
            return yaw - track_angle

    def get_display_info(self):
        '''
        Compute a dictionary of items to display on screen
        while rendering.
        '''
        out = {}
        out['time'] = '{:2.2f}'.format(self.time)
        out['velocity'] =  '{:2.2f}'.format(self.get_velocity())
        out['dist driven'] = '{:2.2f}'.format(self.get_centerline_distance())
        out['nu_val'] = '{:2.2f}'.format(self.get_nu_distance())
        out['model name'] = self.model2.get_model_name()
        return out

    def set_time_rand_fac(self, fac: float):
        self._td_rand_fac = fac
        print('Set time randomisation to {:2.4f}'.format(fac))

    def sample_dt(self):
        '''
        Sample a timestep in dt * (1 + Unif[_td_rand_fac, _td_rand_fac])
        '''
        if self.randomise_timestep:
            rand_num = 2.0 * np.random.rand() - 1.0
            cur_dt = (1.0 + self._td_rand_fac * rand_num) * self.delta_t
        else:
            cur_dt = self.delta_t
        return cur_dt

    def get_curvature(self) -> float:
        s_dist = self.get_sdist()
        return self.track.get_curvature(s_dist)

    def update_state(self, action_raw, delta_t: float) -> np.ndarray:
        '''
        Update the state vector by a single time step.
        '''
        num_states = self.model2.get_num_states()
        out_arr = np.zeros((self.split_timestep, num_states))
        delta_t = self.delta_t / self.split_timestep
        for k in range(self.split_timestep):
            out_arr[k, :] = self.update_state_sub(action_raw, delta_t).flatten()
        t1 = time.time()
        return np.sum(out_arr, axis=0)

    def step_exact(self, action, delta_t: float) -> np.ndarray:
        '''
        Step with exact states
        '''
        old_state = np.copy(self.state)
        y_old = np.copy(self.state)
        # Integrate ODE
        def dfunc(state, time):
            ns = state.shape[0]
            na = action.shape[0]
            state_th = th.tensor(state).reshape(1, ns)
            action_th = th.tensor(action).reshape(1, na)
            state_update = self.model2.forward_noparam(state_th, action_th).detach().numpy().ravel()
            return state_update
        tarr = [self.time, self.time + self.delta_t]
        y_new = integrate.odeint(dfunc, y_old, tarr)
        self.state = y_new[-1, :]
        return y_old - y_new

    def update_state_sub(self, action: th.Tensor, delta_t: float) -> np.ndarray:
        #s_dist = self.get_sdist()
        #tpoint = self.track.get_point(s_dist)
        #tangle = tpoint.get_orientation()
        #tcurve = self.get_curvature()
        #
        action_th = th.tensor(action, requires_grad=False)
        state_mtx = th.zeros((1, self.model2.num_states))
        state_mtx[0, :] = th.tensor(self.state)
        action_mtx = th.zeros((1, self.model2.num_controls))
        action_mtx[0, :] = action_th.detach()
        t0 = time.time()
        state_delta = self.model2.forward_noparam(state_mtx, action_mtx)
        t1 = time.time()
        if self.verbose:
            print('\tT[model_forward]={:e}'.format(t1 - t0))
        self.state += delta_t * state_delta.detach().numpy().flatten()
        return delta_t * state_delta.detach().numpy()

    def update_total_distance(self, old_sdist, new_sdist):
        '''
        update the total distance variable.
        '''
        tlen = self.track.get_length()
        if new_sdist is None or np.isnan(new_sdist):
            return
        if old_sdist is None or np.isnan(old_sdist):
            return
        old_last_elem = (old_sdist >= tlen * 0.95) and (old_sdist < 1.0*tlen)
        new_first_elem = (new_sdist >= 0.0*tlen) and (new_sdist <= 0.05*tlen)
        new_lap = old_last_elem and new_first_elem
        s_update = new_sdist - old_sdist
        if new_lap: 
            print('Finished lap!')
            s_update += tlen
        self._total_distance += s_update
        #print('s: {}, sold: {}, snew: {}'.format(self._total_distance, old_sdist, new_sdist))

    def scale_actions(self, action_raw):
        min_act = self.action_bounds[:, 0]
        max_act = self.action_bounds[:, 1]
        action_scaled = min_act + action_raw * (max_act - min_act)
        return action_scaled

    def step(self, action_raw, other_cars=None):
        '''
        Proceed with one step of explicit euler.
        '''
        old_state = np.copy(self.state)
        old_sdist = self.get_sdist()
        t0 = time.time()
        action_scaled = self.scale_actions(action_raw)
        if self._use_discrete_actions:
            action_scaled = self.action_scale[action_raw, :]
        # Store the current state and action
        if self._record_solution:
            self._store_state(self.state, action_scaled, self.time)
        old_state = np.copy(self.state)
        if self._use_exact_step:
            delta_vec = self.step_exact(action_scaled, self.delta_t)
        else:
            delta_vec = self.update_state(action_scaled, self.delta_t)
        self.time += self.delta_t
        # compute reward, observation, and done
        new_state = np.copy(self.state)
        new_sdist = self.get_sdist()
        self.update_total_distance(old_sdist, new_sdist)
        reward, done = self.compute_rew_done(new_state, old_state)
        infos = {}
        if done:
            #old_sdist = self.track.get_sdist(old_state[0], old_state[1])
            infos['final_dist'] = self._total_distance
        # update the display before collecting the new observation,
        # so that new data shows up in the updated observation.
        t1 = time.time()
        if self.verbose:
            print('\tT[step]={:e}'.format(t1 - t0))
        self._step_callback(action_scaled, delta_vec)
        if self.render_to_screen or self.render_to_ram or self.render_to_file:
            self.render(other_cars=other_cars)
        # collect new observation data.
        observation = self.observe()
        return observation, reward, done, infos

    def _store_state(self, state, action, time):
        '''
        Add current state to trajectory
        '''
        my_dict = {}
        for var in self.model2.states:
            val = float(state[var.get_idx()])
            my_dict[var.get_name()] = val
        for var in self.model2.ctrls:
            val = float(action[var.get_idx()])
            my_dict[var.get_name()] = val
        s_dist = self.get_sdist()
        s_dist = s_dist if s_dist is not None else 0.0
        # Record track variables
        px, py = self.state[self.model2.x.get_idx()], self.state[self.model2.y.get_idx()]
        yaw = self.state[self.model2.yaw.get_idx()]
        my_dict['s'] = self._total_distance
        my_dict['nu'] = self.track.get_nudist(px, py)
        my_dict['xi_angle'] = self.track.get_xi_angle(px, py, yaw)
        my_dict['time'] = time
        self.traj.append(my_dict)

    def _step_callback(self, action, delta_vec):
        pass

    def passed_start(self, old_sdist, new_sdist):
        tlen = self.track.get_length()
        old_last_elem = (old_sdist >= tlen * 0.95) and (old_sdist < 1.0*tlen)
        new_first_elem = (new_sdist >= 0.0*tlen) and (new_sdist <= 0.05*tlen)
        new_lap = old_last_elem and new_first_elem
        return new_lap

    def compute_rew_done(self, new_state, old_state):
        is_done = self.check_done()
        reward_raw = self.reward_func(new_state, old_state)
        if self._bound_check_mode == BoundCheckMode.GEOM.value:
            # Use geometric track position
            old_x, old_y = old_state[[self.model2.x.get_idx(), self.model2.y.get_idx()]]
            new_x, new_y = new_state[[self.model2.x.get_idx(), self.model2.y.get_idx()]]
            old_s = self.track.get_sdist(old_x, old_y)
            new_s = self.track.get_sdist(new_x, new_y)
        elif self._bound_check_mode == BoundCheckMode.VAR.value:
            # This method should no longer be used:
            # raise ValueError('Variable bound check method is often unstable')
            # Use track variables
            s_idx = self.model2.s_dist.get_idx()
            new_s, old_s = new_state[s_idx], old_state[s_idx]
        else:
            raise ValueError('Unknown boundary check method:', self._bound_check_mode)
        if is_done:
            tot_rew = self.reward_func.total_reward
            tot_dist = self._total_distance
            msg = self.finish_state.value
            print('[{}]:\t D={:2.2f}, R={:2.2f}, T={:2.2f}'.format(msg, tot_dist, tot_rew, self.time))
        elif self.passed_start(old_s, new_s):
            print('Completed lap')
            if not self._can_multilap:
                # Environment is not allowed to drive multiple laps
                is_done = True
        return reward_raw, is_done

    def checkpoint_rewards(self, new_state, old_state):
        '''
        @todo: modify to allow for passing laps
        '''
        s_dist = self.track.get_sdist(new_state[0], new_state[1])
        reward = 0.0
        if s_dist is not None:
            self.cp_hit[self.cp_pos<=s_dist] = True
            new_num = np.sum(self.cp_hit)
            if new_num > self.num_cp_hit:
                last_cp = self.cp_pos[self.cp_hit][-1]
                reward = 1.0
                self.num_cp_hit = new_num
                print('Crossed checkpoint at {:2.2f}'.format(last_cp))
        reward = reward - self.delta_t * self._time_penalty
        return reward, self.check_done()

    def classical_rewards(self, new_state, old_state):
        sdist0 = self.track.get_sdist(old_state[0], old_state[1])
        sdist1 = self.track.get_sdist(new_state[0], new_state[1])
        delta_s_reward = sdist1 - sdist0
        # no time penalty right now.
        reward = delta_s_reward - self.delta_t * self._time_penalty
        #reward = delta_s_reward  - self.delta_t * self.time_cost_factor
        is_done = self.check_done()
        fail_pen: float = -1.0
        win_rew: float = +100.0
        near_crash_pen: float = -0.1
        if self.touch_left():
            reward += fail_pen
        if self.touch_right():
            reward += fail_pen
        if self.driving_slow():
            reward += fail_pen
        if self.driven_backwards(sdist1):
            reward += fail_pen
        # Add cost for being close to the boundary
        if self.has_model_tvars():
            nu_dist = self.model2.nu_dist.valf(self.state)
        else:
            px, py = self.state[0:2]
            nu_dist = self.track.get_nudist(px, py)
        width = self.track.get_width()
        bound_dist = 0.5*width - abs(nu_dist)
        bound_dist_scaled = max(0.01, bound_dist / (0.5*width))
        bound_cost = np.log(bound_dist_scaled)
        reward += self.delta_t * self.near_bound_factor * bound_cost
        return reward, is_done

    def check_done(self):
        idx_x = self.model2.x.get_idx()
        idx_y = self.model2.y.get_idx()
        yaw = self.state[self.model2.yaw.get_idx()]
        s_dist = self.get_sdist()
        pos = self.state[[idx_x, idx_y]]
        if not self.check_on_track() or s_dist is None:
            if self.verbose:
                print('vehicle is not on track')
            if self._total_distance >= 0.99 * self.track.get_length():
                self.finish_state = FinishState.finished
            else:
                self.finish_state = FinishState.crash
            return True
        if self.driving_slow():
            if self.verbose:
                print('vehicle too slow')
            self.finish_state = FinishState.too_slow
            return True
        if self.lost_control():
            if self.verbose:
                print('lost vehicle control')
            self.finish_state = FinishState.lost_control
            return True
        if self.driven_backwards(s_dist):
            if self.verbose:
                print('driven backwards')
            self.finish_state = FinishState.backwards
            return True
        if self.wrong_direction():
            if self.verbose:
                print('facing wrong direction')
            self.finish_state = FinishState.lost_control
            return True
        if self.time >= self.time_max:
            if self.verbose:
                print('maximal time exceeded')
            self.finish_state = FinishState.max_time
            return True
        return False

    def check_on_track(self):
        if self._bound_check_mode == BoundCheckMode.GEOM.value:
            # Use geometry bound check
            pos = self.state[[self.model2.x.get_idx(), self.model2.y.get_idx()]]
            return self.track.on_track(pos)
        elif self._bound_check_mode == BoundCheckMode.VAR.value:
            nu_dist = self.state[self.model2.nu_dist.get_idx()]
            s_dist = self.state[self.model2.s_dist.get_idx()]
            nu_cond = abs(nu_dist) <= self.track.get_width()*0.5
            s_cond = self._can_multilap or (s_dist <= self.track.get_length())
            return (nu_cond and s_cond)
        else:
            raise ValueError('Unexpected bound_check_method: ', self._bound_check_mode)

    def near_left(self) -> bool:
        track_w = self.track.get_width()
        nu_pos = self.model2.nu_dist.valf(self.state)
        return nu_pos > 0.4*track_w

    def near_right(self) -> bool:
        track_w = self.track.get_width()
        nu_pos = self.model2.nu_dist.valf(self.state)
        return nu_pos < -0.4*track_w

    def touch_left(self) -> bool:
        track_w = self.track.get_width()
        nu_pos = self.model2.nu_dist.valf(self.state)
        return nu_pos > 0.5*track_w

    def touch_right(self) -> bool:
        track_w = self.track.get_width()
        nu_pos = self.model2.nu_dist.valf(self.state)
        return nu_pos < -0.5*track_w

    def driving_slow(self) -> bool:
        x_vel = self.model2.vx.valf(self.state)
        y_vel = self.model2.vy.valf(self.state)
        min_speed = 0.5
        return (x_vel*x_vel) + (y_vel*y_vel) < min_speed*min_speed

    def lost_control(self) -> bool:
        # Check if vehicle is spinning out of control
        # A whole spin per second means loss of control
        yaw_rate = self.model2.omega.valf(self.state)
        return abs(yaw_rate) > 2.0*np.pi

    def wrong_direction(self) -> bool:
        sdist = self.get_sdist()
        if sdist is None:
            return True
        tpos = self.track.get_point(sdist)
        if tpos is None:
            return True
        tdir = tpos.get_direction().as_np()
        yaw = self.model2.yaw.valf(self.state)
        ydir = np.array([np.cos(yaw), np.sin(yaw)])
        prod = np.dot(tdir, ydir) / np.linalg.norm(ydir)
        vx = self.model2.vx.valf(self.state)
        vy = self.model2.vy.valf(self.state)
        if prod < -0.5:
            # Vehicle is pointing in the wrong direction
            return True
        if vx < 0.0:
            # Vehicle is driving in the wrong direction
            return True
        return prod < 0.0

    def track_finished(self) -> bool:
        s_dist = self.get_sdist()
        track_len = self.track.get_length()
        is_finished = False
        if s_dist is not None:
            is_finished = (s_dist >= track_len - self._finish_tol)
        return is_finished

    def driven_backwards(self, s_dist) -> bool:
        return s_dist <= self.start_position -1e-8

    def set_state(self, state: th.Tensor):
        self.state = th.tensor(state, requires_grad=True)

    def get_state(self) -> np.ndarray:
        '''
        Get a copy of the internal state vector.
        '''
        return np.copy(self.state)

    def get_state_with_tvars(self) -> np.ndarray:
        if self.has_model_tvars():
            return np.copy(self.state)
        ix = self.model2.x.get_idx()
        iy = self.model2.y.get_idx()
        iyaw = self.model2.yaw.get_idx()
        px, py, yaw = self.state[[ix, iy, iyaw]]
        s_dist = self.track.get_sdist(px, py)
        nu = self.track.get_nudist(px, py)
        xi = self.track.get_xi_angle(px, py, yaw)
        tvars = np.array([s_dist, nu, xi])
        # Determine track variables
        state_copy = np.copy(self.state)
        return np.concatenate([state_copy, tvars])

    def set_rand_state(self, s_dist: float, nu_dist: float):
        '''
        Initialise the vehicle to a randomised position.
        '''
        angle_range = [np.deg2rad(-30.0), np.deg2rad(+30.0)]
        velx_range = [1.0, 30.0]
        vely_range = [-3.0, +3.0]
        angle_val = angle_range[0] + (angle_range[1] - angle_range[0])*np.random.rand()
        velx_val = velx_range[0] + (velx_range[1] - velx_range[0])*np.random.rand()
        vely_val = vely_range[0] + (vely_range[1] - vely_range[0])*np.random.rand()
        state_np = self.get_state()
        pos = self.track.get_position(s_dist, nu_dist).as_np()
        track_angle = self.track.get_point(s_dist).get_orientation()
        state_np[self.model2.x.get_idx()] = pos[0]
        state_np[self.model2.y.get_idx()] = pos[1]
        state_np[self.model2.vx.get_idx()] = velx_val
        state_np[self.model2.vy.get_idx()] = vely_val
        state_np[self.model2.yaw.get_idx()] = track_angle + angle_val
        state_np[self.model2.omega.get_idx()] = 0.0
        #
        if isinstance(self.model2, BicycleModel):
            state_np[self.model2.nu_dist.get_idx()] = nu_dist
            state_np[self.model2.s_dist.get_idx()] = s_dist
            state_np[self.model2.xi_angle.get_idx()] = angle_val
        self.state = state_np

    def get_sdist(self):
        if isinstance(self.model2, BicycleModel):
            return self.model2.s_dist.valf(self.state)
        elif isinstance(self.model2, BicycleModel2Tvars):
            return self.model2.s_dist.valf(self.state)
        else:
            px, py = self.state[0:2]
            sdist = self.track.get_sdist(px, py)
            return sdist

    def set_track(self, track: Track):
        self.track = track
        if isinstance(self.model2, BicycleModel):
            self.model2.set_track(self.track)
        if self.display is not None:
            self.display.load_track(self.track)
        tlen = track.get_length()
        print('Loaded track of length {:2.2f}'.format(tlen))
        if isinstance(self.reward_func, CheckpointReward):
            num_cp = int(round(self.track.get_length() * self.reward_density))
            self.reward_func: RewardFunciton = CheckpointReward(self.model2, self.track, num=num_cp)
            self.reward_func.cp_reward = 0.1 / self.reward_density

    def reset(self, init_dist=0.0, print_dist=True):
        '''
        Reset variables to initial start position
        '''
        s_dist = 0.0
        self.reward_func.reset()
        self.traj = []
        # Select a random track
        num_tracks = len(self.track_rotation)
        rand_idx = np.random.randint(num_tracks)
        new_track = self.track_rotation[rand_idx]
        self.set_track(new_track)
        self.init_state(init_dist, init_dist)
        if self.randomise_init:
            s_dist = self.track.get_length() * np.random.rand()
            nu_dist = self.track.get_width() * np.random.rand()
            nu_dist -= 0.5 *self.track.get_width()
            self.set_rand_state(s_dist, nu_dist)
            self.start_position = s_dist
        self._total_distance: float = 0.0
        self.time = 0.0
        self.frame_idx = 0
        self.finish_state: FinishState = FinishState.not_final
        if self.render_to_ram:
            self.render()
        return self.observe()

    def has_model_tvars(self):
        if isinstance(self.model2, BicycleModel2):
            return False
        elif isinstance(self.model2, BicycleModel):
            return True
        elif isinstance(self.model2, BicycleModel2Tvars):
            return True
        else:
            raise ValueError('unknown physics model')

    def _get_observation(self, state_vec: th.tensor):
        '''
        Get observation of each state component.
        Provide one state vector per row of the state_vector.
        '''
        num_raw_obs = state_vec.shape[1]
        selected_indices = np.arange(self._ref_model.get_num_states())
        # insert the track variables if they are not currently present:
        # If we do not have state indices, then we need to append
        # s_dist, nu, xi
        # to the state tensor
        if self._show_track_vars and (not self.has_model_tvars()):
            num_rows = state_vec.shape[0]
            add_tensor = th.zeros((num_rows, 3), dtype=state_vec.dtype, device=state_vec.device)
            for ridx in range(state_vec.shape[0]):    
                px, py = state_vec[ridx, 0:2]
                yaw = state_vec[ridx, self.model2.yaw.get_idx()]
                sdist = self.track.get_sdist(px, py)
                nu = self.track.get_nudist(px, py)
                xi = self.track.get_xi_angle(px, py, yaw)
                if sdist is None or nu is None or xi is None:
                    raise ValueError('was not able to evaluate the track position exactly')
                add_tensor[ridx, 0] = sdist
                add_tensor[ridx, 1] = nu
                add_tensor[ridx, 2] = xi
            state_vec = th.concat([state_vec, add_tensor], axis=1)
        if not self._show_track_vars:
            # Remove track variables from observation
            selected_indices = np.arange(6)
        if not self._show_absolute_states:
            del_vars = [self._ref_model.x, self._ref_model.y, self._ref_model.s_dist]
            del_idxs = [v.get_idx() for v in del_vars]
            selected_indices = np.delete(selected_indices, del_idxs)
        return state_vec[:, selected_indices]
                
    def observe(self):
        t0 = time.time()
        states = th.tensor(self.state[None, :])
        obs = self._get_observation(states)
        t1 = time.time()
        if self.verbose:
            print('\tT[observation]={:e}'.format(t1 - t0))
        return obs[0, :]

    def get_state_infos(self) -> Dict[str, float]:
        '''
        Get an information dict of the current state
        '''
        out_dict = {}
        for var in self.model2.states:
            out_dict[var.get_name()] = self.state[var.get_idx()]
        # Get the track angle and curvature
        pos = self.get_sdist()
        tpoint = self.track.get_point(pos)
        out_dict['track angle'] = tpoint.get_orientation()
        out_dict['track curve'] = tpoint.get_curvature()
        return out_dict

    def render(self, mode='machine', infos=None, other_cars=None):
        '''
        Render scene and flip display, mode is not used for anything.
        '''
        t0 = time.time()
        if self.display is None:
            return
        self.render_scene(infos=infos)
        # Render other cars if available
        if other_cars is not None:
            for px, py, yaw in other_cars:
                self.display.render_car(px, py, yaw, is_other=True)
        self.display.flip()
        # Create a list of rectangles for the track
        if self.render_to_file:
            fname = './figs/frame_{:04d}.png'.format(self.frame_idx)
            self.display.save_frame(fname)
            self.frame_idx += 1
        t1 = time.time()
        if self.verbose: 
            print('\tT[render]={:e}'.format(t1 - t0))

    def render_scene(self, infos=None):
        car_x = self.model2.x.valf(self.state)
        car_y = self.model2.y.valf(self.state)
        car_angle = self.model2.yaw.valf(self.state)
        if self.has_model_tvars():
            track_dist = self.model2.s_dist.valf(self.state)
        else:
            track_dist = self.track.get_sdist(car_x, car_y)
        if track_dist is not None:
            track_point = self.track.get_point(track_dist)
            track_angle = track_point.get_orientation()
        else:
            track_angle = 0.0
        if self.render_state_infos:
            if infos is None:
                infos = {}
            infos.update(self.get_state_infos())
        self.display.update_display(car_x, car_y, car_angle, track_angle, stats_dict=infos)
        self.render_hook()

    def render_hook(self):
        pass

    def export_traj(self) -> Dict[str, List[float]]:
        pd_traj = self.get_traj()
        out_dict = {}
        for vname in pd_traj.columns:
            out_dict[vname] = [float(x) for x in pd_traj[vname].values]
        return out_dict

    def get_traj(self) -> pd.DataFrame:
        pd_traj = pd.DataFrame(self.traj)
        return pd_traj

if __name__ == '__main__':
    track_file = os.path.join('../../Data/tracks/z_track.json')
    with open(track_file) as fstream:
        track_dict = json.load(fstream)
    track = Track(track_dict)
    iter_counter = -1
    model: BikeModelTrack = BikeModelTrack(track, 0.05)
    model.reset(max_dist=0.0)
    x_arr = []
    y_arr = []
    time_0 = time.time()
    done = False
    while not done:
        iter_counter += 1
        s_dist = model.state_vec[model.s_dist_idx]
        car_angle = model.state_vec[model.angle_idx]
        track_angle = track.get_point(s_dist+10.0).get_orientation()
        steer_angle = 0.0
        accel = 0.0
        x_vel = model.state_vec[model.x_vel_idx]
        y_vel = model.state_vec[model.y_vel_idx]
        nu_dist = model.state_vec[model.nu_dist_idx]
        car_speed = (x_vel**2.0+y_vel**2.0)**0.5
        #
        if car_angle < track_angle:
            steer_angle = +min(np.radians(10.0), track_angle-car_angle)
        elif car_angle > track_angle:
            steer_angle = max(-np.radians(10.0), track_angle-car_angle)
        else:
            steer_angle = 0.0
        #
        if car_speed >= 11.0:
            accel = -1.0
        elif car_speed <= 8.0:
            accel = +1.0
        elif car_speed <= 11.0:
            accel = 0.1
        else:
            accel = 0.0
        print('Progress: {:2.2f} ({:2.2}%)'.format(s_dist, s_dist / track.length))
        print('track_angle: {:2.2f}'.format(track_angle))
        print('car_angle: {:2.2f}'.format(car_angle))
        print('nu_dist: {:2.2f}'.format(nu_dist))
        print('xi: {:2.2f}'.format(model.state_vec[model.xi_angle_idx]))
        print('----')
        action = np.array([accel, steer_angle])
        obs, rew, done, infos = model.step(action)
        x, y , *_ = obs
        if iter_counter % 10 == 0:
            # collect display information
            infos = {}
            infos['Car velocity'] = car_speed
            infos['acceleration'] = accel
            infos['steering'] = np.rad2deg(steer_angle)
            infos['progress'] = s_dist
            model.render(infos=infos)
    time_1 = time.time()
    print('Elapsed wall time: {:2.2f}'.format(time_1 - time_0))
