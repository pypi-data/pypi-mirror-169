from abc import ABC, abstractmethod
from dynmodels.dynamic_model import DynamicModel
from track_model.track import Track
import numpy as np


class RewardFunciton(ABC):

    def __init__(self, model: DynamicModel, track: Track):
        self.model: DynamicModel = model
        self.track: Track = track
        self.total_reward: float = 0.0

    def reset(self):
        self.total_reward = 0.0

    def __call__(self, new_state, old_state):
        out_reward = self.get_reward(new_state, old_state)
        self.total_reward += out_reward
        return out_reward

    @abstractmethod 
    def get_reward(self, new_state, old_state):
        return 0.0
