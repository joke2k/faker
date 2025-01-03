import re

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

    def test_currency_code_has_symbol(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.currency_code()
            symbol = faker.currency_symbol(code=code)
            assert isinstance(symbol, str)

    def test_currency_symbol_no_code_supplied(self, faker, num_samples):
        for _ in range(num_samples):
            symbol = faker.currency_symbol()
            assert isinstance(symbol, str)
            assert symbol in self.provider.currency_symbols.values()

    @patch("faker.providers.currency.Provider.random_element")
    def test_currency_symbol_with_valid_code(self, mock_random_element, faker):
        symbol = faker.currency_symbol(code="USD")
        assert symbol == "$"
        mock_random_element.assert_not_called()

    @patch("faker.providers.currency.Provider.random_element")
    def test_currency_symbol_with_invalid_code(self, mock_random_element, faker):
        invalid_code = "FTW"
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

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestAzAz:
    """Test az_AZ currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.az_AZ import Provider as AzAzCurrencyProvider

        cls.provider = AzAzCurrencyProvider
        cls.currencies = cls.provider.currencies

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple) and cur in self.currencies

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestRuRu:
    """Test ru_RU currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.ru_RU import Provider as RuRuCurrencyProvider

        cls.provider = RuRuCurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))

        cls.pricetag_pattern = re.compile(r"\d{1,3}(?:\s\d{3})*,\d{2}\sр\.")

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple) and cur in self.currencies

    def test_currency_name(self, faker, num_samples):
        for _ in range(num_samples):
            name = faker.currency_name()
            assert isinstance(name, str) and name in self.currency_names

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)
            assert self.pricetag_pattern.fullmatch(pricetag)


class TestCsCz:
    """Test cs_CZ currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.cs_CZ import Provider as CsCzCurrencyProvider

        cls.provider = CsCzCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestDeAt:
    """Test de_AT currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.de_AT import Provider as DeAtCurrencyProvider

        cls.provider = DeAtCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestDeDe:
    """Test de_DE currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.de_DE import Provider as DeDeCurrencyProvider

        cls.provider = DeDeCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestEnAu:
    """Test en_AU currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.en_AU import Provider as EnAuCurrencyProvider

        cls.provider = EnAuCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestEnCa:
    """Test en_CA currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.en_CA import Provider as EnCaCurrencyProvider

        cls.provider = EnCaCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


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

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestFaIr:
    """Test fa_IR currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.fa_IR import Provider as FaIrCurrencyProvider

        cls.provider = FaIrCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestFrCa:
    """Test fr_CA currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.fr_CA import Provider as FrCaCurrencyProvider

        cls.provider = FrCaCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestFrFr:
    """Test fr_FR currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.fr_FR import Provider as FrFrCurrencyProvider

        cls.provider = FrFrCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestItIt:
    """Test it_IT currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.it_IT import Provider as ItItCurrencyProvider

        cls.provider = ItItCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestPlPl:
    """Test pl_PL currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.pl_PL import Provider as PlPlCurrencyProvider

        cls.provider = PlPlCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestSkSk:
    """Test sk_SK currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.sk_SK import Provider as SkSkCurrencyProvider

        cls.provider = SkSkCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


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


class TestThTh:
    """Test th_TH currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.th_TH import Provider as ThThCurrencyProvider

        cls.provider = ThThCurrencyProvider
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


class TestRoRo:
    """Test ro_RO currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.ro_RO import Provider as RoRoCurrencyProvider

        cls.provider = RoRoCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestPtBr:
    """Test pt_BR currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.pt_BR import Provider as PtBrCurrencyProvider

        cls.provider = PtBrCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestNlNl:
    """Test nl_NL currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.nl_NL import Provider as NlCurrencyProvider

        cls.provider = NlCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestElGr:
    """Test nl_NL currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.el_GR import Provider as ElGrCurrencyProvider

        cls.provider = ElGrCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestTrTr:
    """Test tr_TR currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.tr_TR import Provider as TrTrCurrencyProvider

        cls.provider = TrTrCurrencyProvider

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestViVn:
    """Test vi_VN currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.vi_VN import Provider as ViVNCurrencyProvider

        cls.provider = ViVNCurrencyProvider
        cls.currencies = cls.provider.currencies

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple) and cur in self.currencies

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)


class TestUkUa(TestCurrencyProvider):
    """Test uk_UA currency provider."""

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.uk_UA import Provider as UkUaCurrencyProvider

        cls.provider = UkUaCurrencyProvider
        cls.currencies = cls.provider.currencies
        cls.cryptocurrencies = cls.provider.cryptocurrencies
        cls.currency_codes, cls.currency_names = tuple(zip(*cls.currencies))
        cls.cryptocurrency_codes, cls.cryptocurrency_names = tuple(zip(*cls.cryptocurrencies))


class TestUzUz:
    """Test uz_UZ currency provider"""

    num_samples = 100

    @classmethod
    def setup_class(cls):
        from faker.providers.currency.uz_UZ import Provider as UzUzCurrencyProvider

        cls.provider = UzUzCurrencyProvider
        cls.currencies = cls.provider.currencies

    def test_currency(self, faker, num_samples):
        for _ in range(num_samples):
            cur = faker.currency()
            assert isinstance(cur, tuple) and cur in self.currencies

    def test_pricetag(self, faker, num_samples):
        for _ in range(num_samples):
            pricetag = faker.pricetag()
            assert isinstance(pricetag, str)
