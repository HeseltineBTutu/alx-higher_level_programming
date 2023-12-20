#!/usr/bin/python3
"""
This module contains functionalities related to geometric shapes.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - size (int): The size of the square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
