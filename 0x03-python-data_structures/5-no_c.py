#!/usr/bin/python3

def no_c(my_string):
    skipped_characters = ['c', 'C']
    result = ''.join(
            char for char in my_string if char not in skipped_characters
            )
    print(result)
    return result
