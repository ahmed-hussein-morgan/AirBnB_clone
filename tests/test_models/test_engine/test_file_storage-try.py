#!/usr/bin/python3
"""tests the file_storage module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

class TestFileStorageModel(unittest.TestCase):
    """test user class"""
    f_storage = FileStorage()
    base = BaseModel()
    def test_attributes(self):
        self.assertIsInstance(self.f_storage._FileStorage__file_path, str)
        self.assertIsInstance(self.f_storage._FileStorage__objects, dict)

    # def test_all(self):
    #     self.assertIsInstance(self.f_storage.all(), dict)

