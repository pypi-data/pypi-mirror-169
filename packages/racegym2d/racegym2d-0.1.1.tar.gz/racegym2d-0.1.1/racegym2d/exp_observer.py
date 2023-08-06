import numpy as np
from abc import ABC, abstractmethod
from .exp_observation import ExplainedObservation


class ExplainedObserver(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_observation(self, x_arr: np.ndarray) -> ExplainedObservation:
        return None
