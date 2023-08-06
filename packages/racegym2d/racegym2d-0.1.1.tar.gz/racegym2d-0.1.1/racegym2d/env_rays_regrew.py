from .env_rays import BikeModelTrackRays
from track_model.track import Track
import numpy as np
from typing import Optional


class BikeModelRaysReg(BikeModelTrackRays):
    '''
    A Bicycle environment with smoother, regularized rewards.
    '''

    def __init__(self, track: Track, delta_t: float, res: int=480):
        super().__init__(track, delta_t, res)
        self._last_action: Optional[np.ndarray] = None
        self._lambda_reg: float = 0.01
        self._verbose: bool = False

    def _step_callback(self, action, delta_vec):
        self._last_action = action

    def compute_reward(self, action, delta_vec):
        reward, infos = super().compute_reward(action, delta_vec)
        temp_penalty = self.get_action_penalty(action)
        if self._verbose:
            print('Reward: {:2.3f}\t Penalty: {:2.3f}'.format(reward, temp_penalty))
        return reward - temp_penalty, infos

    def get_action_penalty(self, new_action: np.ndarray):
        penalty: float = 0.0
        if self._last_action is None:
            penalty = 0.0
        else:
            act_diff = new_action - self._last_action
            act_dist = np.linalg.norm(act_diff)
            penalty = self._lambda_reg * act_dist
        return penalty

    def set_temporal_penalty(self, penalyt_fac: float):
        self._lambda_reg = penalyt_fac
        print('training with temporal penalty: {}'.format(self._lambda_reg))

    def reset(self, max_dist: float=0.0):
        obs = super().reset(max_dist)
        self._last_action = None
        return obs
