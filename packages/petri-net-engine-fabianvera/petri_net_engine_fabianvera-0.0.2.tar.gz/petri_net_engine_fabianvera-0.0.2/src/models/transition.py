class Transition:

    def __init__(self, name: str, key: int):
        self.name: str = name
        self.id: int = key
        # self.outputs: list[int] = []

    # def is_transition_enable(self, places: list):
    #     validation = True
    #     for place in places:
    #         count = 0
    #         for input_value in place.outputs:
    #             if input_value == self.key:
    #                 count += 1
    #         validation = validation and place.validate_relations(count)
    #     return validation
