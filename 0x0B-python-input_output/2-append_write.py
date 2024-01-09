#!/usr/bin/python3
"""
A module for appending a file
"""


def append_write(filename="", text=""):
    """
    A function for appending a file
    
    Attributes:
    - filename - The name of the file
    - text - The text to be appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        appended_data = f.write(text)
    return appended_data
