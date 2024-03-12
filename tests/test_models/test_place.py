import unittest
"""testing place module"""
from models.place import Place


class TestCityModel(unittest.TestCase):
    """test Review class"""

    my_place = Place()
    def test_attributes(self):
        self.assertIsInstance(self.my_place.name, str)
        self.assertIsInstance(self.my_place.user_id, str)
        self.assertIsInstance(self.my_place.city_id, str)
        self.assertIsInstance(self.my_place.description, str)
        self.assertIsInstance(self.my_place.number_rooms, int)
        self.assertIsInstance(self.my_place.number_bathrooms, int)
        self.assertIsInstance(self.my_place.max_guest, int)
        self.assertIsInstance(self.my_place.price_by_night, int)
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertIsInstance(self.my_place.longitude, float)
        self.assertIsInstance(self.my_place.amenity_ids, list)
