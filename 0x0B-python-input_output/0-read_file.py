#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Read a text file
    Params:
      filename: the name of the file to use
    Return: NULL
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
