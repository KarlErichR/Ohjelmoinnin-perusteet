print("Program starting.")
print("String comparisons")
word = input("Insert first word: ")
char = input("Insert a character: ")
if char in word:
    print(f"Word \"{word}\" contains character \"{char}\"")
else:
    print(f"Word \"{word}\" doesn't contain character \"{char}\"")
word2 = input("Insert second word: ")
if word<word2:
    print(f"The first word \"{word}\" is before the second word \"{word2}\"")
elif word>word2:
    print(f"The second word \"{word2}\" is before the first word \"{word}\"")
elif word ==word2:
    print(f"Both inserted words are the same alphabetically, \"{word}\"")
print("Program ending.")