# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from ukpostcodeparser.parser import parse_uk_postcode

from faker import Faker
from faker.providers.address.de_AT import Provider as DeAtProvider
from faker.providers.address.de_DE import Provider as DeProvider
from faker.providers.address.fa_IR import Provider as IrProvider
from faker.providers.address.el_GR import Provider as GrProvider
from faker.providers.address.en_AU import Provider as EnAuProvider
from faker.providers.address.en_CA import Provider as EnCaProvider
from faker.providers.address.en_US import Provider as EnUsProvider
from faker.providers.address.fr_FR import Provider as FrFrProvider
from faker.providers.address.fi_FI import Provider as FiProvider
from faker.providers.address.pt_PT import Provider as PtPtProvider
from faker.providers.address.ja_JP import Provider as JaProvider
from faker.providers.address.ne_NP import Provider as NeProvider
from six import string_types


class TestBaseProvider(unittest.TestCase):
    """ Tests addresses in the base provider """

    def setUp(self):
        self.factory = Faker('')

    def test_alpha_2_country_codes(self):
        country_code = Faker().country_code(representation='alpha-2')
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self):
        country_code = Faker().country_code()
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_3_country_codes(self):
        country_code = Faker().country_code(representation='alpha-3')
        assert len(country_code) == 3
        assert country_code.isalpha()

    def test_bad_country_code_representation(self):
        with self.assertRaises(ValueError):
            Faker().country_code(representation='hello')


class TestAr_AA(unittest.TestCase):
    """ Tests addresses in the ar_AA locale """

    def setUp(self):
        self.factory = Faker('ar_AA')

    def test_alpha_2_country_codes(self):
        country_code = Faker().country_code(representation='alpha-2')
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self):
        country_code = Faker().country_code()
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_3_country_codes(self):
        country_code = Faker().country_code(representation='alpha-3')
        assert len(country_code) == 3
        assert country_code.isalpha()

    def test_bad_country_code_representation(self):
        with self.assertRaises(ValueError):
            Faker().country_code(representation='hello')


class TestCsCZ(unittest.TestCase):
    """ Tests in addresses in the cs_CZ locale """

    def setUp(self):
        self.factory = Faker('cs_CZ')

    def test_street_suffix_short(self):
        street_suffix_short = self.factory.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)

    def test_street_suffix_long(self):
        street_suffix_long = self.factory.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)

    def test_city_name(self):
        city = self.factory.city_name()
        assert isinstance(city, string_types)

    def test_street_name(self):
        street_name = self.factory.street_name()
        assert isinstance(street_name, string_types)

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)

    def test_postcode(self):
        postcode = self.factory.postcode()
        assert isinstance(postcode, string_types)

    def test_city_with_postcode(self):
        city_with_postcode = self.factory.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestDeAT(unittest.TestCase):
    """ Tests in addresses in the de_AT locale """

    def setUp(self):
        self.factory = Faker('de_AT')

    def test_city(self):
        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in DeAtProvider.cities

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in DeAtProvider.states

    def test_street_suffix_short(self):
        street_suffix_short = self.factory.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)
        assert street_suffix_short in DeAtProvider.street_suffixes_short

    def test_street_suffix_long(self):
        street_suffix_long = self.factory.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)
        assert street_suffix_long in DeAtProvider.street_suffixes_long

    def test_country(self):
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in DeAtProvider.countries

    def test_postcode(self):
        postcode = self.factory.postcode()
        assert re.match(r"\d{4}", postcode)

    def test_city_with_postcode(self):
        city_with_postcode = self.factory.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestDeDE(unittest.TestCase):
    """ Tests in addresses in the de_DE locale """

    def setUp(self):
        self.factory = Faker('de_DE')

    def test_city(self):
        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in DeProvider.cities

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in DeProvider.states

    def test_street_suffix_short(self):
        street_suffix_short = self.factory.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)
        assert street_suffix_short in DeProvider.street_suffixes_short

    def test_street_suffix_long(self):
        street_suffix_long = self.factory.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)
        assert street_suffix_long in DeProvider.street_suffixes_long

    def test_country(self):
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in DeProvider.countries

    def test_city_with_postcode(self):
        city_with_postcode = self.factory.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestFaIR(unittest.TestCase):
    """ Tests in addresses in the fa_IR locale """

    def setUp(self):
        self.factory = Faker('fa_IR')

    def test_city_prefix(self):
        city_prefix = self.factory.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in IrProvider.city_prefixes

    def test_secondary_address(self):
        secondary_address = self.factory.secondary_address()
        assert isinstance(secondary_address, string_types)

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in IrProvider.states


class TestFrFR(unittest.TestCase):
    """ Tests addresses in the fr_FR locale """

    def setUp(self):
        self.factory = Faker('fr_FR')

    def test_street_prefix(self):
        street_prefix = self.factory.street_prefix()
        assert isinstance(street_prefix, string_types)
        assert street_prefix in FrFrProvider.street_prefixes

    def test_city_prefix(self):
        city_prefix = self.factory.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in FrFrProvider.city_prefixes

    def test_region(self):
        region = self.factory.region()
        assert isinstance(region, string_types)
        assert region in FrFrProvider.regions

    def test_department(self):
        department = self.factory.department()
        assert isinstance(department, tuple)
        assert department in FrFrProvider.departments

    def test_department_name(self):
        department_name = self.factory.department_name()
        assert isinstance(department_name, string_types)

    def test_department_number(self):
        department_number = self.factory.department_number()
        assert isinstance(department_number, string_types)


class TestHeIL(unittest.TestCase):
    """ Tests addresses in the he_IL locale """

    def setUp(self):
        self.factory = Faker('he_IL')

    def test_city_name(self):
        city_name = self.factory.city_name()
        assert isinstance(city_name, string_types)

    def test_street_title(self):
        street_title = self.factory.street_title()
        assert isinstance(street_title, string_types)


class TestFiFI(unittest.TestCase):
    """ Tests in addresses in the fi_FI locale """

    def setUp(self):
        self.factory = Faker('fi_FI')

    def test_city(self):
        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in FiProvider.cities

    def test_street_suffix(self):
        suffix = self.factory.street_suffix()
        assert isinstance(suffix, string_types)
        assert suffix in FiProvider.street_suffixes

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in FiProvider.states


class TestElGR(unittest.TestCase):
    """ Tests addresses in the el_GR locale """

    def setUp(self):
        self.factory = Faker('el_GR')

    def test_line_address(self):
        address = self.factory.line_address()
        assert isinstance(address, string_types)

    def test_street_prefix_short(self):
        street_prefix_short = self.factory.street_prefix_short()
        assert isinstance(street_prefix_short, string_types)
        assert street_prefix_short in GrProvider.street_prefixes_short

    def test_street_prefix_long(self):
        street_prefix_long = self.factory.street_prefix_long()
        assert isinstance(street_prefix_long, string_types)
        assert street_prefix_long in GrProvider.street_prefixes_long

    def test_street(self):
        street = self.factory.street()
        assert isinstance(street, string_types)
        assert street in GrProvider.localities

    def test_city(self):
        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in GrProvider.cities

    def test_region(self):
        region = self.factory.region()
        assert isinstance(region, string_types)
        assert region in GrProvider.regions


class TestEnAU(unittest.TestCase):
    """ Tests addresses in the en_AU locale """

    def setUp(self):
        self.factory = Faker('en_AU')

    def test_postcode(self):
        for _ in range(100):
            postcode = self.factory.postcode()
            assert re.match(r"\d{4}", postcode)

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in EnAuProvider.states

    def test_city_prefix(self):
        city_prefix = self.factory.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnAuProvider.city_prefixes

    def test_state_abbr(self):
        state_abbr = self.factory.state_abbr()
        assert isinstance(state_abbr, string_types)
        assert state_abbr in EnAuProvider.states_abbr
        assert state_abbr.isupper()


class TestEnNZ(unittest.TestCase):
    """ Tests addresses in the en_NZ locale """

    def setUp(self):
        self.factory = Faker('en_NZ')

    def test_state(self):
        # No states in New Zealand
        state = self.factory.state()
        assert state == ''

    def test_postcode(self):
        for _ in range(100):
            postcode = self.factory.postcode()
            assert re.match(r"\d{4}", postcode)


class TestEnCA(unittest.TestCase):
    """ Tests addresses in en_CA locale """

    def setUp(self):
        self.factory = Faker('en_CA')

    def test_postcode(self):
        for _ in range(100):
            postcode = self.factory.postcode()
            assert re.match(r"[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]",
                            postcode)

    def test_postalcode(self):
        for _ in range(100):
            postalcode = self.factory.postalcode()
            assert re.match(r"[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]",
                            postalcode)

    def test_postal_code_letter(self):
        postal_code_letter = self.factory.postal_code_letter()
        assert re.match(r"[A-Z]", postal_code_letter)

    def test_province(self):
        province = self.factory.province()
        assert isinstance(province, string_types)
        assert province in EnCaProvider.provinces

    def test_province_abbr(self):
        province_abbr = self.factory.province_abbr()
        assert isinstance(province_abbr, string_types)
        assert province_abbr in EnCaProvider.provinces_abbr

    def test_city_prefix(self):
        city_prefix = self.factory.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnCaProvider.city_prefixes

    def test_secondary_address(self):
        secondary_address = self.factory.secondary_address()
        assert isinstance(secondary_address, string_types)


class TestEnGB(unittest.TestCase):
    """ Tests addresses in the en_GB locale """

    def setUp(self):
        self.factory = Faker('en_GB')

    def test_postcode(self):
        for _ in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)


class TestEnUS(unittest.TestCase):
    """ Tests addresses in the en_US locale """

    def setUp(self):
        self.factory = Faker('en_US')

    def test_city_prefix(self):
        city_prefix = self.factory.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnUsProvider.city_prefixes

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in EnUsProvider.states

    def test_state_abbr(self):
        state_abbr = self.factory.state_abbr()
        assert isinstance(state_abbr, string_types)
        states_and_territories = EnUsProvider.states_and_territories_abbr
        assert state_abbr in states_and_territories

    def test_state_abbr_no_territories(self):
        state_abbr = self.factory.state_abbr(include_territories=False)
        assert isinstance(state_abbr, string_types)
        assert state_abbr in EnUsProvider.states_abbr

    def test_postcode(self):
        for _ in range(100):
            postcode = self.factory.postcode()
            assert re.match(r"\d{5}", postcode)

    def test_zipcode(self):
        for _ in range(100):
            zipcode = self.factory.zipcode()
            assert re.match(r"\d{5}", zipcode)

    def test_zipcode_plus4(self):
        for _ in range(100):
            zipcode_plus4 = self.factory.zipcode_plus4()
            assert re.match(r"\d{5}(-\d{4})", zipcode_plus4)

    def test_military_ship(self):
        military_ship = self.factory.military_ship()
        assert isinstance(military_ship, string_types)
        assert military_ship in EnUsProvider.military_ship_prefix
        assert re.match(r"[A-Z]", military_ship)

    def test_military_state(self):
        military_state = self.factory.military_state()
        assert isinstance(military_state, string_types)
        assert military_state in EnUsProvider.military_state_abbr
        assert re.match(r"[A-Z]", military_state)

    def test_military_apo(self):
        military_apo = self.factory.military_apo()
        assert isinstance(military_apo, string_types)

    def test_military_dpo(self):
        military_dpo = self.factory.military_dpo()
        assert isinstance(military_dpo, string_types)


class TestHuHU(unittest.TestCase):
    """ Tests addresses in the hu_HU locale """

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_postcode_first_digit(self):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for _ in range(100):
            pcd = self.factory.postcode()
            assert pcd[2] > "0"

    def test_street_address(self):
        """
        Tests street address.

        A street address must consist of a street name, a place type and a number, and end in a period point.
        """
        address = self.factory.street_address()
        assert address[-1] == '.'
        # Check for correct capitalisation of place type
        assert address.split(" ")[-2][0].islower()
        # Check for street number format
        assert re.match(r"\d{1,4}\.", address.split(" ")[-1])

    def test_street_address_with_county(self):
        """Tests street address with country. A street address must be:
        - in three rows,
        - starting with a valid street address,
        - contain a valid post code,
        - contain the place name validly capitalized.
        """
        address = self.factory.street_address_with_county()
        # Number of rows
        assert len(address.split("\n")) == 3
        first, second, last = address.split("\n")

        # Test street address
        assert first[0].isupper()
        assert first.split(" ")[-2][0].islower()
        assert re.match(r"\d{1,4}\.", first.split(" ")[-1])

        # Test county line
        assert second.split(" ")[-1][0].islower()
        assert second.split(" ")[0][0].isupper()

        # Test postcode
        assert re.match(r"H-[1-9]\d{3}", last.split(" ")[0])

        # Test place name capitalization
        assert last.split(" ")[-1][0].isupper()

    def test_address(self):
        """ Tests the address provider in the hu_HU locale """
        address = self.factory.address()
        assert isinstance(address, string_types)
        address_with_county = self.factory.street_address_with_county()
        assert isinstance(address_with_county, string_types)


class TestJaJP(unittest.TestCase):
    """ Tests addresses in the ja_JP locale """

    def setUp(self):
        self.factory = Faker('ja')

    def test_address(self):
        """ Test"""
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in JaProvider.countries

        prefecture = self.factory.prefecture()
        assert isinstance(prefecture, string_types)
        assert prefecture in JaProvider.prefectures

        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in JaProvider.cities

        town = self.factory.town()
        assert isinstance(town, string_types)
        assert town in JaProvider.towns

        chome = self.factory.chome()
        assert isinstance(chome, string_types)
        assert re.match(r"\d{1,2}丁目", chome)

        ban = self.factory.ban()
        assert isinstance(ban, string_types)
        assert re.match(r"\d{1,2}番", ban)

        gou = self.factory.gou()
        assert isinstance(gou, string_types)
        assert re.match(r"\d{1,2}号", gou)

        building_name = self.factory.building_name()
        assert isinstance(building_name, string_types)
        assert building_name in JaProvider.building_names

        postcode = self.factory.postcode()
        assert isinstance(postcode, string_types)
        assert re.match(r"\d{3}-\d{4}", postcode)

        zipcode = self.factory.zipcode()
        assert isinstance(zipcode, string_types)
        assert re.match(r"\d{3}-\d{4}", zipcode)

        address = self.factory.address()
        assert isinstance(address, string_types)


class TestKoKR(unittest.TestCase):
    """ Tests addresses in the ko_KR locale """

    def setUp(self):
        self.factory = Faker('ko_KR')

    def test_address(self):
        postcode = self.factory.postcode()
        assert isinstance(postcode, string_types)
        assert re.match(r"\d{5}", postcode)

        postal_code = self.factory.postal_code()
        assert isinstance(postal_code, string_types)
        assert re.match(r"\d{5}", postal_code)

        old_postal_code = self.factory.old_postal_code()
        assert isinstance(old_postal_code, string_types)
        assert re.match(r"\d{3}-\d{3}", old_postal_code)


class TestNeNP(unittest.TestCase):
    """ Tests addresses in the ne_NP locale """

    def setUp(self):
        self.factory = Faker('ne_NP')

    def test_address(self):
        """ Tests the street address in ne_NP locale """
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in NeProvider.countries

        district = self.factory.district()
        assert isinstance(district, string_types)
        assert district in NeProvider.districts

        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in NeProvider.cities


class TestNoNO(unittest.TestCase):
    """ Tests the street address in no_NO locale """

    def setUp(self):
        self.factory = Faker('no_NO')

    def test_postcode(self):
        for _ in range(100):
            assert re.match(r'^[0-9]{4}$', self.factory.postcode())

    def test_city_suffix(self):
        suffix = self.factory.city_suffix()
        assert isinstance(suffix, string_types)

    def test_street_suffix(self):
        suffix = self.factory.street_suffix()
        assert isinstance(suffix, string_types)

    def test_address(self):
        address = self.factory.address()
        assert isinstance(address, string_types)


class TestZhTW(unittest.TestCase):
    """ Tests addresses in the zh_tw locale """

    def setUp(self):
        self.factory = Faker('zh_TW')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)

        street = self.factory.street_name()
        assert isinstance(street, string_types)

        city = self.factory.city()
        assert isinstance(city, string_types)

        address = self.factory.address()
        assert isinstance(address, string_types)


class TestZhCN(unittest.TestCase):
    """ Tests addresses in the zh_cn locale """

    def setUp(self):
        self.factory = Faker('zh_CN')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)

        street = self.factory.street_name()
        assert isinstance(street, string_types)

        city = self.factory.street_address()
        assert isinstance(city, string_types)

        province = self.factory.province()
        assert isinstance(province, string_types)

        district = self.factory.district()
        assert isinstance(district, string_types)

        address = self.factory.address()
        assert isinstance(address, string_types)

        for _ in range(100):
            assert re.match(r'\d{5}', self.factory.postcode())


class TestPtBr(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pt_BR')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)

        street = self.factory.street_name()
        assert isinstance(street, string_types)

        city = self.factory.street_address()
        assert isinstance(city, string_types)

        neighborhood = self.factory.neighborhood()
        assert isinstance(neighborhood, string_types)

        state = self.factory.state()
        assert isinstance(state, string_types)

        state_abbr = self.factory.state_abbr()
        assert isinstance(state_abbr, string_types)

        address = self.factory.address()
        assert isinstance(address, string_types)


class TestPtPT(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pt_PT')

    def test_distrito(self):
        distrito = self.factory.distrito()
        assert isinstance(distrito, string_types)
        assert distrito in PtPtProvider.distritos

    def test_freguesia(self):
        freguesia = self.factory.freguesia()
        assert isinstance(freguesia, string_types)
        assert freguesia in PtPtProvider.freguesias
