from dungeon import load_dungeon
from Map import Map
from Player import Player, Warrior, Mage, Thief
from Object import Exit, Bomb, HealPotion, Trap
from util.Bar import Bar
from util.Vector2 import Vector2

HEADER = "-" * 10
MAP_SIZE = Vector2(11, 11)
ALLOWED_MOVEMENTS = {
    "w": Vector2(0, -1),
    "a": Vector2(-1, 0),
    "s": Vector2(0, 1),
    "d": Vector2(1, 0),
}
CHARACTERS = {
    Warrior: "120 Health, 10 Strength, Special ability: Big slash.",
    Mage: "80 Health, 50 Mana, Special ability: Fireball.",
    Thief: "100 Health, 15 Agility, Special ability: Catch & Throw."
}

running = True
new_map = load_dungeon("park")

player = Player(new_map, "Carlo")
hp_bar = Bar("Player HP", player.max_health)

exit = None

for row in new_map.game_layer.grid:
    for cell in row:
        if isinstance(cell, Exit):
            exit = cell

while not exit.Used and player.health>0:
    print(new_map)
    print(hp_bar.render(player.health))

    movement = input("Movement: ").lower()
    
    if len(movement) == 0:
        continue

    direction = ALLOWED_MOVEMENTS.get(movement[-1])

    if direction:
        player.move_rel(direction)

if player.health<=0:
    print(f"{HEADER}YOU DIED!!{HEADER}")
elif exit.Used:
    print(f"{HEADER}\nYou escaped!\n{HEADER}")

print("Steps:", player.steps)

input()