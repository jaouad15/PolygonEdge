# test_polygonedge.py
"""
Tests for PolygonEdge module.
"""

import unittest
from polygonedge import PolygonEdge

class TestPolygonEdge(unittest.TestCase):
    """Test cases for PolygonEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PolygonEdge()
        self.assertIsInstance(instance, PolygonEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PolygonEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
