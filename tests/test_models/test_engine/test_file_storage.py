#!/usr/bin/python3
"""test the file storage engine"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

class test_FileStorageModel(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_new_object_creation(self):
        """Test creating a new object."""
        obj_id = self.f_storage.new(self.base)
        self.assertIsNotNone(obj_id)

    def test_save_method(self):
        """Test saving an object."""
        obj_id = self.f_storage.new(self.base)
        self.f_storage.save()
        loaded_obj = self.f_storage.get(BaseModel, obj_id)
        self.assertIsNotNone(loaded_obj)

    def test_reload_method(self):
        """Test reloading objects from storage."""
        obj_id = self.f_storage.new(self.base)
        self.f_storage.save()
        self.f_storage.reload()
        loaded_obj = self.f_storage.get(BaseModel, obj_id)
        self.assertIsNotNone(loaded_obj)

    def test_all_objects(self):
        """Test retrieving all objects."""
        obj_id = self.f_storage.new(self.base)
        self.f_storage.save()
        all_objs = self.f_storage.all()
        self.assertIn(str(obj_id), all_objs.values())

if __name__ == '__main__':
    unittest.main()