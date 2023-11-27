#!/usr/bin/python3
"""Say_my_name module"""


def say_my_name(first_name, last_name=""):
    """prints full name
    Args:
      first_name: first name
      last_name: last name
    Raises:
      TypeError: if either first_name or last_name is not a str
    Returns: full name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
