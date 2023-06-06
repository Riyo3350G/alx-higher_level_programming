#!/usr/bin/python3
for digit in range(0, 100):
    if digit == 99:
        print("{0:02d}".format(digit), end="\n")
    else:
        print("{:02d}, ".format(digit), end="")
    
