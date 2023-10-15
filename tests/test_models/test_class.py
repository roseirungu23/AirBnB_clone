#!/usr/bin/python3
"""Defines module for test classes"""

import inspect
import pep8
import unittest


class TestClassDocumentation(unittest.TestCase):
    """Implements TestClassDocumentation"""

    def __init__(self, tests, _class):
        """Constructor"""
        super().__init__()
        self.tests = tests
        self.name = _class
        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def test_documentation(self):
        """Test documentation of the module, class, and methods"""
        with self.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.subTest(msg='Documentation method {}'.format(f[0])):
                    doc = f[1].__doc__
                    self.assertGreaterEqual(len(doc), 1)

        with self.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.assertGreaterEqual(len(doc), 1)

    def test_pep8(self, files):
        """Test linter pep8 over the files"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
