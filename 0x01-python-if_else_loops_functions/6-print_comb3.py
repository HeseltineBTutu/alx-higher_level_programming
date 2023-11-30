#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens, 10):
        if tens != ones:
            print("{:d}{:d}".format(tens, ones), end=', ' if tens != 9 or ones != 9 else '\n')
