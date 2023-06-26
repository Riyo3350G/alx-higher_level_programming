#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ctr = 0

    for index in range(0, x):
        try:
            print(f"{my_list[index]}", end="")
            ctr += 1
        except IndexError:
            break
    print()
    return (ctr)
