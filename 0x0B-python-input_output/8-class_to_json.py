#!/usr/bin/python3
"""
A module dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Serialize an object into a dictionary with simple
    data structures for JSON compatibility.

    Args:
    - obj: An instance of a class

    Returns:
    - Dictionary description of the object's attributes

    Note: This function assumes all attributes of the
    object are serializable.
    """
    serializable_attributes = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[attr] = value

    return serializable_attributes
