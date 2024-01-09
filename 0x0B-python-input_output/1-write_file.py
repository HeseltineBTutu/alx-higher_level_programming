#!/usr/bin/python3
"""
A module that writes a file
"""


def write_file(filename="", text=""):
    """
    A function that writes to a file

    Attributes:
    - filename - name of the  file
    - text - the text to be written
    """
    with open(filename, 'w', encoding= 'utf-8') as f:
        data = f.write(text)
    return data
