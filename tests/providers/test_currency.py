import unittest

from faker import Faker
from faker.providers.currency import Provider as CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_currency(self):
        for _ in range(99):
            code = self.factory.currency()
            self.assertIsInstance(code, tuple)
            self.assertIn(code, CurrencyProvider.currencies)

    def test_currency_code(self):
        for _ in range(99):
            code = self.factory.currency_code()
            self.assertIsInstance(code, str)

    def test_currency_name(self):
        for _ in range(99):
            code = self.factory.currency_name()
            self.assertIsInstance(code, str)

    def test_cryptocurrency_code(self):
        for _ in range(99):
            code = self.factory.cryptocurrency_code()
            self.assertIsInstance(code, str)
            self.assertIn(code, CurrencyProvider.cryptocurrencies)
