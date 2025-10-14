def add(event, events):
    events.append(event)
    return events

def insert(event, index, events):
    if index < 0 or index > len(events):
        events.append(event)
    else:
        events.insert(index, event)
    return events

def remove(event, events):
    if event in events:
        events.remove(event)
    return events

def swap(event1, event2, events):
    if event1 in events and event2 in events:
        index1 = events.index(event1)
        index2 = events.index(event2)
        events[index1], events[index2] = events[index2], events[index1]
    return events

def break_cmd(event, events):
    if event in events:
        index = events.index(event)
        events.insert(index + 1, f"{event}-Break")
    else:
        events.append(event)
        events.append(f"{event}-Break")
    return events

initial_events = input().strip()
initial_events = initial_events.split(", ") if initial_events else []

while True:
    command = input()

    if command == "start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        initial_events = add(parts[1], initial_events)
    elif action == "Insert":
        initial_events = insert(parts[1], int(parts[2]), initial_events)
    elif action == "Remove":
        initial_events = remove(parts[1], initial_events)
    elif action == "Swap":
        initial_events = swap(parts[1], parts[2], initial_events)
    elif action == "Break":
        initial_events = break_cmd(parts[1], initial_events)

for i, some_event in enumerate(initial_events, 1):
    print(f"{i}. {some_event}")


