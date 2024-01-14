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

    @classmethod
    def tearDownClass(cls):
        """Teardown the basemodel."""
        del cls.testModel

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

        Test_My_Model = self.testModel.to_dict()

        self.assertIsInstance(Test_My_Model, dict)
        self.assertEqual(Test_My_Model["__class__"], 'BaseModel')
        self.assertEqual(Test_My_Model['id'], self.testModel.id)
        self.assertEqual(Test_My_Model['created_at'],
                         self.testModel.created_at.isoformat())
        self.assertEqual(Test_My_Model["updated_at"],
                         self.testModel.updated_at.isoformat())

    def test_str(self):
        """to test print format method representation."""
        self.assertTrue(str(self.testModel).startswith('[BaseModel]'))
        self.assertIn(self.testModel.id, str(self.testModel))
        self.assertIn(str(self.testModel.__dict__), str(self.testModel))


if __name__ == "__main__":
    unittest.main()
