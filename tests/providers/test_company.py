import re

from datetime import datetime
from unittest.mock import patch

import pytest

from faker.providers.company.en_PH import Provider as EnPhCompanyProvider
from faker.providers.company.fil_PH import Provider as FilPhCompanyProvider
from faker.providers.company.hu_HU import Provider as HuHuCompanyProvider
from faker.providers.company.hy_AM import Provider as HyAmCompanyProvider
from faker.providers.company.it_IT import Provider as ItItCompanyProvider
from faker.providers.company.ja_JP import Provider as JaJpCompanyProvider
from faker.providers.company.nl_NL import Provider as NlNlCompanyProvider
from faker.providers.company.pl_PL import Provider as PlPlCompanyProvider
from faker.providers.company.pl_PL import company_vat_checksum, local_regon_checksum, regon_checksum
from faker.providers.company.pt_BR import company_id_checksum
from faker.providers.company.ru_RU import Provider as RuRuCompanyProvider
from faker.providers.company.ru_RU import calculate_checksum
from faker.providers.company.th_TH import Provider as ThThCompanyProvider
from faker.providers.company.tr_TR import Provider as TrTrCompanyProvider


class TestFiFi:
    """Test fi_FI company provider methods"""

    def _has_valid_checksum(self, company_id):
        factors = [7, 9, 10, 5, 8, 4, 2]
        checksum = 0
        for x, y in zip(company_id[:-2], factors):
            checksum += int(x) * y
        checksum %= 11
        checksum = 11 - checksum if checksum else 0
        return int(company_id[-1]) == checksum

    def test_company_business_id(self, faker, num_samples):
        for _ in range(num_samples):
            company_id = faker.company_business_id()
            assert len(company_id) == 9
            assert self._has_valid_checksum(company_id)


class TestHyAm:
    """Test hy_AM company provider methods"""

    def test_bs(self, faker, num_samples):
        for _ in range(num_samples):
            bs = faker.bs()
            assert isinstance(bs, str)

    def test_catch_phrase(self, faker, num_samples):
        for _ in range(num_samples):
            catch_phrase = faker.catch_phrase()
            assert isinstance(catch_phrase, str)

    def test_company(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.company()
            assert isinstance(company, str)

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in HyAmCompanyProvider.company_suffixes


class TestJaJp:
    """Test ja_JP company provider methods"""

    def test_company_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_prefix()
            assert isinstance(prefix, str)
            assert prefix in JaJpCompanyProvider.company_prefixes

    def test_company_category(self, faker, num_samples):
        for _ in range(num_samples):
            category = faker.company_category()
            assert isinstance(category, str)
            assert category in JaJpCompanyProvider.company_categories

    def test_company(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.company()
            assert isinstance(company, str)
            assert any(
                company.startswith(prefix) or company.endswith(prefix)
                for prefix in JaJpCompanyProvider.company_prefixes
            )
            assert any(
                category in company
                for category in JaJpCompanyProvider.company_categories
            )


class TestPtBr:
    """Test pt_BR company provider methods"""

    def test_company_id_checksum(self):
        assert company_id_checksum([9, 4, 9, 5, 3, 4, 4, 1, 0, 0, 0, 1]) == [5, 1]
        assert company_id_checksum([1, 6, 0, 0, 4, 6, 3, 9, 0, 0, 0, 1]) == [8, 5]

    def test_company_id(self, faker, num_samples):
        for _ in range(num_samples):
            company_id = faker.company_id()
            assert re.fullmatch(r'\d{14}', company_id)

    def test_cnpj(self, faker, num_samples):
        for _ in range(num_samples):
            cnpj = faker.cnpj()
            assert re.fullmatch(r'\d{2}\.\d{3}\.\d{3}/0001-\d{2}', cnpj)


class TestHuHu:
    """Test hu_HU company provider methods"""

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in HuHuCompanyProvider.company_suffixes

    def test_company(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.company()
            assert isinstance(company, str)
            assert company.split(" ")[-1] in HuHuCompanyProvider.company_suffixes


class TestPlPl:
    """Test pl_PL company provider methods"""

    def test_regon_checksum(self):
        assert regon_checksum([1, 2, 3, 4, 5, 6, 7, 8]) == 5
        assert regon_checksum([8, 9, 1, 9, 5, 7, 8, 8]) == 3
        assert regon_checksum([2, 1, 7, 1, 5, 4, 8, 3]) == 8
        assert regon_checksum([7, 9, 3, 5, 4, 7, 9, 3]) == 9
        assert regon_checksum([9, 1, 5, 9, 6, 9, 4, 7]) == 7

    def test_regon(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r'\d{9}', faker.regon())

    def test_local_regon_checksum(self):
        assert local_regon_checksum([1, 2, 3, 4, 5, 6, 7, 8, 5, 1, 2, 3, 4]) == 7
        assert local_regon_checksum([6, 1, 1, 9, 4, 8, 8, 3, 2, 7, 5, 8, 0]) == 3
        assert local_regon_checksum([8, 9, 2, 0, 0, 3, 6, 6, 0, 7, 0, 3, 2]) == 3
        assert local_regon_checksum([3, 5, 7, 7, 1, 0, 2, 2, 2, 5, 4, 3, 3]) == 0
        assert local_regon_checksum([9, 3, 5, 3, 1, 1, 0, 1, 2, 4, 8, 8, 2]) == 1

    def test_local_regon(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r'\d{14}', faker.local_regon())

    def test_company_vat_checksum(self):
        assert company_vat_checksum([7, 7, 5, 7, 7, 7, 6, 0, 5]) == 9
        assert company_vat_checksum([1, 8, 6, 5, 4, 9, 9, 6, 4]) == 2
        assert company_vat_checksum([7, 1, 2, 8, 9, 2, 4, 9, 9]) == 7
        assert company_vat_checksum([3, 5, 4, 6, 1, 0, 6, 5, 8]) == 4
        assert company_vat_checksum([3, 1, 9, 5, 5, 7, 0, 4, 5]) == 0

    def test_company_vat(self, faker, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r'\d{10}', faker.company_vat())

    def test_company_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_prefix()
            assert isinstance(prefix, str)
            assert prefix in PlPlCompanyProvider.company_prefixes

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in PlPlCompanyProvider.company_suffixes


class TestNlNl:
    """Test nl_NL company provider methods"""

    def test_company_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_prefix()
            assert isinstance(prefix, str)
            assert prefix in NlNlCompanyProvider.company_prefixes

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in NlNlCompanyProvider.company_suffixes

    def test_large_companies(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.large_company()
            assert isinstance(company, str)
            assert company in NlNlCompanyProvider.large_companies


class TestEnPh:
    """Test en_PH company provider methods"""

    @classmethod
    def setup_class(cls):
        cls.company_types = EnPhCompanyProvider.company_types
        cls.company_suffixes = EnPhCompanyProvider.company_suffixes.keys()
        cls.company_products = EnPhCompanyProvider.company_products
        cls.national_corporation_pattern = re.compile(r'^National (.*?) Corporation of the Philippines$')

    def test_random_company_noun_chain(self, faker, num_samples):
        for _ in range(num_samples):
            noun_list = faker.random_company_noun_chain().split()
            assert 1 <= len(noun_list) <= 2

    def test_random_company_acronym(self, faker, num_samples):
        for _ in range(num_samples):
            acronym = faker.random_company_acronym()
            assert 2 <= len(acronym) <= 4

    def test_company(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.company()
            if company.split()[-1] in self.company_suffixes and company.split()[-2] in self.company_types:
                continue
            else:
                national_corporation_match = self.national_corporation_pattern.fullmatch(company)
                assert national_corporation_match and national_corporation_match.group(1) in self.company_products


class TestFilPh(TestEnPh):
    """Test fil_PH company provider methods"""

    def test_PH_random_good_service_adjective_chain(self, faker, num_samples):
        for _ in range(num_samples):
            adjectives = faker.random_good_service_adjective_chain().split(' at ')
            assert all(
                adjective in FilPhCompanyProvider.good_service_adjectives
                for adjective in adjectives
            )


class TestTlPh(TestFilPh):
    """Test tl_PH company provider methods"""
    pass


class TestRuRu:
    """Test ru_RU company provider methods"""

    def test_calculate_checksum_nine_digits(self):
        assert calculate_checksum('164027304') == '7'
        assert calculate_checksum('629082979') == '0'
        assert calculate_checksum('0203184580') == '5'
        assert calculate_checksum('1113145630') == '0'
        assert calculate_checksum('70517081385') == '1'
        assert calculate_checksum('60307390550') == '0'

    def test_businesses_inn(self, faker, num_samples):
        for _ in range(num_samples):
            inn = faker.businesses_inn()
            assert len(inn) == 10
            assert calculate_checksum(inn[:9]) == inn[9]

    def test_individuals_inn(self, faker, num_samples):
        for _ in range(num_samples):
            inn = faker.individuals_inn()
            assert len(inn) == 12
            assert calculate_checksum(inn[:10]) == inn[10]
            assert calculate_checksum(inn[:11]) == inn[11]

    def test_businesses_ogrn(self, faker, num_samples):
        max_year = datetime.now().year - 2000
        for _ in range(num_samples):
            ogrn = faker.businesses_ogrn()
            assert len(ogrn) == 13
            assert ogrn[0] in ('1', '5')
            assert 1 <= int(ogrn[1:3]) <= max_year
            assert 1 <= int(ogrn[3:5]) <= 92
            assert int(ogrn[:-1]) % 11 % 10 == int(ogrn[-1])

    def test_individuals_ogrn(self, faker, num_samples):
        max_year = datetime.now().year - 2000
        for _ in range(num_samples):
            ogrn = faker.individuals_ogrn()
            assert len(ogrn) == 15
            assert ogrn[0] == '3'
            assert 1 <= int(ogrn[1:3]) <= max_year
            assert 1 <= int(ogrn[3:5]) <= 92
            assert int(ogrn[:-1]) % 13 % 10 == int(ogrn[-1])

    def test_kpp(self, faker, num_samples):
        for _ in range(num_samples):
            kpp = faker.kpp()
            assert len(kpp) == 9
            assert 1 <= int(kpp[0:2]) <= 92
            assert int(kpp[2:4]) > 0
            assert kpp[4:6] in ('01', '43', '44', '45')

    def test_company_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_prefix()
            assert isinstance(prefix, str)
            assert prefix in RuRuCompanyProvider.company_prefixes

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in RuRuCompanyProvider.company_suffixes

    def test_large_companies(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.large_company()
            assert isinstance(company, str)
            assert company in RuRuCompanyProvider.large_companies

    def test_catchphrase(self, faker, num_samples):
        for _ in range(num_samples):
            catchphrase = faker.catch_phrase()
            assert isinstance(catchphrase, str)
            assert ' и ' in catchphrase

    def test_bs(self, faker, num_samples):
        for _ in range(num_samples):
            bs = faker.bs()
            bs_words = bs.split()
            assert isinstance(bs, str)
            assert bs_words[0] in RuRuCompanyProvider.bsWords[0]


class TestItIt:
    """Test it_IT company provider methods"""

    vat_regex = re.compile(r"^IT\d{7}(0\d{2}|100|120|121|888|999)\d$", flags=re.ASCII)

    def test_company_vat(self, faker, num_samples):
        for _ in range(num_samples):
            company_vat = faker.company_vat()
            assert self.vat_regex.match(company_vat)

    @pytest.mark.parametrize("value, expected", (
        (100, "100"),
        (101, "120"),
        (102, "121"),
        (103, "888"),
        (104, "999"),
    ))
    def test_company_vat_special_cases(self, faker, value, expected):
        # this test allows to get full code coverage for company_vat fixing the internal state of the random generator
        fake = ItItCompanyProvider(generator=faker)

        with patch.object(fake, "random_int", return_value=value, autospec=True):
            company_vat = fake.company_vat()
            assert self.vat_regex.match(company_vat)
            assert company_vat[9:12] == expected


class TestThTh:
    """Test th_TH company provider methods"""

    def test_company_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_prefix()
            assert isinstance(prefix, str)
            assert prefix in ThThCompanyProvider.company_prefixes

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in ThThCompanyProvider.company_suffixes

    def test_company_limited_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.company_limited_prefix()
            assert isinstance(prefix, str)
            assert prefix in ThThCompanyProvider.company_limited_prefixes

    def test_company_limited_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_limited_suffix()
            assert isinstance(suffix, str)
            assert suffix in ThThCompanyProvider.company_limited_suffixes

    def test_nonprofit_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            prefix = faker.nonprofit_prefix()
            assert isinstance(prefix, str)
            assert prefix in ThThCompanyProvider.nonprofit_prefixes

    def test_company(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.company()
            assert isinstance(company, str)


class TestTrTr:
    """Test tr_TR company provider methods"""

    def test_company_suffix(self, faker, num_samples):
        for _ in range(num_samples):
            suffix = faker.company_suffix()
            assert isinstance(suffix, str)
            assert suffix in TrTrCompanyProvider.company_suffixes

    def test_large_companies(self, faker, num_samples):
        for _ in range(num_samples):
            company = faker.large_company()
            assert isinstance(company, str)
            assert company in TrTrCompanyProvider.large_companies
