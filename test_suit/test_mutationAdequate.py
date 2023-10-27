import unittest
from isTriangle import Triangle  # Replace 'your_module' with the actual module name

class TestMutationAdequate(unittest.TestCase):

    def test_mutant_1(self):
        # Test for a mutant that modifies an operator
        result = Triangle.classify(1, 1, 1)
        self.assertEqual(result, Triangle.Type.EQUILATERAL)

    def test_mutant_2(self):
        # Test for a mutant that changes a constant value
        result = Triangle.classify(0, 1, 2)
        self.assertEqual(result, Triangle.Type.INVALID)

    def test_mutant_3(self):
        # Test for a mutant that alters an expression
        result = Triangle.classify(2, 2, 3)
        self.assertEqual(result, Triangle.Type.ISOSCELES)

    def test_mutant_4(self):
        self.assertEqual(Triangle.classify(-1, 2, 2), Triangle.Type.INVALID)

    def test_mutant_5(self):
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)

    def test_mutant_6(self):
        self.assertEqual(Triangle.classify(4, 2, 2), Triangle.Type.INVALID)

    def test_mutant_7(self):
        self.assertEqual(Triangle.classify(-2, 2, 2), Triangle.Type.INVALID)

    def test_mutant_8(self):
        self.assertEqual(Triangle.classify(2, -2, 2), Triangle.Type.INVALID)

    def test_mutant_9(self):
        self.assertEqual(Triangle.classify(2, 2, -2), Triangle.Type.INVALID)

    def test_mutant_10(self):
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)

    def test_mutant_11(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def test_mutant_12(self):
        self.assertEqual(Triangle.classify(2, 4, 2), Triangle.Type.INVALID)

    def test_mutant_13(self):
        self.assertEqual(Triangle.classify(2, 2, 4), Triangle.Type.INVALID)

    def test_mutant_14(self):
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)

    def test_mutant_15(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

    def test_mutant_16(self):
        self.assertEqual(Triangle.classify(5, 12, 13), Triangle.Type.SCALENE)

    def test_mutant_17(self):
        self.assertEqual(Triangle.classify(4, 3, 5), Triangle.Type.SCALENE)

    def test_mutant_18(self):
        self.assertEqual(Triangle.classify(5, 4, 3), Triangle.Type.SCALENE)

    def test_mutant_19(self):
        self.assertEqual(Triangle.classify(2, 1, 3), Triangle.Type.INVALID)

    def test_mutant_20(self):
        self.assertEqual(Triangle.classify(3, 2, 1), Triangle.Type.INVALID)

    def test_mutant_21(self):
        self.assertEqual(Triangle.classify(3, 1, 2), Triangle.Type.INVALID)

    def test_mutant_22(self):
        self.assertEqual(Triangle.classify(1, 3, 2), Triangle.Type.INVALID)




if __name__ == '__main__':
    unittest.main()
