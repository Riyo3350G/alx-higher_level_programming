#!/usr/bin/python3
def print_tebahpla():
    res = ""
    for c in range(122, 96, -1):
        if c % 2 == 0:
            res += chr(c)
        else:
            ores += chr(c - 32)
    print(res, end="")


print_tebahpla()
