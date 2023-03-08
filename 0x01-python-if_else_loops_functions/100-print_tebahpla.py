#!/usr/bin/python3
for letter in range(ord('z'), ord('a')-1, -1):
    print(chr(letter).upper() if (letter-ord('a')) % 2 == 0 else chr(letter), end="")
