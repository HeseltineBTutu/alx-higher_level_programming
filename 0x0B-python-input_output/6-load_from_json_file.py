#!/usr/bin/python3
"""
A module that deals whith deserialization
of objects
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a
    JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
    return x
