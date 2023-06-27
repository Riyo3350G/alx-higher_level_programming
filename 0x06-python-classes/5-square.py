#!/usr/bin/python3
""" class that defines a square"""


class Square:
    """ class that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the area.

        Returns:
            ares.
        """
        return self.__size**2

    @property
    def size(self):
        """Getter for size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

   def my_print(self):
       """print the square. """

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
