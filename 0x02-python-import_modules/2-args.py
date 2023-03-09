#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)
if num_args == 1:
    print("1 argument:", end=' ')
elif num_args > 1:
    print("{} arguments:".format(num_args), end=' ')

if num_args == 0:
    print(".")
else:
    print()

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))


