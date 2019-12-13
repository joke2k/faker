# coding=utf-8

from __future__ import unicode_literals

from itertools import cycle

import unittest
try:
    from unittest import mock
except ImportError:
    import mock
import pytest
import six

from validators import email as validate_email, domain as validate_domain

from faker import Faker
from faker.providers.person.ja_JP import Provider as JaProvider
from faker.utils import text


class TestInternetProvider(unittest.TestCase):
    """ Tests internet """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_email(self):
        email = self.fake.email(domain='example.com')
        assert email.split('@')[1] == 'example.com'

    @mock.patch(
        'faker.providers.internet.Provider.image_placeholder_services',
        {'https://dummyimage.com/{width}x{height}'},
    )
    def test_image_url(self):
        my_width = 500
        my_height = 1024
        url = self.fake.image_url(my_width, my_height)
        assert 'https://dummyimage.com/{}x{}'.format(my_width, my_height) == url
        url = self.fake.image_url()
        assert 'https://dummyimage.com/' in url

    def test_hostname(self):
        hostname_1_level = self.fake.hostname(levels=1)
        hostname_parts = hostname_1_level.split(".")
        assert hostname_1_level
        self.assertIsInstance(hostname_1_level, six.string_types)
        assert len(hostname_parts) == 3

        hostname_0_level = self.fake.hostname(levels=0)
        assert hostname_0_level
        self.assertIsInstance(hostname_0_level, six.string_types)


class TestInternetProviderUrl(unittest.TestCase):
    """ Test internet url generation """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    @staticmethod
    def is_correct_scheme(url, schemes):
        return any(url.startswith('{}://'.format(scheme)) for scheme in schemes)

    def test_url_default_schemes(self):
        for _ in range(100):
            url = self.fake.url()
            assert self.is_correct_scheme(url, ['http', 'https'])

    def test_url_custom_schemes(self):
        schemes_sets = [
            ['usb'],
            ['ftp', 'file'],
            ['usb', 'telnet', 'http'],
        ]
        for _, schemes in zip(range(100), cycle(schemes_sets)):
            url = self.fake.url(schemes=schemes)
            assert self.is_correct_scheme(url, schemes)

    def test_url_empty_schemes_list_generate_schemeless_urls(self):
        for _ in range(100):
            url = self.fake.url(schemes=[])
            assert not url.startswith('http')
            assert url.startswith('://')


class TestJaJP(unittest.TestCase):
    """ Tests internet in the ja_JP locale """

    def setUp(self):
        self.fake = Faker('ja')
        Faker.seed(0)

    def test_internet(self):
        names = JaProvider.last_romanized_names

        domain_word = self.fake.domain_word()
        self.assertIsInstance(domain_word, six.string_types)
        assert any(domain_word == text.slugify(name) for name in names)

        domain_name = self.fake.domain_name()
        deep_domain_name = self.fake.domain_name(3)
        self.assertIsInstance(domain_name, six.string_types)
        self.assertIsInstance(deep_domain_name, six.string_types)
        assert deep_domain_name.count('.') == 3
        with pytest.raises(ValueError):
            self.fake.domain_name(-1)

        user_name = self.fake.user_name()
        self.assertIsInstance(user_name, six.string_types)

        tld = self.fake.tld()
        self.assertIsInstance(tld, six.string_types)


class TestZhCN(unittest.TestCase):

    def setUp(self):
        self.fake = Faker(locale='zh_CN')
        Faker.seed(0)

    def test_email(self):
        email = self.fake.email()
        validate_email(email)

    def test_domain_word(self):
        domain_word = self.fake.domain_word()
        assert len(domain_word) > 1

    @mock.patch(
        'faker.providers.internet.Provider.tld',
        lambda x: 'cn',
    )
    def test_domain_name(self):
        domain_name_1_level = self.fake.domain_name(levels=1)
        domain_parts = domain_name_1_level.split(".")
        assert len(domain_parts) == 2
        assert domain_parts[-1] == 'cn'
        domain_name_2_level = self.fake.domain_name(levels=2)
        domain_parts = domain_name_2_level.split(".")
        assert len(domain_parts) == 3
        assert domain_parts[-1] == 'cn'
        assert domain_parts[1] in ['ac', 'com', 'edu', 'gov', 'mil',
                                   'net', 'org', 'ah', 'bj', 'cq',
                                   'fj', 'gd', 'gs', 'gz', 'gx', 'ha',
                                   'hb', 'he', 'hi', 'hk', 'hl', 'hn',
                                   'jl', 'js', 'jx', 'ln', 'mo', 'nm',
                                   'nx', 'qh', 'sc', 'sd', 'sh', 'sn',
                                   'sx', 'tj', 'xj', 'xz', 'yn', 'zj']


class TestZhTW(unittest.TestCase):

    def setUp(self):
        self.fake = Faker(locale='zh_TW')
        Faker.seed(0)

    def test_email(self):
        email = self.fake.email()
        validate_email(email)


class TestHuHU(unittest.TestCase):
    """ Tests internet module in the hu_HU locale. """

    def setUp(self):
        self.fake = Faker('hu_HU')
        Faker.seed(0)

    def test_internet(self):
        domain_name = self.fake.domain_name()
        self.assertIsInstance(domain_name, six.string_types)
        tld = self.fake.tld()
        self.assertIsInstance(tld, six.string_types)
        email = self.fake.email()
        self.assertIsInstance(email, six.string_types)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pl_PL')
        Faker.seed(0)
        self.provider = self.fake.provider('faker.providers.internet')

    def test_free_email_domain(self):
        domain = self.fake.free_email_domain()
        assert domain in self.provider.free_email_domains

    def test_tld(self):
        tld = self.fake.tld()
        assert tld in self.provider.tlds


class TestNlNl(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('nl_NL')
        Faker.seed(0)

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_safe_email(self):
        email = self.fake.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_free_email(self):
        email = self.fake.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_company_email(self):
        email = self.fake.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'


class TestArAa(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('ar_AA')
        Faker.seed(0)

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_safe_email(self):
        email = self.fake.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_free_email(self):
        email = self.fake.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_company_email(self):
        email = self.fake.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'


class TestPtBR(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pt_BR')
        Faker.seed(0)

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'VitóriaMagalhães',
    )
    def test_ascii_safe_email(self):
        email = self.fake.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'vitoriamagalhaes'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'JoãoSimões',
    )
    def test_ascii_free_email(self):
        email = self.fake.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'joaosimoes'

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'AndréCauã',
    )
    def test_ascii_company_email(self):
        email = self.fake.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'andrecaua'


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker('en_PH')
        Faker.seed(0)

    def test_PH_domain_name(self):
        for i in range(self.num_sample_runs):
            domain = self.fake.domain_name()
            validate_domain(domain)


class TestFilPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('fil_PH')
        Faker.seed(0)


class TestTlPh(TestFilPh):

    def setup_faker(self):
        self.fake = Faker('tl_PH')
        Faker.seed(0)
