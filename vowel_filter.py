text = [text.strip() for text in input().split()]
vowel_list = ["a", "e", "i", "o", "u"]
vowel_word = [word for word in text if len(word) > 0 and
              word[0].lower() in vowel_list and word[-1].lower() in vowel_list]

print("\n".join(vowel_word))



