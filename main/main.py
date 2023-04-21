import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        self.calc = None

    def test_multiply(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calc.division(10, 2)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.subtraction(10, 4)
        self.assertEqual(result, 6)

    def test_adding(self):
        result = self.calc.adding(5, 6)
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()

 
