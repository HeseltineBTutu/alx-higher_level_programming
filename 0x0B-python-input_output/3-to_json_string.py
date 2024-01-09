#!/usr/bin/python
import json
"""
A module representing JSON object
"""


def to_json_string(my_obj):
    """
    A function that returns the JSON representation
    of an object
    """
    x = json.dumps(my_obj)
    return x
