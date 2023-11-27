#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Perform operations on rectangles"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve width value of the rectangle
        Return: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of rectangle width
        Args:
          -Value: value of the rectangle width
        Raises:
          -TypeError: if width is not a integer
          -ValueError: if width is less than 0
        Returns: None
        """
        lst = [int, float]
        if type(value) not in lst:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height value of the rectangle
        Return: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of rectangle height
        Args:
          -Value: value of the rectangle height
        Raises:
          -TypeError: if height is not a integer
          -ValueError: if height is less than 0
        Returns: None
        """
        lst = [int, float]
        if type(value) not in lst:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
