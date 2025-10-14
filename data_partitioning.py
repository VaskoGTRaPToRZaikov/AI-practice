text = input().strip()

if not text:
    print("")
    exit()

text = text.split()

while True:
    command = input().strip()
    if command == "done":
        break

    actions = command.split()
    action = actions[0]

    if action == "split":
        index, parts = int(actions[1]), int(actions[2])
        if index < len(text) and parts > 0 and parts <= len(text[index]):

            parts_size = len(text[index]) // parts
            extra = len(text[index]) % parts

            equal_substrings = []
            position = 0

            for i in range(parts):
                size = parts_size + (1 if i < extra else 0)
                equal_substrings.append(text[index][position:position + size])
                position += size
            text[index:index + 1] = equal_substrings

    elif action == "join":
        start, end = int(actions[1]), int(actions[2])

        if 0 <= start <= end < len(text):

            substrings_merge = "".join(text[start:end + 1])
            text[start:end + 1] = [substrings_merge]

print(" ".join(text))
