from Map import Map
from time import sleep

BOMB_ANIMATION_TIME = 1 # Seconds

"""
Blank object class
"""
class Object:
    def __init__(self):
        pass

    def __repr__(self):
        return "?"

    def object_spawned(self, x, y):
        pass

    def use(self, map:Map, Player):
        pass

class Bomb(Object):
    def __init__(self):
        super().__init__()
        
        self.damage = 10
        self.explosion_radius = 5
    
    def play_animation(self, map:Map, x, y):
        effect_layer = map.effect_layer
        last_placed = []

        for i in range(self.explosion_radius):
            last_placed.clear()

            last_placed.append(effect_layer.place_circle(i%2==0 and "%" or "@", x, y, i))
            last_placed.append(effect_layer.place_circle(i%2==0 and "-" or "|", x, y, i-2))

            sleep(BOMB_ANIMATION_TIME/self.explosion_radius)

            for lp in last_placed:
                effect_layer.clear_positions(lp)

    def use(self, map:Map, Player, x, y):
        self.play_animation(map, x, y)

        Player.take_damage(self.damage)
    