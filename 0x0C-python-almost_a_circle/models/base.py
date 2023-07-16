#!/usr/bin/python3
"""base Module"""


class Base:
    """Base class"""
    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
