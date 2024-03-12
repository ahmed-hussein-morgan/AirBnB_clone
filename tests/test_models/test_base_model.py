import unittest
"""testing base module"""
from models.base_model import BaseModel
from datetime import datetime


class TestSBaseModels(unittest.TestCase):
    """testing the base model"""
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    #time = datetime()

    def test_id(self):
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.my_model.created_at, object)

    def test_save(self):
        self.my_model.before_update = self.my_model.updated_at
        self.my_model.name = "ahmed"
        self.my_model.save()
        self.my_model.after_update = self.my_model.updated_at
        self.assertNotEqual(self.my_model.before_update, self.my_model.after_update)

    def test_str(self):
        n = self.my_model.__class__.__name__
        expected_str = f"[{n}] ({self.my_model.id}) <{self.my_model.__dict__}>"
        self.assertEqual(self.my_model.__str__(), expected_str)
