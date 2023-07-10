#!/usr/bin/python3
"""base_geometry module"""


class BaseGeometry:
    """create a class"""

    def area(self):
        """create a public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator of integers"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
