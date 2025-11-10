standings = {}
results = {}

while True:
    result = input()

    if result == "tournament end":
        break

    teams = result.split(" vs ")
    first_team, others = teams[0], teams[1]

    scores = others.split(":")
    second_team, score1, score2 = scores[0], int(scores[1]), int(scores[2])

    for team in (first_team, second_team):
        if team not in standings:
            standings[team] = 0
            results[team] = {}

    # if first_team not in standings:
    #     standings[first_team] = 0
    #     results[first_team] = {}
    # if second_team not in standings:
    #     standings[second_team] = 0
    #     results[second_team] = {}

    if score1 > score2:
        standings[first_team] += 3
        results[first_team]["wins"] = results[first_team].get("wins", 0) + 1
        results[second_team]["losses"] = results[second_team].get("losses", 0) + 1

    elif score2 > score1:
        standings[second_team] += 3
        results[second_team]["wins"] = results[second_team].get("wins", 0) + 1
        results[first_team]["losses"] = results[first_team].get("losses", 0) + 1

    else:
        standings[first_team] += 1
        standings[second_team] += 1
        results[first_team]["draws"] = results[first_team].get("draws", 0) + 1
        results[second_team]["draws"] = results[second_team].get("draws", 0) + 1

for position, (team, points) in enumerate(sorted(standings.items(), key=lambda x: (-x[1], x[0])), 1):
    win_count, draw_count, lose_count = results[team].get("wins", 0), results[team].get("draws", 0), results[team].get("losses", 0)
    print(f"{position}. {team} - {points}pts (W:{win_count}/D:{draw_count}/L:{lose_count})")

# sorted_teams = sorted(standings.items(), key=lambda x: (x[1], x[0]), reverse=True)
# position = 1
# for team, points in sorted_teams:
#     if "wins" in results[team]:
#         win_count = results[team]["wins"]
#     else:
#         win_count = 0
#     if "draws" in results[team]:
#         draw_count = results[team]["draws"]
#     else:
#         draw_count = 0
#     if "losses" in results[team]:
#         lose_count = results[team]["losses"]
#     else:
#         lose_count = 0
#
#     print(f"{position}. {team} - {points}pts (W:{win_count}/D:{draw_count}/L:{lose_count})")
#     position += 1