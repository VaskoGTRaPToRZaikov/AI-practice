initial_power = int(input())

mine_counts = 0

while True:
    command = input()

    if command == "Expedition over":
        print(f"Veins mined: {mine_counts}. Power remaining: {initial_power}")
        break

    depth = int(command)

    if initial_power >= depth:
        initial_power -= depth
        mine_counts += 1
        if mine_counts % 2 == 0:
            initial_power += mine_counts

    else:
        print(f"Power depleted! Expedition ends with {mine_counts} veins mined and {initial_power} power left.")
        break