import gym
from collections import OrderedDict
import numpy as np
import torch as th
from .env_basic import BikeModelTrack


class WrapperBikeTrackGoal(gym.GoalEnv):

    def __init__(self, bike_env: BikeModelTrack):
        super(WrapperBikeTrackGoal, self).__init__()
        self.my_env = bike_env
        # Make the observation space
        bound_low = self.my_env.observation_space.bounded_below
        bound_high = self.my_env.observation_space.bounded_above
        obs_space = gym.spaces.Box(bound_low, bound_high)
        blow, bhih = np.array([-10.0]), np.array([10.0**9.0])
        agoal_space = gym.spaces.Box(blow, bhih)  # put only the achieved s_dist progress here.
        dgoal_space = gym.spaces.Box(blow, bhih)
        self.observation_space = gym.spaces.Dict({
                'observation': obs_space,
                'achieved_goal': agoal_space,
                'desired_goal': dgoal_space
            })
        # Make the action space
        self.action_space = self.my_env.action_space
        self.desired_goal = self.my_env.track.get_length()

    def step(self, action: th.Tensor):
        obs, rew, done, info = self.my_env.step(action)
        new_obs = self._get_obs()
        new_rew = self.compute_reward(new_obs['achieved_goal'], new_obs['desired_goal'], None)
        new_done = self.is_done(done, new_obs)
        return new_obs, new_rew, new_done, info

    def compute_reward(self, achieved_goal, desired_goal, info):
        #print('achieved_goal:', achieved_goal)
        #print('desired_goal:', desired_goal)
        if isinstance(desired_goal, np.ndarray):
            res = (achieved_goal > desired_goal).astype(np.float64)
            return res.ravel()
        if achieved_goal > desired_goal:
            return 1.0
        return 0.0

    def is_done(self, done: bool, obs: OrderedDict):
        if obs['achieved_goal'] >= obs['desired_goal']:
            return True
        return done

    def _get_obs(self):
        '''
        Helper to create the observation.
        '''
        obs = self.my_env.observe()
        val_idx =  self.my_env.model2.s_dist.get_idx()
        achieved_dist = obs[val_idx]
        goal_dist = th.Tensor([self.desired_goal])
        return OrderedDict([
                ('observation', obs),
                ('achieved_goal', achieved_dist),
                ('desired_goal', goal_dist)])

    def reset(self):
        '''
        Reset the environment to initial values
        '''
        self.my_env.reset() 
        goal_len = np.random.rand() * self.my_env.track.get_length()
        self.desired_goal = goal_len
        return self._get_obs()

    def close(self):
        self.my_env.close()
