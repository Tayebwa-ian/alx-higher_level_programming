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
