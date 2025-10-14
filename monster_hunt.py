sequence_of_distances = [int(number) for number in input().strip().split()]

removed_sum = 0

while True:
    command = input().strip()

    if command == "done":
        break

    index = int(command)
    removed = 0

    if sequence_of_distances:
        if index < 0:
                last = sequence_of_distances[-1]
                sequence_of_distances.insert(0, last)
                removed = sequence_of_distances.pop(0)
        elif index >= len(sequence_of_distances):
                first = sequence_of_distances[0]
                sequence_of_distances.append(first)
                removed = sequence_of_distances.pop(-1)
        else:
                removed = sequence_of_distances.pop(index)

        removed_sum += removed

        for i in range(len(sequence_of_distances)):
            if sequence_of_distances[i] <= removed:
                sequence_of_distances[i] += removed
            else:
                sequence_of_distances[i] -= removed

print(removed_sum)


