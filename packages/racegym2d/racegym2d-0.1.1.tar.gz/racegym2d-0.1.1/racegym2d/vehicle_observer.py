from .exp_observer import ExplainedObserver
from .exp_observation import ExplainedObservation


class VehicleObserver(ExplainedObserver):


    def __init__(self, start_idx):
        self.obs_start_idx = start_idx
        self.states_start_idx = start_idx
        self.num_states: int = 9
        self.num_params: int = 9

