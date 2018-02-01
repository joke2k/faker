# coding=utf-8

from __future__ import unicode_literals

import unittest

import mock

from email_validator import validate_email

from faker import Faker
from faker.providers.person.ja_JP import Provider as JaProvider
from faker.utils import text
from tests import string_types


class TestInternetProvider(unittest.TestCase):
    """ Tests internet """

    def setUp(self):
        self.factory = Faker()

    def test_email(self):
        email = self.factory.email(domain='example.com')
        self.assertEqual(email.split('@')[1], 'example.com')


class TestInternetProviderUrl(unittest.TestCase):
    """ Test internet url generation """

    def setUp(self):
        self.factory = Faker()

    @staticmethod
    def is_http(url):
        return url.startswith('http://')

    @staticmethod
    def is_https(url):
        return url.startswith('https://')

    def test_url(self):
        urls = [self.factory.url() for i in range(100)]
        self.assertTrue(all(self.is_http(url) or self.is_https(url) for url in urls))

    def test_url_only_http(self):
        urls = [self.factory.url(exclude_scheme='https') for i in range(100)]
        self.assertTrue(all(self.is_http(url) for url in urls))

    def test_url_only_https(self):
        urls = [self.factory.url(exclude_scheme='http') for i in range(100)]
        self.assertTrue(all(self.is_https(url) for url in urls))

    def test_url_raises_error(self):
        with self.assertRaises(ValueError):
            self.factory.url(exclude_scheme=['http', 'https'])


class TestJaJP(unittest.TestCase):
    """ Tests internet in the ja_JP locale """

    def setUp(self):
        self.factory = Faker('ja')

    def test_internet(self):
        names = JaProvider.last_romanized_names

        domain_word = self.factory.domain_word()
        self.assertIsInstance(domain_word, string_types)
        self.assertTrue(any(domain_word == text.slugify(name) for name in names))

        domain_name = self.factory.domain_name()
        deep_domain_name = self.factory.domain_name(3)
        self.assertIsInstance(domain_name, string_types)
        self.assertIsInstance(deep_domain_name, string_types)
        self.assertEqual(deep_domain_name.count('.'), 3)
        self.assertRaises(ValueError, self.factory.domain_name, -1)

        user_name = self.factory.user_name()
        self.assertIsInstance(user_name, string_types)

        tld = self.factory.tld()
        self.assertIsInstance(tld, string_types)


class TestZhCN(unittest.TestCase):

    def setUp(self):
        self.factory = Faker(locale='zh_CN')

    def test_email(self):
        email = self.factory.email()
        validate_email(email, check_deliverability=False)


class TestZhTW(unittest.TestCase):

    def setUp(self):
        self.factory = Faker(locale='zh_TW')

    def test_email(self):
        email = self.factory.email()
        validate_email(email, check_deliverability=False)


class TestHuHU(unittest.TestCase):
    """ Tests internet module in the hu_HU locale. """

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_internet(self):
        domain_name = self.factory.domain_name()
        self.assertIsInstance(domain_name, string_types)
        tld = self.factory.tld()
        self.assertIsInstance(tld, string_types)
        email = self.factory.email()
        self.assertIsInstance(email, string_types)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pl_PL')
        self.provider = self.factory.provider('faker.providers.internet')

    def test_free_email_domain(self):
        domain = self.factory.free_email_domain()
        self.assertIn(domain, self.provider.free_email_domains)

    def test_tld(self):
        tld = self.factory.tld()
        self.assertIn(tld, self.provider.tlds)


class TestNlNl(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('nl_NL')
        self.provider = self.factory.provider('faker.providers.internet')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné'
    )
    def test_ascii_safe_email(self):
        email = self.factory.ascii_safe_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'fabienne')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné'
    )
    def test_ascii_free_email(self):
        email = self.factory.ascii_free_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'fabienne')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné'
    )
    def test_ascii_company_email(self):
        email = self.factory.ascii_company_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'fabienne')


class TestArAa(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('ar_AA')
        self.provider = self.factory.provider('faker.providers.internet')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل'
    )
    def test_ascii_safe_email(self):
        email = self.factory.ascii_safe_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'asyl')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل'
    )
    def test_ascii_free_email(self):
        email = self.factory.ascii_free_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'asyl')

    @mock.patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل'
    )
    def test_ascii_company_email(self):
        email = self.factory.ascii_company_email()
        validate_email(email, check_deliverability=False)
        self.assertEqual(email.split('@')[0], 'asyl')
