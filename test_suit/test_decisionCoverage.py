import unittest
from isTriangle import Triangle  # Replace 'your_module' with the actual module name

class TestDecisionCoverage(unittest.TestCase):

    def test_invalid_sides(self):
        # Test for invalid sides (Triangle.Type.INVALID)
        result = Triangle.classify(0, 1, 2)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_violates_triangle_inequality(self):
        # Test for violating the triangle inequality (Triangle.Type.INVALID)
        result = Triangle.classify(1, 1, 3)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_scalene_triangle(self):
        # Test for a scalene triangle (Triangle.Type.SCALENE)
        result = Triangle.classify(3, 4, 5)
        self.assertEqual(result, Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        # Test for an equilateral triangle (Triangle.Type.EQUILATERAL)
        result = Triangle.classify(1, 1, 1)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    def test_isosceles_triangle(self):
        # Test for an isosceles triangle (Triangle.Type.ISOSCELES)
        result = Triangle.classify(2, 2, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

if __name__ == '__main__':
    unittest.main()
