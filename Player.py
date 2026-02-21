from Entity import Entity
from util.Vector2 import Vector2
from datetime import datetime

# TODO:
# Class choice (Warrior, Mage, Thief)
# Nice to have: Abilities
# Thief: Steal objects
# Mage: Fireball
# Warrior: Slash

PLAYER_START_HEALTH = 100

class Player(Entity):
    def __init__(self, map, name):
        super().__init__(map, name, PLAYER_START_HEALTH, "G", map.player_spawn_point)

        self.steps = 0
    
    def move_abs(self, new_position):
        self.steps += 1
        return super().move_abs(new_position)

class Character(Player):
    def __init__(self, map, name):
        super().__init__(map, name)

        self.ability_cooldown = 5

        # unix timestamp that shows when player can use the ability
        self.cooldown = 0

        # Character stats
        self.strength = 0
        self.mana = 0
        self.agility = 0

    
    def use_ability(self):
        if self.cooldown > datetime().timestamp():
            return False
        
        self.cooldown = datetime().timestamp() + self.ability_cooldown

        return True

def Warrior(Character):
    def __init__(self, map, name):
        super().__init__(map, name)

        self.set_maxhealth(120)

        self.char = "G"
        self.strength = 10

def Mage(Character):
    def __init__(self, map, name):
        super().__init__(map, name)

        self.set_maxhealth(80)

        self.char = "M"
        self.mana = 50

def Thief(Character):
    def __init__(self, map, name):
        super().__init__(map, name)

        self.set_maxhealth(100)

        self.char = "L"
        self.agility = 15