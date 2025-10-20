def receive(some_inventory:list, items:list) -> list:
    for i in range(1, len(items)):
        item = items[i]
        if item not in some_inventory:
            some_inventory.insert(0, item)
    return some_inventory

def relocate(some_inventory: list, some_index:int) ->list:
    if 0 <= some_index < len(some_inventory):
        moved_item = some_inventory.pop(some_index)
        some_inventory.append(moved_item)

    return some_inventory

def ship(some_inventory:list, some_count:int) ->list:
    index_for_remove = len(some_inventory) - some_count
    removed_items = some_inventory[index_for_remove:]
    some_inventory = some_inventory[:index_for_remove]
    if removed_items:
        print(', '.join(removed_items))

    return some_inventory

inventory = input().split("|")

while True:

    command = input()

    if command == "Closing time!":
        break

    parts = command.split()
    action = parts[0]

    if action == "Receive":
        inventory = receive(inventory, parts)

    elif action == "Relocate":
        index = int(parts[1])
        inventory = relocate(inventory, index)

    elif action == "Ship":
        count = int(parts[1])
        inventory = ship(inventory, count)

if inventory:
    average_item_length = sum(len(item) for item in inventory) / len(inventory)
    print(f"Average item length: {average_item_length:.2f} units.")
else:
    print("Empty warehouse.")

