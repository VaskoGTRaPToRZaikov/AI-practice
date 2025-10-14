message = input().strip()
if not message:
    print("")
    exit()

message_list = list(message.split())
encrypted_message = []


for word in message_list:
    if len(word) == 1:
        encrypted_message.append(word)
        continue
    if len(word) == 2:
        encrypted_message.append(word[1] + word[0])
        continue

    current_list = list(word)
    current_list[0], current_list[-1] = current_list[-1], current_list[0]

    for index in range(1, len(word) - 1):
        current_list[index] = str(ord(current_list[index]))

    encrypted_message.append("-".join(current_list))

print(" ".join(encrypted_message))




