libraries = {}

while True:
    info = input()

    if info == "end of registrations":
        break

    capacity_info = info.split(":")
    library, capacity = capacity_info[0], int(capacity_info[1])
    libraries[library] = {}
    libraries[library] = {"capacity": capacity, "books": {}}

while True:
    books_info = input()

    if books_info == "end of books":
        break

    parts = books_info.split("=>")
    library, book, author, copies = parts[0], parts[1], parts[2], int(parts[3])

    if library in libraries:
        current_total = sum(libraries[library]["books"].values())
        if current_total + copies <= libraries[library]["capacity"]:
            key = f"{book}|{author}"
            libraries[library]["books"][key] = libraries[library]["books"].get(key, 0) + copies

totals = {library: sum(libraries[library]["books"].values()) for library in libraries}

if totals:
    most_popular_library = max(totals, key=totals.get)
    print(f"Most popular library: {most_popular_library} with {totals[most_popular_library]} books")

sorted_libraries = sorted(libraries.keys())

for library in sorted_libraries:
    print(library)
    book_items = list(libraries[library]["books"].items())
    sorted_books = sorted(book_items, key=lambda x: (-x[1], x[0].split("|")[0]))

    for key, current_copies in sorted_books:
        book, author = key.split("|")
        print(f"  {book} by {author}: {current_copies} copies")