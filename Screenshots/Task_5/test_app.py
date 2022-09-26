import unittest
import app

class TestApp(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(app.factors(1), [1])
        self.assertEqual(app.factors(4), [2,2])
        self.assertEqual(app.factors(5), [5])
        self.assertEqual(app.factors(10), [2,5])

    def test_is_prime(self):
        self.assertFalse(app.is_prime(1), True)
        self.assertTrue(app.is_prime(2), False)
        self.assertTrue(app.is_prime(3), False)
        self.assertFalse(app.is_prime(4), True)
        self.assertTrue(app.is_prime(5), False)

    def test_vowels(self):
        self.assertEqual(app.vowels("qamil"), ['a','i'])
        self.assertEqual(app.vowels("bcdfghjklmnpqrstvzyw"), [])
        self.assertEqual(app.vowels("aeiou"), ['a','e','i','o','u'])
