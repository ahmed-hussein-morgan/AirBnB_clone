import unittest
"""testing base module"""
from models.base_model import BaseModel


class TestSBaseModels(unittest.TestCase):
    """testing the base model"""
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89

    def test_id(self):
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.my_model.created_at, object)

    def test_save(self):
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.save(), object)