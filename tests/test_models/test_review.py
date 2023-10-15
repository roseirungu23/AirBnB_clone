#!/usr/bin/python3
"""Defines TestReview class"""

import unittest
import json
import pep8
import datetime

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Implements TestReview class"""

    def test_doc_module(self):
        """Module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes and class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            review = Review()
            self.assertIsInstance(review.place_id, str)
            self.assertIsInstance(review.user_id, str)
            self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
