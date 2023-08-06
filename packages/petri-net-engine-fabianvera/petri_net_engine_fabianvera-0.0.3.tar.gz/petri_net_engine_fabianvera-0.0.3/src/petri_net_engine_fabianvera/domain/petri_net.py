import numpy as np


class PetriNet:

    def __init__(self):
        self.places = []
        self.places_as_dict = {}
        self.markings = []
        self.transitions = []
        self.transitions_as_dict = {}
        self.inputs_matrix = []
        self.outputs_matrix = []
        self.entries = []
        self.outputs = []

    def add_place(self, place):
        self.places_as_dict[place['name']] = place
        self.places.append(place)
        self.markings.append(place['tokens'])
        return True

    def add_transition(self, transition):
        self.transitions_as_dict[transition['name']] = {
            'transition': transition,
            'index': self.transitions_as_dict.__len__()
        }
        self.transitions.append(transition)
        return True

    def add_input(self, place, transition, number):
        self.entries.append({'place': place, 'transition': transition, 'number': number})
        return True

    def add_output(self, transition, place, number):
        self.outputs.append({'transition': transition, 'place': place, 'number': number})
        return True

    def get_markings(self):
        return np.array(self.markings)

    def generate_inputs_matrix(self):
        inputs_matrix = []
        for transition in self.transitions_as_dict:
            index = 0
            inputs_of_current_transition = [0] * len(self.places)
            for place in self.places:
                for entry in self.entries:
                    if entry['place'] == place['name'] and entry['transition'] == transition:
                        inputs_of_current_transition[index] = entry['number']
                index += 1
            inputs_matrix.append(inputs_of_current_transition)
        self.inputs_matrix = inputs_matrix

    def generate_outputs_matrix(self):
        outputs_matrix = []
        for transition in self.transitions_as_dict:
            index = 0
            outputs_for_current_transition = [0] * len(self.places)
            for place in self.places:
                for output in self.outputs:
                    if output['place'] == place['name'] and output['transition'] == transition:
                        outputs_for_current_transition[index] = output['number']
                index += 1
            outputs_matrix.append(outputs_for_current_transition)
        self.outputs_matrix = outputs_matrix

    def get_inputs_matrix_for_transition(self, transition: str):
        return self.inputs_matrix[self.transitions_as_dict[transition]['index']]

    def get_outputs_matrix_for_transition(self, transition: str):
        return self.outputs_matrix[self.transitions_as_dict[transition]['index']]
