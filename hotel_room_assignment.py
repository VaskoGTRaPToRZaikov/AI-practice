number_of_guests = int(input())
rooms = list(map(int, input().split()))
max_capacity = 3

for i in range(len(rooms)):
    free_spots = max_capacity - rooms[i]

    current_room_spots = min(free_spots, number_of_guests)
    number_of_guests -= current_room_spots
    rooms[i] += current_room_spots

    if number_of_guests == 0:
        break

if number_of_guests == 0 and any(room < max_capacity for room in rooms):
    print(f"Rooms have vacancies! {' '.join(map(str, rooms))}")

elif number_of_guests > 0 and any(room == max_capacity for room in rooms):
    print(f"No more rooms! {number_of_guests} guests waiting! {' '.join(map(str, rooms))}")

else:
    print(f"{' '.join(map(str, rooms))}")
