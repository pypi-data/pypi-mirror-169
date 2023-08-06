import numpy as np
from .env_basic import BikeModelTrack
from .env_rays import BikeModelTrackRays
from .env_visual import BikeModelTrackVisual
from stable_baselines3.common.vec_env import VecEnv


class MultiprocessEnvWrapper(VecEnv):

    def __init__(self, num_envs: int=10):
        self.num_envs = 10


