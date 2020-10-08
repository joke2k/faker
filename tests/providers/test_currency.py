from unittest.mock import patch

import pytest


class TestCurrencyProvider:
    """Test currency provider methods"""
    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency import Provider as CurrencyProvider
        cls.provider = CurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.cryptocurrencies = cls.provider.cryptocurrencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))
        cls.cryptocurrency_codes, cls.cryptocurrency_names = tuple(zip(*cls.cryptocurrencies))

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple)
            assert cur in self.currencies

    def test_currency_code(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.currency_code()
            assert isinstance(code, str) and code in self.currency_codes

    def test_currency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.currency_name()
            assert isinstance(name, str) and name in self.currency_names

    def test_currency_symbol_no_code_supplied(self, faker, num_samples):
        for _ in range(num_samples):
            symbol = faker.currency_symbol()
            assert isinstance(symbol, str)
            assert symbol in self.provider.currency_symbols.values()

    @patch('faker.providers.currency.Provider.random_element')
    def test_currency_symbol_with_valid_code(self, mock_random_element, faker):
        symbol = faker.currency_symbol(code='USD')
        assert symbol == '$'
        mock_random_element.assert_not_called()

    @patch('faker.providers.currency.Provider.random_element')
    def test_currency_symbol_with_invalid_code(self, mock_random_element, faker):
        invalid_code = 'FTW'
        with pytest.raises(KeyError):
            faker.currency_symbol(code=invalid_code)
        mock_random_element.assert_not_called()

    def test_cryptocurrency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.cryptocurrency()
            assert isinstance(cur, tuple)
            assert cur in self.cryptocurrencies

    def test_cryptocurrency_code(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.cryptocurrency_code()
            assert isinstance(code, str) and code in self.cryptocurrency_codes

    def test_cryptocurrency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.cryptocurrency_name()
            assert isinstance(name, str) and name in self.cryptocurrency_names


class TestRuRu:
    """Test ru_RU currency provider"""
    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.ru_RU import Provider as RuRuCurrencyProvider
        cls.provider = RuRuCurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple) and cur in self.currencies

    def test_currency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.currency_name()
            assert isinstance(name, str) and name in self.currency_names


class TestEsEs:
    """Test es_ES currency provider"""
    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.es_ES import Provider as EsEsCurrencyProvider
        cls.provider = EsEsCurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert cur in self.currencies

    def test_currency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.currency_name()
            assert name in self.currency_names


class TestSvSe:
    """Test sv_SE currency provider"""
    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.sv_SE import Provider as SvSeCurrencyProvider
        cls.provider = SvSeCurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert cur in self.currencies

    def test_currency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.currency_name()
            assert name in self.currency_names
