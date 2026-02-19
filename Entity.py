import math
from util.Vector2 import Vector2

def clamp(x, min_number, max_number):
    return min(max(x, min_number), max_number)

class Entity:
    def __init__(self, map, name, health, char="E", position=Vector2(0, 0)):
        # Health
        self.max_health = health
        self.health = self.max_health

        # In-game representation
        self.name = name
        self.char = char

        game_layer = map.game_layer
        self.position = position
        
        # The parent layer where the entity is
        self.map = map
        self.layer = game_layer
        
        map.game_layer.place_object(self, self.position)

    def __repr__(self):
        return self.char
    
    def move_abs(self, new_position):
        if not self.layer.in_bounds(new_position):
            return

        last_position = self.position
        self.position = new_position

        # Clear past position in grid
        self.layer.grid[last_position.y][last_position.x] = None
        self.map.game_layer.place_object(self, new_position)

    def move_rel(self, position):
        abs_pos = self.position + position

        self.move_abs(abs_pos)

    def on_death(self, owner=None):
        print("Entity died! Cause: ", owner)

    def take_damage(self, damage, owner=None):
        # Check if entity is already dead
        if self.health<=0:
            return
        
        self.health = clamp(self.health-damage, 0, self.max_health)

        if self.health <= 0:
            self.on_death(owner)


