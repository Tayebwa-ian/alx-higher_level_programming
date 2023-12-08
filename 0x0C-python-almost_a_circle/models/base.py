#!/usr/bin/python3
"""Models Module"""


class Base:
    """This class will be the “base” of all other classes
    Attr:
      __nb_objects: numbers of objects created from this class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Intialization of this class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
