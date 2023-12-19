#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            if count < x:
                try:
                    value = int(element)
                    print("{:d}".format(value), end="")
                    count += 1
                except ValueError:
                    pass
            else:
                break
    except TypeError:
        pass
    print()
    return count
