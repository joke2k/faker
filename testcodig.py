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

    def test_invalid_letters(self):
        passport = 'A11234567'
        self.assertFalse(re.match(r'^[A-Z]{2}[0-9]{7}$', passport))

    def test_invalid_letter_length(self):
        passport = 'A1234567'
        self.assertFalse(re.match(r'^[A-Z]{2}[0-9]{7}$', passport))

    def test_invalid_digit_characters(self):
        passport = 'AB1234A67'
        self.assertFalse(re.match(r'^[A-Z]{2}[0-9]{7}$', passport))

    def test_invalid_digit_length(self):
        passport = 'AB123456'
        self.assertFalse(re.match(r'^[A-Z]{2}[0-9]{7}$', passport))


if __name__ == '__main__':
    unittest.main()
