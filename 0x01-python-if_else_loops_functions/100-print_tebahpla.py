#!/usr/bin/python3

characters = range(122, 96, -1)
result = ''
for i, char in enumerate(characters):
    if i % 2 == 0:
        result += chr(char).lower()
    else:
        result += chr(char).upper()
print(result)
