version = [int(number.strip()) for number in input().split(".")]

for i in range(len(version) - 1, -1, -1):
    if version[i] > 0:
        version[i] -= 1
        break
    else:
        version[i] = 9
        if i > 0:
            version[i - 1] -= 1

print(".".join(map(str, version)))
