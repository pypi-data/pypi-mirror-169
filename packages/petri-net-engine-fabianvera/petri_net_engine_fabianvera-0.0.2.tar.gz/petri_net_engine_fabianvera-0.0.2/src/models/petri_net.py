from . import Place
from . import Transition
import numpy as np


class ValidationPlaceExist(Exception):
    """Place exists"""
    pass


class ValidationTransitionExist(Exception):
    """Transition exists"""
    pass


class PetriNet:

    def __init__(self, places: list[Place], transitions: list[Transition], inputs: list[int][int],
                 outputs: list[int][int]):
        self.places: list[Place] = places
        self.transitions: list[Transition] = transitions
        self.inputs = np.array(inputs)
        self.outputs = np.array(outputs)

    def add_place(self, place_to_add: Place):
        for place in self.places:
            if place.id == place_to_add.id:
                return False
        self.places.append(place_to_add)
        return True

    def add_transition(self, transition_to_add: Transition):
        for transition in self.transitions:
            if transition.id == transition_to_add.id:
                # raise ValidationTransitionExist("Transicion ya existe")
                return False
        self.transitions.append(transition_to_add)
        return True

    def add_input(self, place: Place, transition: Transition):
        pass
