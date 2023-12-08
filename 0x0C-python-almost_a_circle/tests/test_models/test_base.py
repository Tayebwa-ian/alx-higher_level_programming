#!/usr/bin/python3
"""Testing base class module"""
import unittest
from models import base


class TestBase(unittest.TestCase):
    """Test case for base class"""
    def setUp(self):
        """Create some class objects to use in testing"""
        self.obj = base.Base()

    def test_module_doc(self):
        """check if module catains documentation"""
        self.assertGreater(len(base.__doc__), 0)

    def test_class_doc(self):
        """check if class has documentation"""
        self.assertGreater(len(self.obj.__doc__), 0)

    def test_access_to_private_atrr(self):
        """Check if the private class attribute raises error if
        you try to access it via the object"""
        with self.assertRaises(AttributeError):
            self.obj.__nb_objects

if __name__ == "__main__":
    unittest.main()
