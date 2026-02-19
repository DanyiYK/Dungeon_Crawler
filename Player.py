from Entity import Entity
from util.Vector2 import Vector2

PLAYER_START_HEALTH = 100

class Player(Entity):
    def __init__(self, map, name):
        super().__init__(map, name, PLAYER_START_HEALTH, "G", Vector2())

        self.steps = 0
    
    def move_abs(self, new_position):
        self.steps += 1
        return super().move_abs(new_position)