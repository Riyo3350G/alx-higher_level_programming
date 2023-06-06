#!/usr/bin/python3
for digit in range(0, 100):
    print("{:02d}, ".format(digit), end="")
    if digit == 99:
        print("{0:02d}".format(digit), end="\n")
