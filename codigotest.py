import unittest
from faker import Faker
import re

class TestPassportProvider(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.provider = self.fake.passport_number

    def test_valid_passport_number(self):
        passport = self.provider()
        self.assertRegex(passport, r'^[A-Z]{2}[0-9]{7}$')

   
    def test_letters_are_uppercase(self):
        passport = self.provider()
        letters = passport[:2]
        self.assertTrue(all(l.isalpha() and l.isupper() for l in letters))

  
    def test_letters_length(self):
        passport = self.provider()
        self.assertEqual(len(passport[:2]), 2)

    def test_digits_are_numbers(self):
        passport = self.provider()
        digits = passport[2:]
        self.assertTrue(digits.isdigit())

    
    def test_digits_length(self):
        passport = self.provider()
        self.assertEqual(len(passport[2:]), 7)


if __name__ == '__main__':
    unittest.main()
