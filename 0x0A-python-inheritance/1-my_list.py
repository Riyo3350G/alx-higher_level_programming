#!/usr/bin/python3
"""
module contains class MyList
"""


class MyList(list):
    """ define the class """

    def __init__(self):
        """init"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
