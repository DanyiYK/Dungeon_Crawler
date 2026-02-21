import random
from Map import Map
from Player import Warrior, Mage, Thief
from Object import Object, Exit, Bomb, HealPotion, Trap
from util.Bar import Bar
from util.Vector2 import Vector2

DUNGEON_PATH = "./dungeons/"
RANDOM_SPAWNABLE = [HealPotion, Trap]

def set_spawnpoint(map, position):
    map.player_spawn_point = position
    
    return None

def random_object(map, position):
    return random.choice(RANDOM_SPAWNABLE)()

def spawn_bomb(map, position):
    return Bomb()


TRANSLATION_TABLE = {
    "-": None,
    "#": "#",
    "/": "/",
    "\\": "\\",
    "b": spawn_bomb,
    "S": set_spawnpoint,
    "r": random_object
}

def translate_character(map, position, char):
    result = TRANSLATION_TABLE.get(char)

    if callable(result):
        result = result(map, position)

    return result

def load_dungeon(name):
    content = []

    try:
        with open(DUNGEON_PATH + name, "r") as x:
            content = x.readlines()
    except FileNotFoundError:
        print(f"Dungeon file \"{name}\" not found!")
        
        return Map(1, 1)

    map_size = Vector2(len(content[0]), len(content))
    print("SIZE:", map_size)
    map = Map(map_size)
    grid = []

    for y, line in enumerate(content):
        row = []

        for x, char in enumerate(line):
            row.append(translate_character(map, Vector2(x, y), char))
        
        grid.append(row)
        
    map.game_layer.grid = grid

    return map