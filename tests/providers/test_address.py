import re

from typing import Pattern
from unittest import mock

import pytest

from faker import Faker, providers
from faker.providers.address.az_AZ import Provider as AzAzAddressProvider
from faker.providers.address.cs_CZ import Provider as CsCzAddressProvider
from faker.providers.address.da_DK import Provider as DaDkAddressProvider
from faker.providers.address.de_AT import Provider as DeAtAddressProvider
from faker.providers.address.de_CH import Provider as DeChAddressProvider
from faker.providers.address.de_DE import Provider as DeDeAddressProvider
from faker.providers.address.el_GR import Provider as ElGrAddressProvider
from faker.providers.address.en_AU import Provider as EnAuAddressProvider
from faker.providers.address.en_BD import Provider as EnBdAddressProvider
from faker.providers.address.en_CA import Provider as EnCaAddressProvider
from faker.providers.address.en_GB import Provider as EnGbAddressProvider
from faker.providers.address.en_IE import Provider as EnIeAddressProvider
from faker.providers.address.en_IN import Provider as EnInAddressProvider
from faker.providers.address.en_MS import Provider as EnMsAddressProvider
from faker.providers.address.en_NZ import Provider as EnNzAddressProvider
from faker.providers.address.en_PH import Provider as EnPhAddressProvider
from faker.providers.address.en_US import Provider as EnUsAddressProvider
from faker.providers.address.es_CO import Provider as EsCoAddressProvider
from faker.providers.address.es_ES import Provider as EsEsAddressProvider
from faker.providers.address.es_MX import Provider as EsMxAddressProvider
from faker.providers.address.fa_IR import Provider as FaIrAddressProvider
from faker.providers.address.fi_FI import Provider as FiFiAddressProvider
from faker.providers.address.fr_CA import Provider as FrCaAddressProvider
from faker.providers.address.fr_CH import Provider as FrChAddressProvider
from faker.providers.address.fr_FR import Provider as FrFrAddressProvider
from faker.providers.address.he_IL import Provider as HeIlAddressProvider
from faker.providers.address.hi_IN import Provider as HiInAddressProvider
from faker.providers.address.hr_HR import Provider as HrHrAddressProvider
from faker.providers.address.hu_HU import Provider as HuHuAddressProvider
from faker.providers.address.hy_AM import Provider as HyAmAddressProvider
from faker.providers.address.id_ID import Provider as IdIdAddressProvider
from faker.providers.address.it_IT import Provider as ItItAddressProvider
from faker.providers.address.ja_JP import Provider as JaJpAddressProvider
from faker.providers.address.ka_GE import Provider as KaGeAddressProvider
from faker.providers.address.ko_KR import Provider as KoKrAddressProvider
from faker.providers.address.ne_NP import Provider as NeNpAddressProvider
from faker.providers.address.no_NO import Provider as NoNoAddressProvider
from faker.providers.address.pt_BR import Provider as PtBrAddressProvider
from faker.providers.address.pt_PT import Provider as PtPtAddressProvider
from faker.providers.address.ro_RO import Provider as RoRoAddressProvider
from faker.providers.address.ru_RU import Provider as RuRuAddressProvider
from faker.providers.address.sk_SK import Provider as SkSkAddressProvider
from faker.providers.address.sl_SI import Provider as SlSiAddressProvider
from faker.providers.address.sv_SE import Provider as SvSeAddressProvider
from faker.providers.address.ta_IN import Provider as TaInAddressProvider
from faker.providers.address.th_TH import Provider as ThThAddressProvider
from faker.providers.address.uk_UA import Provider as UkUaAddressProvider
from faker.providers.address.vi_VN import Provider as ViVNAddressProvider
from faker.providers.address.zh_CN import Provider as ZhCnAddressProvider
from faker.providers.address.zh_TW import Provider as ZhTwAddressProvider
from faker.providers.address.zu_ZA import Provider as ZuZaAddressProvider


class TestBaseProvider:
    """Test address provider methods"""

    def test_alpha_2_country_codes(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code(representation="alpha-2")
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code()
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_3_country_codes(self, faker, num_samples):
        for _ in range(num_samples):
            country_code = faker.country_code(representation="alpha-3")
            assert len(country_code) == 3
            assert country_code.isalpha()

    def test_bad_country_code_representation(self, faker, num_samples):
        for _ in range(num_samples):
            with pytest.raises(ValueError):
                faker.country_code(representation="hello")

    def _collect_fakers_for_locales(self):
        cached_locales = []
        language_locale_codes = providers.BaseProvider.language_locale_codes
        for code, countries in language_locale_codes.items():
            for country in countries:
                name = f"{code}_{country}"
                try:
                    faker = Faker(name)
                    cached_locales.append(faker)
                except AttributeError as e:
                    print(f"Cannot generate faker for {name}: {e}. Skipped")

        return cached_locales

    def _fakers_for_locales(self):
        if not hasattr(self.__class__, "cached_locales"):
            self.__class__.cached_locales = self._collect_fakers_for_locales()
        return self.cached_locales

    def test_administrative_unit_all_locales(self):
        for faker in self._fakers_for_locales():
            if faker.current_country_code() not in ["IL", "GE", "TW", "UA", "NZ"]:
                try:
                    assert isinstance(faker.administrative_unit(), str)
                except Exception as e:
                    raise e.__class__(faker.current_country_code(), *e.args)

    def test_country_code_all_locales(self):
        for faker in self._fakers_for_locales():
            assert isinstance(faker.current_country(), str)

    def test_current_country_errors(self):
        dt = providers.date_time
        countries_duplicated = [*dt.Provider.countries, *dt.Provider.countries]
        with mock.patch.object(dt.Provider, "countries", countries_duplicated), pytest.raises(ValueError) as e:
            Faker("en_US").current_country()
        assert "Ambiguous" in str(e)
        country_code = "faker.providers.address.Provider.current_country_code"
        with pytest.raises(ValueError), mock.patch(country_code, lambda self: "en_ZZ"):
            Faker("en_US").current_country()


class TestAzAz:
    """Test az_AZ address provider methods"""

    def test_street_suffix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_long = faker.street_suffix()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in AzAzAddressProvider.street_suffixes

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in AzAzAddressProvider.cities

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street()
            assert isinstance(street_name, str)
            assert street_name in AzAzAddressProvider.streets

    def test_settlement_name(self, faker, num_samples):
        for _ in range(num_samples):
            settlement_name = faker.settlement()
            assert isinstance(settlement_name, str)
            assert settlement_name in AzAzAddressProvider.settlements

    def test_village_name(self, faker, num_samples):
        for _ in range(num_samples):
            village_name = faker.village()
            assert isinstance(village_name, str)
            assert village_name in AzAzAddressProvider.villages

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"AZ\d{4}", postcode)
            assert int(postcode[2:]) in range(900, 6600)


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
            assert re.fullmatch(r"\d{3} \d{2}", postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r"\d{3} \d{2} (?P<city>.*)", city_with_postcode)
            assert match.group("city") in CsCzAddressProvider.cities


class TestDaDk:
    """Test dk_DK address provider methods"""

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix = faker.street_suffix()
            assert isinstance(street_suffix, str)
            assert street_suffix in DaDkAddressProvider.street_suffixes

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_dk_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            dk_street_name = faker.dk_street_name()
            assert isinstance(dk_street_name, str)

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in DaDkAddressProvider.cities

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in DaDkAddressProvider.states

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)


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
            assert re.fullmatch(r"\d{4}", postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r"\d{4} (?P<city>.*)", city_with_postcode)
            assert match.groupdict()["city"] in DeAtAddressProvider.cities


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
            assert re.fullmatch(r"\d{5}", postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r"\d{5} (?P<city>.*)", city_with_postcode)
            assert match.groupdict()["city"] in DeDeAddressProvider.cities


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
            assert re.fullmatch(r"\d{4}", postcode)

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


class TestEnBd:
    """Test en_BD address provider methods"""

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in EnBdAddressProvider.cities

    def test_area_name(self, faker, num_samples):
        for _ in range(num_samples):
            area_name = faker.area_name()
            assert isinstance(area_name, str)
            assert area_name in EnBdAddressProvider.area_names

    def test_building_name(self, faker, num_samples):
        for _ in range(num_samples):
            building_name = faker.building_name()
            assert isinstance(building_name, str)
            assert building_name in EnBdAddressProvider.building_names

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnBdAddressProvider.city_prefixes

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in EnBdAddressProvider.cities

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)

    def test_town(self, faker, num_samples):
        for _ in range(num_samples):
            town = faker.town()
            assert isinstance(town, str)


class TestEnCa:
    """Test en_CA address provider methods"""

    valid_postcode_letter_re = r"[{}]".format("".join(EnCaAddressProvider.postal_code_letters))
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
                    faker.postcode_in_province("XX")

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
            assert re.fullmatch(r"(?:Apt\.|Suite) \d{3}", secondary_address)


class TestEnGb:
    """Test en_GB address provider methods"""

    def test_postcode(self, faker, num_samples):
        ukpcp = pytest.importorskip("ukpostcodeparser.parser")
        for _ in range(num_samples):
            assert isinstance(ukpcp.parse_uk_postcode(faker.postcode()), tuple)

    def test_county(self, faker, num_samples):
        for _ in range(num_samples):
            county = faker.county()
            assert isinstance(county, str)
            assert county in EnGbAddressProvider.counties


class TestEnIe:
    """Test en_IE address provider methods"""

    def test_postcode(self, faker, num_samples):
        """https://stackoverflow.com/questions/33391412/validation-for-irish-eircode"""
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"(?:^[AC-FHKNPRTV-Y][0-9]{2}|D6W)[ -]?[0-9AC-FHKNPRTV-Y]{4}$", postcode)

    def test_county(self, faker, num_samples):
        for _ in range(num_samples):
            county = faker.county()
            assert isinstance(county, str)
            assert county in EnIeAddressProvider.counties


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
            states_and_territories = EnUsAddressProvider.known_usps_abbr
            assert state_abbr in states_and_territories

    def test_state_abbr_states_only(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr(include_territories=False, include_freely_associated_states=False)
            assert isinstance(state_abbr, str)
            assert state_abbr in EnUsAddressProvider.states_abbr

    def test_state_abbr_no_territories(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr(include_territories=False)
            assert isinstance(state_abbr, str)
            assert (
                state_abbr in EnUsAddressProvider.states_abbr
                or state_abbr in EnUsAddressProvider.freely_associated_states_abbr
            )

    def test_state_abbr_no_freely_associated_states(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr(include_freely_associated_states=False)
            assert isinstance(state_abbr, str)
            assert state_abbr in EnUsAddressProvider.states_abbr or state_abbr in EnUsAddressProvider.territories_abbr

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.postcode()
            assert isinstance(code, str) and len(code) == 5
            assert 501 <= int(code) <= 99950

    def test_postcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.known_usps_abbr:
                code = faker.postcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.postcode_in_state("XX")

    def test_zipcode(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode = faker.zipcode()
            assert isinstance(zipcode, str) and len(zipcode) == 5
            assert 501 <= int(zipcode) <= 99950

    def test_zipcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.known_usps_abbr:
                code = faker.zipcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            faker.zipcode_in_state("XX")

    def test_zipcode_plus4(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode_plus4 = faker.zipcode_plus4()
            assert isinstance(zipcode_plus4, str)
            zipcode, plus4 = zipcode_plus4.split("-")
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
            assert re.fullmatch(r"PSC \d{4}, Box \d{4}", military_apo)

    def test_military_dpo(self, faker, num_samples):
        for _ in range(num_samples):
            military_dpo = faker.military_dpo()
            assert isinstance(military_dpo, str)
            assert re.fullmatch(r"Unit \d{4} Box \d{4}", military_dpo)

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
            faker.postalcode_in_state("XX")

    def test_state_abbr_determinism(self, faker):
        faker.seed_instance(0)
        first = faker.state_abbr()
        faker.seed_instance(0)
        assert faker.state_abbr() == first


class TestEsCo:
    """Test es_CO address provider methods"""

    def test_department_code(self, faker, num_samples):
        for _ in range(num_samples):
            department_code = faker.department_code()
            assert isinstance(department_code, str)
            assert department_code in EsCoAddressProvider.departments

    def test_department(self, faker, num_samples):
        for _ in range(num_samples):
            department = faker.department()
            assert isinstance(department, str)
            assert department in EsCoAddressProvider.departments.values()

    def test_municipality_code(self, faker, num_samples):
        municipality_codes = {municipality_code for municipality_code, _ in EsCoAddressProvider.municipalities}
        for _ in range(num_samples):
            municipality_code = faker.municipality_code()
            assert isinstance(municipality_code, str)
            assert municipality_code in municipality_codes

    def test_municipality(self, faker, num_samples):
        municipalities = {municipality for _, municipality in EsCoAddressProvider.municipalities}
        for _ in range(num_samples):
            municipality = faker.municipality()
            city = faker.city()
            assert isinstance(municipality, str)
            assert isinstance(city, str)
            assert municipality in municipalities
            assert city in municipalities

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EsCoAddressProvider.street_prefixes

    def test_street_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix = faker.street_suffix()
            assert isinstance(street_suffix, str)

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)
            assert re.fullmatch(r"\d{1,2}[A-Z]?-\d{1,2}", building_number)

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)

    def test_street_address(self, faker, num_samples):
        for _ in range(num_samples):
            street_address = faker.street_address()
            assert isinstance(street_address, str)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{6}", postcode)

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)


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
            assert re.fullmatch(r"Apt\. \d{2}|Piso \d|Puerta \d", secondary_address)

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

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert len(postcode) == 5
            assert 1000 <= int(postcode) <= 52100


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
                r"\d{3} \d{3}|\d{3} Interior \d{3}|\d{3} Edif\. \d{3} , Depto\. \d{3}",
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
            assert re.fullmatch(r"(?:سوئیت|واحد) \d{3}", secondary_address)

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

    def test_postcode(self, faker, num_samples):
        department_numbers = [dept_num for dept_num, dept_name in FrFrAddressProvider.departments]
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert len(postcode) == 5
            assert (
                postcode[:3] in department_numbers  # for 3 digits departments number
                or postcode[:2] == "20"  # for Corsica : "2A" or "2B"
                or postcode[:2] in department_numbers  # any other
            )


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
            faker.postcode_in_state("XX")

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r"բն\. \d{1,2}", secondary_address)

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


class TestItIt:
    """Test it_IT address provider methods"""

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in ItItAddressProvider.cities

    def test_postcode_city_province(self, faker, num_samples):
        for _ in range(num_samples):
            postcode_city_province = faker.postcode_city_province()
            assert isinstance(postcode_city_province, str)
            match = re.fullmatch(r"(?P<cap>\d{5}), (?P<city>.*) \((?P<province>[A-Z]{2})\)", postcode_city_province)
            assert match
            assert match.group("cap") in ItItAddressProvider.postcode_formats
            assert match.group("city") in ItItAddressProvider.cities
            assert match.group("province") in ItItAddressProvider.states_abbr

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in ItItAddressProvider.city_prefixes

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            match = re.findall(r".* \d{1,2}", secondary_address)
            assert match

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in ItItAddressProvider.states

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in ItItAddressProvider.states_abbr


class TestJaJp:
    """Test ja_JP address provider methods"""

    def test_chome(self, faker, num_samples):
        for _ in range(num_samples):
            chome = faker.chome()
            assert isinstance(chome, str)
            match = re.fullmatch(r"(?P<chome_number>\d{1,2})丁目", chome)
            assert match
            assert 1 <= int(match.group("chome_number")) <= 42

    def test_ban(self, faker, num_samples):
        for _ in range(num_samples):
            ban = faker.ban()
            assert isinstance(ban, str)
            match = re.fullmatch(r"(?P<ban_number>\d{1,2})番", ban)
            assert match
            assert 1 <= int(match.group("ban_number")) <= 27

    def test_gou(self, faker, num_samples):
        for _ in range(num_samples):
            gou = faker.gou()
            assert isinstance(gou, str)
            match = re.fullmatch(r"(?P<gou_number>\d{1,2})号", gou)
            assert match
            assert 1 <= int(match.group("gou_number")) <= 20

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
            assert re.fullmatch(r"\d{3}-\d{4}", postcode)

    def test_zipcode(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode = faker.zipcode()
            assert isinstance(zipcode, str)
            assert re.fullmatch(r"\d{3}-\d{4}", zipcode)


class TestKoKr:
    """Test ko_KR address provider methods"""

    def test_old_postal_code(self, faker, num_samples):
        for _ in range(num_samples):
            old_postal_code = faker.old_postal_code()
            assert isinstance(old_postal_code, str)
            assert re.fullmatch(r"\d{3}-\d{3}", old_postal_code)

    def test_postal_code(self, faker, num_samples):
        for _ in range(num_samples):
            postal_code = faker.postal_code()
            assert isinstance(postal_code, str)
            assert re.fullmatch(r"\d{5}", postal_code)

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{5}", postcode)

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)

    def test_borough(self, faker, num_samples):
        for _ in range(num_samples):
            borough = faker.borough()
            assert isinstance(borough, str)
            assert borough in KoKrAddressProvider.boroughs

    def test_town(self, faker, num_samples):
        for _ in range(num_samples):
            town = faker.town()
            assert isinstance(town, str)

    def test_town_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            town_suffix = faker.town_suffix()
            assert isinstance(town_suffix, str)
            assert town_suffix in KoKrAddressProvider.town_suffixes

    def test_building_name(self, faker, num_samples):
        for _ in range(num_samples):
            building_name = faker.building_name()
            assert isinstance(building_name, str)

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)
            assert "#" not in building_number

    def test_building_number_underground(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number_underground()
            assert isinstance(building_number, str)
            assert "#" not in building_number
            assert building_number[:2] == "지하"

    def test_building_number_segregated(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number_segregated()
            assert isinstance(building_number, str)
            assert "#" not in building_number
            assert "-" in building_number

    def test_building_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            building_suffix = faker.building_suffix()
            assert isinstance(building_suffix, str)
            assert building_suffix in KoKrAddressProvider.building_suffixes

    def test_building_dong(self, faker, num_samples):
        for _ in range(num_samples):
            building_dong = faker.building_dong()
            assert isinstance(building_dong, str)

    def test_road_address(self, faker, num_samples):
        for _ in range(num_samples):
            road_address = faker.road_address()
            assert isinstance(road_address, str)


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
            assert re.fullmatch(r"^[0-9]{4}$", faker.postcode())

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
            assert re.fullmatch(r"[1-9]\d{2}(?:\d{2})?", postcode)

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
        city_pattern: Pattern = re.compile(r"(?P<city_name>.*?)[市縣]?")
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            match = city_pattern.fullmatch(city)
            assert match
            assert match.group("city_name") in ZhTwAddressProvider.cities

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
            assert re.fullmatch(r"[1-9]\d{5}", postcode)

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
        city_pattern: Pattern = re.compile(r".*?[市县]")
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
            assert re.fullmatch(r"\d{8}", postcode)

    def test_formatted_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{5}-?\d{3}", postcode)


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
        cls.building_number_pattern: Pattern = re.compile(
            r"(?:[1-9]|[1-9]\d{1,3})(?:[A-J]|\s[A-J]|-[A-J]|\sUnit\s[A-J])?",
        )
        cls.address_pattern: Pattern = re.compile(
            r"(?P<street_address>.*), (?P<lgu>.*?), (?P<postcode>\d{4}) (?P<province>.*?)",
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
            assert floor_number[-2:] in ["th", "st", "nd", "rd"]

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            match = self.address_pattern.fullmatch(address)
            street_address = match.group("street_address")
            lgu = match.group("lgu")
            postcode = match.group("postcode")
            province = match.group("province")
            assert match
            assert street_address
            assert lgu in self.province_lgus or lgu in self.metro_manila_lgus
            assert int(postcode) in self.postcodes
            assert province in self.provinces or province == "Metro Manila"


class TestFilPh(TestEnPh):
    """Test fil_PH address provider methods"""

    @classmethod
    def setup_class(cls):
        cls.building_number_pattern: Pattern = re.compile(
            r"(?:[1-9]|[1-9]\d{1,3})(?:[A-J]|\s[A-J]|-[A-J]|\sUnit\s[A-J])?",
        )
        cls.address_pattern: Pattern = re.compile(
            r"(?P<street_address>.*), (?P<lgu>.*?), (?P<postcode>\d{4}) (?P<province>.*?)",
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
            assert floor_number[-2:] in ["th", "st", "nd", "rd"]

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            match = self.address_pattern.fullmatch(address)
            street_address = match.group("street_address")
            lgu = match.group("lgu")
            postcode = match.group("postcode")
            province = match.group("province")
            assert match
            assert street_address
            assert lgu in self.province_lgus or lgu in self.metro_manila_lgus
            assert int(postcode) in self.postcodes
            assert province in self.provinces or province == "Metro Manila"


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
        region_pattern: Pattern = re.compile(
            r"(?:респ\. (?P<region_republic>.*))|"
            r"(?:(?P<region_krai>.*?) край)|"
            r"(?:(?P<region_oblast>.*?) обл.)|"
            r"(?:(?P<region_ao>.*?) АО)",
        )
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            match = region_pattern.fullmatch(region)
            assert match
            groupdict = match.groupdict()
            assert any(
                [
                    groupdict.get("region_republic") in RuRuAddressProvider.region_republics,
                    groupdict.get("region_krai") in RuRuAddressProvider.region_krai,
                    groupdict.get("region_oblast") in RuRuAddressProvider.region_oblast,
                    groupdict.get("region_ao") in RuRuAddressProvider.region_ao,
                ]
            )

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{6}", postcode)

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

    @pytest.mark.parametrize(
        "street_title,street_suffix,expected",
        [
            ("Фрунзе", "ул.", "ул. Фрунзе"),
            ("Ставропольская", "ул.", "ул. Ставропольская"),
            ("Фрунзе", "пр.", "пр. Фрунзе"),
            ("Осенняя", "пр.", "пр. Осенний"),
            ("Гвардейская", "пр.", "пр. Гвардейский"),
            ("Рыбацкая", "пр.", "пр. Рыбацкий"),
            ("Безымянная", "пр.", "пр. Безымянный"),
            ("Проезжая", "ш.", "ш. Проезжее"),
            ("Магистральная", "ш.", "ш. Магистральное"),
        ],
        ids=[
            "feminine_suffix_and_noflex_title",
            "feminine_suffix_and_flex_title",
            "non_feminine_suffix_and_noflex_title",
            "masc_suffix_and_irregular_masc_title",
            "masc_suffix_and_ck_street_stem",
            "masc_suffix_and_uk_street_stem",
            "masc_suffix_and_other_stem",
            "neu_suffx_and_iregular_neu_street_title",
            "neu_suffix_and_regular_street_title",
        ],
    )
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

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in ThThAddressProvider.cities

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
            assert re.fullmatch(r"[1-9]\d{4}", postcode)


class TestEnIn:
    """Test en_IN address provider methods"""

    def test_city_name(self, faker, num_samples):
        """Tests `city names` are fetched correctly"""

        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in EnInAddressProvider.cities

    def test_state(self, faker, num_samples):
        """Tests `states` are fetched correctly"""

        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in EnInAddressProvider.states

    def test_union_territories(self, faker, num_samples):
        """Tests `union_territories` are fetched correctly"""

        for _ in range(num_samples):
            union_territory = faker.union_territory()
            assert isinstance(union_territory, str)
            assert (union_territory,) in EnInAddressProvider.union_territories

    @pytest.mark.parametrize("pincodes", ["pincode_in_state", "zipcode_in_state", "postcode_in_state"])
    def test_pincodes_in_state(self, faker, num_samples, pincodes):
        """Test `pincodes` for state and union territories"""

        for _ in range(num_samples):
            include_ut = faker.random_element([True, False])
            pincode = getattr(faker, pincodes)(include_union_territories=include_ut)
            assert isinstance(pincode, int)
            assert len(str(pincode)) == 6

    @pytest.mark.parametrize(
        "pincodes",
        [
            ("pincode_in_army"),
            ("zipcode_in_army"),
            ("postcode_in_army"),
            ("postcode_in_military"),
            ("zipcode_in_military"),
            ("pincode_in_military"),
        ],
    )
    def test_pincodes_in_military(self, faker, num_samples, pincodes):
        """Test `pincodes` for Army"""

        for _ in range(num_samples):
            pincode = getattr(faker, pincodes)()
            assert isinstance(pincode, int)
            assert len(str(pincode)) == 6


class TestSkSk:
    """Test sk_SK address provider methods"""

    def test_street_suffix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_short = faker.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in SkSkAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_suffix_long = faker.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in SkSkAddressProvider.street_suffixes_long

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in SkSkAddressProvider.cities

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in SkSkAddressProvider.streets

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in SkSkAddressProvider.states

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{3} \d{2}", postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r"\d{3} \d{2} (?P<city>.*)", city_with_postcode)
            assert match.group("city") in SkSkAddressProvider.cities


class TestDeCh:
    """Test de_CH address provider methods"""

    def test_canton_name(self, faker, num_samples):
        for _ in range(num_samples):
            canton_name = faker.canton_name()
            assert isinstance(canton_name, str)
            assert any(canton_name == cantons[1] for cantons in DeChAddressProvider.cantons)

    def test_canton_code(self, faker, num_samples):
        for _ in range(num_samples):
            canton_code = faker.canton_code()
            assert isinstance(canton_code, str)
            assert any(canton_code == cantons[0] for cantons in DeChAddressProvider.cantons)

    def test_canton(self, faker, num_samples):
        for _ in range(num_samples):
            canton = faker.canton()
            assert isinstance(canton, tuple)
            assert canton in DeChAddressProvider.cantons

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in DeChAddressProvider.cities


class TestRoRo:
    """Test ro_RO address provider methods"""

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)

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
            assert street_prefix in RoRoAddressProvider.street_prefixes

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)
            assert building_number[:3] == "Nr."

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(
                r"Bl. \d{2}  Sc. \d{2} Ap. \d{3}",
                secondary_address,
            )

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in RoRoAddressProvider.cities

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city_name()
            assert isinstance(city, str)
            assert city in RoRoAddressProvider.cities

    def test_state(self, faker, num_samples):
        states = [state_name for state_abbr, state_name in RoRoAddressProvider.states]
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in states

    def test_state_abbr(self, faker, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in RoRoAddressProvider.states]
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in state_abbrs
            assert state_abbr.isupper()

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{6}", postcode)

    def test_city_with_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            city_with_postcode = faker.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r"\d{6} (?P<city>.*)", city_with_postcode)
            assert match.group("city") in RoRoAddressProvider.cities


class TestEnMs:
    """Test en_MS address provider methods"""

    def test_city_prefix_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix_abbr = faker.city_prefix_abbr()
            assert isinstance(city_prefix_abbr, str)
            assert city_prefix_abbr in EnMsAddressProvider.city_prefix_abbrs

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnMsAddressProvider.city_prefixes

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert "%" not in city
            assert "#" not in city
            assert "?" not in city

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EnMsAddressProvider.street_prefixes

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_building_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            building_prefix = faker.building_prefix()
            assert isinstance(building_prefix, str)

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)

    def test_city_state(self, faker, num_samples):
        for _ in range(num_samples):
            city_state = faker.city_state()
            assert isinstance(city_state, str)

    @pytest.mark.parametrize(
        "fn_name",
        [
            ("administrative_unit"),
            ("state"),
        ],
    )
    def test_state_administrative_unit(self, faker, num_samples, fn_name):
        for _ in range(num_samples):
            state = getattr(faker, fn_name)()
            assert isinstance(state, str)
            assert state in [x for v in EnMsAddressProvider.states.values() for x in v]

    def test_postcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnMsAddressProvider.states.keys():
                code = faker.postcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnMsAddressProvider.states_postcode[state_abbr][0][0]
                assert int(code) <= EnMsAddressProvider.states_postcode[state_abbr][-1][1]

        with pytest.raises(KeyError):
            faker.postcode_in_state("XX")

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            code = faker.postcode()
            assert re.fullmatch(r"\d{5}", code)


class TestEnNz:
    """Test en_NZ address provider methods"""

    def test_te_reo_part(self, faker, num_samples):
        for _ in range(num_samples):
            to_reo_part = faker.te_reo_part()
            assert isinstance(to_reo_part, str)
            assert to_reo_part in EnNzAddressProvider.te_reo_parts

    def test_reo_first(self, faker, num_samples):
        for _ in range(num_samples):
            te_reo_first = faker.te_reo_first()
            assert isinstance(te_reo_first, str)
            assert te_reo_first in [str(i).capitalize() for i in EnNzAddressProvider.te_reo_parts]

    def test_reo_ending(self, faker, num_samples):
        for _ in range(num_samples):
            te_reo_ending = faker.te_reo_ending()
            assert isinstance(te_reo_ending, str)
            assert te_reo_ending in EnNzAddressProvider.te_reo_parts or EnNzAddressProvider.te_reo_endings

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnNzAddressProvider.city_prefixes

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in EnNzAddressProvider.city_suffixes

    def test_rd_number(self, faker, num_samples):
        for _ in range(num_samples):
            rd_number = faker.rd_number()
            assert isinstance(rd_number, str)
            assert rd_number in [str(i) for i in range(1, 11)]

    def test_secondary_address(self, faker, num_samples):
        for _ in range(num_samples):
            secondary_address = faker.secondary_address()
            assert isinstance(secondary_address, str)
            assert secondary_address.split(" ")[0] in [
                i.split(" ")[0] for i in EnNzAddressProvider.secondary_address_formats
            ]


class TestFrCh:
    """Test fr_CH address provider methods"""

    def test_canton_name(self, faker, num_samples):
        for _ in range(num_samples):
            canton_name = faker.canton_name()
            assert isinstance(canton_name, str)
            assert any(canton_name == cantons[1] for cantons in FrChAddressProvider.cantons)

    def test_canton_code(self, faker, num_samples):
        for _ in range(num_samples):
            canton_code = faker.canton_code()
            assert isinstance(canton_code, str)
            assert any(canton_code == cantons[0] for cantons in FrChAddressProvider.cantons)

    def test_canton(self, faker, num_samples):
        for _ in range(num_samples):
            canton = faker.canton()
            assert isinstance(canton, tuple)
            assert canton in FrChAddressProvider.cantons


class TestHuHu:
    """Test hu_HU address provider methods"""

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in HuHuAddressProvider.counties

    def test_street_address_with_county(self, faker, num_samples):
        for _ in range(num_samples):
            street_address_with_county = faker.street_address_with_county()
            assert isinstance(street_address_with_county, str)
            match = re.fullmatch(r".* \d*.\n.* [A-Za-zÀ-ȕ]*\nH-\d{4} [A-Za-zÀ-ȕ]*", street_address_with_county)
            assert match

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in HuHuAddressProvider.city_prefs

    def test_city_part(self, faker, num_samples):
        for _ in range(num_samples):
            city_part = faker.city_part()
            assert isinstance(city_part, str)
            assert city_part in HuHuAddressProvider.city_parts

    def test_real_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            real_city_name = faker.real_city_name()
            assert isinstance(real_city_name, str)
            assert real_city_name in HuHuAddressProvider.real_city_names

    def test_frequent_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            frequent_street_name = faker.frequent_street_name()
            assert isinstance(frequent_street_name, str)
            assert frequent_street_name in HuHuAddressProvider.frequent_street_names

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            match = re.fullmatch(r"H-\d{4}", postcode)
            assert match

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)

    def test_building_number(self, faker, num_samples):
        for _ in range(num_samples):
            building_number = faker.building_number()
            assert isinstance(building_number, str)
            match = re.fullmatch(r"\d{0,3}.", building_number)
            assert match

    def test_city(self, faker, num_samples):
        # generating possible variations for cities for hu_Hu locale
        real_cities = [city.lower() for city in HuHuAddressProvider.real_city_names]
        cities_part_suffix = [
            "".join([part, suffix])
            for part in HuHuAddressProvider.city_parts
            for suffix in HuHuAddressProvider.city_suffixes
        ]
        cities_prefix_part_suffix = [
            "".join([pref, part_suffix])
            for pref in HuHuAddressProvider.city_prefs
            for part_suffix in cities_part_suffix
        ]
        cities = real_cities + cities_part_suffix + cities_prefix_part_suffix
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city.lower() in cities
            assert city[0].isupper()


class TestIdId:
    """Test id_ID address provider methods"""

    def test_street(self, faker, num_samples):
        for _ in range(num_samples):
            street = faker.street()
            assert isinstance(street, str)
            assert street in IdIdAddressProvider.streets

    def test_street_prefix_short(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix_short = faker.street_prefix_short()
            assert isinstance(street_prefix_short, str)
            assert street_prefix_short in IdIdAddressProvider.street_prefixes_short

    def test_street_prefix_long(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix_long = faker.street_prefix_long()
            assert isinstance(street_prefix_long, str)
            assert street_prefix_long in IdIdAddressProvider.street_prefixes_long

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in IdIdAddressProvider.cities

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in IdIdAddressProvider.states

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in IdIdAddressProvider.states_abbr

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in IdIdAddressProvider.countries


class TestKaGe:
    """Test ka_GE address provider methods"""

    def test_street_title(self, faker, num_samples):
        for _ in range(num_samples):
            street_title = faker.street_title()
            assert isinstance(street_title, str)
            assert street_title in KaGeAddressProvider.street_titles

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in KaGeAddressProvider.city_names


class TestSlSi:
    """Test sl_SI address provider methods"""

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in SlSiAddressProvider.cities

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in SlSiAddressProvider.streets

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in SlSiAddressProvider.states


class TestSvSe:
    """Test sv_SE address provider methods"""

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in SvSeAddressProvider.street_prefixes

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in SvSeAddressProvider.cities

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in SvSeAddressProvider.states


class TestUkUa:
    """Test uk_UA address provider methods"""

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in UkUaAddressProvider.city_prefixes

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in UkUaAddressProvider.city_names

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            match = re.findall(r"\d{5}", postcode)
            assert match

    def test_street_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in UkUaAddressProvider.street_prefixes

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in UkUaAddressProvider.street_titles

    def test_street_title(self, faker, num_samples):
        for _ in range(num_samples):
            street_title = faker.street_title()
            assert isinstance(street_title, str)

    def test_region(self, faker, num_samples):
        for _ in range(num_samples):
            region = faker.region()
            assert isinstance(region, str)
            assert region in UkUaAddressProvider.region_names


class TestViVn:
    """Test vi_VN address provider methods"""

    def test_city_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in ViVNAddressProvider.city_prefixes

    def test_state(self, faker, num_samples):
        for _ in range(num_samples):
            state = faker.state()
            assert isinstance(state, str)
            assert state in ViVNAddressProvider.provinces

    def test_state_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            state_abbr = faker.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in ViVNAddressProvider.provinces_abbr

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str) and len(postcode) == 6
            assert 100000 <= int(postcode) <= 999999

    def test_postcode_in_state(self, faker, num_samples):
        for _ in range(num_samples):
            for state_abbr in ViVNAddressProvider.provinces_abbr:
                postcode = faker.postcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{6}", postcode)
                assert int(postcode) >= ViVNAddressProvider.provinces_postcode[state_abbr][0]
                assert int(postcode) <= ViVNAddressProvider.provinces_postcode[state_abbr][1]

        with pytest.raises(ValueError):
            faker.postcode_in_state("XX")

    def test_state_abbr_determinism(self, faker):
        faker.seed_instance(0)
        first = faker.state_abbr()
        faker.seed_instance(0)
        assert faker.state_abbr() == first


class TestFrCa:
    """Test fr_CA address provider methods"""

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in FrCaAddressProvider.provinces

    def test_province_abbr(self, faker, num_samples):
        for _ in range(num_samples):
            province_abbr = faker.province_abbr()
            assert isinstance(province_abbr, str)
            assert province_abbr in FrCaAddressProvider.provinces_abbr

    def test_city_prefixes(self, faker, num_samples):
        for _ in range(num_samples):
            city_prefix = faker.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in FrCaAddressProvider.city_prefixes

    def test_city_suffixes(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffixes = faker.city_suffix()
            assert isinstance(city_suffixes, str)
            assert city_suffixes in FrCaAddressProvider.city_suffixes

    def test_street_prefixes(self, faker, num_samples):
        for _ in range(num_samples):
            street_prefix = faker.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in FrCaAddressProvider.street_prefixes

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.administrative_unit()
            assert isinstance(province, str)
            assert province in FrCaAddressProvider.provinces


class TestPlPl:
    """Test pl_PL address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            match = re.findall(r"^\d{2}-\d{3}$", postcode)
            assert match

    def test_zipcode(self, faker, num_samples):
        for _ in range(num_samples):
            zipcode = faker.zipcode()
            match = re.findall(r"^\d{2}-\d{3}$", zipcode)
            assert match

    def test_postalcode(self, faker, num_samples):
        for _ in range(num_samples):
            postalcode = faker.postalcode()
            match = re.findall(r"^^\d{2}-\d{3}$$", postalcode)
            assert match


class TestZuZa:
    """Test zu_ZA address provider methods"""

    def test_postcode(self, faker, num_samples):
        for _ in range(num_samples):
            postcode = faker.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)

    def test_city_name(self, faker, num_samples):
        for _ in range(num_samples):
            city_name = faker.city_name()
            assert isinstance(city_name, str)
            assert city_name in ZuZaAddressProvider.cities

    def test_city_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            city_suffix = faker.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in ZuZaAddressProvider.city_suffixes

    def test_city(self, faker, num_samples):
        for _ in range(num_samples):
            city = faker.city()
            assert isinstance(city, str)
            assert city in ZuZaAddressProvider.cities

    def test_country(self, faker, num_samples):
        for _ in range(num_samples):
            country = faker.country()
            assert isinstance(country, str)
            assert country in ZuZaAddressProvider.countries

    def test_street_name(self, faker, num_samples):
        for _ in range(num_samples):
            street_name = faker.street_name()
            assert isinstance(street_name, str)
            assert street_name in ZuZaAddressProvider.street_names

    def test_address(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.address()
            assert isinstance(address, str)

    def test_province(self, faker, num_samples):
        for _ in range(num_samples):
            province = faker.province()
            assert isinstance(province, str)
            assert province in ZuZaAddressProvider.provinces

    def test_administrative_unit(self, faker, num_samples):
        for _ in range(num_samples):
            administrative_unit = faker.administrative_unit()
            assert isinstance(administrative_unit, str)
            assert administrative_unit in ZuZaAddressProvider.provinces
