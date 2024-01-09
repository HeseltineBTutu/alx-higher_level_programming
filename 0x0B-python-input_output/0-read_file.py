#!/usr/bin/python3
"""
This module reads from a file
"""


def read_file(filename=""):
    """
    A function  that reads a file.

    Attributes:
    - filename - the name of the file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
