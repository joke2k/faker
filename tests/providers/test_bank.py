import re

import pytest

from faker.providers.bank import Provider as BankProvider
from faker.providers.bank.az_AZ import Provider as AzAzBankProvider
from faker.providers.bank.cs_CZ import Provider as CsCZBankProvider
from faker.providers.bank.de_CH import Provider as DeChBankProvider
from faker.providers.bank.el_GR import Provider as ElGrBankProvider
from faker.providers.bank.en_GB import Provider as EnGbBankProvider
from faker.providers.bank.en_IE import Provider as EnIeBankProvider
from faker.providers.bank.en_PH import Provider as EnPhBankProvider
from faker.providers.bank.es_AR import Provider as EsArBankProvider
from faker.providers.bank.es_ES import Provider as EsEsBankProvider
from faker.providers.bank.es_MX import Provider as EsMxBankProvider
from faker.providers.bank.es_MX import is_valid_clabe
from faker.providers.bank.fi_FI import Provider as FiFiBankProvider
from faker.providers.bank.fr_FR import Provider as FrFrBankProvider
from faker.providers.bank.nl_BE import Provider as NlBeBankProvider
from faker.providers.bank.no_NO import Provider as NoNoBankProvider
from faker.providers.bank.pl_PL import Provider as PlPlBankProvider
from faker.providers.bank.pt_PT import Provider as PtPtBankProvider
from faker.providers.bank.sk_SK import Provider as SkSKBankProvider
from faker.providers.bank.th_TH import Provider as ThThBankProvider
from faker.providers.bank.tr_TR import Provider as TrTrBankProvider
from faker.providers.bank.uk_UA import Provider as UkUaBankProvider


def is_valid_iban(iban):
    check = iban[4:] + iban[:4]
    check = int("".join(BankProvider.ALPHA.get(c, c) for c in check))
    return check % 97 == 1


def is_valid_aba(aba):
    d = [int(n) for n in aba]
    chkdgt = 3 * (d[0] + d[3] + d[6]) + 7 * (d[1] + d[4] + d[7]) + (d[2] + d[5] + d[8])
    if chkdgt % 10 == 0:
        return True
    return False


class TestAzAz:
    """Test az_AZ bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"[A-Z]{4}\d{20}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == AzAzBankProvider.country_code
            assert re.fullmatch(r"\d{2}[A-Z]{4}\d{20}", iban[2:])

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            bank = faker.bank()
            assert bank in AzAzBankProvider.banks


class TestCsCz:
    """Test cs_CZ bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{20}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == CsCZBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{20}", iban[2:])


class TestSkSk:
    """Test sk_SK bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{20}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == SkSKBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{20}", iban[2:])


class TestNoNo:
    """Test no_NO bank provider"""

    def test_aba(self, faker, num_samples):
        for _ in range(num_samples):
            aba = faker.aba()
            assert len(aba) == 9
            assert is_valid_aba(aba)

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{11}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == NoNoBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{11}", iban[2:])


class TestFaIr:
    """Test fa_IR bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"IR\d{24}", faker.bban())

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\D{7,25}", faker.bank())


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
            assert re.fullmatch(r"\d{24}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == PlPlBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{24}", iban[2:])


class TestUkUa:
    """Test uk_UA bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{27}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == UkUaBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{27}", iban[2:])


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


class TestEnIe:
    """Test en_IE bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EnIeBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])


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


class TestEsMx:
    """Test es_MX bank provider"""

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.bank() in EsMxBankProvider.banks

    @pytest.mark.parametrize(
        "clabe,validity",
        [
            ("002864631170560203", True),
            ("002864631170560202", False),
            ("00286463117056020", False),
            ("0028646311705602030", False),
            ("00286463117056020A", False),
        ],
        ids=[
            "valid",
            "bad_control_digit",
            "too_short",
            "too_long",
            "non_numeric_characters",
        ],
    )
    def test_clabe_validation(self, clabe, validity):
        assert is_valid_clabe(clabe) is validity

    def test_clabe(self, faker, num_samples):
        for _ in range(num_samples):
            clabe = faker.clabe()
            assert is_valid_clabe(clabe)
            assert int(clabe[:3].lstrip("0")) in EsMxBankProvider.bank_codes

    def test_clabe_bank_code(self, faker, num_samples):
        bank_code = 133
        for _ in range(num_samples):
            clabe = faker.clabe(bank_code=bank_code)
            assert is_valid_clabe(clabe)
            assert int(clabe[:3].lstrip("0")) == bank_code


class TestEsAr:
    """Test es_AR bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"[A-Z]{4}\d{20}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EsArBankProvider.country_code
            assert re.fullmatch(r"\d{2}[A-Z]{4}\d{20}", iban[2:])


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


class TestDeDe:
    """Test de_DE bank provider"""

    def test_swift_use_dataset(self, faker, num_samples):
        regex = re.compile("[A-Z]{6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3})?")
        for _ in range(num_samples):
            code = faker.swift(use_dataset=True)
            assert regex.fullmatch(code) is not None


class TestEnPh:
    """Test en_PH bank provider"""

    def test_swift(self, faker, num_samples):
        regex = re.compile("[A-Z]{4}PH[A-Z0-9]{2}(?:[A-Z0-9]{3})?")
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
            assert code[8:11] == "XXX"


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


class TestThTh:
    """Test th_TH bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{10}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == ThThBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{10}", iban[2:])


class TestElGr:
    """Test el_GR bank provider"""

    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", faker.bban())

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == ElGrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])


class TestEnIn:
    """Test en_IN bank provider"""

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\D{7,25}", faker.bank())


class TestNlBe:
    def test_bban(self, faker, num_samples):
        for _ in range(num_samples):
            bban = faker.bban()
            assert re.fullmatch(r"\d{12}", bban)
            account_number = bban[:-2]
            check_digits = int(bban[-2:])
            assert (97 - (int(account_number) % 97)) == check_digits or check_digits == 97

    def test_iban(self, faker, num_samples):
        for _ in range(num_samples):
            iban = faker.iban()
            assert iban[:2] == NlBeBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{12}", iban[2:])
            bban = iban[4:]
            account_number = bban[:-2]
            check_digits = int(bban[-2:])
            assert (97 - (int(account_number) % 97)) == check_digits or check_digits == 97

    def test_swift8_use_dataset(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.swift8(use_dataset=True)
            assert len(code) == 8
            assert code[:4] in NlBeBankProvider.swift_bank_codes
            assert code[4:6] == NlBeBankProvider.country_code
            assert code[6:8] in NlBeBankProvider.swift_location_codes

    def test_swift11_use_dataset(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.swift11(use_dataset=True)
            assert len(code) == 11
            assert code[:4] in NlBeBankProvider.swift_bank_codes
            assert code[4:6] == NlBeBankProvider.country_code
            assert code[6:8] in NlBeBankProvider.swift_location_codes
            assert code[8:11] in NlBeBankProvider.swift_branch_codes


class TestZhCn:
    """Test zh_CN bank provider"""

    def test_bank(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.match(r"[\u4e00-\u9fa5]{2,20}", faker.bank())
