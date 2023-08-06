import numpy as np
import gym
from .env_basic import BikeModelTrack
from .env_basic import Track
from typing import List, Dict


class BikeModelTrackVisualDict(BikeModelTrack):

    def __init__(self, track: Track, delta_t: float, disp_res: int, screen_render=False, params=None):
        print('Making dict-visual environment with {} resolution'.format(disp_res, 1))
        self.render_to_ram: bool = True
        self.render_to_file: bool = False
        self.render_to_screen: bool = False
        super().__init__(track, delta_t, disp_res=disp_res, params=params, screen_render=screen_render)
        self._show_absolute_states: bool = False
        fig_w, fig_h = self.display.figure_shape
        # figure shape and 1 colour channel (grey-scale)
        self.obs_shape = (1, fig_w, fig_h)
        self.frame_data: np.ndarray = np.zeros(self.obs_shape, dtype=np.uint8)
        self.frame_idx: int = 0
        self.verbose: bool = False

    def init_obs_space(self):
        # New observation space, as env does not use current states
        low, high = 0, 255
        fig_w, fig_h = self.display.data_shape
        img_shape = (1, fig_w, fig_h)
        img_observation = gym.spaces.Box(low, high, shape=img_shape, dtype=np.uint8)
        speed_observation = super().get_obs_space()
        dict_spaces = {'visual': img_observation, 'base': speed_observation}
        dict_obs_space = gym.spaces.Dict(dict_spaces)
        self.observation_space = dict_obs_space

    def observe(self):
        self.render()
        frame_data = self.display.get_image_data(rgb=False)
        frame_data = frame_data[None, :, :]
        parent_obs = super().observe()
        out_data = {'visual': frame_data, 'base': parent_obs}
        return out_data
