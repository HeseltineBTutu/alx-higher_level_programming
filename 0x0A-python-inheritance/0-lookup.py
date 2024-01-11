#!/usr/bin/python3
"""
Module: 0-lookup

This module provides a function for looking up attributes
and methods of an object.
"""


def lookup(obj):
    """
    Obtain a list of attributes and methods associated with an object.

    Arguments:
    - obj: An object for which attributes and methods are to be looked up.

    Returns:
    - A list containing the names of attributes and methods
    associated with the object.
    """
    my_list = []

    for items in dir(obj):
        my_list.append(items)
    return my_list
