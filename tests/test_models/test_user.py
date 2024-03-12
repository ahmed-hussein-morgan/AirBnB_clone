import unittest
"""testing user module"""
from models.user import User


class TestUserModel(unittest.TestCase):
    """test user class"""

    my_user = User()
    def test_attributes(self):
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
