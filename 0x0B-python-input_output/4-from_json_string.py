#!/usr/bin/python3
"""
A module representing Json String
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object
    represented by a JSON string
    """
    x = json.loads(my_str)
    return x
