from util.Vector2 import Vector2
import math

CHAR_PER_RANGE = 8
FULL_CIRCLE = 2*math.pi

class Layer:
    def __init__(self, sizeX, sizeY):
        self.grid = []
        self.size = Vector2(sizeX, sizeY)

        for _ in range(sizeY):
            row = []
            self.grid.append(row)
            
            for _ in range(sizeX):
                row.append(None)
    
    def clear(self):
        for row in self.grid:
            for column in range(len(row)):
                row[column] = None

    """
    Returns true if position is inside Layer
    """
    def in_bounds(self, position:Vector2):
        size = self.size
        x, y = position.x, position.y

        return(x > 0 or x < size.x) or (y > 0 or y < size.y)

    """
    Safely retrieves an object
    """
    def get_object(self, position:Vector2):
        if not self.in_bounds(position):
            return None
        
        return self.grid[position.y][position.x]

    def place_object(self, object, x, y):
        if not self.in_bounds(Vector2(x, y)):
            return False
        
        self.grid[y][x] = object

        if not isinstance(object, str):
            object.object_spawned(self, x, y)

        return True

    """
    Takes a list of Vector2, sets the positions in the grid to None
    """    
    def clear_positions(self, position_list):
        for position in position_list:
            self.grid[position[1]][position[0]] = None

    """
    Draws a circle on the grid, returns a list of positions where the single pixels were placed.
    """
    def place_circle(self, object, centerX, centerY, circle_range):
        placed_positions = []

        circle_char_count = circle_range*CHAR_PER_RANGE
        for x in range(circle_char_count):
            rad = FULL_CIRCLE * x/circle_char_count
            
            x = round(math.cos(rad)*circle_range) + centerX
            y = round(math.sin(rad)*circle_range) + centerY

            placed = self.place_object(object, x, y)

            if placed:
                placed_positions.append([x, y])

        return placed_positions