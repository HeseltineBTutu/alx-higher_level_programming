#!/usr/bin/python3

output = ''
for char_code in range(122, 96, -1):
    char = chr(char_code)
    if (122 - char_code) % 2 == 0:
        output += "{}".format(char.lower())
    else:
        output += "{}".format(char.upper())
print(output, end='')
