first_sequence = [text.strip() for text in input().split(",")]
second_sequence = [text.strip() for text in input().split(",")]

new_list = [subword for subword in second_sequence if
            any(subword in word for word in first_sequence)]


print(new_list)
