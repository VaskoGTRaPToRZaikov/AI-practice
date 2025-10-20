def tag(some_targets:list, some_index:int, power:int) ->list:
    some_targets[some_index] -= power
    if some_targets[some_index] <= 0:
        some_targets.pop(some_index)

    return some_targets

def spawn(some_targets:list, some_index:int, value:int) ->list:
    if 0 <= some_index <= len(some_targets):
        some_targets.insert(some_index, value)
    else:
        print("Invalid spawn!")

    return some_targets

def blast(some_targets:list, some_index:int, radius:int) ->list:
    start_index = some_index - radius
    end_index = some_index + radius
    if 0 <= start_index and end_index < len(some_targets):
        targets_before_radius = some_targets[:start_index]
        targets_after_radius = some_targets[end_index:]
        some_targets = targets_before_radius + targets_after_radius
    else:
        print("Blast missed!")

    return some_targets



targets = list(map(int, input().split()))

while True:
    command = input()

    if command == "Game over":
        break

    parts = command.split()
    action, index, parameter = parts[0], int(parts[1]), int(parts[2])

    if action == "Tag":
        targets = tag(targets, index, parameter)

    elif action == "Spawn":
        targets = spawn(targets, index, parameter)

    elif action == "Blast":
        targets = blast(targets, index, parameter)

print("|".join(map(str, targets)))

