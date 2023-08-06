import numpy as np
import gym
from .env_basic import BikeModelTrack
from .env_basic import Track
from typing import List, Dict
import matplotlib.pyplot as plt


class BikeModelTrackVisual(BikeModelTrack):

    def __init__(self, track: Track, delta_t: float, disp_res: int, screen_render=False, nframes=1, params=None):
        print('Making visual environment with {} resolution'.format(disp_res))
        self.frame_stack_height: int = nframes
        self.render_to_ram: bool = True
        self.render_to_file: bool = False
        self.render_to_screen: bool = False
        super().__init__(track, delta_t, disp_res=disp_res, params=params, screen_render=screen_render)
        fig_w, fig_h = self.display.figure_shape
        self.obs_shape = (self.frame_stack_height, fig_h, fig_w)
        self.frame_stack: np.ndarray = np.zeros(self.obs_shape, dtype=np.uint8)
        self.frame_idx: int = 0
        self.init_frame_stack()
        self.verbose: bool = False
        self.debug_mode: bool = False


    def init_frame_stack(self):
        self.render()
        img_data = self.display.get_image_data(rgb=False)
        for k in range(self.frame_stack_height):
            self.frame_stack[k, :, :] = img_data.T

    def add_stack_frame(self, frame_data: np.ndarray):
        self.frame_stack[0:-1, :, :,] = self.frame_stack[1:, :, :]
        self.frame_stack[-1, :, :] = frame_data.T

    def init_obs_space(self):
        # New observation space, as env does not use current states
        low, high = 0.0, 255.0
        fig_w, fig_h = self.display.figure_shape
        shape = (self.frame_stack_height, fig_h, fig_w)
        self.observation_space = gym.spaces.Box(low, high, shape=shape, dtype=np.float32)

    def _check_identical(self):
        '''
        Check if all the images are identical.
        '''
        numf = self.frame_stack_height
        diff_mtx = np.zeros((numf, numf))
        for i in range(self.frame_stack_height):
            for j in range(i+1, self.frame_stack_height):
                mi = self.frame_stack[i, :, :]
                mj = self.frame_stack[j, :, :]
                diff_mtx[i, j] = np.linalg.norm(mi - mj)
        if np.max(diff_mtx) < 1e-6:
            print('All images are identical')
            return True
        return False

    def _show_frame_stack(self):
        '''
        Debug method to look at the current frame stack
        '''
        num_rows = 1
        num_cols = 1
        frac = 16.0 / 9.0
        while num_rows * num_cols < self.frame_stack_height:
            if num_cols / num_rows < frac:
                num_cols += 1
            else:
                num_rows += 1
        idx = 1
        fig = plt.figure(figsize=(16, 9))
        ident = self._check_identical()
        msg = 'Index {}, t={:2.5f}, Identical={}'
        msg = msg.format(self.frame_idx, self.time, ident)
        plt.suptitle(msg)
        for idx in range(self.frame_stack_height):
            img = self.frame_stack[idx, :, :]
            plt.subplot(num_rows, num_cols, idx+1)
            plt.imshow(img)
            plt.title('idx={}'.format(idx))
        plt.show()

    def observe(self):
        self.render()
        frame_data = self.display.get_image_data(rgb=False)
        self.add_stack_frame(frame_data)
        if self.debug_mode:
            self._show_frame_stack()
        return self.frame_stack

    def reset(self):
        result = super().reset()
        print('Environment was reset.')
        self.frame_idx = 0 
        self.init_frame_stack()
        return result

    def step(self, action):
        res = super().step(action)
        self.frame_idx += 1
        return res

