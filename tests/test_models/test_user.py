import unittest
"""testing user module"""
from models.user import User
from models.base_model import BaseModel


class TestUserModel(unittest.TestCase):
    """test user class"""
    base = BaseModel()
    my_user = User()
    def test_attributes(self):
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
