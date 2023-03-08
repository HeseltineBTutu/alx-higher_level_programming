#!/usr/bin/python3
def remove_char_at(str, n):
    """
    This function creates a copy of the input string, removing the character
    at the position n.

    Parameters:
        str (str): the input string
        n (int): the position of the character to remove (0-based index)

    Returns:
        str: a copy of the input string with
        the character at position n removed
    """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
