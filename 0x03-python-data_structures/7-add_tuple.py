#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Handling tuples smaller than 2 elements by padding with 0
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]

    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
