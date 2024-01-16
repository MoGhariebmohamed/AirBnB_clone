#!/usr/bin/python3
"""test user class from basemodel"""
import os
import models
import unittest
from datetime import datetime
from models.user import User

class Testuser(unittest.TestCase):
    """class for testing existance of user class"""
    def test_typeUser(self):
        self.assertEqual(User, type(User()))

    def test_value(self):
        self.assertIn(User(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(User().id))

    def test_createTime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updateTime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_emailUser(self):
        self.assertEqual(str, type(User.email))

    def test_passwordUser(self):
        self.assertEqual(str, type(User.password))

    def test_firstName(self):
        self.assertEqual(str, type(User.first_name))

    def test_lastName(self):
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
