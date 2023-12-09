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
        Return: None
        """
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
        Returns: None
        """
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
        Returns: None
        """
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
        Returns: None
        """
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
        Returns: None
        """
        self.__y = value
