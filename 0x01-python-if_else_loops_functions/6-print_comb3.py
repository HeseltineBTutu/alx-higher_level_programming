#!/usr/bin/python3
for num in range(10):
    for j in range(num+1, 10):
        if num == 0 and j == 1:
            print("01", end=", ")
        else:
            print("{0:02d}".format(10*num+j), end=", ")
print("{0:02d}".format(89))
