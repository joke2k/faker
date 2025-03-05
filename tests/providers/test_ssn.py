import random
import re
import unittest

from datetime import datetime
from itertools import cycle
from typing import Pattern, Tuple
from unittest import mock

import freezegun
import pytest

from validators.i18n.es import es_cif as is_cif
from validators.i18n.es import es_nie as is_nie
from validators.i18n.es import es_nif as is_nif

from faker import Factory, Faker
from faker.providers.ssn.el_GR import tin_checksum as gr_tin_checksum
from faker.providers.ssn.en_CA import checksum as ca_checksum
from faker.providers.ssn.es_CL import rut_check_digit as cl_rut_checksum
from faker.providers.ssn.es_CO import nit_check_digit
from faker.providers.ssn.es_MX import curp_checksum as mx_curp_checksum
from faker.providers.ssn.es_MX import ssn_checksum as mx_ssn_checksum
from faker.providers.ssn.et_EE import checksum as et_checksum
from faker.providers.ssn.fi_FI import Provider as fi_Provider
from faker.providers.ssn.fr_FR import calculate_checksum as fr_calculate_checksum
from faker.providers.ssn.hr_HR import checksum as hr_checksum
from faker.providers.ssn.it_IT import checksum as it_checksum
from faker.providers.ssn.lv_LV import Provider as lv_Provider
from faker.providers.ssn.no_NO import Provider as no_Provider
from faker.providers.ssn.no_NO import checksum as no_checksum
from faker.providers.ssn.pl_PL import calculate_month as pl_calculate_mouth
from faker.providers.ssn.pl_PL import checksum as pl_checksum
from faker.providers.ssn.pt_BR import checksum as pt_checksum
from faker.providers.ssn.ro_RO import ssn_checksum as ro_ssn_checksum
from faker.providers.ssn.ro_RO import vat_checksum as ro_vat_checksum
from faker.providers.ssn.uk_UA import Provider as uk_Provider
from faker.providers.ssn.zh_TW import checksum as tw_checksum
from faker.utils.checksums import luhn_checksum


class TestSvSE(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("sv_SE")
        Faker.seed(0)

    def partial_sum(self, number, mult_factor):
        quotient, remainder = divmod(number * mult_factor, 10)
        return quotient + remainder

    def ssn_checksum(self, ssn):
        """Validates the checksum digit and returns a Boolean"""
        ssn = ssn.replace("-", "")
        if len(ssn) == 12:
            ssn = ssn[2:]
        if len(ssn) != 10:
            return False

        mult_factors = cycle([2, 1])
        final_sum = sum(self.partial_sum(int(char), mf) for char, mf in zip(ssn[:9], mult_factors))
        chksum = -final_sum % 10
        return chksum == int(ssn[-1])

    def validate_date_string(self, date_str):
        date_len = len(date_str)
        if date_len == 6:
            year_fmt = "%y"
        elif date_len == 8:
            year_fmt = "%Y"
        else:
            return False

        try:
            if date_str != datetime.strptime(date_str, f"{year_fmt}%m%d").strftime(f"{year_fmt}%m%d"):
                raise ValueError
            return True
        except ValueError:
            return False

    def test_pers_id_short_with_dash(self):
        """Regression case that ensures previous implementations work as-is"""
        for _ in range(100):
            pers_id = self.fake.ssn()
            assert re.search(r"\d{6}-\d{4}", pers_id)
            assert self.validate_date_string(pers_id[:6]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_short_no_dash(self):
        for _ in range(100):
            pers_id = self.fake.ssn(dash=False)
            assert re.search(r"\d{10}", pers_id)
            assert self.validate_date_string(pers_id[:6]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_long_with_dash(self):
        for _ in range(100):
            pers_id = self.fake.ssn(long=True)
            assert re.search(r"\d{8}-\d{4}", pers_id)
            assert self.validate_date_string(pers_id[:8]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_long_no_dash(self):
        for _ in range(100):
            pers_id = self.fake.ssn(long=True, dash=False)
            assert re.search(r"\d{12}", pers_id)
            assert self.validate_date_string(pers_id[:8]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_org_id_short_with_dash(self):
        for _ in range(100):
            org_id = self.fake.org_id()
            assert re.search(r"\d{6}-\d{4}", org_id)
            assert int(org_id[2:4]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_short_no_dash(self):
        for _ in range(100):
            org_id = self.fake.org_id(dash=False)
            assert re.search(r"\d{10}", org_id)
            assert int(org_id[2:4]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_long_with_dash(self):
        for _ in range(100):
            org_id = self.fake.org_id(long=True)
            assert re.search(r"\d{8}-\d{4}", org_id)
            assert int(org_id[4:6]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_long_no_dash(self):
        for _ in range(100):
            org_id = self.fake.org_id(long=True, dash=False)
            assert re.search(r"\d{12}", org_id)
            assert int(org_id[4:6]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_vat_id(self):
        for _ in range(100):
            vat_id = self.fake.vat_id()
            assert re.search(r"SE\d{12}", vat_id)
            assert int(vat_id[2]) in (1, 2, 3, 5, 6, 7, 8, 9)
            assert int(vat_id[6:8]) >= 20

    def test_org_and_vat_id(self):
        for _ in range(100):
            oid, vid = self.fake.org_and_vat_id()
            assert oid.replace("-", "")[-10:] == vid[4:-2]
            assert re.search(r"SE\d{12}", vid)


class TestBgBG(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("bg_BG")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^BG\d{9,10}$", self.fake.vat_id())


class TestCsCZ(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("cs_CZ")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^CZ\d{8,10}$", self.fake.vat_id())

    def test_birth_number(self):
        for _ in range(100):
            birth_number = self.fake.birth_number()
            assert len(birth_number) in [10, 11]
            assert birth_number[6] == "/"
            assert int(birth_number.replace("/", "")) % 11 == 0


class TestSkSK(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("sk_SK")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^SK\d{10}$", self.fake.vat_id())

    def test_birth_number(self):
        for _ in range(100):
            birth_number = self.fake.birth_number()
            assert len(birth_number) in [10, 11]
            assert birth_number[6] == "/"
            assert int(birth_number.replace("/", "")) % 11 == 0


class TestDeAT(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("de_AT")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^ATU\d{8}$", self.fake.vat_id())

    def test_ssn(self):
        for _ in range(100):
            ssn: str = self.fake.ssn()
            assert len(ssn) == 10
            assert len(self.fake.ssn(self.fake.date_of_birth())) == 10

    def test_ssn_checkdigit(self):
        for _ in range(100):
            ssn: str = self.fake.ssn()
            ssn_digits: list[int] = [int(char) for char in ssn[:3] + ssn[4:]]
            factors: list[int] = [3, 7, 9, 5, 8, 4, 2, 1, 6]
            sum: int = 0
            for index, digit in enumerate(ssn_digits):
                sum += digit * factors[index]
            assert sum % 11 == int(ssn[3])


class TestDeDe(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("de_DE")
        self.rvnr_pattern: Pattern = re.compile(r"\d{8}[A-Z]\d{3}")
        self.kvnr_pattern: Pattern = re.compile(r"[A-Z]\d{19}")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^DE\d{9}$", self.fake.vat_id())

    def test_rvnr(self):
        for _ in range(100):
            rvnr = self.fake.rvnr()
            assert self.rvnr_pattern.fullmatch(rvnr)

    def test_rvnr_birthdate(self):
        for _ in range(100):
            birthdate: datetime.date = self.fake.date_object()
            rvnr = self.fake.rvnr(birthdate)
            assert self.rvnr_pattern.fullmatch(rvnr)
            assert rvnr[2:8] == birthdate.strftime("%d%m%y")

    def test_kvnr(self):
        for _ in range(100):
            kvnr = self.fake.kvnr()
            assert self.kvnr_pattern.fullmatch(kvnr)


class TestElCY(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("el_CY")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^CY\d{9}\w$", self.fake.vat_id())


class TestElGr(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("el_GR")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            prefix = random.choice([True, False])
            vat_id = self.fake.vat_id(prefix=prefix)
            assert re.search(r"^(EL)?\d{9}$", vat_id)
            assert vat_id[2 if prefix else 0] in ("7", "8", "9", "0")
            assert str(gr_tin_checksum(vat_id[2:-1] if prefix else vat_id[:-1])) == vat_id[-1]

    def test_tin(self):
        for _ in range(100):
            tin = self.fake.tin()
            assert re.search(r"^\d{9}$", tin)
            assert tin[0] in ("1", "2", "3", "4")
            assert str(gr_tin_checksum(tin[:-1])) == tin[-1]

    def test_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn()
            assert re.search(r"^\d{11}$", ssn)
            assert datetime.strptime(ssn[:6], "%d%m%y")
            assert luhn_checksum(ssn) == 0

    def test_police_id(self):
        for _ in range(100):
            assert re.search(r"^[ΑΒΕΖΗΙΚΜΝΟΡΤΥΧ]{1,2}\d{6}$", self.fake.police_id())


class TestEnCA(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("en_CA")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(100):
            sin = self.fake.ssn()

            # Ensure that generated SINs are 11 characters long
            # including spaces, consist of spaces and digits only, and
            # satisfy the validation algorithm.
            assert len(sin) == 11
            assert sin.replace(" ", "").isdigit()
            assert ca_checksum(sin) == int(sin[-1])


class TestEnUS(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("en_US")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn(taxpayer_identification_number_type="SSN")

            # Ensure that generated SINs are 11 characters long
            # including dashes, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # An United States Social Security Number
            # (SSN) is a tax processing number issued by the Internal
            # Revenue Service with the format "AAA-GG-SSSS".  The
            # number is divided into three parts: the first three
            # digits, known as the area number because they were
            # formerly assigned by geographical region; the middle two
            # digits, known as the group number; and the final four
            # digits, known as the serial number. SSNs with the
            # following characteristics are not allocated:
            #
            # 1) Numbers with all zeros in any digit group
            # (000-##-####, ###-00-####, ###-##-0000).
            #
            # 2) Numbers with 666 or 900-999 in the first digit group.
            #
            # https://en.wikipedia.org/wiki/Social_Security_number

            assert len(ssn) == 11
            assert ssn.replace("-", "").isdigit()

            [area, group, serial] = ssn.split("-")

            assert 1 <= int(area) <= 899 and int(area) != 666
            assert 1 <= int(group) <= 99
            assert 1 <= int(serial) <= 9999
            assert area != "666"

    def test_invalid_ssn(self):
        # Magic Numbers below generate '666-92-7944', '000-54-2963', '956-GG-9478', '436-00-1386',
        # and 134-76-0000 respectively. The "group" (GG) returned for '956-GG-9478 will be a random
        # number, and that random number is not in the "itin_group_numbers" List. The random GG occurs
        # even when using the same seed_instance() due to using random.choice() for GG to avoid valid
        # ITINs being returned as an invalid SSN:
        #
        # Ensure that generated SSNs are 11 characters long
        # including dashes, consist of dashes and digits only, and the tested number
        # violates the requirements below, ensuring an INVALID SSN is returned:
        #
        # A United States Social Security Number
        # (SSN) is a tax processing number issued by the Internal
        # Revenue Service with the format "AAA-GG-SSSS".  The
        # number is divided into three parts: the first three
        # digits, known as the area number because they were
        # formerly assigned by geographical region; the middle two
        # digits, known as the group number; and the final four
        # digits, known as the serial number. SSNs with the
        # following characteristics are not allocated:
        #
        # 1) Numbers with all zeros in any digit group
        # (000-##-####, ###-00-####, ###-##-0000).
        #
        # 2) Numbers with 666 or 900-999 in the first digit group.
        #
        # https://en.wikipedia.org/wiki/Social_Security_number
        #
        # ITIN explained:
        # https://www.irs.gov/individuals/international-taxpayers/general-itin-information

        itin_group_numbers = [
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            90,
            91,
            92,
            94,
            95,
            96,
            97,
            98,
            99,
        ]

        self.fake.seed_instance(2432)
        ssn = self.fake.ssn(taxpayer_identification_number_type="INVALID_SSN")

        assert len(ssn) == 11
        assert ssn.replace("-", "").isdigit()
        assert ssn.startswith("666")

        self.fake.seed_instance(1514)
        ssn = self.fake.ssn(taxpayer_identification_number_type="INVALID_SSN")

        assert ssn.startswith("000")

        self.fake.seed_instance(2)
        ssn = self.fake.ssn(taxpayer_identification_number_type="INVALID_SSN")
        [area, group, serial] = ssn.split("-")

        assert 900 <= int(area) <= 999 and int(group) not in itin_group_numbers

        self.fake.seed_instance(0)
        ssn = self.fake.ssn(taxpayer_identification_number_type="INVALID_SSN")
        [area, group, serial] = ssn.split("-")

        assert int(area) < 900 and int(group) == 0

        self.fake.seed_instance(1)
        ssn = self.fake.ssn(taxpayer_identification_number_type="INVALID_SSN")
        [area, group, serial] = ssn.split("-")

        assert int(area) < 900 and int(serial) == 0

    def test_prohibited_ssn_value(self):
        # 666 is a prohibited value. The magic number selected as a seed
        # is one that would (if not specifically checked for) return an
        # SSN with an area of '666'.

        Faker.seed(19031)
        ssn = self.fake.ssn()
        [area, group, serial] = ssn.split("-")
        assert area != "666"

    def test_itin(self):
        for _ in range(100):
            itin = self.fake.ssn(taxpayer_identification_number_type="ITIN")

            # Ensure that generated SINs are 11 characters long
            # including dashes, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # An United States Individual Taxpayer Identification Number
            # (ITIN) is a tax processing number issued by the Internal
            # Revenue Service. It is a nine-digit number that always begins
            # with the number 9 and has a range of 70-88 in the fourth and
            # fifth digit. Effective April 12, 2011, the range was extended
            # to include 900-70-0000 through 999-88-9999, 900-90-0000
            # through 999-92-9999 and 900-94-0000 through 999-99-9999.
            # https://www.irs.gov/individuals/international-taxpayers/general-itin-information

            assert len(itin) == 11
            assert itin.replace("-", "").isdigit()

            [area, group, serial] = itin.split("-")

            assert 900 <= int(area) <= 999
            assert 70 <= int(group) <= 88 or 90 <= int(group) <= 92 or 94 <= int(group) <= 99
            assert 0 <= int(serial) <= 9999

    def test_ein(self):
        ein_prefix_choices = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "71",
            "72",
            "73",
            "74",
            "75",
            "76",
            "77",
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "90",
            "91",
            "92",
            "93",
            "94",
            "95",
            "98",
            "99",
        ]

        for _ in range(100):
            ein = self.fake.ssn(taxpayer_identification_number_type="EIN")

            # An United States An Employer Identification Number (EIN) is
            # also known as a Federal Tax Identification Number, and is
            # used to identify a business entity. EINs follow a format of a
            # two-digit prefix followed by a hyphen and a seven-digit sequence.
            # https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
            #
            # Ensure that generated EINs are 10 characters long
            # including a dash, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # There are only certain EIN Prefix values assigned:
            # https://www.irs.gov/businesses/small-businesses-self-employed/how-eins-are-assigned-and-valid-ein-prefixes

            assert len(ein) == 10
            assert ein.replace("-", "").isdigit()

            [prefix, sequence] = ein.split("-")

            assert prefix in ein_prefix_choices
            assert 0 <= int(sequence) <= 9999999

    def test_bad_tin_type(self):
        with self.assertRaises(ValueError):
            self.fake.ssn(taxpayer_identification_number_type="badValue")

    def test_wrong_tin_type_case(self):
        with self.assertRaises(ValueError):
            self.fake.ssn(taxpayer_identification_number_type="ssn")


class TestEsCO(unittest.TestCase):
    def setUp(self):
        self._NUIP_REGEX: Pattern = re.compile(r"1[012]\d{8}|[1-9]\d{6,7}")
        self._NATURAL_PERSON_NIT_REGEX: Pattern = self._NUIP_REGEX
        self._CHECK_DIGIT_REGEX: Pattern = re.compile(r"\d")
        self._LEGAL_PERSON_NIT_REGEX: Pattern = re.compile(r"[89]\d{8}")
        self.fake = Faker("es_CO")
        Faker.seed(0)

    def test_nuip(self):
        for _ in range(100):
            assert self._NUIP_REGEX.fullmatch(self.fake.nuip())
            assert self._NUIP_REGEX.fullmatch(self.fake.natural_person_nit())

    def test_natural_person_nit_with_check_digit(self):
        for _ in range(100):
            natural_person_nit, check_digit = self.fake.natural_person_nit_with_check_digit().split("-")
            assert self._NATURAL_PERSON_NIT_REGEX.fullmatch(natural_person_nit)
            assert self._CHECK_DIGIT_REGEX.fullmatch(check_digit)
            assert nit_check_digit(natural_person_nit) == check_digit

    def test_legal_person_nit(self):
        for _ in range(100):
            assert self._LEGAL_PERSON_NIT_REGEX.fullmatch(self.fake.legal_person_nit())

    def test_legal_person_nit_with_check_digit(self):
        for _ in range(100):
            legal_person_nit, check_digit = self.fake.legal_person_nit_with_check_digit().split("-")
            assert self._LEGAL_PERSON_NIT_REGEX.fullmatch(legal_person_nit)
            assert self._CHECK_DIGIT_REGEX.fullmatch(check_digit)
            assert nit_check_digit(legal_person_nit) == check_digit

    def test_nit_check_digit(self):
        # NITs and check digits of some Colombian state entities.
        # Source: <https://www.funcionpublica.gov.co/web/sigep/entidades>
        for nit, check_digit in (
            ("830040256", "0"),
            ("899999003", "1"),
            ("892301483", "2"),
            ("800194600", "3"),
            ("899999403", "4"),
            ("860042945", "5"),
            ("830114475", "6"),
            ("811000231", "7"),
            ("899999027", "8"),
            ("900639630", "9"),
        ):
            with self.subTest(nit=nit, check_digit=check_digit):
                assert nit_check_digit(nit) == check_digit


class TestEsES(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("es_ES")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^ES\w\d{8}$|^ES\d{8}\w$|^ES\w\d{7}\w$", self.fake.vat_id())

    def test_nie(self):
        for _ in range(100):
            assert is_nie(self.fake.nie())

    def test_nif(self):
        for _ in range(100):
            assert is_nif(self.fake.nif())

    def test_cif(self):
        for _ in range(100):
            assert is_cif(self.fake.cif())

    def test_doi(self):
        assert len(self.fake.doi()) == 9

    def test_nuss(self):
        for _ in range(50):
            nuss = self.fake.nuss()
            assert isinstance(nuss, str)
            assert 12 == len(nuss)
        for _ in range(50):
            nuss = self.fake.nuss(company=True)
            assert isinstance(nuss, str)
            assert 11 == len(nuss)


class TestEsCA(TestEsES):
    def setUp(self):
        self.fake = Faker("es_CA")
        Faker.seed(0)


class TestEsMX:
    def setup_method(self):
        self.fake = Faker("es_MX")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn()

            assert len(ssn) == 11
            assert ssn.isnumeric()
            assert mx_ssn_checksum(map(int, ssn[:-1])) == int(ssn[-1])

    def test_curp(self):
        for _ in range(100):
            curp = self.fake.curp()

            assert len(curp) == 18
            assert re.search(r"^[A-Z]{4}\d{6}[A-Z]{6}[0A]\d$", curp)
            assert mx_curp_checksum(curp[:-1]) == int(curp[-1])

    def test_rfc_natural(self):
        for _ in range(100):
            rfc = self.fake.rfc()

            assert len(rfc) == 13
            assert re.search(r"^[A-Z]{4}\d{6}[0-9A-Z]{3}$", rfc)

    def test_rfc_legal(self):
        for _ in range(100):
            rfc = self.fake.rfc(natural=False)

            assert len(rfc) == 12
            assert re.search(r"^[A-Z]{3}\d{6}[0-9A-Z]{3}$", rfc)

    @pytest.mark.parametrize(
        "gender,pattern",
        [
            ("M", r"^[A-Z]{6}\d{8}M\d{3}$"),
            ("H", r"^[A-Z]{6}\d{8}H\d{3}$"),
            (None, r"^[A-Z]{6}\d{8}[HM]\d{3}$"),
        ],
        ids=["woman", "man", "any"],
    )
    def test_elector_code(self, gender, pattern):
        for _ in range(100):
            elector_code = self.fake.elector_code(gender=gender)

            assert len(elector_code) == 18
            assert re.search(pattern, elector_code)

    def test_elector_code_unsupported_gender(self):
        with pytest.raises(ValueError, match="Gender must be"):
            self.fake.elector_code("Z")


class TestEsCL(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("es_CL")
        Faker.seed(0)

    def test_rut(self):
        for _ in range(100):
            rut = self.fake.rut(min=10000000)
            digits, check_digit = self._extract_digits(rut)

            assert len(rut) == 12
            assert check_digit == cl_rut_checksum(digits)

    @staticmethod
    def _extract_digits(rut) -> Tuple[int, str]:
        """Extracts the digits and check digit from a formatted RUT."""
        char_filter = re.compile(r"[^0-9]")
        check_digit = rut[-1]
        digits = char_filter.sub("", rut[:-1])

        return int(digits), check_digit


class TestEtEE(unittest.TestCase):
    """Tests SSN in the et_EE locale"""

    def setUp(self):
        self.fake = Faker("et_EE")

        Faker.seed(0)

    def test_ssn_checksum(self):
        assert et_checksum([4, 4, 1, 1, 1, 3, 0, 4, 9, 2]) == 3
        assert et_checksum([3, 6, 7, 0, 1, 1, 6, 6, 2, 7]) == 8
        assert et_checksum([4, 7, 0, 0, 4, 2, 1, 5, 0, 1]) == 2
        assert et_checksum([3, 9, 7, 0, 3, 0, 4, 3, 3, 6]) == 0

    @freezegun.freeze_time("2019-03-11")
    def test_ssn(self):
        self.fake.seed_instance(1)
        value = self.fake.ssn()
        assert re.search(r"^\d{11}$", value)
        assert not value.endswith("0")

        self.fake.seed_instance(0)
        value = self.fake.ssn()

        assert re.search(r"^\d{11}$", value)
        assert value.endswith("0")

    @freezegun.freeze_time("2002-01-01")
    def test_ssn_2000(self):
        self.fake.seed_instance(0)
        value = self.fake.ssn(min_age=0, max_age=1)
        assert re.search(r"^\d{11}$", value)
        assert value[0] in ("5", "6")

    @freezegun.freeze_time("2101-01-01")
    def test_ssn_2100(self):
        self.fake.seed_instance(0)
        value = self.fake.ssn(min_age=0, max_age=1)
        assert re.search(r"^\d{11}$", value)
        assert value[0] in ("7", "8")

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^EE\d{9}$", self.fake.vat_id())


class TestFiFI(unittest.TestCase):
    """Tests SSN in the fi_FI locale"""

    def setUp(self):
        self.fake = Faker("fi_FI")
        Faker.seed(0)
        self.provider = fi_Provider

    def test_century_code(self):
        assert self.provider._get_century_code(1900) == "-"
        assert self.provider._get_century_code(1999) == "-"
        assert self.provider._get_century_code(2000) == "A"
        assert self.provider._get_century_code(2999) == "A"
        assert self.provider._get_century_code(1800) == "+"
        assert self.provider._get_century_code(1899) == "+"
        with pytest.raises(ValueError):
            self.provider._get_century_code(1799)
        with pytest.raises(ValueError):
            self.provider._get_century_code(3000)

    def test_ssn_sanity(self):
        for age in range(100):
            self.fake.ssn(min_age=age, max_age=age + 1)

    def test_valid_ssn(self):
        ssn = self.fake.ssn(artificial=False)
        individual_number = int(ssn[7:10])
        assert individual_number <= 899

    def test_artifical_ssn(self):
        ssn = self.fake.ssn(artificial=True)
        individual_number = int(ssn[7:10])
        assert individual_number >= 900

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^FI\d{8}$", self.fake.vat_id())

    @freezegun.freeze_time("2023-10-23")
    def test_ssn_without_age_range(self):
        current_year = 2023
        age = current_year - 1995
        ssn = self.fake.ssn(min_age=age, max_age=age, artificial=True)
        assert "95-" in ssn
        age = current_year - 2013
        ssn = self.fake.ssn(min_age=age, max_age=age, artificial=True)
        assert "13A" in ssn
        age = current_year - 1898
        ssn = self.fake.ssn(min_age=age, max_age=age, artificial=True)
        assert "98+" in ssn


class TestFrFR(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("fr_FR")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^FR[\w\d]{2} \d{9}$", self.fake.vat_id())

    def test_ssn(self) -> None:
        for _ in range(100):
            assert re.search(r"^\d{15}$", self.fake.ssn())

    def test_checksum(self) -> None:
        assert fr_calculate_checksum(2570533063999) == 3


class TestFrCH:
    @pytest.mark.parametrize(
        "digits,expected",
        [
            ("22500105", "CHE225001055"),
            ("60362354", "CHE603623540"),
            ("36806684", "CHE368066842"),
        ],
        ids=[
            "checksum_remainder_11",
            "checksum_remainder_10",
            "checksum_remainder_other",
        ],
    )
    def test_checksum(self, digits, expected):
        """The checksum of the Swiss UID number is calculated correctly
        given a certain input of 8 digits."""
        fake = Faker("fr_CH")
        Faker.seed(0)

        with mock.patch(
            "faker.providers.ssn.fr_CH.Provider.numerify",
            return_value=digits,
            autospec=True,
        ):
            result = fake.vat_id()
            assert result == expected


class TestEnGB(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("en_GB")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(
                r"^GB\d{3} \d{4} \d{2}(?: \d{3})?$|^GB(?:GD|HA)\d{3}$",
                self.fake.vat_id(),
            )


class TestHrHR(unittest.TestCase):
    """Tests SSN in the hr_HR locale"""

    def setUp(self):
        self.fake = Faker("hr_HR")
        Faker.seed(0)

    def test_ssn_checksum(self):
        assert hr_checksum([0, 0, 2, 2, 8, 2, 6, 9, 2, 8]) == 9
        assert hr_checksum([5, 8, 9, 3, 6, 9, 5, 1, 2, 5]) == 1
        assert hr_checksum([5, 7, 8, 0, 2, 0, 3, 4, 2, 3]) == 7
        assert hr_checksum([4, 3, 3, 3, 1, 4, 6, 7, 6, 2]) == 2
        assert hr_checksum([0, 5, 9, 3, 7, 7, 5, 9, 1, 8]) == 7
        assert hr_checksum([7, 1, 1, 4, 9, 9, 1, 2, 4, 1]) == 6

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r"^\d{11}$", self.fake.ssn())

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^HR\d{11}$", self.fake.vat_id())


class TestHuHU(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("hu_HU")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn()
            assert ssn.isdigit()
            assert len(ssn) >= 10
            assert len(ssn) <= 12

        for _ in range(100):
            dob_val = (
                f"{self.fake.random_int(0, 99):02d}"
                f"{self.fake.random_int(1, 12):02d}"
                f"{self.fake.random_int(1, 31):02d}"
            )
            dob = self.fake.random.choice([None, dob_val])
            gender = self.fake.random.choice([None, "F", "M", "z"])
            try:
                ssn = self.fake.ssn(dob=dob, gender=gender)
                assert ssn.isdigit()
                assert len(ssn) >= 10
                assert len(ssn) <= 12
            except ValueError:
                pass

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^HU\d{8}$", self.fake.vat_id())


class TestItIT(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("it_IT")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^IT\d{11}$", self.fake.vat_id())

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r"^[A-Z]{6}\d{2}[ABCDEHLMPRST][0-7]\d[A-Z]\d{3}[A-Z]$", self.fake.ssn())

    def test_checksum(self) -> None:
        assert it_checksum("MDDMRA80L41H501") == "R"

    def test_ssn_with_latin_chars(self):
        generator = Factory.create("it_IT")
        generator.last_name = mock.MagicMock(return_value="Foà")
        ssn = generator.ssn()
        self.assertEqual(len(ssn), 16)
        self.assertEqual(ssn[:3], "FOA")


class TestPtBR(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("pt_BR")
        Faker.seed(0)

    def test_pt_BR_ssn_checksum(self):
        assert pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]) == 2
        assert pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]) == 0

    def test_pt_BR_ssn(self):
        for _ in range(100):
            assert re.search(r"^\d{11}$", self.fake.ssn())

    def test_pt_BR_cpf(self):
        for _ in range(100):
            assert re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}", self.fake.cpf())

    def test_pt_BR_rg(self):
        for _ in range(100):
            to_test = self.fake.rg()
            if "X" in to_test:
                assert re.search(r"^\d{8}X", to_test)
            else:
                assert re.search(r"^\d{9}$", to_test)


class TestNlBE(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("nl_BE")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(1000):
            ssn = self.fake.ssn()
            assert len(ssn) == 11
            gen_seq = ssn[6:9]
            gen_chksum = ssn[9:11]
            gen_seq_as_int = int(gen_seq)
            gen_chksum_as_int = int(gen_chksum)
            # Check that the sequence nr is between 1 inclusive and 998 inclusive
            assert gen_seq_as_int > 0
            assert gen_seq_as_int <= 998

            # validate checksum calculation
            # Since the century is not part of ssn, try both below and above year 2000
            ssn_below = int(ssn[0:9])
            chksum_below = 97 - (ssn_below % 97)
            ssn_above = ssn_below + 2000000000
            chksum_above = 97 - (ssn_above % 97)
            results = [chksum_above, chksum_below]
            assert gen_chksum_as_int in results


class TestNlNL(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("nl_NL")
        Faker.seed(0)

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^NL\d{9}B\d{2}$", self.fake.vat_id())


class TestNoNO(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("no_NO")
        Faker.seed(0)

    def test_no_NO_ssn_checksum(self):
        assert no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7], no_Provider.scale1) == 6
        assert no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7, 6], no_Provider.scale2) == 7

    def test_no_NO_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn()
            assert ssn.isdigit()
            assert len(ssn) == 11

    def test_no_NO_ssn_dob_passed(self):
        test_data = [("20010203", "030201"), ("19991231", "311299")]
        for date_of_birth, expected_dob_part in test_data:
            ssn = self.fake.ssn(dob=date_of_birth)
            assert ssn[:6] == expected_dob_part

    def test_no_NO_ssn_invalid_dob_passed(self):
        with pytest.raises(ValueError):
            self.fake.ssn(dob="010401")
        with pytest.raises(ValueError):
            self.fake.ssn(dob="hello_world")
        with pytest.raises(ValueError):
            self.fake.ssn(dob="001301")

    def test_no_NO_ssn_gender_passed(self):
        # Females have even number at index 8
        ssn = self.fake.ssn(gender="F")
        assert int(ssn[8]) % 2 == 0
        # Males have odd number at index 8
        ssn = self.fake.ssn(gender="M")
        assert int(ssn[8]) % 2 == 1

    def test_no_NO_ssn_invalid_gender_passed(self):
        with pytest.raises(ValueError):
            self.fake.ssn(gender="A")


class TestPlPL(unittest.TestCase):
    """Tests SSN in the pl_PL locale"""

    def setUp(self):
        self.fake = Faker("pl_PL")
        Faker.seed(0)

    def test_ssn_checksum(self):
        assert pl_checksum([0, 5, 2, 6, 2, 8, 1, 2, 3, 6]) == 5
        assert pl_checksum([8, 5, 0, 5, 0, 8, 1, 5, 5, 8]) == 7
        assert pl_checksum([4, 5, 1, 1, 1, 0, 0, 2, 4, 3]) == 3
        assert pl_checksum([9, 1, 0, 7, 2, 6, 1, 4, 8, 7]) == 3
        assert pl_checksum([8, 1, 1, 2, 1, 4, 1, 1, 8, 7]) == 6

    def test_calculate_month(self):
        assert pl_calculate_mouth(datetime.strptime("1 1 1900", "%m %d %Y")) == 1
        assert pl_calculate_mouth(datetime.strptime("12 1 1900", "%m %d %Y")) == 12
        assert pl_calculate_mouth(datetime.strptime("1 1 1999", "%m %d %Y")) == 1

        assert pl_calculate_mouth(datetime.strptime("1 1 2000", "%m %d %Y")) == 21
        assert pl_calculate_mouth(datetime.strptime("12 1 2000", "%m %d %Y")) == 32
        assert pl_calculate_mouth(datetime.strptime("1 1 2099", "%m %d %Y")) == 21

        assert pl_calculate_mouth(datetime.strptime("1 1 2100", "%m %d %Y")) == 41
        assert pl_calculate_mouth(datetime.strptime("12 1 2100", "%m %d %Y")) == 52
        assert pl_calculate_mouth(datetime.strptime("1 1 2199", "%m %d %Y")) == 41

        assert pl_calculate_mouth(datetime.strptime("1 1 2200", "%m %d %Y")) == 61
        assert pl_calculate_mouth(datetime.strptime("12 1 2200", "%m %d %Y")) == 72
        assert pl_calculate_mouth(datetime.strptime("1 1 2299", "%m %d %Y")) == 61

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r"^\d{11}$", self.fake.ssn())

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^PL\d{10}$", self.fake.vat_id())


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.sss_pattern: Pattern = re.compile(r"^\d{2}-\d{7}-\d$")
        self.gsis_pattern: Pattern = re.compile(r"^\d{11}$")
        self.philhealth_pattern: Pattern = re.compile(r"^\d{2}-\d{9}-\d$")
        self.pagibig_pattern: Pattern = re.compile(r"^\d{4}-\d{4}-\d{4}$")
        self.umid_pattern: Pattern = re.compile(r"^\d{4}-\d{7}-\d$")
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker("en_PH")
        Faker.seed(0)

    def test_PH_sss(self):
        for i in range(self.num_sample_runs):
            assert self.sss_pattern.match(self.fake.sss())

    def test_PH_gsis(self):
        for i in range(self.num_sample_runs):
            assert self.gsis_pattern.match(self.fake.gsis())

    def test_PH_philhealth(self):
        for i in range(self.num_sample_runs):
            assert self.philhealth_pattern.match(self.fake.philhealth())

    def test_PH_pagibig(self):
        for i in range(self.num_sample_runs):
            assert self.pagibig_pattern.match(self.fake.pagibig())

    def test_PH_umid(self):
        for i in range(self.num_sample_runs):
            assert self.umid_pattern.match(self.fake.umid())


class TestFilPh(TestEnPh):
    def setup_faker(self):
        self.fake = Faker("fil_PH")
        Faker.seed(0)


class TestThTH(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("th_TH")
        Faker.seed(0)

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r"^[1-8]-[1-9]\d{3}-\d{5}-\d{2}-\d$", self.fake.ssn())

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^[1-8]-[1-9]\d{3}-\d{5}-\d{2}-\d$", self.fake.vat_id())


class TestTlPh(TestEnPh):
    def setup_faker(self):
        self.fake = Faker("tl_PH")
        Faker.seed(0)


class TestTrTr(unittest.TestCase):
    num_sample_runs = 10

    def setUp(self):
        self.fake = Faker("tr_TR")
        self.samples = [self.fake.ssn() for _ in range(self.num_sample_runs)]
        Faker.seed(0)

    def first_part_non_zero(self):
        for sample in self.samples:
            assert sample[0] != 0

    def compare_first_ten_and_last_part(self):
        for sample in self.samples:
            first_ten_number = sample[:-1]
            last_part = sample[-1]
            assert sum(int(x) for x in f"{first_ten_number}") % 10 == last_part


class TestEnIn(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("en_IN")
        Faker.seed(0)
        test_samples = 10
        self.aadhaar_ids = [self.fake.aadhaar_id() for _ in range(test_samples)]

    def test_length(self):
        for aadhaar_id in self.aadhaar_ids:
            assert len(aadhaar_id) == 12

    def test_first_digit_non_zero(self):
        for aadhar_id in self.aadhaar_ids:
            assert aadhar_id[0] != "0"

    def test_valid_luhn(self):
        for aadhaar_id in self.aadhaar_ids:
            assert luhn_checksum(aadhaar_id) == 0


class TestZhCN(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("zh_CN")
        Faker.seed(0)

    def test_zh_CN_ssn(self):
        for _ in range(100):
            ssn = self.fake.ssn()
            assert len(ssn) == 18

    def test_zh_CN_ssn_invalid_gender_passed(self):
        with pytest.raises(ValueError):
            self.fake.ssn(gender="X")
        with pytest.raises(ValueError):
            self.fake.ssn(gender="*")
        with pytest.raises(ValueError):
            self.fake.ssn(gender="22")

    def test_zh_CN_ssn_gender_passed(self):
        # Females have even number at index 17
        ssn = self.fake.ssn(gender="F")
        assert int(ssn[16]) % 2 == 0
        # Males have odd number at index 17
        ssn = self.fake.ssn(gender="M")
        assert int(ssn[16]) % 2 == 1

    def test_zh_CN_ssn_invalid_area_code_passed(self):
        ssn = self.fake.ssn(area_code=12)
        assert int(ssn[0:6]) > 0

        ssn = self.fake.ssn(area_code={})
        assert int(ssn[0:6]) > 0

        ssn = self.fake.ssn(area_code=[])
        assert int(ssn[0:6]) > 0

        ssn = self.fake.ssn(area_code=None)
        assert int(ssn[0:6]) > 0

        ssn = self.fake.ssn()
        assert int(ssn[0:6]) > 0

    def test_zh_CN_ssn_area_code_passed(self):
        #
        ssn = self.fake.ssn(area_code="654225")
        assert int(ssn[0:6]) == 654225

        ssn = self.fake.ssn(area_code="820000")
        assert int(ssn[0:6]) == 820000

        ssn = self.fake.ssn(area_code="830000")
        assert int(ssn[0:6]) == 830000


class TestRoRO(unittest.TestCase):
    """Tests SSN in the ro_RO locale"""

    def setUp(self):
        self.fake = Faker("ro_RO")
        Faker.seed(0)

    def test_ssn_checksum(self):
        assert ro_ssn_checksum("188050510739") == 0
        assert ro_ssn_checksum("181111512587") == 1
        assert ro_ssn_checksum("190123152499") == 2
        assert ro_ssn_checksum("601100452314") == 3
        assert ro_ssn_checksum("296072904713") == 4
        assert ro_ssn_checksum("601100452314") == 3
        assert ro_ssn_checksum("192080516368") == 6
        assert ro_ssn_checksum("602041144519") == 7
        assert ro_ssn_checksum("197061731387") == 8
        assert ro_ssn_checksum("294112120140") == 9

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r"^\d{13}$", self.fake.ssn())

    def test_vat_checksum(self):
        assert ro_vat_checksum("1") == 9
        assert ro_vat_checksum("41") == 8
        assert ro_vat_checksum("181") == 2
        assert ro_vat_checksum("82421") == 5
        assert ro_vat_checksum("424694") == 7
        assert ro_vat_checksum("3918774") == 6
        assert ro_vat_checksum("99380784") == 1
        assert ro_vat_checksum("971775895") == 8

    def test_vat_id(self):
        for _ in range(100):
            vat = self.fake.vat_id().replace("RO", "")
            assert vat.isdigit()
            assert len(vat) >= 2 and len(vat) <= 10


class TestAzAz(unittest.TestCase):
    num_sample_runs = 10

    def setUp(self):
        self.fake = Faker("az_AZ")
        self.samples = [self.fake.ssn() for _ in range(self.num_sample_runs)]
        Faker.seed(0)

    def check_length(self):
        for sample in self.samples:
            assert len(sample) == 7


class TestLvLV(unittest.TestCase):
    num_sample_runs = 10

    def setUp(self):
        self.fake = Faker("lv_LV")
        Faker.seed(0)
        self.samples = [self.fake.ssn() for _ in range(self.num_sample_runs)]
        self.provider = lv_Provider

    def test_century_code(self):
        assert self.provider._get_century_code(1900) == 1
        assert self.provider._get_century_code(1999) == 1
        assert self.provider._get_century_code(2000) == 2
        assert self.provider._get_century_code(2999) == 2
        assert self.provider._get_century_code(1800) == 0
        assert self.provider._get_century_code(1899) == 0
        with pytest.raises(ValueError):
            self.provider._get_century_code(1799)
        with pytest.raises(ValueError):
            self.provider._get_century_code(3000)

    def test_ssn_sanity(self):
        for age in range(100):
            self.fake.ssn(min_age=age, max_age=age + 1)

    def check_length(self):
        for sample in self.samples:
            assert len(sample) == 12

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r"^LV\d{11}$", self.fake.vat_id())


class TestZhTW(unittest.TestCase):
    num_sample_runs = 10

    def setUp(self):
        self.fake = Faker("zh_TW")
        Faker.seed(0)
        self.samples = [self.fake.ssn() for _ in range(self.num_sample_runs)]

    def test_length(self):
        for sample in self.samples:
            assert len(sample) == 10

    def test_gender(self):
        """only '1' and '2' are allowed in the second char"""
        for sample in self.samples:
            assert sample[1] == "1" or sample[1] == "2"

    def test_checksum(self):
        for sample in self.samples:
            assert tw_checksum(sample) % 10 == 0


class TestUkUA(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("uk_Ua")
        Faker.seed(0)
        self.provider = uk_Provider

    def test_ssn_len(self):
        assert len(self.fake.ssn()) == 10

    def test_start_ssn(self):
        assert self.fake.ssn("21-06-1994")[:5] == "34505"

    def test_ssn_gender(self):
        m = self.fake.ssn(gender="M")
        w = self.fake.ssn(gender="F")
        assert int(m[8]) % 2 != 0, "Must be odd for men"
        assert int(w[8]) % 2 == 0, "Must be even for women"

    def test_incorrect_birthday(self):
        with pytest.raises(ValueError):
            self.fake.ssn(birthday="1994-06-01")

    def test_incorrect_gender(self):
        with pytest.raises(ValueError):
            self.fake.ssn(gender="f")
