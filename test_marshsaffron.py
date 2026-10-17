# test_marshsaffron.py
"""
Tests for MarshSaffron module.
"""

import unittest
from marshsaffron import MarshSaffron

class TestMarshSaffron(unittest.TestCase):
    """Test cases for MarshSaffron class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarshSaffron()
        self.assertIsInstance(instance, MarshSaffron)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarshSaffron()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
