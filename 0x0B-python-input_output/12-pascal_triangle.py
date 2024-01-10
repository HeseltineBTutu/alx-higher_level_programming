#!/usr/bin/python3
"""
A function that generates pascal triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of
    integer representing the Pascal's triangle
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j-1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
