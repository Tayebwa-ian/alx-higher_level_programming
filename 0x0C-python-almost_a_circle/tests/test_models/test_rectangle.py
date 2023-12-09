#!/usr/bin/python3
"""Testing rectangle class module"""
import unittest
from models import rectangle


class TestRectangle(unittest.TestCase):
    """Test several case for a rectangle"""
    def setUp(self):
        """create rectangle objects to use"""
        self.obj1 = rectangle.Rectangle(10, 2)
        self.obj2 = rectangle.Rectangle(10, 2, 0, 0, 12)

    def test_missing_params(self):
        """check if an instance is successfully created
        with some missing params"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle()
        with self.assertRaises(TypeError):
            rectangle.Rectangle(3)

    def test_width_setting(self):
        """check for setting and retrieving width functions"""
        self.obj1.width = 3
        self.obj2.width = -2
        self.assertEqual(self.obj1.width, 3)
        self.assertEqual(self.obj2.width, -2)

    def test_height_setting(self):
        """check for setting and retrieving height functions"""
        self.obj1.height = 3
        self.assertEqual(self.obj1.height, 3)

    def test_x_setting(self):
        """check for setting and retrieving x functions"""
        self.obj1.x = 3
        self.assertEqual(self.obj1.x, 3)

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

