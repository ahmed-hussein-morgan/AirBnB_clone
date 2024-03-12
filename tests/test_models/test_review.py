import unittest
"""testing review module"""
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """test Review class"""

    my_review = Review()
    def test_attributes(self):
        self.assertIsInstance(self.my_review.place_id, str)
        self.assertIsInstance(self.my_review.user_id, str)
        self.assertIsInstance(self.my_review.text, str)
