from .abstract_reward_function import RewardFunciton
from track_model.track import Track
from dynmodels.dynamic_model import DynamicModel
import numpy as np


class CheckpointReward(RewardFunciton):
    
    def __init__(self, model: DynamicModel, track: Track, num: int):
        super().__init__(model, track)
        # Setup checkpoints
        self.cp_dists = np.linspace(0.0, track.get_length(), num+1)[0:-1]
        self.cp_reward: float = 1.0

    def _cp_crossed(self, s_new: float, s_old: float) -> int:
        # Check if crossed finish line
        old_fin = (s_old >= self.cp_dists[-1] and s_old < self.track.get_length())
        new_fin = (s_new >= self.cp_dists[0] and s_new < self.cp_dists[1])
        if old_fin and new_fin:
            diff = 1
        else:
            a0 = np.sum(s_old >= self.cp_dists)
            a1 = np.sum(s_new >= self.cp_dists)
            diff = 1 if a1 > a0 else 0
        return diff

    def get_reward(self, new_state, old_state):
        new_x, new_y = new_state[0:2]
        old_x, old_y = old_state[0:2]
        s_new = self.track.get_sdist(new_x, new_y)
        s_old = self.track.get_sdist(old_x, old_y)
        if s_new is None or s_old is None:
            return 0.0
        return self._cp_crossed(s_new, s_old) * self.cp_reward

