#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle class"""
    def __init__(self, size):
        """Overrides the supper class init func to make it a square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calaculate the area of a rectangle
        Return: area
        """
        return self.__size * 2