transport_data = {}

while True:
    command = input()

    if command == "end of day":
        break

    parts = command.split()
    bus_number, stop_name, passengers = parts[0], parts[1], int(parts[2])

    if bus_number not in transport_data:
        transport_data[bus_number] = {}

    if stop_name not in transport_data[bus_number]:
        transport_data[bus_number][stop_name] = 0

    transport_data[bus_number][stop_name] += passengers

sorted_buses = sorted(transport_data.items(), key=lambda x: sum(x[1].values()), reverse=True)

for bus, stops in sorted_buses:
    total = sum(stops.values())
    print(f"Line {bus}: {total} passengers")

    sorted_stops = sorted(stops.items(), key=lambda x: x[1], reverse=True)
    for stop, count in sorted_stops:
        print(f"--- {stop}: {count}")


