#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


class TestOne(unittest.TestCase):

    def setUp(self):
        self.rect = __import__('1-rectangle').Rectangle

    def test_new_empty(self):
        new_rect = self.rect()
        self.assertEqual(new_rect.width, 0)
        self.assertEqual(new_rect.height, 0)

    def test_new_none(self):
        # expecting a type exception, using context manager
        with self.assertRaises(TypeError) as cm:
            new_rect = self.rect(None, None)
        # check the string of the exception
        self.assertEqual(cm.exception.args[0], "height must be an integer")

    def test_new_negative(self):
        # expecting a value exception
        with self.assertRaises(ValueError) as cm:
            new_rect = self.rect(-1, 2)
        # check the string of the exception
        self.assertEqual(cm.exception.args[0], "width must be >= 0")

    def test_new_change(self):
        new_rect = self.rect()
        # expecting a value exception
        with self.assertRaises(ValueError) as cm:
            new_rect.height = -1
        # check the string of the exception
        self.assertEqual(cm.exception.args[0], "height must be >= 0")


class TestTwo(TestOne):

    def setUp(self):
        self.rect = __import__('2-rectangle').Rectangle

    def test_area(self):
        area = self.rect(5, 4).area()
        self.assertEqual(area, 20)

    def test_perimeter(self):
        perimeter = self.rect(5, 4).perimeter()
        self.assertEqual(perimeter, 18)

    def test_zero_perimeter(self):
        perimeter = self.rect(0, 4).perimeter()
        self.assertEqual(perimeter, 0)


class TestThree(TestTwo):

    def setUp(self):
        self.rect = __import__('3-rectangle').Rectangle

    def test_str(self):
        new_rect = self.rect(4, 2)
        exp_str = "####\n####"
        self.assertEqual(new_rect.__str__(), exp_str)

    def test_zero_str(self):
        new_rect = self.rect(0, 2)
        exp_str = ""
        self.assertEqual(new_rect.__str__(), exp_str)


class TestFour(TestThree):

    def setUp(self):
        self.rect = __import__('4-rectangle').Rectangle

    @unittest.skip("Import the actual Rectangle for valid test")
    def test_repr(self):
        new_rect = self.rect(4, 2)
        eval_rect = eval(new_rect.__repr__())
        self.assertEqual(new_rect.width, eval_rect.width)
        self.assertEqual(new_rect.height, eval_rect.height)
        self.assertEqual(new_rect.area(), eval_rect.area())
        self.assertEqual(type(new_rect), type(eval_rect))


if __name__ == '__main__':
    TestFour.run()
