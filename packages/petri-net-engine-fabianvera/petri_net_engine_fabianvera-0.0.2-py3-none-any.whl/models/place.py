class Place:

    def __init__(self, name: str, id: int, tokens: int):
        self.name: str = name
        self.id: int = id
        self.tokens: int = tokens

    def validate_relations(self, relations_number: int):
        return relations_number <= self.tokens
