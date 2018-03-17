import unittest

from faker import Faker
from faker.providers.currency import Provider as CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_currency(self):
        for _ in range(99):
            cur = self.factory.currency()
            self.assertIsInstance(cur, tuple)
            self.assertIn(cur, CurrencyProvider.currencies)

    def test_currency_code(self):
        for _ in range(99):
            code = self.factory.currency_code()
            self.assertIsInstance(code, str)

    def test_currency_name(self):
        for _ in range(99):
            name = self.factory.currency_name()
            self.assertIsInstance(name, str)

    def test_cryptocurrency(self):
        for _ in range(99):
            cur = self.factory.cryptocurrency()
            self.assertIsInstance(cur, tuple)
            self.assertIn(cur, CurrencyProvider.cryptocurrencies)

    def test_cryptocurrency_code(self):
        for _ in range(99):
            code = self.factory.cryptocurrency_code()
            self.assertIsInstance(code, str)

    def test_cryptocurrency_name(self):
        for _ in range(99):
            name = self.factory.cryptocurrency_name()
            self.assertIsInstance(name, str)
