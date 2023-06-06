#!/usr/bin/env python3
def print_tebahpla():
    for c in range(122, 96, -1):
        if c % 2 == 0:
            print(chr(c), end="")
        else:
            print(chr(c - 32), end="")


print_tebahpla()
