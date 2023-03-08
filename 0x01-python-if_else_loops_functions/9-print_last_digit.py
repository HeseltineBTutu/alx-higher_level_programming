#!/usr/bin/python3
def print_last_digit(number):
    """a function that prints the last digit of a number"""
    result = abs(number) % 10
    print(result)
    return result
