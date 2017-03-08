import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
LETTERS = "aeioubcdfghjklmnpqrstvwxyz"
WORD_SIZE = 10

word_format = random.choice(LETTERS)
for i in range(1,WORD_SIZE,1):
    word_format += random.choice(LETTERS)
#str(input("please enter your word to convert")).lower()
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(LETTERS)
    else:
        word += kind
print(word)