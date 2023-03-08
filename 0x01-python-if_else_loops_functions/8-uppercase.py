#!/usr/bin/python3
def uppercase(str):
    """Function that prints a string in uppercase"""
    for char in str:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{0}".format(uppercase_char), end="")
    print()
