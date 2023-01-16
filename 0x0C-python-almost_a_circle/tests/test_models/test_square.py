#!/usr/bin/python3
""" Test Square Class  """
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Square class test cases """

    def setUp(self):
        """ setup """
        self.ins = Square(1)

    def tearDown(self):
        """ teardown """
        # remove instance, risky cause only during garbage collect
        del self.ins

    def test_type(self):
        """ test type of instance """
        self.assertEqual(type(self.ins), Square)

    def test_instance(self):
        """ test instance is of Square """
        self.assertIsInstance(self.ins, Square)

    def test_subclass(self):
        """ test subclass is of Base """
        self.assertTrue(issubclass(self.ins.__class__, Base))

    def test_valid_new(self):
        """ test creating valid new instances """
        new_a = Square(1, 1)
        new_b = Square(1, 1, 1)
        new_c = Square(1, 1, 1, 88)
        """ test setup instance, no pos attribute set """
        self.assertEqual(self.ins.id, 1)
        self.assertEqual(self.ins.size, 1)
        self.assertEqual(self.ins.x, 0)
        self.assertEqual(self.ins.y, 0)
        """ test new_a instance, 1 pos attribute set: x """
        self.assertEqual(new_a.id, 2)
        self.assertEqual(new_a.size, 1)
        self.assertEqual(new_a.x, 1)
        self.assertEqual(new_a.y, 0)
        """ test new_b instance, 2 pos attribute set: x, y """
        self.assertEqual(new_b.id, 3)
        self.assertEqual(new_b.size, 1)
        self.assertEqual(new_b.x, 1)
        self.assertEqual(new_b.y, 1)
        """ test new_c instance, all pos attribute set: x, y, id set """
        self.assertEqual(new_c.id, 88)
        self.assertEqual(new_c.size, 1)
        self.assertEqual(new_c.x, 1)
        self.assertEqual(new_c.y, 1)
        """ test new_d instance, all pos attribute set: x, y, id set """
        del new_a
        del new_b
        del new_c

    def test_invalid_new(self):
        """ test creating invalid new instances """
        """ missing/more argument """
        with self.assertRaises(TypeError):
            new_a = Square()
        with self.assertRaises(TypeError):
            new_a = Square(width=1)
        with self.assertRaises(TypeError):
            new_a = Square(1, 1, 1, 1, 1, 1)
        """ invalid argument """
        with self.assertRaises(TypeError) as cm:
            new_a = Square(None, 1)
        self.assertEqual(cm.exception.args[0], "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = Square(0, 8)
        self.assertEqual(cm.exception.args[0], "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            new_a = Square(1, None)
        self.assertEqual(cm.exception.args[0], "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = Square(8, -1)
        self.assertEqual(cm.exception.args[0], "x must be >= 0")
        with self.assertRaises(TypeError) as cm:
            new_a = Square(2, 5, None)
        self.assertEqual(cm.exception.args[0], "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = Square(2, 5, -1)
        self.assertEqual(cm.exception.args[0], "y must be >= 0")
        with self.assertRaises(ValueError) as cm:
            new_a = Square(2, 5, 77, "bad id")
        self.assertEqual(cm.exception.args[0], "id must be an integer")

    def test_valid_create_class_kwargs(self):
        """ test create class method with key words args """
        """ test new_a instance, 1 len atrib, 0 pos attribute set, id set """
        sample_dict = {"id": 88, "size": 1}
        new_a = self.ins.create(**sample_dict)
        self.assertEqual(new_a.id, 88)
        self.assertEqual(new_a.size, 1)
        self.assertTrue(isinstance(new_a, Square))
        self.assertIsNot(self.ins, new_a)
        """ test new_b instance, 1 len atrib, 1 pos attribute set, id set """
        sample_dict["id"] = 1337
        sample_dict["x"] = 1
        new_b = self.ins.create(**sample_dict)
        self.assertEqual(new_b.id, 1337)
        self.assertEqual(new_b.size, 1)
        self.assertEqual(new_b.x, 1)
        self.assertTrue(isinstance(new_b, Square))
        self.assertIsNot(self.ins, new_b)
        """ test new_c instance, 1 len atrib, 2 pos attribute set, id set """
        sample_dict["id"] = 96
        sample_dict["y"] = 1
        new_c = self.ins.create(**sample_dict)
        self.assertEqual(new_c.id, 96)
        self.assertEqual(new_c.size, 1)
        self.assertEqual(new_c.x, 1)
        self.assertEqual(new_c.y, 1)
        self.assertTrue(isinstance(new_c, Square))
        self.assertIsNot(self.ins, new_c)
        """ test new_d instance, 1 len atrib, 2 pos attribute set, id None """
        sample_dict["id"] = None
        sample_dict["y"] = 1
        new_d = self.ins.create(**sample_dict)
        self.assertEqual(new_d.id, 5)
        self.assertEqual(new_d.size, 1)
        self.assertEqual(new_d.x, 1)
        self.assertEqual(new_d.y, 1)
        self.assertTrue(isinstance(new_d, Square))
        self.assertIsNot(self.ins, new_d)
        del new_a
        del new_b
        del new_c
        del new_d

    def test_invalid_create_class_kwargs(self):
        """ test invalid create class method with args """
        sample_dict = {"id": None, "size": None, "x": None, "y": None}
        with self.assertRaises(TypeError) as cm:
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            sample_dict["id"] = 50
            sample_dict["size"] = 0
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            sample_dict["size"] = 5
            sample_dict["x"] = None
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            sample_dict["x"] = -1
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "x must be >= 0")
        with self.assertRaises(TypeError) as cm:
            sample_dict["x"] = 5
            sample_dict["y"] = None
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            sample_dict["y"] = -7
            new_a = self.ins.create(**sample_dict)
        self.assertEqual(cm.exception.args[0], "y must be >= 0")

    def test_valid_create_class_args(self):
        """ test create class method with positional args """
        """ test new_a instance, 1 len atrib, 0 pos attribute set, id None """
        sample_dict = {"id": None, "size": 1}
        new_a = self.ins.create(*sample_dict.values())
        self.assertEqual(new_a.id, 2)
        self.assertEqual(new_a.size, 1)
        self.assertTrue(isinstance(new_a, Square))
        self.assertIsNot(self.ins, new_a)
        """ test new_b instance, 1 len atrib, 0 pos attribute set, id set """
        sample_dict["id"] = 47
        new_b = self.ins.create(*sample_dict.values())
        self.assertEqual(new_b.id, 47)
        self.assertEqual(new_b.size, 1)
        self.assertTrue(isinstance(new_b, Square))
        self.assertIsNot(self.ins, new_b)
        """ test new_c instance, 1 len atrib, 1 pos attribute set, id set """
        sample_dict["id"] = 1337
        sample_dict["x"] = 1
        new_c = self.ins.create(*sample_dict.values())
        self.assertEqual(new_c.id, 1337)
        self.assertEqual(new_c.size, 1)
        self.assertEqual(new_c.x, 1)
        self.assertTrue(isinstance(new_c, Square))
        self.assertIsNot(self.ins, new_c)
        """ test new_d instance, 1 len atrib, 2 pos attribute set, id set """
        sample_dict["id"] = 96
        sample_dict["y"] = 1
        new_d = self.ins.create(*sample_dict.values())
        self.assertEqual(new_d.id, 96)
        self.assertEqual(new_d.size, 1)
        self.assertEqual(new_d.x, 1)
        self.assertEqual(new_d.y, 1)
        self.assertTrue(isinstance(new_d, Square))
        self.assertIsNot(self.ins, new_d)
        del new_a
        del new_b
        del new_c
        del new_d

    def test_invalid_create_class_args(self):
        """ test invalid create class method with args """
        with self.assertRaises(TypeError) as cm:
            new_a = self.ins.create(1, None)
        self.assertEqual(cm.exception.args[0], "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = self.ins.create(1, 0)
        self.assertEqual(cm.exception.args[0], "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            new_a = self.ins.create(1, 20, None)
        self.assertEqual(cm.exception.args[0], "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = self.ins.create(1, 50, -1)
        self.assertEqual(cm.exception.args[0], "x must be >= 0")
        with self.assertRaises(TypeError) as cm:
            new_a = self.ins.create(1, 50, 1, None)
        self.assertEqual(cm.exception.args[0], "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            new_a = self.ins.create(1, 50, 1, -1)
        self.assertEqual(cm.exception.args[0], "y must be >= 0")
        with self.assertRaises(TypeError) as cm:
            new_a = self.ins.create("bad id", 50, 2, 5)
        self.assertEqual(cm.exception.args[0], "id must be an integer")

    def test_valid_to_json_string(self):
        """ test static to json string """
        j_str = Square.to_json_string([self.ins.to_dictionary()])
        j_str_empty = Square.to_json_string([])
        """ check type """
        self.assertEqual(type(j_str), str)
        """ check includes id """
        self.assertTrue(j_str.find("id"))
        """ validate by tranforming back """
        self.assertEqual(
            self.ins.to_dictionary(), Square.from_json_string(j_str)[0])
        """ empty list check """
        self.assertEqual(j_str_empty, "[]")

    def test_invalid_to_json_string(self):
        """ test static to json string invalid """
        with self.assertRaises(TypeError) as cm:
            j_str = Square.to_json_string([None])
        self.assertEqual(
            cm.exception.args[0], "List must only contain dictionary instances"
        )
        with self.assertRaises(TypeError) as cm:
            j_str = Square.to_json_string(["tt", 99])
        self.assertEqual(
            cm.exception.args[0], "List must only contain dictionary instances"
        )
        with self.assertRaises(TypeError) as cm:
            j_str = Square.to_json_string("hello")
        self.assertEqual(cm.exception.args[0], "Argument must be a list")

    def test_valid_from_json_string(self):
        """ test static to json string """
        arr = Square.from_json_string(
            '[{"id": 5, "size": 5, "x": 0, "y": 0}]')
        """ check type """
        self.assertEqual(type(arr), list)
        self.assertEqual(type(arr[0]), dict)
        """ check values """
        self.assertEqual(arr[0]["id"], 5)
        self.assertEqual(arr[0]["size"], 5)
        self.assertEqual(arr[0]["x"], 0)

    def test_invalid_from_json_string(self):
        """ test static to json string invalid """
        """ bad arg type """
        with self.assertRaises(TypeError):
            arr = Square.from_json_string(None)
        """ bad json string """
        with self.assertRaises(TypeError):
            arr = Square.from_json_string('[{"id":]')

    def test_save_to_file(self):
        """ test save to file of Base class """
        pass

    def test_save_to_file_csv(self):
        """ test save to file csv of Base class """
        pass

    def test_load_from_file(self):
        """ test load from file of Base class """
        pass

    def test_load_to_file_csv(self):
        """ test load to file csv of Base class """
        pass
