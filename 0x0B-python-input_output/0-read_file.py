#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, encoding="UTF8") as f:
        lines = f.read()
    print(lines, end="")
    f.close()
