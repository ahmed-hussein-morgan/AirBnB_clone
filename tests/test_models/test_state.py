import unittest
"""testing state module"""
from models.state import State


class TestStateModel(unittest.TestCase):
    """test state class"""

    my_state = State()
    def test_name(self):
        self.assertIsInstance(self.my_state.name, str)
