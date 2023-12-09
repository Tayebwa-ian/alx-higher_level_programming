#!/usr/bin/python3
"""Rectangle Module"""
from .base import Base


class Rectangle(Base):
    """Rectangle class that inerits from the base class
    Performs rectangle operations
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Intializes rectangle class
        Params:
          width: rectangle width
          height: rectangle height
          x: instance attribute
          y:: another instance attribute
          id: id of the created object
        Raises:
          TypeError: if width, height, x or y is not integer
          ValueError: if width and height are <= 0 or if x and y are < 0
        Return: None
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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
          TypeError: if value is not an integer
          ValueError: if value is less or equal to zero
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
          TypeError: if value is not an integer
          ValueError: if value is less or equal to zero
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Retrieve x
        Return: height of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x
        Args:
          -Value: value of x
        Raises:
          TypeError: if value is not an integer
          ValueError: if value is less than zero
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Retrieve y
        Return: height of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y
        Args:
          -Value: value of y
        Raises:
          TypeError: if value is not an integer
          ValueError: if value is less than zero
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
