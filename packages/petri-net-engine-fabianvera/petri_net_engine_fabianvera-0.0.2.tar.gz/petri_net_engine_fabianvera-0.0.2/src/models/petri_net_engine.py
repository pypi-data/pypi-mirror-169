from . import PetriNet
from . import Transition


class PetriNetEngine:

    def __init__(self, petri_net: PetriNet):
        self.petri_net = petri_net
        pass

    def search_transitions_enabled(self):
        return self.petri_net

    def fire_transition(self, transition: Transition):
        print("Firing transition")
        return transition
