from Map import Map
from Player import Player
from Object import Exit, Bomb, HealPotion
from util.Bar import Bar
from util.Vector2 import Vector2

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

while not exit.Used and player.health>0:
    print(new_map)
    print(hp_bar.render(player.health))

    movement = input("Movement: ").lower()
    
    if len(movement) == 0:
        continue

    direction = ALLOWED_MOVEMENTS.get(movement[0])

    if direction:
        player.move_rel(direction)

if player.health<=0:
    print("SEI MORTO!")
elif exit.Used:
    print("Sei uscito")

print(new_map)
print(hp_bar.render(player.health))


input()