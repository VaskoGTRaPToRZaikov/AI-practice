sequence_of_integers = [int(number.strip()) for number in input().split(",")]
try:
    if any(number < 1 for number in sequence_of_integers):
        print("Invalid input")
        exit()
    else:
        if len(sequence_of_integers) > 0:
            max_number = max(sequence_of_integers)
            groups = [[] for _ in range((max_number - 1) // 5 + 1)]

            for number in sequence_of_integers:
                group_index = (number - 1) // 5
                groups[group_index].append(number)

            for i, group in enumerate(groups):
                if group:
                    print(f"Group of {(i + 1) * 5}'s: {sorted(group)}")

except ValueError:
    print("Invalid input")

