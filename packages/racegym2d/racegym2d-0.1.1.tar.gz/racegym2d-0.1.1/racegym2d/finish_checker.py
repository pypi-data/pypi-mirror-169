'''
Class to check whether we have reached the end of an environment
'''
import numpy as np


class FinishChecker():

    def __init__(self, model: DynamicModel):
        self.model = model
        pass

    def check_done(self, state: np.ndarray) -> Bool:
        return False 


class VariableBou
