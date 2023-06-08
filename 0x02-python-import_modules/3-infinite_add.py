#!/usr/bin/python3

import sys
if __name__ == "__main__":
    rev = 0
    arg_ctr = len(sys.argv)
    if arg_ctr == 1:
        print("0")
    else:
        for i in range(1, arg_ctr):
            rev += int(sys.argv[i])
        print(rev)
