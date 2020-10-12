import re

import pytest

from faker.providers.bank import Provider as BankProvider
from faker.providers.bank.de_CH import Provider as DeChBankProvider
from faker.providers.bank.en_GB import Provider as EnGbBankProvider
from faker.providers.bank.en_PH import Provider as EnPhBankProvider
from faker.providers.bank.es_ES import Provider as EsEsBankProvider
from faker.providers.bank.fi_FI import Provider as FiFiBankProvider
from faker.providers.bank.fr_FR import Provider as FrFrBankProvider
from faker.providers.bank.no_NO import Provider as NoNoBankProvider
from faker.providers.bank.pl_PL import Provider as PlPlBankProvider
from faker.providers.bank.pt_PT import Provider as PtPtBankProvider
from faker.providers.bank.tr_TR import Provider as TrTrBankProvider


def is_valid_iban(iban):
    check = iban[4:] + iban[:4]
    check = int(''.join(BankProvider.ALPHA.get(c, c) for c in check))
    return check % 97 == 1


class TestNoNo:
    """Test no_NO bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{11}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == NoNoBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{11}", iban[2:])


class TestFiFi:
    """Test fi_FI bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{14}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == FiFiBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{14}", iban[2:])


class TestPlPl:
    """Test pl_PL bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{26}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == PlPlBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{26}", iban[2:])


class TestEnGb:
    """Test en_GB bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"[A-Z]{4}\d{14}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EnGbBankProvider.country_code
            assert re.fullmatch(r"\d{2}[A-Z]{4}\d{14}", iban[2:])


class TestRuRu:
    """Test ru_RU bank provider"""

    def test_bic(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"04\d{7,9}", faker.bic())

    def test_correspondent_account(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"301\d{17}", faker.correspondent_account())

    def test_checking_account(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\d{3}0\d{16}", faker.checking_account())

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\D{3,41}", faker.bank())


class TestPtPt:
    """Test pt_PT bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{21}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == PtPtBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{21}", iban[2:])


class TestEsEs:
    """Test es_ES bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{20}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EsEsBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{20}", iban[2:])


class TestFrFr:
    """Test fr_FR bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == FrFrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])


class TestEnPh:
    """Test en_PH bank provider"""

    def test_swift(self, faker, num_samples):
        regex = re.compile('[A-Z]{4}PH[A-Z0-9]{2}(?:[A-Z0-9]{3})?')
        for _ in range(num_samples):
            code = faker.swift()
            assert regex.fullmatch(code) is not None

    def test_swift_invalid_length(self, faker):
        faker.swift(length=8)
        faker.swift(length=11)
        with pytest.raises(AssertionError):
            faker.swift(length=5)

    def test_swift8_use_dataset(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.swift8(use_dataset=True)
            assert len(code) == 8
            assert code[:4] in EnPhBankProvider.swift_bank_codes
            assert code[4:6] == EnPhBankProvider.country_code
            assert code[6:8] in EnPhBankProvider.swift_location_codes

    def test_swift11_use_dataset(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.swift11(use_dataset=True)
            assert len(code) == 11
            assert code[:4] in EnPhBankProvider.swift_bank_codes
            assert code[4:6] == EnPhBankProvider.country_code
            assert code[6:8] in EnPhBankProvider.swift_location_codes
            assert code[8:11] in EnPhBankProvider.swift_branch_codes

    def test_swift11_is_primary(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.swift11(primary=True)
            assert len(code) == 11
            assert code[8:11] == 'XXX'


class TestFilPh(TestEnPh):
    """Test fil_PH bank provider"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH bank provider"""
    pass


class TestTrTr:
    """Test tr_TR bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{22}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == TrTrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{22}", iban[2:])


class TestDeCh:
    """Test de_CH bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{17}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == DeChBankProvider.country_code
            assert re.fullmatch(r"\d{19}", iban[2:])


class TestFrCh(TestDeCh):
    """Test fr_CH bank provider"""
    pass


class TestItCh(TestDeCh):
    """Test it_CH bank provider"""
    pass
