class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character.upper()
        self.patterns = {
            "a1b1c1": 0, "a1a2a3": 0, "b1b2b3": 0, "c1c2c3": 0,
            "a1b2c3": 0, "a2b2c2": 0, "a3b3c3": 0, "c1b2a3": 0
        }
        self.position = ""

    def won(self):
        for pattern in self.patterns:
            if self.position in pattern:
                self.patterns[pattern] += 1
        return any(count == 3 for count in self.patterns.values())

    def to_default(self):
        for pattern in self.patterns:
            self.patterns[pattern] = 0

    def __str__(self):
        return f"{self.name} has chosen {self.character}"
