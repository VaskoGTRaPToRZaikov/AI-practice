scores = list(map(int, input().split()))

average_score = sum(scores) / len(scores)

fewer_than_average = [number for number in scores if number < average_score]

fewer_than_average.sort()

if fewer_than_average:
    print(" ".join(map(str, fewer_than_average[:3])))
else:
    print("No scores")