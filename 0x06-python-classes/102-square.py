#!/usr/bin/python3
""" Square module """


class Square:
    """Perform square operations"""
    def __init__(self, size=0):
        """Initialisation of the square class

        Args:
          -size (int): length of the square
        Returns: None
        """
        self.__size = size

    def area(self):
        """calculate area of a square
        Returns: the result
        """
        return self.__size**2

    @property
    def size(self):
        """Get the size attribute
        Return: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
          -value: size of the square
        Raises:
          -ValueError: if value is less )
          -TypeError: if value is negative
        Return: None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
