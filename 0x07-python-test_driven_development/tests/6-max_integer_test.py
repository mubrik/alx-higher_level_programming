#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        result = max_integer([])
        self.assertIs(result, None)

    def test_one_num(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_all_equal(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_max_start(self):
        result = max_integer([10, 5, 5, 5])
        self.assertEqual(result, 10)

    def test_max_end(self):
        result = max_integer([10, 5, 5, 21])
        self.assertEqual(result, 21)

    def test_max_middle(self):
        result = max_integer([10, 5, 50, 5, 21])
        self.assertEqual(result, 50)

    def test_one_neg(self):
        result = max_integer([10, -1, 50, 5, 21])
        self.assertEqual(result, 50)

    def test_all_neg(self):
        result = max_integer([-10, -1, -50, -5, -21])
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
