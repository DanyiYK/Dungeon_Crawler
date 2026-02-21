class Destroyable:
    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return self.char

class Wall:
    def __init__(self):
        super().__init__("d")