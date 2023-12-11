#!/usr/bin/python3
"""Testing base class module"""
import unittest
from models import base
import json


class TestBase(unittest.TestCase):
    """Test case for base class"""
    def setUp(self):
        """Create some class objects to use in testing"""
        self.obj = base.Base()

    def test_class_doc(self):
        """check if class has documentation"""
        self.assertGreater(len(self.obj.__doc__), 0)

    def test_access_to_private_atrr(self):
        """Check if the private class attribute raises error if
        you try to access it via the object"""
        with self.assertRaises(AttributeError):
            self.obj.__nb_objects

    def test_too_many_args(self):
        """testing too many args to init"""
        with self.assertRaises(TypeError):
            base.Base(1, 1)

    def test_to_json_string(self):
        """Testing regular to json string"""
        base.Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = base.Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """Test for passing empty list"""
        json_s = base.Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        """testting None to a json"""
        json_s = base.Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests normal from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
        {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = base.Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_frjs_empty(self):
        """Tests from_json_string  empty string"""
        self.assertEqual([], base.Base.from_json_string(""))

    def test_frjs_None(self):
        """Testing from_json_string   none string"""
        self.assertEqual([], base.Base.from_json_string(None))

if __name__ == "__main__":
    unittest.main()
