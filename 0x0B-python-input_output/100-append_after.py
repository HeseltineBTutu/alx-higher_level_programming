#!/usr/bin/python3
"""
A module for searching and updating file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Searches for a specific word in a file and updates it with a replacement.

    Args:
    - filename (str): The name of the file to be searched and updated.
    - search_string (str): The word to be searched in the file.
    - new_string (str): The word to replace the search_word if found.

    Returns:
    None
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    found = False
    for i, line in enumerate(lines):
        if search_string in line:
            lines[i] = line.replace(search_string, new_string)
            found = True

    if found:
        with open(filename, 'w') as f:
            f.writelines(lines)
