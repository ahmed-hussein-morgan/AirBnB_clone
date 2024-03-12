import unittest
"""testing place module"""
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """test Review class"""

    my_place = Place()
    def test_attribute1(self):
        self.assertIsInstance(self.my_place.name, str)

    def test_attribute2(self):
        self.assertIsInstance(self.my_place.user_id, str)
    
    def test_attribute3(self):
        self.assertIsInstance(self.my_place.city_id, str)

    def test_attribute4(self):
        self.assertIsInstance(self.my_place.description, str)
    
    def test_attribute5(self):
        self.assertIsInstance(self.my_place.number_rooms, int)

    def test_attribute6(self):
        self.assertIsInstance(self.my_place.number_bathrooms, int)

    def test_attribute7(self):
        self.assertIsInstance(self.my_place.max_guest, int)
        self.assertIsInstance(self.my_place.price_by_night, int)
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertIsInstance(self.my_place.longitude, float)
        self.assertIsInstance(self.my_place.amenity_ids, list)
