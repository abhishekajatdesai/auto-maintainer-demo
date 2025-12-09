import unittest
from app import add

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, -20), -30)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)

    def test_add_with_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 0), -5)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(-1.5, 2.0), 0.5)

if __name__ == '__main__':
    unittest.main()