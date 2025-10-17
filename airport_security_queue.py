number_of_passengers = int(input())
number_of_lines = list(map(int, input().split()))

max_line_capacity = 5

for i in range(len(number_of_lines)):
    free_spots = max_line_capacity - number_of_lines[i]
    assigned_passengers = min(free_spots, number_of_passengers)
    number_of_passengers -= assigned_passengers
    number_of_lines[i] += assigned_passengers

    if number_of_passengers <= 0:
        if any(line < max_line_capacity for line in number_of_lines):
            print(f"Lanes have empty spots! {" ".join(map(str, number_of_lines))}")
            break
        else:
            print(" ".join(map(str, number_of_lines)))
            break


if number_of_passengers:
    print(f"Not enough lanes! {number_of_passengers} passengers waiting! {" ".join(map(str, number_of_lines))}")

