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


if __name__ == "__main__":
    unittest.main()
