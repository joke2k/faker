# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

import six

from faker import Faker
from faker.providers.company import ru_RU as ru
from faker.providers.company.hy_AM import Provider as HyAmProvider
from faker.providers.company.ja_JP import Provider as JaProvider
from faker.providers.company.nl_NL import Provider as NlProvider
from faker.providers.company.pl_PL import (
    company_vat_checksum, regon_checksum, local_regon_checksum, Provider as PlProvider,
)
from faker.providers.company.pt_BR import company_id_checksum
from faker.utils.datetime_safe import datetime


class TestFiFI(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('fi_FI')
        Faker.seed(0)

    def test_company_business_id(self):
        self.fake.random.seed(6)
        company_id = self.fake.company_business_id()
        assert company_id.endswith('0')
        for seed in range(0, 11):
            self.fake.random.seed(seed)
            self.fake.company_business_id()


class TestHyAm(unittest.TestCase):
    """ Tests companies in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_bs(self):
        bs = self.fake.bs()
        assert isinstance(bs, six.string_types)

    def test_catch_phrase(self):
        catch_phrase = self.fake.catch_phrase()
        assert isinstance(catch_phrase, six.string_types)

    def test_company(self):
        company = self.fake.company()
        assert isinstance(company, six.string_types)

    def test_company_suffix(self):
        suffix = self.fake.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in HyAmProvider.company_suffixes


class TestJaJP(unittest.TestCase):
    """ Tests companies in the ja_JP locale """

    def setUp(self):
        self.fake = Faker('ja')
        Faker.seed(0)

    def test_company(self):
        prefixes = JaProvider.company_prefixes
        prefix = self.fake.company_prefix()
        assert isinstance(prefix, six.string_types)
        assert prefix in prefixes

        categories = JaProvider.company_categories
        category = self.fake.company_category()
        assert isinstance(category, six.string_types)
        assert category in categories

        company = self.fake.company()
        assert isinstance(company, six.string_types)
        assert any(company.startswith(prefix) or company.endswith(prefix) for prefix in prefixes)
        assert any(category in company for category in categories)


class TestPtBR(unittest.TestCase):
    """ Tests company in the pt_BR locale """

    def setUp(self):
        self.fake = Faker('pt_BR')
        Faker.seed(0)

    def test_pt_BR_company_id_checksum(self):
        assert company_id_checksum([9, 4, 9, 5, 3, 4, 4, 1, 0, 0, 0, 1]) == [5, 1]
        assert company_id_checksum([1, 6, 0, 0, 4, 6, 3, 9, 0, 0, 0, 1]) == [8, 5]

    def test_pt_BR_company_id(self):
        for _ in range(100):
            assert re.search(r'^\d{14}$', self.fake.company_id())

    def test_pt_BR_cnpj(self):
        for _ in range(100):
            cnpj = self.fake.cnpj()
            assert re.search(r'\d{2}\.\d{3}\.\d{3}/0001-\d{2}', cnpj)


class TestHuHU(unittest.TestCase):
    """ Tests company in the hu_HU locale """

    def setUp(self):
        self.fake = Faker('hu_HU')
        Faker.seed(0)
        self.valid_suffixes = ('Kft.', 'Kht.', 'Zrt.', 'Bt.', 'Nyrt.', 'Kkt.')

    def test_company_suffix(self):
        suffix = self.fake.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in self.valid_suffixes

    def test_company(self):
        company = self.fake.company()
        assert isinstance(company, six.string_types)
        assert company.split(" ")[-1] in self.valid_suffixes


class TestPlPL(unittest.TestCase):
    """ Tests company in the pl_PL locale """

    def setUp(self):
        self.fake = Faker('pl_PL')
        Faker.seed(0)

    def test_regon_checksum(self):
        assert regon_checksum([1, 2, 3, 4, 5, 6, 7, 8]) == 5
        assert regon_checksum([8, 9, 1, 9, 5, 7, 8, 8]) == 3
        assert regon_checksum([2, 1, 7, 1, 5, 4, 8, 3]) == 8
        assert regon_checksum([7, 9, 3, 5, 4, 7, 9, 3]) == 9
        assert regon_checksum([9, 1, 5, 9, 6, 9, 4, 7]) == 7

    def test_regon(self):
        for _ in range(100):
            assert re.search(r'^\d{9}$', self.fake.regon())

    def test_local_regon_checksum(self):
        assert local_regon_checksum([1, 2, 3, 4, 5, 6, 7, 8, 5, 1, 2, 3, 4]) == 7
        assert local_regon_checksum([6, 1, 1, 9, 4, 8, 8, 3, 2, 7, 5, 8, 0]) == 3
        assert local_regon_checksum([8, 9, 2, 0, 0, 3, 6, 6, 0, 7, 0, 3, 2]) == 3
        assert local_regon_checksum([3, 5, 7, 7, 1, 0, 2, 2, 2, 5, 4, 3, 3]) == 0
        assert local_regon_checksum([9, 3, 5, 3, 1, 1, 0, 1, 2, 4, 8, 8, 2]) == 1

    def test_local_regon(self):
        for _ in range(100):
            assert re.search(r'^\d{14}$', self.fake.local_regon())

    def test_company_vat_checksum(self):
        assert company_vat_checksum([7, 7, 5, 7, 7, 7, 6, 0, 5]) == 9
        assert company_vat_checksum([1, 8, 6, 5, 4, 9, 9, 6, 4]) == 2
        assert company_vat_checksum([7, 1, 2, 8, 9, 2, 4, 9, 9]) == 7
        assert company_vat_checksum([3, 5, 4, 6, 1, 0, 6, 5, 8]) == 4
        assert company_vat_checksum([3, 1, 9, 5, 5, 7, 0, 4, 5]) == 0

    def test_company_vat(self):
        for _ in range(100):
            assert re.search(r'^\d{10}$', self.fake.company_vat())

    def test_company_prefix(self):
        prefixes = PlProvider.company_prefixes
        prefix = self.fake.company_prefix()
        assert isinstance(prefix, six.string_types)
        assert prefix in prefixes

    def test_company_suffix(self):
        suffixes = PlProvider.company_suffixes
        suffix = self.fake.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in suffixes


class TestNlNL(unittest.TestCase):
    """ Tests company in the nl_NL locale """

    def setUp(self):
        self.fake = Faker('nl_NL')
        Faker.seed(0)

    def test_company_prefix(self):
        prefixes = NlProvider.company_prefixes
        prefix = self.fake.company_prefix()
        assert isinstance(prefix, six.string_types)
        assert prefix in prefixes

    def test_company_suffix(self):
        suffixes = NlProvider.company_suffixes
        suffix = self.fake.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in suffixes

    def test_large_companies(self):
        companies = NlProvider.large_companies
        company = self.fake.large_company()
        assert isinstance(company, six.string_types)
        assert company in companies


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.national_corporation_pattern = re.compile(r'^National (.*?) Corporation of the Philippines$')
        self.setup_constants()
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker('en_PH')
        Faker.seed(0)

    def setup_constants(self):
        from faker.providers.company.en_PH import Provider
        self.company_types = Provider.company_types
        self.company_suffixes = Provider.company_suffixes.keys()
        self.company_products = Provider.company_products

    def test_PH_random_company_noun_chain(self):
        for i in range(self.num_sample_runs):
            noun_list = self.fake.random_company_noun_chain().split()
            assert len(noun_list) in range(1, 3)

    def test_PH_random_company_acronym(self):
        for i in range(self.num_sample_runs):
            assert len(self.fake.random_company_acronym()) in range(2, 5)

    def test_PH_company(self):
        for i in range(self.num_sample_runs):
            company = self.fake.company()
            if company.split()[-1] in self.company_suffixes and company.split()[-2] in self.company_types:
                continue
            else:
                national_corporation_match = self.national_corporation_pattern.match(company)
                assert national_corporation_match and national_corporation_match.group(1) in self.company_products


class TestFilPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('fil_PH')
        Faker.seed(0)

    def setup_constants(self):
        super(TestFilPh, self).setup_constants()
        from faker.providers.company.fil_PH import Provider
        self.good_service_adjectives = Provider.good_service_adjectives

    def test_PH_random_good_service_adjective_chain(self):
        for i in range(self.num_sample_runs):
            adjectives = self.fake.random_good_service_adjective_chain().split(' at ')
            assert adjectives[0] in self.good_service_adjectives and adjectives[1] in self.good_service_adjectives


class TestTlPh(TestFilPh):

    def setup_faker(self):
        self.fake = Faker('tl_PH')
        Faker.seed(0)


class TestRuRu(unittest.TestCase):
    """ Tests company in the ru_RU locale """

    num_sample_runs = 1000

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)

    def test_calculate_checksum_nine_digits(self):
        assert ru.calculate_checksum('164027304') == '7'
        assert ru.calculate_checksum('629082979') == '0'
        assert ru.calculate_checksum('0203184580') == '5'
        assert ru.calculate_checksum('1113145630') == '0'
        assert ru.calculate_checksum('70517081385') == '1'
        assert ru.calculate_checksum('60307390550') == '0'

    def test_businesses_inn(self):
        for i in range(self.num_sample_runs):
            inn = self.fake.businesses_inn()

            assert len(inn) == 10
            assert ru.calculate_checksum(inn[:9]) == inn[9]

    def test_individuals_inn(self):
        for i in range(self.num_sample_runs):
            inn = self.fake.individuals_inn()

            assert len(inn) == 12
            assert ru.calculate_checksum(inn[:10]) == inn[10]
            assert ru.calculate_checksum(inn[:11]) == inn[11]

    def test_businesses_ogrn(self):
        max_year = datetime.now().year - 2000

        for i in range(self.num_sample_runs):
            ogrn = self.fake.businesses_ogrn()

            assert len(ogrn) == 13
            assert ogrn[0] in ('1', '5')
            assert 1 <= int(ogrn[1:3]) <= max_year
            assert 1 <= int(ogrn[3:5]) <= 92
            assert int(ogrn[:-1]) % 11 % 10 == int(ogrn[-1])

    def test_individuals_ogrn(self):
        max_year = datetime.now().year - 2000

        for i in range(self.num_sample_runs):
            ogrn = self.fake.individuals_ogrn()

            assert len(ogrn) == 15
            assert ogrn[0] == '3'
            assert 1 <= int(ogrn[1:3]) <= max_year
            assert 1 <= int(ogrn[3:5]) <= 92
            assert int(ogrn[:-1]) % 13 % 10 == int(ogrn[-1])

    def test_kpp(self):
        for i in range(self.num_sample_runs):
            kpp = self.fake.kpp()

            assert len(kpp) == 9
            assert 1 <= int(kpp[0:2]) <= 92
            assert int(kpp[2:4]) > 0
            assert kpp[4:6] in ('01', '43', '44', '45')
