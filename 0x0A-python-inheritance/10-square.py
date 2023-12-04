#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle class"""
    def __init__(self, size):
        """Overrides the supper class init func to make it a square"""
        Rectangle.__init__(self, size, size)
