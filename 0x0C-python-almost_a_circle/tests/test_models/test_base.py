#!/usr/bin/python3
""" Test Base Class  """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Base class test cases """

    def setUp(self):
        """ setup """
        self.ins = Base()

    def tearDown(self):
        """ teardown """
        # remove instance, risky cause only during garbage collect
        del self.ins

    def test_new(self):
        """ test a new instance """
        self.assertEqual(self.ins.id, 1)

    def test_add(self):
        """ test add new instance """
        new = Base()
        self.assertEqual(new.id, 2)

    def test_new_with_id(self):
        """ test add new instance with an id """
        new = Base(800)
        self.assertEqual(self.ins.id, 1)
        self.assertEqual(new.id, 800)

    def test_type(self):
        """ test type of instance """
        self.assertEqual(type(self.ins), Base)

    def test_instance(self):
        """ test instance is of Base """
        self.assertIsInstance(self.ins, Base)

    def test_create_class(self):
        """ test create class method """
        new = self.ins.create()
        self.assertEqual(self.ins.id, 1)
        self.assertEqual(new.id, 2)

    def test_save_to_file(self):
        """ test save to file of Base class """
        with self.assertRaises(NotImplementedError) as cm:
            self.ins.save_to_file([])
        self.assertEqual(
            cm.exception.args[0], "Rectangle and Square intances only")

    def test_save_to_file_csv(self):
        """ test save to file csv of Base class """
        with self.assertRaises(NotImplementedError) as cm:
            self.ins.save_to_file_csv([])
        self.assertEqual(
            cm.exception.args[0], "Rectangle and Square intances only")

    def test_load_from_file(self):
        """ test load from file of Base class """
        with self.assertRaises(NotImplementedError) as cm:
            self.ins.load_from_file()
        self.assertEqual(
            cm.exception.args[0], "Rectangle and Square intances only")

    def test_load_to_file_csv(self):
        """ test load to file csv of Base class """
        with self.assertRaises(NotImplementedError) as cm:
            self.ins.load_from_file_csv()
        self.assertEqual(
            cm.exception.args[0], "Rectangle and Square intances only")
