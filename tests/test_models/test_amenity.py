import unittest
"""testing Amenity module"""
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """test Amenity class"""

    my_amenity = Amenity()
    def test_name(self):
        self.assertIsInstance(self.my_amenity.name, str)
