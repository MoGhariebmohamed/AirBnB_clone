#!/usr/bin/python3
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import sys

class Test_Base_Model(unittest.TestCase):
    """This class for unittest."""

    @classmethod
    def setUpClass(cls):
        """Runs this setup before each test."""
        cls.testModel = BaseModel()
        try:
            os.rename("file.json", "new.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Teardown the basemodel."""
        del cls.testModel
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("new.json", "exist.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test the init function"""
        self.assertIsNotNone(self.testModel.id)
        self.assertIsNotNone(self.testModel.created_at)
        self.assertIsNotNone(self.testModel.updated_at)

    def test_save(self):
        """to test save method output."""
        vlaue_updated_at = self.testModel.updated_at
        value_now_updated_at = self.testModel.save()
        self.assertNotEqual(vlaue_updated_at, value_now_updated_at)

    def test_to_dict(self):
        """to test dictionary method output."""
        Test_MyModel = self.testModel.to_dict()
        self.assertIsInstance(Test_MyModel, dict)
        self.assertEqual(Test_MyModel["__class__"], 'BaseModel')
        self.assertEqual(Test_MyModel['id'], self.testModel.id)
        self.assertEqual(Test_MyModel['created_at'],
                         self.testModel.created_at.isoformat())
        self.assertEqual(Test_MyModel["updated_at"],
                         self.testModel.updated_at.isoformat())

    def test_str(self):
        """to test print format method representation."""
        self.assertTrue(str(self.testModel).startswith('[BaseModel]'))
        self.assertIn(self.testModel.id, str(self.testModel))
        self.assertIn(str(self.testModel.__dict__), str(self.testModel))



if __name__ == "__main__":
    unittest.main()
