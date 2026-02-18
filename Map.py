import os
from Layer import Layer
from time import sleep

EMPTY_CELL = "."

class Map:
    def __init__(self, sizeX, sizeY):
        self.game_layer = Layer(sizeX, sizeY)
        self.effect_layer = Layer(sizeX, sizeY)

        # Layer rendering priority
        self.layers = [
            self.game_layer,
            self.effect_layer
        ]

    def __repr__(self):
        output = ""

        for y, row in enumerate(self.game_layer.grid):
            for x in range(len(row)):
                output += self._get_char_at_pos(x, y) + " "
            
            output += "\n"
        
        return output

    def _get_char_at_pos(self, x, y):
        for layer in self.layers:
            if layer.grid[y][x]:
                return str(layer.grid[y][x])

        return EMPTY_CELL
    



x = Map(20, 20)