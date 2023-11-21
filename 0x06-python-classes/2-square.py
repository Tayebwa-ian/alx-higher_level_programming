#!/usr/bin/python3
""" Square module """


class Square:
    """Perform square operations"""
    def __init__(self, size=0):
        """Initialisation of the square class

        Args:
          -size (int): length of the square
        Raises:
          -ValueError: when size is negative number
          -TypeError: when size is not and integer
        Returns: nothing
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
