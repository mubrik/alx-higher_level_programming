#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        result = max_integer([])
        self.assertIs(result, None)

    def test_all_equal(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
