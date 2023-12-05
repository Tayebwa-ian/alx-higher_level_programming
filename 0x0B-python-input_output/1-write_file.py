#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """write to a file
    Params:
      filename: the name of the file to write to
      text: the message to write to the file
    Return: Number of characters written to a file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
