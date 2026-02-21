import random
from Map import Map
from Player import Warrior, Mage, Thief
from Object import Object, Exit, Bomb, HealPotion, Trap, StrongBomb
from Destroyable import Wall, DamagedWall
from util.Bar import Bar
from util.Vector2 import Vector2

DUNGEON_PATH = "./dungeons/"
RANDOM_SPAWNABLE = [HealPotion, Trap]

# TODO: Find a better way to parse a map file, lol

def set_spawnpoint(map, position):
    map.player_spawn_point = position
    
    return None

TRANSLATION_TABLE = {
    "-": None,
    "#": "#",
    "/": "/",
    "|": "|",
    "\\": "\\",
    "0": lambda _, p: StrongBomb(), #spawn_strong_bomb,
    "E": lambda _, p: Exit(),
    "b": lambda _, p: Bomb(),
    "r": lambda _, p: random.choice(RANDOM_SPAWNABLE)(),
    "d": lambda _, position: position.x%2==0 and Wall() or DamagedWall(),
    "S": set_spawnpoint,
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