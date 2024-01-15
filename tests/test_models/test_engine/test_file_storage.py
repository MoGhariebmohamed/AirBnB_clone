#!/usr/bin/python3
import os
import unittest
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import sys


class Test_filestorage_exist(unittest.TestCase):
    """This class for existance of file sorage."""
    def test_FileStorage_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_no_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_strpath(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def teststorage_filestrg(self):
        self.assertEqual(type(models.storage), FileStorage)

class Test_eachMethod(unittest.TestCase):
    """This class for unittest of methods for filestorage class."""

    @classmethod
    def setUp(clas):
        """Runs this setup before each test."""
        clas.test_basemodel = BaseModel()
        try:
            os.rename("file.json", "any.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDown(clas):
        """Teardown the FileStorage"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("any.json", "new.json")
        except FileNotFoundError:
            pass
        del clas.test_basemodel
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the all return object method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test the new objects method"""
        models.storage.new(self.test_basemodel)
        self.assertIn("BaseModel." + self.test_basemodel.id, models.storage.all().keys())
        self.assertIn(self.test_basemodel, models.storage.all().values())
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        models.storage.new(self.test_basemodel)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.test_basemodel.id, save_text)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """"Test the reload metod"""
        models.storage.new(self.test_basemodel)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.test_basemodel.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)



if __name__ == "__main__":
    unittest.main()
