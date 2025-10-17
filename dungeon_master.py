def potion(energy:int, healing:int) -> tuple[int, int]:
    current_energy = energy
    energy += healing

    if energy > MAX_HEALTH:
        energy = MAX_HEALTH

    healed = energy - current_energy

    return energy, healed

def chest(score:int, coins:int) -> tuple[int, int]:
    score += coins

    return score, coins

MAX_HEALTH = 100
initial_energy = MAX_HEALTH
points = 0
room_number = 0
best_room_number = 0
best_value = 0

rooms = input().split("|")

for current_room in rooms:
    room_number += 1
    parts = current_room.split()
    action, value = parts[0], int(parts[1])
    gained_value = 0

    if action == "potion":
        initial_energy, gained_value = potion(initial_energy, value)
        print(f"You healed {gained_value} health.")

    elif action == "chest":
        points, gained_value = chest(points, value)
        print(f"You found {gained_value} coins.")

    elif action == "monster":
        initial_energy -= value
        print(f"Monster hit you for {value} damage.")

    if best_value < gained_value:
        best_value = gained_value
        best_room_number = room_number

    if initial_energy <= 0:
        print(f"You died at room {room_number}!")
        if best_room_number != 0:
            print(f"Best room: {best_room_number}")
        else:
            print(f"Died before completing any room.")
        break

if initial_energy > 0:
    print(f"You've made it!\nPoints: {points}\nHealth: {initial_energy}")
