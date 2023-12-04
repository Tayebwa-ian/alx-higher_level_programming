#!/usr/bin/python3
"""Base Geometry module"""


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
          ValeError: if value is less than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".
                            format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".
                             format(name))
