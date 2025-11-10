tournament_standing = {}

while True:

    info = input()

    if info == "tournament end":
        break

    if "->" in info:
        parts = info.split("->")
        player_name, game_name, player_points = parts[0], parts[1], int(parts[2])

        if player_name not in tournament_standing:
            tournament_standing[player_name] = {}

        if player_points > tournament_standing[player_name].get(game_name, 0):
            tournament_standing[player_name][game_name] = player_points
    elif " vs " in info:
        first_player, second_player = info.split(" vs ")
        if (first_player in tournament_standing and second_player in tournament_standing
                and any(game in tournament_standing[first_player] for game in tournament_standing[second_player])):
            first_player_total_points = sum(tournament_standing[first_player].values())
            second_player_total_points = sum(tournament_standing[second_player].values())

            if first_player_total_points > second_player_total_points:
                del tournament_standing[second_player]
            elif second_player_total_points > first_player_total_points:
                del tournament_standing[first_player]


sorted_players = sorted(tournament_standing, key=lambda x: (-sum(tournament_standing[x].values()), x))

for player in sorted_players:
    total_points = sum(tournament_standing[player].values())
    print(f"{player} - {total_points} points")
    games = sorted(tournament_standing[player].items(), key=lambda x: -x[1])
    for game, point in games:
        print(f"  {game}: {point}")

