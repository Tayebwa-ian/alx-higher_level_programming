#!/usr/bin/python3
""" Square module """


class Square:
    """Perform square operations"""
    def __init__(self, size=0, position=(0,0)):
        """Initialisation of the square class

        Args:
          -size (int): length of the square
        Returns: None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position attribute
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position attribute
        Args:
          -value: a tupe of two integers
        Raises:
          -TypeError: if value is not a tuple of 2 integers
        Return: None
        """
        if (type(value) != tuple or
            len(value) != 2) or (type(value[0]) != int or
                                 type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__poistion = value

    def my_print(self):
        """Prints square of #s to the stdout
        Return: None
        """
        if self.__size == 0:
            print()
        else:
            print("\n"*self.__position[1], end="")
            for i in range(self.__size):
                for n in range(self.__position[0]):
                    print("_", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
