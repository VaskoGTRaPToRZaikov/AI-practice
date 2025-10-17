fuel = int(input())
count = 0

while True:
    command = input()

    if command == "Mission complete":
        print(f"Resources harvested: {count}. Fuel remaining: {fuel}")
        break
    count += 1
    distance = int(command)

    if count % 4 == 0:
        fuel += distance

    if fuel >= distance:
        fuel -= distance
    else:
        print(f"Insufficient fuel! Mission ends with {count - 1} resources harvested and {fuel} fuel left.")
        break


