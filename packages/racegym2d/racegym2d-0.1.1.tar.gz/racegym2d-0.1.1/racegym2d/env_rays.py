from .env_basic import BikeModelTrack
from track_model.track import Track
from track_model.finite_line import FiniteLine
from track_model.finite_line import FiniteLineGroup
import time
import numpy as np
import torch as th
import gym


class BikeModelTrackRays(BikeModelTrack):

    def __init__(self, track: Track, delta_t: float, num_rays: int=50, res:int=-1, screen_render=False):
        self.num_rays = num_rays
        self.ray_length: float = 250.0
        self.ray_angles = np.linspace(-0.75*np.pi, +0.75*np.pi, self.num_rays)
        self.old_cam_angle = track.get_point(0.0).get_orientation()
        self.draw_rays = True
        super().__init__(track, delta_t, disp_res=res, screen_render=screen_render)
        self.verbose = False
        # Construct line groups for left and right boundary.
        self.init_bounds()

    def set_draw_rays(self, draw_rays:bool = False):
        self.draw_rays = draw_rays

    def init_bounds(self): 
        track_len = self.track.get_length()
        self.track_resolution = int(round(self.track.get_length()/10.0))
        self.left_bound: FiniteLineGroup = FiniteLineGroup()
        self.right_bound: FiniteLineGroup = FiniteLineGroup()
        self.boundary: FiniteLineGroup = FiniteLineGroup()
        track_points = np.linspace(0.5, track_len-0.5, self.track_resolution)
        width = self.track.width
        for which in ['left', 'right']:
            for k in range(1, self.track_resolution):
                # Left start:
                start_dist = track_points[k-1] - 0.5
                end_dist = track_points[k] + 0.5
                point_start = self.track.get_point(start_dist)
                point_end = self.track.get_point(end_dist)
                start = point_start.get_bound(width, which=which).as_tuple()
                end = point_end.get_bound(width, which=which).as_tuple()
                new_line = FiniteLine(start, end)
                self.boundary.add_line(new_line, recompute=False)
        self.boundary.recompute_eqs()

    def get_obs_bounds(self):
        state_bounds = super(BikeModelTrackRays, self).get_obs_bounds()
        state_bounds.extend(self.get_ray_obs_bounds()) 
        return state_bounds

    def get_ray_obs_bounds(self):
        lb, ub = 0.0, self.ray_length
        bounds = [(lb, ub) for k in range(self.num_rays)]
        return bounds

    def observe_rays(self):
        bound_elem = self.boundary.num_lines
        car_angle = self.model2.yaw.valf(self.state)
        car_pos_x = self.model2.x.valf(self.state)
        car_pos_y = self.model2.y.valf(self.state)
        car_pos_rep = np.zeros((bound_elem, 2))
        car_pos_rep[:, 0] = car_pos_x
        car_pos_rep[:, 1] = car_pos_y
        ray_directions = np.zeros((self.num_rays, 2))
        ray_directions[:, 0] = np.cos(self.ray_angles + car_angle)
        ray_directions[:, 1] = np.sin(self.ray_angles + car_angle)
        ray_starts = np.zeros((self.num_rays, 2))
        ray_starts[:, 0] = car_pos_x
        ray_starts[:, 1] = car_pos_y
        # ray_ends = ray_starts + 1.0 * ray_directions
        ray_dists = np.repeat(self.ray_length, self.num_rays)
        for k in range(self.num_rays):
            bound_dist = self.ray_length
            # Compute boundary intersection
            ray_start = ray_starts[k, :]
            ray_direct = ray_directions[k, :]
            isect_points, valid_isect = self.boundary.get_ray_intersections(ray_start, ray_direct)
            isect_dist = np.linalg.norm(isect_points - car_pos_rep, axis=1)
            if np.any(valid_isect):
                min_dist = np.min(isect_dist[valid_isect])
                bound_dist = min(min_dist, self.ray_length)
            ray_dists[k] = bound_dist
        return ray_dists

    def _observe_rays_multi(self, state_vec: th.Tensor):
        t0 = time.time()
        device = str(state_vec.device)
        num_states = state_vec.shape[0]
        num_rays = self.num_rays
        num_bounds = self.boundary.num_lines
        car_anglei = self.model2.yaw.get_idx()
        car_xi = self.model2.x.get_idx()
        car_yi = self.model2.y.get_idx()
        car_x = state_vec[:, car_xi]
        car_y = state_vec[:, car_yi]
        car_a = state_vec[:, car_anglei]
        car_xr = car_x.tile((num_rays, 1)).T
        car_yr = car_y.tile((num_rays, 1)).T
        car_ar = car_a.tile((num_rays, 1)).T
        # Check the dimension of this!
        ray_angles = th.tensor(self.ray_angles, device=device)
        ray_angles = ray_angles.tile((num_states, 1))
        # Construct this guy better. Avoid th.zeros, th.ones, th.tensor entirely
        #ray_origin = th.zeros((2, num_states, num_rays), dtype=th.float64, device=device)
        ray_origin = th.stack([car_xr, car_yr], dim=2)
        #assert ray_origin[:, :, 0] == car_xr -> tested these two
        #assert ray_origin[:, :, 1] == car_yr
        ray_xdir = th.cos(ray_angles + car_ar)
        ray_ydir = th.sin(ray_angles + car_ar)
        ray_directions = th.stack([ray_xdir, ray_ydir], dim=2)
        # ray_ends = ray_starts + 1.0 * ray_directions
        ray_dists = self.ray_length * th.ones((num_states, num_rays), dtype=th.float64, device=device)
        for k in range(num_states):
            # Compute boundary intersection
            car_xr = th.tile(car_x[k], (num_rays, num_bounds))
            car_yr = th.tile(car_y[k], (num_rays, num_bounds))
            car_pos = th.stack([car_xr, car_yr], dim=2)
            #car_pos[:, :, 0] = car_x[k]
            #car_pos[:, :, 1] = car_y[k]
            ray_start = ray_origin[k, :, :]
            ray_dir = ray_directions[k, :, :]
            isect_points, valid_isect = self.boundary.get_multi_ray_intersections(ray_start, ray_dir)
            isect_dists = th.linalg.norm(isect_points - car_pos, axis=2)
            isect_dists[~valid_isect] = self.ray_length
            isect_dist = th.min(isect_dists, dim=1)[0]
            ray_dists[k, :] = isect_dist 
        t1 = time.time()
        rps = num_rays / (t1 - t0)
        msg = 'performed {} ray observations in {:2.4f} sec [{:e} ray/sec] on {}'
        msg = msg.format(num_rays, t1 - t0, rps, device)
        if self.verbose:
            print(msg)
        return ray_dists

    def step(self, action, draw_infos=None):
        #print('Action:', action)
        obs, rew, done, info = super(BikeModelTrackRays, self).step(action)
        #print('New state: ', obs)
        if self.render_to_screen:
            self.render(infos=draw_infos)
        return obs, rew, done, info

    def _get_observation(self, state_vec: th.Tensor):
        '''
        Get observation of each state component.
        Provide one state vector per row of the state_vector.
        '''
        # Get the observation for each for of the state vector.
        original_obs = super()._get_observation(state_vec)
        ray_obs = self._observe_rays_multi(state_vec)
        full_obs = th.hstack([original_obs, ray_obs])
        return full_obs

    def observe(self):
        state_mtx = th.tensor(self.state[None, :])
        original_obs = super()._get_observation(state_mtx)
        original_obs = original_obs.numpy()[0, :]
        ray_obs = self.observe_rays()
        #state_mtx = th.tensor(self.state[None, :])
        #res = self._get_observation(state_mtx)
        #res = res[0, :].numpy()
        #return res
        res = np.concatenate([original_obs, ray_obs])
        return res

    def _render_rays(self):
        ray_angles = self.ray_angles + self.model2.yaw.valf(self.state)
        # ray_length = self.observe_rays()
        state_th = th.tensor(self.state[None, :])
        ray_length = self.observe_rays()
        car_x = self.model2.x.valf(self.state)
        car_y = self.model2.y.valf(self.state)
        if self.display is not None:
            self.display.render_car_rays(car_x, car_y, ray_angles, ray_length)
            self.display.render_track_bound(self.boundary)

    def render_hook(self):
        if self.draw_rays:
            #print('drawing rays')
            self._render_rays()
