from dynmodels.bicycle_model import BicycleModel
from dynmodels.bicycle_model_v2 import BicycleModel2
from dynmodels.bicycle_model_v2_tvars import BicycleModel2Tvars
import numpy as np


class BoundChecker():
    '''
    Class to check whether we have reached the end of an environment
    '''
    def __init__(self, model: DynamicModel):
        self.model = model
        pass

    def check_done(self, state: np.ndarray) -> Bool:
        return False 


class VariableBoundChecker(BoundChecker):
    
    def __init__(self, model: DynamicModel):
        super().__init__(model)
        # Check if the model supports track variables
        if isinstance(self.model, BicycleModel2):
            # Model does not support track variables
            raise ValueError('Model does not support track variables')

    def check_done(self, state: np.ndarray):
