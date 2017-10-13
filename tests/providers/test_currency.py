import unittest

from faker import Faker
from faker.providers.currency import Provider as CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_cryptocurrency_code(self):
        for _ in range(99):
            code = self.factory.cryptocurrency_code()
            self.assertIsInstance(code, str)
            self.assertIn(code, CurrencyProvider.cryptocurrencies)
