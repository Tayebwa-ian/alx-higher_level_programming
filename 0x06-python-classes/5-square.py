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

    def my_print(self):
        """Prints square of #s to the stdout
        Return: None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
