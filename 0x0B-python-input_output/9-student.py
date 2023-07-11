#!/usr/bin/python3
"""student module"""


class Student:
    """class represent a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a dictionary representation of the Student"""
        return self.__dict__
