from time import sleep
from util.Vector2 import Vector2
from Entity import Entity
from Destroyable import Destroyable

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
        super().__init__("E", False)

        self.Used = False
    
    def use(self, map, entity, position:Vector2):
        self.Used = True

class HealPotion(Object):
    def __init__(self):
        super().__init__("+")

        self.heal = 25

    def use(self, map, entity, position:Vector2):
        entity.take_damage(-self.heal)

class Trap(Object):
    def __init__(self):
        super().__init__("X")

        self.damage = 15

    def use(self, map, entity, position:Vector2):
        entity.take_damage(self.damage, self.__class__.__name__)

class Bomb(Object):
    def __init__(self):
        super().__init__("b")
        
        self.damaged_entities = []
        self.damage = 45
        self.explosion_radius = 6

    def damage_near(self, map, position, range):
        for y, row in enumerate(map.game_layer.grid):
            for x, cell_item in enumerate(row):
                if(position - Vector2(x, y)).magnitude() > range:
                    continue

                if isinstance(cell_item, Entity) and not(cell_item in self.damaged_entities):
                    cell_item.take_damage(self.damage, self.__class__.__name__)
                    self.damaged_entities.append(cell_item)
                elif isinstance(cell_item, Destroyable):
                    row[x] = None

    def play_animation(self, map, position:Vector2):
        effect_layer = map.effect_layer
        x, y = position.x, position.y
        last_placed = []

        for i in range(self.explosion_radius):
            last_placed.append(effect_layer.place_circle(i%2==0 and "%" or "@", x, y, i))
            last_placed.append(effect_layer.place_circle(i%2==0 and "*" or "+", x, y, i-2))
            
            self.damage_near(map, position, i)

            print("KABOOM!")
            print(effect_layer.parent)

            sleep(BOMB_ANIMATION_TIME/self.explosion_radius)

            for lp in last_placed:
                effect_layer.clear_positions(lp)
            
            last_placed.clear()
        
        effect_layer.clear_positions(lp)

    def use(self, map, entity, position:Vector2):
        self.play_animation(map, position)

        # entity.take_damage(self.damage, self.__class__.__name__)

        sleep(.25)
        
        print(map)

class StrongBomb(Bomb):
    def __init__(self):
        super().__init__()

        self.explosion_radius = 100
        self.char = "0"