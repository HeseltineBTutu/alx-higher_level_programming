#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name from arguments

    num_args = len(arguments)
    plural = 's' if num_args != 1 else ''
    end_char = '.' if num_args == 0 else ':'
    
    print(f"Number of argument{plural}: {num_args}{end_char}")

    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")

