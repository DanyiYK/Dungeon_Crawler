from Map import Map
from Player import Player
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

running = True
new_map = Map(MAP_SIZE)

player = Player(new_map, "Carlo")
hp_bar = Bar("Player HP", player.max_health)

exit = Exit()

new_map.game_layer.place_object(exit, Vector2(9, 9))

new_map.game_layer.place_object(Bomb(), Vector2(1, 0))
new_map.game_layer.place_object(Bomb(), Vector2(2, 6))

new_map.game_layer.place_object(HealPotion(), Vector2(6, 8))
new_map.game_layer.place_object(HealPotion(), Vector2(10, 2))

new_map.game_layer.place_object(Trap(), Vector2(10, 9))
new_map.game_layer.place_object(Trap(), Vector2(0, 8))
new_map.game_layer.place_object(Trap(), Vector2(7, 7))
new_map.game_layer.place_object(Trap(), Vector2(4, 9))
new_map.game_layer.place_object(Trap(), Vector2(4, 2))

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
    print(f"{HEADER}\You escaped!\n{HEADER}")

print("Steps:", player.steps)

input()