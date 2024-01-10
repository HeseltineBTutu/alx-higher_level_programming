#!/usr/bin/python3
"""
A module writes an Object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes ojject to a text file
    using JSON representation.

    Attributes:
    - my_obj - the object to be written.
    - filename - The name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
