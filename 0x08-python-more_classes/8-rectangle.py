#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Perform operations on rectangles"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intialises the class and calculates number of instances formed
        Args:
          -width: rectangle width
          -height: rectangle height
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width value of the rectangle
        Return: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of rectangle width
        Args:
          -Value: value of the rectangle width
        Raises:
          -TypeError: if width is not a integer
          -ValueError: if width is less than 0
        Returns: None
        """
        lst = [int, float]
        if type(value) not in lst:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height value of the rectangle
        Return: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of rectangle height
        Args:
          -Value: value of the rectangle height
        Raises:
          -TypeError: if height is not a integer
          -ValueError: if height is less than 0
        Returns: None
        """
        lst = [int, float]
        if type(value) not in lst:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle
        Return: Area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """calculate rectangle perimeter
        Return: parameter if width of height is not zero and 0 otherwise
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """string representation of a printable rectangle object
        Returns: a string of #character of a rectangle or empty string
        """
        result = ""
        if self.height == 0 or self.width == 0:
            return result
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.print_symbol)
            if i != (self.height - 1):
                result += "\n"
        return result

    def __repr__(self):
        """string representation of a printable rectangle object
        Returns: a recreatable string object representation
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message before destroying an instance
        Also reduces the number of instances when one is destroyed
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find the bigger rectangle based of area
        Args:
          rect_1: the first rectangle
          rect_2: the seconf rectangle
        Rasies:
          TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        Returns: Bigger traingle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
