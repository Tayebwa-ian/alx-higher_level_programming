#!/usr/bin/python3
"""Testing rectangle class module"""
import unittest
from models import rectangle, base


class TestRectangle(unittest.TestCase):
    """Test several case for a rectangle"""
    def setUp(self):
        """create rectangle objects to use"""
        self.obj1 = rectangle.Rectangle(10, 2)
        self.obj2 = rectangle.Rectangle(4, 2, 0, 0, 12)

    def test_missing_params(self):
        """check if an instance is successfully created
        with some missing params"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle()
        with self.assertRaises(TypeError):
            rectangle.Rectangle(3)

    def test_instantiation_with_invalid_input(self):
        """Check for Creation of instances with invalid inputs"""
        with self.assertRaises(ValueError):
            rectangle.Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(4, -3)
        with self.assertRaises(ValueError):
            rectangle.Rectangle(10, 2, 0, -2)
        with self.assertRaises(TypeError):
            rectangle.Rectangle("2", 8)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(4, 2, "0", 0)

    def test_width_setting(self):
        """check for setting and retrieving width functions"""
        self.obj1.width = 3
        self.assertEqual(self.obj1.width, 3)

    def test_height_setting(self):
        """check for setting and retrieving height functions"""
        self.obj1.height = 3
        self.assertEqual(self.obj1.height, 3)

    def test_x_setting(self):
        """check for setting and retrieving x functions"""
        self.obj1.x = 3
        self.obj2.x = 0
        self.assertEqual(self.obj1.x, 3)
        self.assertEqual(self.obj2.x, 0)

    def test_y_setting(self):
        """check for setting and retrieving y functions"""
        self.obj1.y = 4
        self.assertEqual(self.obj1.y, 4)

    def test_documentation(self):
        """check for module, class and methods documentation"""
        self.assertGreater(len(rectangle.__doc__), 0)
        self.assertGreater(len(self.obj2.__doc__), 0)
        self.assertGreater(len(self.obj2.width.__doc__), 0)
        self.assertGreater(len(self.obj2.height.__doc__), 0)
        self.assertGreater(len(self.obj2.x.__doc__), 0)
        self.assertGreater(len(self.obj2.y.__doc__), 0)
        self.assertGreater(len(self.obj2.__init__.__doc__), 0)

    def test_invalid_width_input(self):
        """set width value with invalid input"""
        with self.assertRaises(TypeError):
            self.obj1.width = "1"
        with self.assertRaises(TypeError):
            self.obj2.width = [1,2]
        with self.assertRaises(TypeError):
            self.obj1.width = 4.3
        with self.assertRaises(ValueError):
            self.obj1.width = 0
        with self.assertRaises(ValueError):
            self.obj2.width = -3

    def test_invalid_height_input(self):
        """set height value with invalid input"""
        with self.assertRaises(TypeError):
            self.obj1.height = "1"
        with self.assertRaises(TypeError):
            self.obj2.height = 1.83
        with self.assertRaises(ValueError):
            self.obj1.height = 0
        with self.assertRaises(ValueError):
            self.obj2.height = -3

    def test_invalid_x_input(self):
        """set x value with invalid input"""
        with self.assertRaises(TypeError):
            self.obj1.x = "1"
        with self.assertRaises(TypeError):
            self.obj2.x = [1,2]
        with self.assertRaises(TypeError):
            self.obj1.x = 4.3
        with self.assertRaises(ValueError):
            self.obj2.x = -3

    def test_invalid_y_input(self):
        """set y value with invalid input"""
        with self.assertRaises(TypeError):
            self.obj1.y = "1"
        with self.assertRaises(TypeError):
            self.obj2.y = [1,2]
        with self.assertRaises(TypeError):
            self.obj1.y = 4.3
        with self.assertRaises(ValueError):
            self.obj2.y = -3

    def test_rectangle_area(self):
        """Test for correct output value for area of the rectangle"""
        self.assertEqual(self.obj1.area(), 20)
        self.assertEqual(self.obj2.area(), 8)

    def test_rectangle_inheritance(self):
        """check if rectangle inherits from base class"""
        self.assertIsInstance(self.obj1, type(base.Base()))
        self.assertIsInstance(self.obj2, type(base.Base()))

    def test_update(self):
        """Check updating function works with args and kwargs"""
        self.obj1.update(2, 5, 8, 9, 2)
        self.obj2.update(6)
        self.assertEqual(self.obj1.id, 2)
        self.assertEqual(self.obj1.area(), 40)
        self.assertEqual(self.obj2.id, 6)
        with self.assertRaises(TypeError):
            self.obj1.update(1, "3", 4)
        with self.assertRaises(ValueError):
            self.obj1.update(1, 3, 0)
        with self.assertRaises(TypeError):
            self.obj1.update(1, 4, 3, "2")
        with self.assertRaises(ValueError):
            self.obj1.update(2, 4, 5, 0, -2)
        self.obj2.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(self.obj2), "[Rectangle] (2) 2/2 - 2/2")
        self.obj2.update(width=4)
        self.assertEqual(self.obj2.width, 4)
        with self.assertRaises(TypeError):
            self.obj2.update(y="2")
