#!/usr/bin/python3
for alpha_lower in range(ord('a'), ord('z') + 1):
    if alpha_lower != ord('e') and alpha_lower != ord('q'):
        print("{:c}".format(alpha_lower), end="")
