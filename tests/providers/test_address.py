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
from faker.providers.address.es_ES import Provider as EsEsProvider
from faker.providers.address.es_MX import Provider as EsMxProvider
from faker.providers.address.fr_FR import Provider as FrFrProvider
from faker.providers.address.fi_FI import Provider as FiProvider
from faker.providers.address.hy_AM import Provider as HyAmProvider
from faker.providers.address.pt_PT import Provider as PtPtProvider
from faker.providers.address.ja_JP import Provider as JaProvider
from faker.providers.address.ne_NP import Provider as NeProvider
from six import string_types


class TestBaseProvider(unittest.TestCase):
    """ Tests addresses in the base provider """

    def setUp(self):
        self.fake = Faker('')
        Faker.seed(0)

    def test_alpha_2_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-2')
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self):
        country_code = self.fake.country_code()
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_3_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-3')
        assert len(country_code) == 3
        assert country_code.isalpha()

    def test_bad_country_code_representation(self):
        with self.assertRaises(ValueError):
            self.fake.country_code(representation='hello')


class TestAr_AA(unittest.TestCase):
    """ Tests addresses in the ar_AA locale """

    def setUp(self):
        self.fake = Faker('ar_AA')
        Faker.seed(0)

    def test_alpha_2_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-2')
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self):
        country_code = self.fake.country_code()
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_3_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-3')
        assert len(country_code) == 3
        assert country_code.isalpha()

    def test_bad_country_code_representation(self):
        with self.assertRaises(ValueError):
            self.fake.country_code(representation='hello')


class TestCsCZ(unittest.TestCase):
    """ Tests in addresses in the cs_CZ locale """

    def setUp(self):
        self.fake = Faker('cs_CZ')
        Faker.seed(0)

    def test_street_suffix_short(self):
        street_suffix_short = self.fake.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)

    def test_street_suffix_long(self):
        street_suffix_long = self.fake.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)

    def test_city_name(self):
        city = self.fake.city_name()
        assert isinstance(city, string_types)

    def test_street_name(self):
        street_name = self.fake.street_name()
        assert isinstance(street_name, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)

    def test_postcode(self):
        postcode = self.fake.postcode()
        assert isinstance(postcode, string_types)

    def test_city_with_postcode(self):
        city_with_postcode = self.fake.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestDeAT(unittest.TestCase):
    """ Tests in addresses in the de_AT locale """

    def setUp(self):
        self.fake = Faker('de_AT')
        Faker.seed(0)

    def test_city(self):
        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in DeAtProvider.cities

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in DeAtProvider.states

    def test_street_suffix_short(self):
        street_suffix_short = self.fake.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)
        assert street_suffix_short in DeAtProvider.street_suffixes_short

    def test_street_suffix_long(self):
        street_suffix_long = self.fake.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)
        assert street_suffix_long in DeAtProvider.street_suffixes_long

    def test_country(self):
        country = self.fake.country()
        assert isinstance(country, string_types)
        assert country in DeAtProvider.countries

    def test_postcode(self):
        postcode = self.fake.postcode()
        assert re.match(r"\d{4}", postcode)

    def test_city_with_postcode(self):
        city_with_postcode = self.fake.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestDeDE(unittest.TestCase):
    """ Tests in addresses in the de_DE locale """

    def setUp(self):
        self.fake = Faker('de_DE')
        Faker.seed(0)

    def test_city(self):
        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in DeProvider.cities

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in DeProvider.states

    def test_street_suffix_short(self):
        street_suffix_short = self.fake.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)
        assert street_suffix_short in DeProvider.street_suffixes_short

    def test_street_suffix_long(self):
        street_suffix_long = self.fake.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)
        assert street_suffix_long in DeProvider.street_suffixes_long

    def test_country(self):
        country = self.fake.country()
        assert isinstance(country, string_types)
        assert country in DeProvider.countries

    def test_city_with_postcode(self):
        city_with_postcode = self.fake.city_with_postcode()
        assert isinstance(city_with_postcode, string_types)


class TestElGR(unittest.TestCase):
    """ Tests addresses in the el_GR locale """

    def setUp(self):
        self.fake = Faker('el_GR')
        Faker.seed(0)

    def test_line_address(self):
        address = self.fake.line_address()
        assert isinstance(address, string_types)

    def test_street_prefix_short(self):
        street_prefix_short = self.fake.street_prefix_short()
        assert isinstance(street_prefix_short, string_types)
        assert street_prefix_short in GrProvider.street_prefixes_short

    def test_street_prefix_long(self):
        street_prefix_long = self.fake.street_prefix_long()
        assert isinstance(street_prefix_long, string_types)
        assert street_prefix_long in GrProvider.street_prefixes_long

    def test_street(self):
        street = self.fake.street()
        assert isinstance(street, string_types)
        assert street in GrProvider.localities

    def test_city(self):
        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in GrProvider.cities

    def test_region(self):
        region = self.fake.region()
        assert isinstance(region, string_types)
        assert region in GrProvider.regions


class TestEnAU(unittest.TestCase):
    """ Tests addresses in the en_AU locale """

    def setUp(self):
        self.fake = Faker('en_AU')
        Faker.seed(0)

    def test_postcode(self):
        for _ in range(100):
            postcode = self.fake.postcode()
            assert re.match(r"\d{4}", postcode)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in EnAuProvider.states

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnAuProvider.city_prefixes

    def test_state_abbr(self):
        state_abbr = self.fake.state_abbr()
        assert isinstance(state_abbr, string_types)
        assert state_abbr in EnAuProvider.states_abbr
        assert state_abbr.isupper()


class TestEnNZ(unittest.TestCase):
    """ Tests addresses in the en_NZ locale """

    def setUp(self):
        self.fake = Faker('en_NZ')
        Faker.seed(0)

    def test_state(self):
        # No states in New Zealand
        state = self.fake.state()
        assert state == ''

    def test_postcode(self):
        for _ in range(100):
            postcode = self.fake.postcode()
            assert re.match(r"\d{4}", postcode)


class TestEnCA(unittest.TestCase):
    """ Tests addresses in en_CA locale """

    def setUp(self):
        self.fake = Faker('en_CA')
        Faker.seed(0)
        self.valid_postcode_letter_re = r'[{}]'.format(
            ''.join(EnCaProvider.postal_code_letters))
        self.valid_postcode_re = r"{0}[0-9]{0} ?[0-9]{0}[0-9]".format(
            self.valid_postcode_letter_re)

    def test_postcode(self):
        for _ in range(100):
            postcode = self.fake.postcode()
            assert re.match(self.valid_postcode_re, postcode)

    def test_postcode_in_province(self):
        for province_abbr in EnCaProvider.provinces_abbr:
            code = self.fake.postcode_in_province(province_abbr)
            assert code[0] in EnCaProvider.provinces_postcode_prefixes[
                province_abbr]

        with self.assertRaises(Exception):
            self.fake.postcode_in_province('XX')

    def test_postalcode(self):
        for _ in range(100):
            postalcode = self.fake.postalcode()
            assert re.match(self.valid_postcode_letter_re, postalcode)

    def test_postal_code_letter(self):
        postal_code_letter = self.fake.postal_code_letter()
        assert re.match(self.valid_postcode_letter_re, postal_code_letter)

    def test_province(self):
        province = self.fake.province()
        assert isinstance(province, string_types)
        assert province in EnCaProvider.provinces

    def test_province_abbr(self):
        province_abbr = self.fake.province_abbr()
        assert isinstance(province_abbr, string_types)
        assert province_abbr in EnCaProvider.provinces_abbr

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnCaProvider.city_prefixes

    def test_secondary_address(self):
        secondary_address = self.fake.secondary_address()
        assert isinstance(secondary_address, string_types)


class TestEnGB(unittest.TestCase):
    """ Tests addresses in the en_GB locale """

    def setUp(self):
        self.fake = Faker('en_GB')
        Faker.seed(0)

    def test_postcode(self):
        for _ in range(100):
            assert isinstance(parse_uk_postcode(self.fake.postcode()), tuple)


class TestEnUS(unittest.TestCase):
    """ Tests addresses in the en_US locale """

    def setUp(self):
        self.fake = Faker('en_US')
        Faker.seed(0)

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EnUsProvider.city_prefixes

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in EnUsProvider.states

    def test_state_abbr(self):
        state_abbr = self.fake.state_abbr()
        assert isinstance(state_abbr, string_types)
        states_and_territories = EnUsProvider.states_and_territories_abbr
        assert state_abbr in states_and_territories

    def test_state_abbr_no_territories(self):
        state_abbr = self.fake.state_abbr(include_territories=False)
        assert isinstance(state_abbr, string_types)
        assert state_abbr in EnUsProvider.states_abbr

    def test_postcode(self):
        for _ in range(100):
            code = self.fake.postcode()
            assert re.match(r"\d{5}", code)

    def test_postcode_in_state(self):
        for state_abbr in EnUsProvider.states_abbr:
            code = self.fake.postcode_in_state(state_abbr)
            assert re.match(r"\d{5}", code)
            assert int(code) >= EnUsProvider.states_postcode[state_abbr][0]
            assert int(code) <= EnUsProvider.states_postcode[state_abbr][1]

        with self.assertRaises(Exception):
            self.fake.postcode_in_state('XX')

    def test_zipcode(self):
        for _ in range(100):
            zipcode = self.fake.zipcode()
            assert re.match(r"\d{5}", zipcode)

    def test_zipcode_in_state(self):
        for state_abbr in EnUsProvider.states_abbr:
            code = self.fake.zipcode_in_state(state_abbr)
            assert re.match(r"\d{5}", code)
            assert int(code) >= EnUsProvider.states_postcode[state_abbr][0]
            assert int(code) <= EnUsProvider.states_postcode[state_abbr][1]

        with self.assertRaises(Exception):
            self.fake.zipcode_in_state('XX')

    def test_zipcode_plus4(self):
        for _ in range(100):
            zipcode_plus4 = self.fake.zipcode_plus4()
            assert re.match(r"\d{5}(-\d{4})", zipcode_plus4)

    def test_military_ship(self):
        military_ship = self.fake.military_ship()
        assert isinstance(military_ship, string_types)
        assert military_ship in EnUsProvider.military_ship_prefix
        assert re.match(r"[A-Z]", military_ship)

    def test_military_state(self):
        military_state = self.fake.military_state()
        assert isinstance(military_state, string_types)
        assert military_state in EnUsProvider.military_state_abbr
        assert re.match(r"[A-Z]", military_state)

    def test_military_apo(self):
        military_apo = self.fake.military_apo()
        assert isinstance(military_apo, string_types)

    def test_military_dpo(self):
        military_dpo = self.fake.military_dpo()
        assert isinstance(military_dpo, string_types)

    def test_postalcode(self):
        for _ in range(100):
            postalcode = self.fake.postalcode()
            assert re.match(r"\d{5}", postalcode)

    def test_postalcode_in_state(self):
        for state_abbr in EnUsProvider.states_abbr:
            code = self.fake.postalcode_in_state(state_abbr)
            assert re.match(r"\d{5}", code)
            assert int(code) >= EnUsProvider.states_postcode[state_abbr][0]
            assert int(code) <= EnUsProvider.states_postcode[state_abbr][1]

        with self.assertRaises(Exception):
            self.fake.postalcode_in_state('XX')


class TestEsES(unittest.TestCase):
    """ Tests in addresses in the fa_IR locale """

    def setUp(self):
        self.fake = Faker('es_ES')
        Faker.seed(0)

    def test_state_name(self):
        state_name = self.fake.state_name()
        assert isinstance(state_name, string_types)
        assert state_name in EsEsProvider.states

    def test_street_prefix(self):
        street_prefix = self.fake.street_prefix()
        assert isinstance(street_prefix, string_types)
        assert street_prefix in EsEsProvider.street_prefixes

    def test_secondary_address(self):
        secondary_address = self.fake.secondary_address()
        assert isinstance(secondary_address, string_types)


class TestEsMX(unittest.TestCase):
    """ Tests the addresses in the es_MX locale """

    def setUp(self):
        self.fake = Faker('es_MX')
        Faker.seed(0)

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in EsMxProvider.city_prefixes

    def test_city_suffix(self):
        city_suffix = self.fake.city_suffix()
        assert isinstance(city_suffix, string_types)
        assert city_suffix in EsMxProvider.city_suffixes

    def test_city_adjective(self):
        city_adjective = self.fake.city_adjective()
        assert isinstance(city_adjective, string_types)
        assert city_adjective in EsMxProvider.city_adjectives

    def test_street_prefix(self):
        street_prefix = self.fake.street_prefix()
        assert isinstance(street_prefix, string_types)
        assert street_prefix in EsMxProvider.street_prefixes

    def test_secondary_address(self):
        secondary_address = self.fake.secondary_address()
        assert isinstance(secondary_address, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)

    def test_state_abbr(self):
        state_abbr = self.fake.state_abbr()
        assert isinstance(state_abbr, string_types)


class TestFaIR(unittest.TestCase):
    """ Tests in addresses in the fa_IR locale """

    def setUp(self):
        self.fake = Faker('fa_IR')
        Faker.seed(0)

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in IrProvider.city_prefixes

    def test_secondary_address(self):
        secondary_address = self.fake.secondary_address()
        assert isinstance(secondary_address, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in IrProvider.states


class TestFrFR(unittest.TestCase):
    """ Tests addresses in the fr_FR locale """

    def setUp(self):
        self.fake = Faker('fr_FR')
        Faker.seed(0)

    def test_street_prefix(self):
        street_prefix = self.fake.street_prefix()
        assert isinstance(street_prefix, string_types)
        assert street_prefix in FrFrProvider.street_prefixes

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in FrFrProvider.city_prefixes

    def test_region(self):
        region = self.fake.region()
        assert isinstance(region, string_types)
        assert region in FrFrProvider.regions

    def test_department(self):
        department = self.fake.department()
        assert isinstance(department, tuple)
        assert department in FrFrProvider.departments

    def test_department_name(self):
        department_name = self.fake.department_name()
        assert isinstance(department_name, string_types)

    def test_department_number(self):
        department_number = self.fake.department_number()
        assert isinstance(department_number, string_types)


class TestHeIL(unittest.TestCase):
    """ Tests addresses in the he_IL locale """

    def setUp(self):
        self.fake = Faker('he_IL')
        Faker.seed(0)

    def test_city_name(self):
        city_name = self.fake.city_name()
        assert isinstance(city_name, string_types)

    def test_street_title(self):
        street_title = self.fake.street_title()
        assert isinstance(street_title, string_types)


class TestHiIN(unittest.TestCase):
    """ Tests addresses in the hi_IN locale """

    def setUp(self):
        self.fake = Faker('hi_IN')
        Faker.seed(0)

    def test_city_name(self):
        city_name = self.fake.city_name()
        assert isinstance(city_name, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)


class TestTaIN(unittest.TestCase):
    """ Tests addresses in the ta_IN locale """

    def setUp(self):
        self.fake = Faker('ta_IN')
        Faker.seed(0)

    def test_city_name(self):
        city_name = self.fake.city_name()
        assert isinstance(city_name, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)


class TestFiFI(unittest.TestCase):
    """ Tests in addresses in the fi_FI locale """

    def setUp(self):
        self.fake = Faker('fi_FI')
        Faker.seed(0)

    def test_city(self):
        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in FiProvider.cities

    def test_street_suffix(self):
        suffix = self.fake.street_suffix()
        assert isinstance(suffix, string_types)
        assert suffix in FiProvider.street_suffixes

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in FiProvider.states


class TestHRHR(unittest.TestCase):
    """ Tests addresses in the hr_HR locale """

    def setUp(self):
        self.fake = Faker('hr_HR')
        Faker.seed(0)

    def test_city_name(self):
        city_name = self.fake.city_name()
        assert isinstance(city_name, string_types)

    def test_street_name(self):
        street_name = self.fake.street_name()
        assert isinstance(street_name, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)


class TestHuHU(unittest.TestCase):
    """ Tests addresses in the hu_HU locale """

    def setUp(self):
        self.fake = Faker('hu_HU')
        Faker.seed(0)

    def test_postcode_first_digit(self):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for _ in range(100):
            pcd = self.fake.postcode()
            assert pcd[2] > "0"

    def test_street_address(self):
        """
        Tests street address.

        A street address must consist of a street name, a place type and a number, and end in a period point.
        """
        address = self.fake.street_address()
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
        address = self.fake.street_address_with_county()
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
        address = self.fake.address()
        assert isinstance(address, string_types)
        address_with_county = self.fake.street_address_with_county()
        assert isinstance(address_with_county, string_types)


class TestHyAM(unittest.TestCase):
    """ Tests addresses in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_address(self):
        address = self.fake.address()
        assert isinstance(address, string_types)

    def test_building_number(self):
        building_number = self.fake.building_number()
        assert isinstance(building_number, string_types)
        assert len(building_number) <= 3

    def test_city(self):
        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in HyAmProvider.cities

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)
        assert city_prefix in HyAmProvider.city_prefixes

    def test_city_suffix(self):
        city_suffix = self.fake.city_suffix()
        assert isinstance(city_suffix, string_types)

    def test_country(self):
        country = self.fake.country()
        assert isinstance(country, string_types)
        assert country in HyAmProvider.countries

    def test_alpha_2_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-2')
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self):
        country_code = self.fake.country_code()
        assert len(country_code) == 2
        assert country_code.isalpha()

    def test_alpha_3_country_codes(self):
        country_code = self.fake.country_code(representation='alpha-3')
        assert len(country_code) == 3
        assert country_code.isalpha()

    def test_bad_country_code_representation(self):
        with self.assertRaises(ValueError):
            self.fake.country_code(representation='hello')

    def test_postcode(self):
        postcode = self.fake.postcode()
        assert isinstance(postcode, string_types)
        assert re.match(r"\d{4}", postcode)
        assert int(postcode) >= 200
        assert int(postcode) <= 4299

    def test_postcode_in_state(self):
        for state_abbr in HyAmProvider.states_abbr:
            code = self.fake.postcode_in_state(state_abbr)
            assert re.match(r"\d{4}", code)
            assert int(code) >= HyAmProvider.states_postcode[state_abbr][0]
            assert int(code) <= HyAmProvider.states_postcode[state_abbr][1]

        with self.assertRaises(Exception):
            self.fake.postcode_in_state('XX')

    def test_secondary_address(self):
        secondary_address = self.fake.secondary_address()
        assert isinstance(secondary_address, string_types)

    def test_state(self):
        state = self.fake.state()
        assert isinstance(state, string_types)
        assert state in HyAmProvider.states

    def test_state_abbr(self):
        state_abbr = self.fake.state_abbr()
        assert isinstance(state_abbr, string_types)
        assert state_abbr in HyAmProvider.states_abbr
        assert state_abbr.isupper()

    def test_street(self):
        street = self.fake.street()
        assert isinstance(street, string_types)
        assert street in HyAmProvider.streets

    def test_street_address(self):
        street_address = self.fake.street_address()
        assert isinstance(street_address, string_types)

    def test_street_name(self):
        street_name = self.fake.street_name()
        assert isinstance(street_name, string_types)

    def test_street_prefix(self):
        street_prefix = self.fake.street_prefix()
        assert isinstance(street_prefix, string_types)
        assert street_prefix in HyAmProvider.street_prefixes

    def test_street_suffix(self):
        suffix = self.fake.street_suffix()
        assert isinstance(suffix, string_types)
        assert suffix in HyAmProvider.street_suffixes

    def test_village(self):
        village = self.fake.village()
        assert isinstance(village, string_types)
        assert village in HyAmProvider.villages

    def test_village_prefix(self):
        village_prefix = self.fake.village_prefix()
        assert isinstance(village_prefix, string_types)
        assert village_prefix in HyAmProvider.village_prefixes


class TestJaJP(unittest.TestCase):
    """ Tests addresses in the ja_JP locale """

    def setUp(self):
        self.fake = Faker('ja')
        Faker.seed(0)

    def test_address(self):
        """ Test"""
        country = self.fake.country()
        assert isinstance(country, string_types)
        assert country in JaProvider.countries

        prefecture = self.fake.prefecture()
        assert isinstance(prefecture, string_types)
        assert prefecture in JaProvider.prefectures

        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in JaProvider.cities

        town = self.fake.town()
        assert isinstance(town, string_types)
        assert town in JaProvider.towns

        chome = self.fake.chome()
        assert isinstance(chome, string_types)
        assert re.match(r"\d{1,2}丁目", chome)

        ban = self.fake.ban()
        assert isinstance(ban, string_types)
        assert re.match(r"\d{1,2}番", ban)

        gou = self.fake.gou()
        assert isinstance(gou, string_types)
        assert re.match(r"\d{1,2}号", gou)

        building_name = self.fake.building_name()
        assert isinstance(building_name, string_types)
        assert building_name in JaProvider.building_names

        postcode = self.fake.postcode()
        assert isinstance(postcode, string_types)
        assert re.match(r"\d{3}-\d{4}", postcode)

        zipcode = self.fake.zipcode()
        assert isinstance(zipcode, string_types)
        assert re.match(r"\d{3}-\d{4}", zipcode)

        address = self.fake.address()
        assert isinstance(address, string_types)


class TestKoKR(unittest.TestCase):
    """ Tests addresses in the ko_KR locale """

    def setUp(self):
        self.fake = Faker('ko_KR')
        Faker.seed(0)

    def test_address(self):
        postcode = self.fake.postcode()
        assert isinstance(postcode, string_types)
        assert re.match(r"\d{5}", postcode)

        postal_code = self.fake.postal_code()
        assert isinstance(postal_code, string_types)
        assert re.match(r"\d{5}", postal_code)

        old_postal_code = self.fake.old_postal_code()
        assert isinstance(old_postal_code, string_types)
        assert re.match(r"\d{3}-\d{3}", old_postal_code)


class TestNeNP(unittest.TestCase):
    """ Tests addresses in the ne_NP locale """

    def setUp(self):
        self.fake = Faker('ne_NP')
        Faker.seed(0)

    def test_address(self):
        """ Tests the street address in ne_NP locale """
        country = self.fake.country()
        assert isinstance(country, string_types)
        assert country in NeProvider.countries

        district = self.fake.district()
        assert isinstance(district, string_types)
        assert district in NeProvider.districts

        city = self.fake.city()
        assert isinstance(city, string_types)
        assert city in NeProvider.cities


class TestNoNO(unittest.TestCase):
    """ Tests the street address in no_NO locale """

    def setUp(self):
        self.fake = Faker('no_NO')
        Faker.seed(0)

    def test_postcode(self):
        for _ in range(100):
            assert re.match(r'^[0-9]{4}$', self.fake.postcode())

    def test_city_suffix(self):
        suffix = self.fake.city_suffix()
        assert isinstance(suffix, string_types)

    def test_street_suffix(self):
        suffix = self.fake.street_suffix()
        assert isinstance(suffix, string_types)

    def test_address(self):
        address = self.fake.address()
        assert isinstance(address, string_types)


class TestZhTW(unittest.TestCase):
    """ Tests addresses in the zh_tw locale """

    def setUp(self):
        self.fake = Faker('zh_TW')
        Faker.seed(0)

    def test_address(self):
        country = self.fake.country()
        assert isinstance(country, string_types)

        street = self.fake.street_name()
        assert isinstance(street, string_types)

        city = self.fake.city()
        assert isinstance(city, string_types)

        address = self.fake.address()
        assert isinstance(address, string_types)


class TestZhCN(unittest.TestCase):
    """ Tests addresses in the zh_cn locale """

    def setUp(self):
        self.fake = Faker('zh_CN')
        Faker.seed(0)

    def test_address(self):
        country = self.fake.country()
        assert isinstance(country, string_types)

        street = self.fake.street_name()
        assert isinstance(street, string_types)

        city = self.fake.street_address()
        assert isinstance(city, string_types)

        province = self.fake.province()
        assert isinstance(province, string_types)

        district = self.fake.district()
        assert isinstance(district, string_types)

        address = self.fake.address()
        assert isinstance(address, string_types)

        for _ in range(100):
            assert re.match(r'\d{5}', self.fake.postcode())


class TestPtBr(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pt_BR')
        Faker.seed(0)

    def test_address(self):
        country = self.fake.country()
        assert isinstance(country, string_types)

        street = self.fake.street_name()
        assert isinstance(street, string_types)

        city = self.fake.street_address()
        assert isinstance(city, string_types)

        neighborhood = self.fake.neighborhood()
        assert isinstance(neighborhood, string_types)

        state = self.fake.state()
        assert isinstance(state, string_types)

        state_abbr = self.fake.state_abbr()
        assert isinstance(state_abbr, string_types)

        address = self.fake.address()
        assert isinstance(address, string_types)


class TestPtPT(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pt_PT')
        Faker.seed(0)

    def test_distrito(self):
        distrito = self.fake.distrito()
        assert isinstance(distrito, string_types)
        assert distrito in PtPtProvider.distritos

    def test_concelho(self):
        concelho = self.fake.concelho()
        assert isinstance(concelho, string_types)
        assert concelho in PtPtProvider.concelhos

    def test_freguesia(self):
        freguesia = self.fake.freguesia()
        assert isinstance(freguesia, string_types)
        assert freguesia in PtPtProvider.freguesias


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.building_number_pattern = re.compile(
            r'^(?:[1-9]|[1-9]\d{1,3})(?:[A-J]|\s[A-J]|-[A-J]|\sUnit\s[A-J])?$',
        )
        self.address_pattern = re.compile(
            r'^(?P<street_address>.*), (?P<lgu>.*?), (?P<postcode>\d{4}) (?P<province>.*?)$',
        )
        self.setup_constants()
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker('en_PH')
        Faker.seed(0)

    def setup_constants(self):
        from faker.providers.address.en_PH import Provider
        self.metro_manila_postcodes = Provider.metro_manila_postcodes
        self.luzon_province_postcodes = Provider.luzon_province_postcodes
        self.visayas_province_postcodes = Provider.visayas_province_postcodes
        self.mindanao_province_postcodes = Provider.mindanao_province_postcodes
        self.postcodes = Provider.postcodes
        self.provinces = Provider.provinces
        self.province_lgus = Provider.province_lgus
        self.metro_manila_lgus = Provider.metro_manila_lgus

    def test_PH_metro_manila_postcode(self):
        for i in range(self.num_sample_runs):
            assert int(self.fake.metro_manila_postcode()) in self.metro_manila_postcodes

    def test_PH_luzon_province_postcode(self):
        for i in range(self.num_sample_runs):
            assert int(self.fake.luzon_province_postcode()) in self.luzon_province_postcodes

    def test_PH_visayas_province_postcode(self):
        for i in range(self.num_sample_runs):
            assert int(self.fake.visayas_province_postcode()) in self.visayas_province_postcodes

    def test_PH_mindanao_province_postcode(self):
        for i in range(self.num_sample_runs):
            assert int(self.fake.mindanao_province_postcode()) in self.mindanao_province_postcodes

    def test_PH_postcode(self):
        for i in range(self.num_sample_runs):
            assert int(self.fake.postcode()) in self.postcodes

    def test_PH_building_number(self):
        for i in range(self.num_sample_runs):
            assert self.building_number_pattern.match(self.fake.building_number())

    def test_PH_floor_unit_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.floor_unit_number()
            assert 2 <= int(number[:-2]) <= 99
            assert 1 <= int(number[-2:]) <= 40

    def test_PH_address(self):
        for i in range(self.num_sample_runs):
            address = self.fake.address()
            match = self.address_pattern.match(address)
            street_address = match.group('street_address')
            lgu = match.group('lgu')
            postcode = match.group('postcode')
            province = match.group('province')
            assert match
            assert street_address
            assert lgu in self.province_lgus or lgu in self.metro_manila_lgus
            assert int(postcode) in self.postcodes
            assert province in self.provinces or province == 'Metro Manila'


class TestFilPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('fil_PH')
        Faker.seed(0)


class TestTlPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('tl_PH')
        Faker.seed(0)


class TestRuRU(unittest.TestCase):
    """ Tests addresses in the ru_RU locale """

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)

    def test_city_name(self):
        city = self.fake.city_name()
        assert isinstance(city, string_types)

    def test_country(self):
        country = self.fake.country()
        assert isinstance(country, string_types)

    def test_region(self):
        region = self.fake.region()
        assert isinstance(region, string_types)

    def test_postcode(self):
        postcode = self.fake.postcode()
        assert isinstance(postcode, string_types)

    def test_city_prefix(self):
        city_prefix = self.fake.city_prefix()
        assert isinstance(city_prefix, string_types)

    def test_street_suffix(self):
        street_suffix = self.fake.street_suffix()
        assert isinstance(street_suffix, string_types)

    def test_street_title(self):
        street_title = self.fake.street_title()
        assert isinstance(street_title, string_types)

    def test_street_name(self):
        street_name = self.fake.street_name()
        assert isinstance(street_name, string_types)
