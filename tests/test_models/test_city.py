import unittest
"""testing city module"""
from models.city import City


class TestCityModel(unittest.TestCase):
    """test city class"""

    my_city = City()
    def test_name(self):
        self.assertIsInstance(self.my_city.name, str)
        self.assertIsInstance(self.my_city.state_id, str)
