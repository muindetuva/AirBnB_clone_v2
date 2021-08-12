#!/usr/bin/python3
"""
Contains tests for the amenity class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Tests for the amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        The init method
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test that the name is a string
        """
        new = self.value()
        new.name = "Tuva"
        self.assertEqual(type(new.name), str)
