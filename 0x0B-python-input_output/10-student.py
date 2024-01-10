#!/usr/bin/python3
"""
A class that defines a student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            # If attrs is None or not provided, retrieve all attributes
            return self.__dict__

        filtered_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attrs[attr] = getattr(self, attr)

        return filtered_attrs
