#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name from arguments

    num_args = len(arguments)

    if num_args == 0:
        print("0 arguments.")
    else:
        plural = 's' if num_args != 1 else ''
        print(f"{num_args} argument{plural}:")

        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

