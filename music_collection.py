music_collection = {}

while True:
    info = input()

    if info == "play music":
        artist_info = input()
        break

    parts = info.split("|")

    artist, album, song, duration = parts[0], parts[1], parts[2], int(parts[3])

    if artist not in music_collection:
        music_collection[artist] = {}

    if album not in music_collection[artist]:
        music_collection[artist][album] = {}

    music_collection[artist][album][song] = duration

if artist_info in music_collection:
    albums = music_collection[artist_info]
    print(f"{artist_info}:")

    sorted_albums = sorted(albums.items(), key=lambda x: sum(x[1].values()), reverse=True)

    for current_album, current_song in sorted_albums:
        total_duration = sum(current_song.values())
        print(f"Album: {current_album} ({total_duration}s)")

        sorted_songs = sorted(current_song.items(), key=lambda x: x[1], reverse=True)
        for song, durations in sorted_songs:
            print(f"-- {song} ({durations}s)")

else:
    print("Invalid artist")





