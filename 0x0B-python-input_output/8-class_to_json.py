#!/usr/bin/python3
"""
A module dictionary description with simple data structure
"""
import json


def class_to_json(obj):
    """
    a function that returns the dictionary description
    with simple data structures

    Attributes:
    - obj - serialized objected
    """
    json_data = json.dumps(obj.__dict__)
    return json_data
