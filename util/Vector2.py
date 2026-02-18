import math

floor = math.floor

"""
Avoids division by zero
"""
def safe_div(x, y):
    if y==0:
        return 0
    
    return x/y

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def magnitude(self):
        return abs(math.sqrt(pow(self.x, 2) + pow(self.y, 2)))

    def clone(self):
        return Vector2(self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        return Vector2(self.x*other.x, self.y*other.y)

    def __truediv__(self, other):
        return Vector2(safe_div(self.x, other.x), safe_div(self.y, other.y))
    
    def __floordiv__(self, other):
        return Vector2(floor(safe_div(self.x, other.x)), floor(safe_div(self.y, other.y)))
    
    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"