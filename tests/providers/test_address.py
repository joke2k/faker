import re

from unittest import mock

import pytest

from ukpostcodeparser.parser import parse_uk_postcode

from faker.providers.address.cs_CZ import Provider as CsCzAddressProvider
from faker.providers.address.de_AT import Provider as DeAtAddressProvider
from faker.providers.address.de_DE import Provider as DeDeAddressProvider
from faker.providers.address.el_GR import Provider as ElGrAddressProvider
from faker.providers.address.en_AU import Provider as EnAuAddressProvider
from faker.providers.address.en_CA import Provider as EnCaAddressProvider
from faker.providers.address.en_GB import Provider as EnGbAddressProvider
from faker.providers.address.en_PH import Provider as EnPhAddressProvider
from faker.providers.address.en_US import Provider as EnUsAddressProvider
from faker.providers.address.es_ES import Provider as EsEsAddressProvider
from faker.providers.address.es_MX import Provider as EsMxAddressProvider
from faker.providers.address.fa_IR import Provider as FaIrAddressProvider
from faker.providers.address.fi_FI import Provider as FiFiAddressProvider
from faker.providers.address.fr_FR import Provider as FrFrAddressProvider
from faker.providers.address.he_IL import Provider as HeIlAddressProvider
from faker.providers.address.hi_IN import Provider as HiInAddressProvider
from faker.providers.address.hr_HR import Provider as HrHrAddressProvider
from faker.providers.address.hy_AM import Provider as HyAmAddressProvider
from faker.providers.address.ja_JP import Provider as JaJpAddressProvider
from faker.providers.address.ne_NP import Provider as NeNpAddressProvider
from faker.providers.address.no_NO import Provider as NoNoAddressProvider
from faker.providers.address.pt_BR import Provider as PtBrAddressProvider
from faker.providers.address.pt_PT import Provider as PtPtAddressProvider
from faker.providers.address.ru_RU import Provider as RuRuAddressProvider
from faker.providers.address.ta_IN import Provider as TaInAddressProvider
from faker.providers.address.th_TH import Provider as ThThAddressProvider
from faker.providers.address.zh_CN import Provider as ZhCnAddressProvider
from faker.providers.address.zh_TW import Provider as ZhTwAddressProvider


class TestBaseProvider:
    """Test address provider methods"""

    def test_alpha_2_country_codes(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code(representation='alpha-2')
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code()
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_3_country_codes(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code(representation='alpha-3')
            assert len(country_code) == 3
            assert country_code.isalpha()

    def test_bad_country_code_representation(self, faker, num_samples):
        for _ in range(num_samples):
            with pytest.raises(ValueError):
                faker.country_code(representation='hello')


class TestCsCz:
    """Test cs_CZ address provider methods"""

    def test_street_suffix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_short = faker.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in CsCzAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_long = faker.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in CsCzAddressProvider.street_suffixes_long

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in CsCzAddressProvider.cities

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in CsCzAddressProvider.streets

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in CsCzAddressProvider.states

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{3} \d{2}', postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{3} \d{2} (?P<city>.*)', city_with_postcode)
            assert match.group('city') in CsCzAddressProvider.cities


class TestDeAt:
    """Test de_AT address provider methods"""

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in DeAtAddressProvider.cities

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in DeAtAddressProvider.states

    def test_street_suffix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_short = faker.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in DeAtAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_long = faker.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in DeAtAddressProvider.street_suffixes_long

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in DeAtAddressProvider.countries

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{4}', postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{4} (?P<city>.*)', city_with_postcode)
            assert match.groupdict()['city'] in DeAtAddressProvider.cities


class TestDeDe:
    """Test de_DE address provider methods"""

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in DeDeAddressProvider.cities

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in DeDeAddressProvider.states

    def test_street_suffix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_short = faker.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in DeDeAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_long = faker.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in DeDeAddressProvider.street_suffixes_long

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in DeDeAddressProvider.countries

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}', postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{5} (?P<city>.*)', city_with_postcode)
            assert match.groupdict()['city'] in DeDeAddressProvider.cities


class TestElGr:
    """Test el_GR address provider methods"""

    def test_line_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.line_address()
            assert isinstance(address, str)

    def test_street_prefix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix_short = faker.street_prefix_short()
            assert isinstance(street_prefix_short, str)
            assert street_prefix_short in ElGrAddressProvider.street_prefixes_short

    def test_street_prefix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix_long = faker.street_prefix_long()
            assert isinstance(street_prefix_long, str)
            assert street_prefix_long in ElGrAddressProvider.street_prefixes_long

    def test_street(self, faker, num_samples):
        for _ in range(num_samples):
            street = faker.street()
            assert isinstance(street, str)
            assert street in ElGrAddressProvider.localities

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in ElGrAddressProvider.cities

    def test_region(self, faker, num_samples):
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            assert region in ElGrAddressProvider.regions


class TestEnAu:
    """Test en_AU address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{4}', postcode)

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in EnAuAddressProvider.states

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnAuAddressProvider.city_prefixes

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in EnAuAddressProvider.states_abbr
            assert state_abbr.isupper()


class TestEnNz:
    """Test en_NZ address provider methods"""

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            # No states in New Zealand
            assert faker.state() == ''

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)


class TestEnCa:
    """Test en_CA address provider methods"""

    valid_postcode_letter_re = r'[{}]'.format(
            ''.join(EnCaAddressProvider.postal_code_letters))
    valid_postcode_re = r"{0}[0-9]{0} ?[0-9]{0}[0-9]".format(valid_postcode_letter_re)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(self.valid_postcode_re, postcode)

    def test_postcode_in_province(self, faker, num_samples):
        for _ in range(num_samples):
            for province_abbr in EnCaAddressProvider.provinces_abbr:
                code = faker.postcode_in_province(province_abbr)
                assert code[0] in EnCaAddressProvider.provinces_postcode_prefixes[province_abbr]
                with pytest.raises(Exception):
                    faker.postcode_in_province('XX')

    def test_postalcode(self, faker, num_samples):
        for _ in range(num_samples):
            postalcode = faker.postalcode()
            assert isinstance(postalcode, str)
            assert re.fullmatch(self.valid_postcode_re, postalcode)

    def test_postal_code_letter(self, faker, num_samples):
        for _ in range(num_samples):
            postal_code_letter = faker.postal_code_letter()
            assert isinstance(postal_code_letter, str)
            assert re.fullmatch(self.valid_postcode_letter_re, postal_code_letter)

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in EnCaAddressProvider.provinces

    def test_province_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            province_abbr = faker.province_abbr()
            assert isinstance(province_abbr, str)
            assert province_abbr in EnCaAddressProvider.provinces_abbr

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnCaAddressProvider.city_prefixes

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'(?:Apt\.|Suite) \d{3}', secondary_address)


class TestEnGb:
    """Test en_GB address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert isinstance(parse_uk_postcode(faker.postcode()), tuple)

    def test_county(self, faker, num_samples):
        for _ in range(num_samples):
            county = faker.county()
            assert isinstance(county, str)
            assert county in EnGbAddressProvider.counties


class TestEnUS:
    """Test en_US address provider methods"""

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnUsAddressProvider.city_prefixes

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in EnUsAddressProvider.states

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            states_and_territories = EnUsAddressProvider.states_and_territories_abbr
            assert state_abbr in states_and_territories

    def test_state_abbr_no_territories(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr(include_territories=False)
            assert isinstance(state_abbr, str)
            assert state_abbr in EnUsAddressProvider.states_abbr

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.postcode()
            assert isinstance(code, str) and len(code) == 5
            assert 501 <= int(code) <= 99950

    def test_postcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = faker.postcode_in_state(state_abbr)
                assert re.fullmatch(r'\d{5}', code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.postcode_in_state('XX')

    def test_zipcode(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode = faker.zipcode()
            assert isinstance(zipcode, str) and len(zipcode) == 5
            assert 501 <= int(zipcode) <= 99950

    def test_zipcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = faker.zipcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.zipcode_in_state('XX')

    def test_zipcode_plus4(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode_plus4 = faker.zipcode_plus4()
            assert isinstance(zipcode_plus4, str)
            zipcode, plus4 = zipcode_plus4.split('-')
            assert 501 <= int(zipcode) <= 99950
            assert 1 <= int(plus4) <= 9999

    def test_military_ship(self, faker, num_samples):
        for _ in range(num_samples):
            military_ship = faker.military_ship()
            assert isinstance(military_ship, str)
            assert military_ship in EnUsAddressProvider.military_ship_prefix

    def test_military_state(self, faker, num_samples):
        for _ in range(num_samples):
            military_state = faker.military_state()
            assert isinstance(military_state, str)
            assert military_state in EnUsAddressProvider.military_state_abbr

    def test_military_apo(self, faker, num_samples):
        for _ in range(num_samples):
            military_apo = faker.military_apo()
            assert isinstance(military_apo, str)
            assert re.fullmatch(r'PSC \d{4}, Box \d{4}', military_apo)

    def test_military_dpo(self, faker, num_samples):
        for _ in range(num_samples):
            military_dpo = faker.military_dpo()
            assert isinstance(military_dpo, str)
            assert re.fullmatch(r'Unit \d{4} Box \d{4}', military_dpo)

    def test_postalcode(self, faker, num_samples):
        for _ in range(num_samples):
            postalcode = faker.postalcode()
            assert isinstance(postalcode, str) and len(postalcode) == 5
            assert 501 <= int(postalcode) <= 99950

    def test_postalcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = faker.postalcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.postalcode_in_state('XX')


class TestEsEs:
    """Test es_ES address provider methods"""

    def test_state_name(self, faker, num_samples):
        for _ in range(num_samples):
            state_name = faker.state_name()
            assert isinstance(state_name, str)
            assert state_name in EsEsAddressProvider.states

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EsEsAddressProvider.street_prefixes

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'Apt\. \d{2}|Piso \d|Puerta \d', secondary_address)

    def test_regions(self, faker, num_samples):
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            assert region in EsEsAddressProvider.regions

    def test_autonomous_community(self, faker, num_samples):
        for _ in range(num_samples):
            # Spanish regions, also known as "autonomous communities"
            autonomous_community = faker.autonomous_community()
            assert isinstance(autonomous_community, str)
            assert autonomous_community in EsEsAddressProvider.regions


class TestEsMx:
    """Test es_MX address provider methods"""

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EsMxAddressProvider.city_prefixes

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in EsMxAddressProvider.city_suffixes

    def test_city_adjective(self, faker, num_samples):
        for _ in range(num_samples):
            city_adjective = faker.city_adjective()
            assert isinstance(city_adjective, str)
            assert city_adjective in EsMxAddressProvider.city_adjectives

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EsMxAddressProvider.street_prefixes

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(
                r'\d{3} \d{3}|\d{3} Interior \d{3}|\d{3} Edif\. \d{3} , Depto\. \d{3}',
                secondary_address,
            )

    def test_state(self, faker, num_samples):
        states = [state_name for state_abbr, state_name in EsMxAddressProvider.states]
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in states

    def test_state_abbr(self, faker, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in EsMxAddressProvider.states]
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in state_abbrs


class TestFaIr:
    """Test fa_IR address provider methods"""

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in FaIrAddressProvider.city_prefixes

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'(?:سوئیت|واحد) \d{3}', secondary_address)

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in FaIrAddressProvider.states


class TestFrFr:
    """Test fr_FR address provider methods"""

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in FrFrAddressProvider.street_prefixes

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in FrFrAddressProvider.city_prefixes

    def test_region(self, faker, num_samples):
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            assert region in FrFrAddressProvider.regions

    def test_department(self, faker, num_samples):
        for _ in range(num_samples):
            department = faker.department()
            assert isinstance(department, tuple)
            assert department in FrFrAddressProvider.departments

    def test_department_name(self, faker, num_samples):
        department_names = [dept_name for dept_num, dept_name in FrFrAddressProvider.departments]
        for _ in range(num_samples):
            department_name = faker.department_name()
            assert isinstance(department_name, str)
            assert department_name in department_names

    def test_department_number(self, faker, num_samples):
        department_numbers = [dept_num for dept_num, dept_name in FrFrAddressProvider.departments]
        for _ in range(num_samples):
            department_number = faker.department_number()
            assert isinstance(department_number, str)
            assert department_number in department_numbers


class TestHeIl:
    """Test he_IL address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in HeIlAddressProvider.city_names

    def test_street_title(self, faker, num_samples):
        for _ in range(num_samples):
            street_title = faker.street_title()
            assert isinstance(street_title, str)
            assert street_title in HeIlAddressProvider.street_titles


class TestHiIn:
    """Test hi_IN address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in HiInAddressProvider.cities

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in HiInAddressProvider.states


class TestTaIn:
    """Test ta_IN address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in TaInAddressProvider.cities

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in TaInAddressProvider.states


class TestFiFi:
    """Test fi_FI address provider methods"""

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in FiFiAddressProvider.cities

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.street_suffix()
            assert isinstance(suffix, str)
            assert suffix in FiFiAddressProvider.street_suffixes

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in FiFiAddressProvider.states


class TestHrHr:
    """Test hr_HR address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in HrHrAddressProvider.cities

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in HrHrAddressProvider.streets

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in HrHrAddressProvider.states


class TestHuHu:
    """Test hu_HU address provider methods"""

    def test_postcode(self, faker, num_samples):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for _ in range(num_samples):
            pcd = faker.postcode()
            assert re.fullmatch(r'H-[1-9]\d{3}', pcd)

    def test_street_address(self, faker, num_samples):
        """
        Tests street address.

        A street address must consist of a street name, a place type and a number, and end in a period point.
        """
        for _ in range(num_samples):
            address = faker.street_address()
            assert address[-1] == '.'
            # Check for correct capitalisation of place type
            assert address.split(" ")[-2][0].islower()
            # Check for street number format
            assert re.fullmatch(r"\d{1,4}\.", address.split(" ")[-1])

    def test_street_address_with_county(self, faker, num_samples):
        """Tests street address with country. A street address must be:
        - in three rows,
        - starting with a valid street address,
        - contain a valid post code,
        - contain the place name validly capitalized.
        """
        for _ in range(num_samples):
            address = faker.street_address_with_county()
            # Number of rows
            assert len(address.split("\n")) == 3
            first, second, last = address.split("\n")

            # Test street address
            assert first[0].isupper()
            assert first.split(" ")[-2][0].islower()
            assert re.fullmatch(r"\d{1,4}\.", first.split(" ")[-1])

            # Test county line
            assert second.split(" ")[-1][0].islower()
            assert second.split(" ")[0][0].isupper()

            # Test postcode
            assert re.fullmatch(r"H-[1-9]\d{3}", last.split(" ")[0])

            # Test place name capitalization
            assert last.split(" ")[-1][0].isupper()

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)
            address_with_county = faker.street_address_with_county()
            assert isinstance(address_with_county, str)


class TestHyAm:
    """Test hy_AM address provider methods"""

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)
            assert 0 <= int(building_number) <= 999

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in HyAmAddressProvider.cities

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in HyAmAddressProvider.city_prefixes

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in HyAmAddressProvider.countries

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert 200 <= int(postcode) <= 4299

    def test_postcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in HyAmAddressProvider.states_abbr:
                code = faker.postcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{4}", code)
                assert int(code) >= HyAmAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= HyAmAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.postcode_in_state('XX')

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'բն\. \d{1,2}', secondary_address)

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in HyAmAddressProvider.states

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in HyAmAddressProvider.states_abbr
            assert state_abbr.isupper()

    def test_street(self, faker, num_samples):
        for _ in range(num_samples):
            street = faker.street()
            assert isinstance(street, str)
            assert street in HyAmAddressProvider.streets

    def test_street_address(self, faker, num_samples):
        for _ in range(num_samples):
            street_address = faker.street_address()
            assert isinstance(street_address, str)

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in HyAmAddressProvider.street_prefixes

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.street_suffix()
            assert isinstance(suffix, str)
            assert suffix in HyAmAddressProvider.street_suffixes

    def test_village(self, faker, num_samples):
        for _ in range(num_samples):
            village = faker.village()
            assert isinstance(village, str)
            assert village in HyAmAddressProvider.villages

    def test_village_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            village_prefix = faker.village_prefix()
            assert isinstance(village_prefix, str)
            assert village_prefix in HyAmAddressProvider.village_prefixes


class TestJaJp:
    """Test ja_JP address provider methods"""

    def test_chome(self, faker, num_samples):
        for _ in range(num_samples):
            chome = faker.chome()
            assert isinstance(chome, str)
            match = re.fullmatch(r"(?P<chome_number>\d{1,2})丁目", chome)
            assert match
            assert 1 <= int(match.group('chome_number')) <= 42

    def test_ban(self, faker, num_samples):
        for _ in range(num_samples):
            ban = faker.ban()
            assert isinstance(ban, str)
            match = re.fullmatch(r"(?P<ban_number>\d{1,2})番", ban)
            assert match
            assert 1 <= int(match.group('ban_number')) <= 27

    def test_gou(self, faker, num_samples):
        for _ in range(num_samples):
            gou = faker.gou()
            assert isinstance(gou, str)
            match = re.fullmatch(r"(?P<gou_number>\d{1,2})号", gou)
            assert match
            assert 1 <= int(match.group('gou_number')) <= 20

    def test_town(self, faker, num_samples):
        for _ in range(num_samples):
            town = faker.town()
            assert isinstance(town, str)
            assert town in JaJpAddressProvider.towns

    def test_prefecture(self, faker, num_samples):
        for _ in range(num_samples):
            prefecture = faker.prefecture()
            assert isinstance(prefecture, str)
            assert prefecture in JaJpAddressProvider.prefectures

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in JaJpAddressProvider.cities

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in JaJpAddressProvider.countries

    def test_building_name(self, faker, num_samples):
        for _ in range(num_samples):
            building_name = faker.building_name()
            assert isinstance(building_name, str)
            assert building_name in JaJpAddressProvider.building_names

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{3}-\d{4}', postcode)

    def test_zipcode(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode = faker.zipcode()
            assert isinstance(zipcode, str)
            assert re.fullmatch(r'\d{3}-\d{4}', zipcode)


class TestKoKr:
    """Test ko_KR address provider methods"""

    def test_old_postal_code(self, faker, num_samples):
        for _ in range(num_samples):
            old_postal_code = faker.old_postal_code()
            assert isinstance(old_postal_code, str)
            assert re.fullmatch(r'\d{3}-\d{3}', old_postal_code)

    def test_postal_code(self, faker, num_samples):
        for _ in range(num_samples):
            postal_code = faker.postal_code()
            assert isinstance(postal_code, str)
            assert re.fullmatch(r'\d{5}', postal_code)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}', postcode)


class TestNeNp:
    """Test ne_NP address provider methods"""

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in NeNpAddressProvider.provinces

    def test_district(self, faker, num_samples):
        for _ in range(num_samples):
            district = faker.district()
            assert isinstance(district, str)
            assert district in NeNpAddressProvider.districts

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in NeNpAddressProvider.cities

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in NeNpAddressProvider.countries


class TestNoNo:
    """Test no_NO address provider methods"""

    def test_postcode(self, faker):
        for _ in range(100):
            assert re.fullmatch(r'^[0-9]{4}$', faker.postcode())

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in NoNoAddressProvider.city_suffixes

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix = faker.street_suffix()
            assert isinstance(street_suffix, str)
            assert street_suffix in NoNoAddressProvider.street_suffixes

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)


class TestZhTw:
    """Test zh_TW address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{2}(?:\d{2})?', postcode)

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in ZhTwAddressProvider.cities

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in ZhTwAddressProvider.city_suffixes

    def test_city(self, faker, num_samples):
        city_pattern = re.compile(r'(?P<city_name>.*?)[市縣]?')
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            match = city_pattern.fullmatch(city)
            assert match
            assert match.group('city_name') in ZhTwAddressProvider.cities

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in ZhTwAddressProvider.countries

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in ZhTwAddressProvider.street_names

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)


class TestZhCn:
    """Test zh_CN address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{5}', postcode)

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in ZhCnAddressProvider.cities

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in ZhCnAddressProvider.city_suffixes

    def test_city(self, faker, num_samples):
        city_pattern = re.compile(r'.*?[市县]')
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city_pattern.fullmatch(city)

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in ZhCnAddressProvider.provinces

    def test_district(self, faker, num_samples):
        for _ in range(num_samples):
            district = faker.district()
            assert isinstance(district, str)
            assert district in ZhCnAddressProvider.districts

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in ZhCnAddressProvider.countries

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)


class TestPtBr:
    """Test pt_BR address provider methods"""

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in PtBrAddressProvider.countries

    def test_bairro(self, faker, num_samples):
        for _ in range(num_samples):
            bairro = faker.bairro()
            assert isinstance(bairro, str)
            assert bairro in PtBrAddressProvider.bairros

    def test_neighborhood(self, faker, num_samples):
        for _ in range(num_samples):
            neighborhood = faker.neighborhood()
            assert isinstance(neighborhood, str)
            assert neighborhood in PtBrAddressProvider.bairros

    def test_estado(self, faker, num_samples):
        for _ in range(num_samples):
            estado = faker.estado()
            assert isinstance(estado, tuple)
            assert estado in PtBrAddressProvider.estados

    def test_estado_nome(self, faker, num_samples):
        state_names = [state_name for state_abbr, state_name in PtBrAddressProvider.estados]
        for _ in range(num_samples):
            estado_nome = faker.estado_nome()
            assert isinstance(estado_nome, str)
            assert estado_nome in state_names

    def test_estado_sigla(self, faker, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in PtBrAddressProvider.estados]
        for _ in range(num_samples):
            estado_sigla = faker.estado_sigla()
            assert isinstance(estado_sigla, str)
            assert estado_sigla in state_abbrs

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            street = faker.street_name()
            assert isinstance(street, str)
            city = faker.street_address()
            assert isinstance(city, str)
            address = faker.address()
            assert isinstance(address, str)

    def test_raw_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode(formatted=False)
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{8}', postcode)

    def test_formatted_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}-?\d{3}', postcode)


class TestPtPt:
    """Test pt_PT address provider methods"""

    def test_distrito(self, faker, num_samples):
        for _ in range(num_samples):
            distrito = faker.distrito()
            assert isinstance(distrito, str)
            assert distrito in PtPtAddressProvider.distritos

    def test_concelho(self, faker, num_samples):
        for _ in range(num_samples):
            concelho = faker.concelho()
            assert isinstance(concelho, str)
            assert concelho in PtPtAddressProvider.concelhos

    def test_freguesia(self, faker, num_samples):
        for _ in range(num_samples):
            freguesia = faker.freguesia()
            assert isinstance(freguesia, str)
            assert freguesia in PtPtAddressProvider.freguesias

    def test_place_name(self, faker, num_samples):
        for _ in range(num_samples):
            place_name = faker.place_name()
            assert isinstance(place_name, str)
            assert place_name in PtPtAddressProvider.places


class TestEnPh:
    """Test en_PH address provider methods"""

    @classmethod
    def setup_class(cls):
        cls.building_number_pattern = re.compile(
            r'(?:[1-9]|[1-9]\d{1,3})(?:[A-J]|\s[A-J]|-[A-J]|\sUnit\s[A-J])?',
        )
        cls.address_pattern = re.compile(
            r'(?P<street_address>.*), (?P<lgu>.*?), (?P<postcode>\d{4}) (?P<province>.*?)',
        )
        cls.metro_manila_postcodes = EnPhAddressProvider.metro_manila_postcodes
        cls.luzon_province_postcodes = EnPhAddressProvider.luzon_province_postcodes
        cls.visayas_province_postcodes = EnPhAddressProvider.visayas_province_postcodes
        cls.mindanao_province_postcodes = EnPhAddressProvider.mindanao_province_postcodes
        cls.postcodes = EnPhAddressProvider.postcodes
        cls.provinces = EnPhAddressProvider.provinces
        cls.province_lgus = EnPhAddressProvider.province_lgus
        cls.metro_manila_lgus = EnPhAddressProvider.metro_manila_lgus

    def test_metro_manila_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert int(faker.metro_manila_postcode()) in self.metro_manila_postcodes

    def test_luzon_province_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert int(faker.luzon_province_postcode()) in self.luzon_province_postcodes

    def test_visayas_province_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert int(faker.visayas_province_postcode()) in self.visayas_province_postcodes

    def test_mindanao_province_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert int(faker.mindanao_province_postcode()) in self.mindanao_province_postcodes

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            assert int(faker.postcode()) in self.postcodes

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            assert self.building_number_pattern.fullmatch(faker.building_number())

    def test_floor_unit_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.floor_unit_number()
            assert 2 <= int(number[:-2]) <= 99
            assert 1 <= int(number[-2:]) <= 40

    def test_ordinal_floor_number(self, faker, num_samples):
        for _ in range(num_samples):
            floor_number = faker.ordinal_floor_number()
            assert floor_number[-2:] in ['th', 'st', 'nd', 'rd']

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            match = self.address_pattern.fullmatch(address)
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
    """Test fil_PH address provider methods"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH address provider methods"""
    pass


class TestRuRu:
    """Test ru_RU address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in RuRuAddressProvider.city_names

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in RuRuAddressProvider.countries

    def test_region(self, faker, num_samples):
        region_pattern = re.compile(
            r'(?:респ\. (?P<region_republic>.*))|'
            r'(?:(?P<region_krai>.*?) край)|'
            r'(?:(?P<region_oblast>.*?) обл.)|'
            r'(?:(?P<region_ao>.*?) АО)',
        )
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            match = region_pattern.fullmatch(region)
            assert match
            groupdict = match.groupdict()
            assert any([
                groupdict.get('region_republic') in RuRuAddressProvider.region_republics,
                groupdict.get('region_krai') in RuRuAddressProvider.region_krai,
                groupdict.get('region_oblast') in RuRuAddressProvider.region_oblast,
                groupdict.get('region_ao') in RuRuAddressProvider.region_ao,
            ])

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{6}', postcode)

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in RuRuAddressProvider.city_prefixes

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix = faker.street_suffix()
            assert isinstance(street_suffix, str)
            assert street_suffix in RuRuAddressProvider.street_suffixes

    def test_street_title(self, faker, num_samples):
        for _ in range(num_samples):
            street_title = faker.street_title()
            assert isinstance(street_title, str)

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    @pytest.mark.parametrize("street_title,street_suffix,expected", [
        ("Фрунзе", "ул.", "ул. Фрунзе"),
        ("Ставропольская", "ул.", "ул. Ставропольская"),
        ("Фрунзе", "пр.", "пр. Фрунзе"),
        ("Осенняя", "пр.", "пр. Осенний"),
        ("Гвардейская", "пр.", "пр. Гвардейский"),
        ("Рыбацкая", "пр.", "пр. Рыбацкий"),
        ("Безымянная", "пр.", "пр. Безымянный"),
        ("Проезжая", "ш.", "ш. Проезжее"),
        ("Магистральная", "ш.", "ш. Магистральное"),
    ], ids=[
        "feminine_suffix_and_noflex_title",
        "feminine_suffix_and_flex_title",
        "non_feminine_suffix_and_noflex_title",
        "masc_suffix_and_irregular_masc_title",
        "masc_suffix_and_ck_street_stem",
        "masc_suffix_and_uk_street_stem",
        "masc_suffix_and_other_stem",
        "neu_suffx_and_iregular_neu_street_title",
        "neu_suffix_and_regular_street_title",
    ])
    def test_street_name_lexical(self, faker, street_title, street_suffix, expected):
        """Test that random street names are formed correctly, given
        the case of suffixes and streets that have been randomly selected.
        """
        title_patch = mock.patch(
            "faker.providers.address.ru_RU.Provider.street_title",
            autospec=True,
            return_value=street_title,
        )
        suffix_patch = mock.patch(
            "faker.providers.address.ru_RU.Provider.street_suffix",
            autospec=True,
            return_value=street_suffix,
        )

        with title_patch, suffix_patch:
            result = faker.street_name()
            assert result == expected


class TestThTh:
    """Test th_TH address provider methods"""

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in ThThAddressProvider.countries

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in ThThAddressProvider.provinces

    def test_amphoe(self, faker, num_samples):
        for _ in range(num_samples):
            amphoe = faker.amphoe()
            assert isinstance(amphoe, str)
            assert amphoe in ThThAddressProvider.amphoes

    def test_tambon(self, faker, num_samples):
        for _ in range(num_samples):
            tambon = faker.tambon()
            assert isinstance(tambon, str)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{4}', postcode)
