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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        my_perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            my_perimeter = 0
        return my_perimeter

    def __str__(self):
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print(f"Bye rectangle...")
