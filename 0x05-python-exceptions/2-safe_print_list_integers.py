#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ctr = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            ctr += 1
        except (TypeError, ValueError):
            pass
    print()
    return ctr
