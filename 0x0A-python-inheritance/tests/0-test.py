#!/usr/bin/python3
"""Unittest for lookup module
"""
import unittest
lookup = __import__('0-lookup').lookup


class TestLookup(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(TypeError) as cm:
            result = lookup()

    def test_none(self):
        result = lookup(None)
        self.assertIsInstance(result, list)

    def test_correct(self):
        result = lookup([])
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
