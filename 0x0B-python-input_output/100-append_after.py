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

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
