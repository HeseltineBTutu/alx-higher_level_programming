#!/usr/bin/python3
def uppercase(str):
    """Function that prints a string in uppercase"""
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}{}".format(result, ""))
