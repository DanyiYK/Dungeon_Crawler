from time import sleep
from util.Vector2 import Vector2

BOMB_ANIMATION_TIME = 1 # Seconds

"""
Blank object class
"""
class Object:
    def __init__(self, char="?", destroy_on_use = True):
        self.destroy_on_use = destroy_on_use
        self.char = char

    def __repr__(self):
        return self.char

    def object_spawned(self, position:Vector2):
        pass

    def use(self, map, entity, position:Vector2):
        pass

class Exit(Object):
    def __init__(self):
        super().__init__("e", False)

        self.Used = False
    
    def use(self, map, entity, position:Vector2):
        self.Used = True

class HealPotion(Object):
    def __init__(self):
        super().__init__("p")

        self.heal = 25

    def use(self, map, entity, position:Vector2):
        entity.take_damage(-self.heal)

class Bomb(Object):
    def __init__(self):
        super().__init__("b")
        
        self.damage = 20
        self.explosion_radius = 6

    def play_animation(self, map, position:Vector2):
        effect_layer = map.effect_layer
        x, y = position.x, position.y
        last_placed = []

        for i in range(self.explosion_radius):
            last_placed.append(effect_layer.place_circle(i%2==0 and "%" or "@", x, y, i))
            last_placed.append(effect_layer.place_circle(i%2==0 and "*" or "+", x, y, i-2))
            
            print("KABOOM!")
            print(effect_layer.parent)

            sleep(BOMB_ANIMATION_TIME/self.explosion_radius)

            for lp in last_placed:
                effect_layer.clear_positions(lp)
            
            last_placed.clear()
        
        effect_layer.clear_positions(lp)

    def use(self, map, entity, position:Vector2):
        self.play_animation(map, position)

        entity.take_damage(self.damage, Bomb.__name__)

        sleep(.25)
        
        print(map)