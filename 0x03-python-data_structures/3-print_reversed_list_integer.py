#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_integer = my_list[::-1]
    for integer in reversed_integer:
        print("{:d}".format(integer))
