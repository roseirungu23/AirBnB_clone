#!/usr/bin/python3
"""Defines class TestAmenity"""

import unittest
import json
import pep8
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Implements tests for the Amenity class"""

    def test_doc_module(self):
        """Module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Tests that models/amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style
                         errors(and warnings).")

    def test_inheritance(self):
        """Validates the inheritance of Amenity from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Validates the types of attributes in the Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
