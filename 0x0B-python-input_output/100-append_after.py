#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    insrtd_text = ""
    with open(filename) as f:
        for line in f:
            insrtd_text += line
            if search_string in line:
                insrtd_text += new_string
    with open(filename, "w") as r:
        r.write(insrtd_text)
