number_of_rooms = int(input())

extra_desks = 0

for room in range(1, number_of_rooms + 1):
    try:
        desks, students = input().strip().split()
        desks, students = len(desks), int(students)

        if desks < students:
            print(f"{students - desks} more desks needed in room {room}")
        extra_desks += desks - students
    except ValueError:
        exit("Invalid input")

if extra_desks >= 0:
    print(f"All set, {extra_desks} extra desks left")
else:
    print(f"Not enough desks, {extra_desks} desks needed")


