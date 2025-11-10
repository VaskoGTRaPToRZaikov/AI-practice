library_data = {}

while True:
    command = input()

    if command == "library close":
        break

    parts = command.split("-")
    book_title, reader_name, days = parts[0], parts[1], int(parts[2])

    if book_title not in library_data:
        library_data[book_title] = {"reader": reader_name, "days": days}

    if reader_name == library_data[book_title]["reader"]:
        if library_data[book_title]["days"] > days:
            library_data[book_title]["days"] = days

for book, info in library_data.items():
    reader = info["reader"]
    remaining_days = info["days"]
    print(f"{book} -> {reader} ({remaining_days} days)")

