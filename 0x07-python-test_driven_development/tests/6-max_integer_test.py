#!/usr/bin/python3
"""Unit tests modules for max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_correct_inputs(self):
        """Test with all possible correct expected inputs"""
        self.assertEqual(max_integer([3, 4, 56, 78, 2, 9]), 78)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, -4, -5, 5, 3]), 5)
        self.assertEqual(max_integer([1, 2, 3.3]), 3.3)

    def test_wrong_inputs(self):
        """Test with all possible wrong input values"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([9, 0, "seed"])
        with self.assertRaises(TypeError):
            max_integer([8, 4, []])
        with self.assertRaises(TypeError):
            max_integer(8)

if __name__ == "__main__":
    unittest.main()
