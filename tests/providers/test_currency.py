import unittest

from faker import Faker
from faker.providers.currency import Provider as CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_currency(self):
        for _ in range(99):
            cur = self.factory.currency()
            assert isinstance(cur, tuple)
            assert cur in CurrencyProvider.currencies

    def test_currency_code(self):
        for _ in range(99):
            code = self.factory.currency_code()
            assert isinstance(code, str)

    def test_currency_name(self):
        for _ in range(99):
            name = self.factory.currency_name()
            assert isinstance(name, str)

    def test_cryptocurrency(self):
        for _ in range(99):
            cur = self.factory.cryptocurrency()
            assert isinstance(cur, tuple)
            assert cur in CurrencyProvider.cryptocurrencies

    def test_cryptocurrency_code(self):
        for _ in range(99):
            code = self.factory.cryptocurrency_code()
            assert isinstance(code, str)

    def test_cryptocurrency_name(self):
        for _ in range(99):
            name = self.factory.cryptocurrency_name()
            assert isinstance(name, str)
