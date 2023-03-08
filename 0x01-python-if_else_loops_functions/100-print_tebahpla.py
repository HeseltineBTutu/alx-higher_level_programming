#!/usr/bin/python3
for letter in range(90, 64, -1):
    if letter % 2 == 0:
        letter = chr(letter + 32)
    else:
        letter = chr(letter)
    print("{0}".format(letter), end="")
