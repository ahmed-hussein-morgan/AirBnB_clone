import unittest
"""testing user module"""
from models.user import User
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel


class TestFileStorageModel(unittest.TestCase):
    """test user class"""
    f_storage = FileStorage()
    base = BaseModel()
    def test_attributes(self):
        self.assertIsInstance(self.f_storage._FileStorage__file_path, str)
        self.assertIsInstance(self.f_storage._FileStorage__objects, dict)

