#!/usr/bin/python3
"""base_geometry module"""


class BaseGeometry:
    """create a class"""

    def area(self):
        """create a public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value if positive """
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
