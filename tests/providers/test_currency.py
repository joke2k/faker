import re
import unittest

from faker import Faker
from faker.providers.currency import Provider as CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_currency(self):
        for _ in range(99):
            cur = self.fake.currency()
            assert isinstance(cur, tuple)
            assert cur in CurrencyProvider.currencies

    def test_currency_code(self):
        for _ in range(99):
            code = self.fake.currency_code()
            assert isinstance(code, str)

    def test_currency_name(self):
        for _ in range(99):
            name = self.fake.currency_name()
            assert isinstance(name, str)

    def test_currency_symbol(self):
        for _ in range(99):
            symbol = self.fake.currency_symbol()
            assert isinstance(symbol, str)
            assert symbol in CurrencyProvider.currency_symbols.values()

    def test_cryptocurrency(self):
        for _ in range(99):
            cur = self.fake.cryptocurrency()
            assert isinstance(cur, tuple)
            assert cur in CurrencyProvider.cryptocurrencies

    def test_cryptocurrency_code(self):
        for _ in range(99):
            code = self.fake.cryptocurrency_code()
            assert isinstance(code, str)

    def test_cryptocurrency_name(self):
        for _ in range(99):
            name = self.fake.cryptocurrency_name()
            assert isinstance(name, str)


class TestRuRu(unittest.TestCase):
    """ Tests currency in the ru_RU locale """

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)

    def test_currency(self):
        for _ in range(99):
            cur = self.fake.currency()
            assert isinstance(cur, tuple)
            assert re.match(r'[А-Яа-я]', cur[1])

    def test_currency_name(self):
        for _ in range(99):
            name = self.fake.currency_name()
            assert isinstance(name, str)
            assert re.match(r'[А-Яа-я]', name)
