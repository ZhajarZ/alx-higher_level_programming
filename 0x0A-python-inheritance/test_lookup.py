#!/usr/bin/python3
"""Test the lookup function."""

import unittest
from object_attributes import lookup  # Import the lookup function from your module

class TestLookupFunction(unittest.TestCase):
    def test_builtin_object(self):
        # Test with a built-in object (e.g., a list)
        result = lookup([])
        self.assertTrue(isinstance(result, list))
        self.assertIn('append', result)
        self.assertIn('pop', result)

    def test_custom_object(self):
        # Test with a custom object (e.g., an instance of MyClass)
        class MyClass:
            def __init__(self):
                self.attribute1 = 42
                self.attribute2 = "Hello"

        obj = MyClass()
        result = lookup(obj)
        self.assertTrue(isinstance(result, list))
        self.assertIn('attribute1', result)
        self.assertIn('attribute2', result)

if __name__ == '__main__':
    unittest.main()
