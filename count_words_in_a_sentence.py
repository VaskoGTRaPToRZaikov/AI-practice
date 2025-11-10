words = input().split()

words_counter = {}
word = ""

for text in words:
    word = ''.join(char for char in text if char.isalpha()).lower()
    if word:
        if word not in words_counter:
            words_counter[word] = 0
        words_counter[word] += 1

sorted_counter = sorted(words_counter.items())

for word, count in sorted_counter:
    print(f"{word} -> {count}")