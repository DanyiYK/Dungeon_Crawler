from util.Vector2 import Vector2
from Layer import Layer
from Object import Object
from Entity import Entity

EMPTY_CELL = "."

class Map:
    def __init__(self, size:Vector2):
        self.size = size
        self.game_layer = Layer(self, size)
        self.effect_layer = Layer(self, size)

        self.player_spawn_point = Vector2(0, 0)

        # Map layers, in priority order
        self.layers = [
            self.game_layer,
            self.effect_layer
        ]

    def __repr__(self):
        output = "_ "

        for i in range(self.size.x):
            i = i < 10 and i or 9
            output += f"_ "

        output += "\n"

        for y, row in enumerate(self.game_layer.grid):
            output += f"| "
            for x in range(len(row)):
                output += self._get_char_at_pos(x, y) + " "
            
            output += "\n"
        
        return output

    def _get_char_at_pos(self, x, y):
        for layer in self.layers:
            if layer.grid[y][x]:
                return str(layer.grid[y][x])

        return EMPTY_CELL