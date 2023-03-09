#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)
if num_args == 1:
    print("1 argument:")
elif num_args == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(num_args))

for i in range(num_args):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
