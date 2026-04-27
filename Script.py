text = input("Enter a string: ")
words = text.strip().split()
last_word_length = len(words[-1])
print("Length of last word:", last_word_length)