from .abstract_reward_function import RewardFunciton
from track_model.track import Track
from dynmodels.dynamic_model import DynamicModel
import numpy as np


class SDistReward(RewardFunciton):
    
    def __init__(self, model: DynamicModel, track: Track):
        super().__init__(model, track)
        self.reward_factor: float = 0.1
        self.track_cutoff: float = 0.98 * self.track.get_length()

    def _sdist_crossed(self, s_new, s_old):
        if s_old > self.track_cutoff and s_new >= 0.0:
            s_old = s_old - self.track_cutoff
        return s_new - s_old

    def get_reward(self, new_state, old_state):
        new_x, new_y = new_state[0:2]
        old_x, old_y = old_state[0:2]
        s_new = self.track.get_sdist(new_x, new_y)
        s_old = self.track.get_sdist(old_x, old_y)
        if s_new is None or s_old is None:
            return 0.0
        s_diff = self._sdist_crossed(s_new, s_old)
        return self.reward_factor * s_diff
