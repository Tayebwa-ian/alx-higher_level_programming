#!/usr/bin/python3
"""append string to end of the file"""


def append_write(filename="", text=""):
    """append to the file
    Params:
      filename: the name of the file to append to
      text: the text to add to the file
    Return: number of bytes added
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
