#!/usr/bin/python3
"""Function that returns True if object is instance of a given class"""


def is_same_class(obj, a_class):
    """ check if object is isnatnce of a class given
    Params:
      obj: the object to check
      a_class: the class to check against
    Return: True if object is instance and false otherwise
    """
    return type(obj) is a_class
