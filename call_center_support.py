agent1_efficiency = int(input())
agent2_efficiency = int(input())
agent3_efficiency = int(input())
total_calls = int(input())
hours = 0

overall_efficiency = agent1_efficiency + agent2_efficiency + agent3_efficiency

while total_calls:
    hours += 1

    if hours % 3 == 0:
        continue

    total_calls -= min(overall_efficiency, total_calls)

print(f"Time needed: {hours}h.")

