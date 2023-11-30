#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)
    print(result)
