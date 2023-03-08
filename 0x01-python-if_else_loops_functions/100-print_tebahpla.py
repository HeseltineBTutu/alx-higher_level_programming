#!/usr/bin/python3
for letter in range(90, 64, -1):
    print("{0}{1}".format(chr(letter + 32) if letter % 2 == 0 else chr(letter), ""), end="")
