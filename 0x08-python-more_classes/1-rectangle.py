#!/usr/bin/python3
"""
This module contains functionalities related to geometric shapes.
"""


class Rectangle:
    """
    A class Representing a rectangle.

    Attributes:
    - width (int): The width of the rectangle
    - height (int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    try:
        myrectangle = Rectangle(-2, 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
