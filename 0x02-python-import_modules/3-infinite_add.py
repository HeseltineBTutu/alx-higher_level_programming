#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    args = sys.argv[1:]
    for i in range(len(args)):
        count += int(sys.argv[i + 1])
    print("{}".format(count))
