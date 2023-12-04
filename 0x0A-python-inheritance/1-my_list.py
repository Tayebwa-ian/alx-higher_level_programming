#!/usr/bin/python3
""" Mylist Module"""


class MyList(list):
    """Perform list operations
    """
    def __init__(self):
        """intializing the class with an item"""
        self.mylist = []
        super().__init__()

    def append(self, item):
        """Adds item to the list
        Param:
          item: the integer item to add to the list
        Raises:
          TypeError: if item is not an integer
        Return: a new list with appended item
        """
        if type(item) is int:
            self.mylist.append(item)
        else:
            raise TypeError("This list allows only integer items to be added")

    def print_sorted(self):
        """Arrange items in the list in ascending order"""
        print(sorted(self.mylist))

    def __str__(self):
        """Return a string representation of the object of this class"""
        return("{}".format(self.mylist))
