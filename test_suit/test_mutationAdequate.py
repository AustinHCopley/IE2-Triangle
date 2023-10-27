import unittest
from isTriangle import Triangle  # Replace 'your_module' with the actual module name

class TestMutationAdequate(unittest.TestCase):

    def test_mutant_1(self):
        # Test for a mutant that modifies an operator
        result = Triangle.classify(1, 1, 1)
        self.assertNotEqual(result, Triangle.Type.EQUILATERAL)

    def test_mutant_2(self):
        # Test for a mutant that changes a constant value
        result = Triangle.classify(0, 1, 2)
        self.assertNotEqual(result, Triangle.Type.INVALID)

    def test_mutant_3(self):
        # Test for a mutant that alters an expression
        result = Triangle.classify(2, 2, 3)
        self.assertNotEqual(result, Triangle.Type.ISOSCELES)

    def test_mutant_4(self):
        self.assertNotEqual(Triangle.classify(-1, 2, 2), Triangle.Type.INVALID)

    def test_mutant_5(self):
        self.assertNotEqual(Triangle.classify(1, 2, 2), Triangle.Type.INVALID)

    def test_mutant_6(self):
        self.assertNotEqual(Triangle.classify(4, 2, 2), Triangle.Type.INVALID)

    def test_mutant_7(self):
        self.assertNotEqual(Triangle.classify(-1, 2, 2), Triangle.Type.INVALID)

    def test_mutant_8(self):
        self.assertNotEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)

    def test_mutant_9(self):
        self.assertNotEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)



if __name__ == '__main__':
    unittest.main()
