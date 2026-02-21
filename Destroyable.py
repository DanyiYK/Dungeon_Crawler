class Destroyable:
    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return self.char

class DamagedWall(Destroyable):
    def __init__(self):
        super().__init__("=")

class Wall(Destroyable):
    def __init__(self):
        super().__init__("@")