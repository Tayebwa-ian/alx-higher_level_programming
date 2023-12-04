#!/usr/bin/python3
"""Rectangle Module"""


class BaseGeometry:
    """ The base geometry class
    """
    def area(self):
        """calculate the area of the polygon
        Raises:
          Expection: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer argument
        Raises:
          TypeError: if value is not  integer
          ValueError: if value is less than zero
        Return: the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".
                            format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".
                             format(name))
        return name

class Rectangle(BaseGeometry):
    """The rectangle class"""
    def __init__(self, width, height):
        """intialization of the class
        Params:
          width: width of the rectangle
          height: Height of the rectangle
        """
        self.width =self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
