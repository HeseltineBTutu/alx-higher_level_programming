#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_args = sum(int(arg) for arg in arguments)
    print(num_args)
