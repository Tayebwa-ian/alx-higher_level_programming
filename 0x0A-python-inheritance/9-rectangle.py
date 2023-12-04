#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The rectangle class"""
    def __init__(self, width, height):
        """intialization of the class
        Params:
          width: width of the rectangle
          height: Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calaculate the area of a rectangle
        Return: area
        """
        return self.__width * self.__height

    def __str__(self):
        """returns the string rep of the object"""
        return("[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height))
