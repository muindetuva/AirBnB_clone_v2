#!/usr/bin/python3
"""
Contains tests for the City Model
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Tests for the city model
    """

    def test_state_id(self):
        """
        Test that the id is a str
        """
        new = self.value()
        new.state_id =" id"
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test that the name is a str
        """
        new = self.value()
        new.name = "Chicago"
        self.assertEqual(type(new.name), str)
