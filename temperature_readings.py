temperatures = list(map(int, input().split()))

average_temperature = sum(temperatures) / len(temperatures)

fewer_than_average = [temp for temp in temperatures if temp > average_temperature]

fewer_than_average = sorted(fewer_than_average, reverse=True)

if fewer_than_average:
    print(" ".join(map(str, fewer_than_average[:4])))
else:
    print("No readings")