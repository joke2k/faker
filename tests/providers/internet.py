# coding=utf-8

from __future__ import unicode_literals

import unittest

from email_validator import validate_email

from faker import Factory
from faker.providers.person.ja_JP import Provider as JaProvider
from faker.utils import text
from .. import string_types


class TestJaJP(unittest.TestCase):
    """ Tests internet in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_internet(self):
        names = JaProvider.last_romanized_names

        domain_word = self.factory.domain_word()
        assert isinstance(domain_word, string_types)
        assert any(domain_word == text.slugify(name) for name in names)

        domain_name = self.factory.domain_name()
        deep_domain_name = self.factory.domain_name(3)
        assert isinstance(domain_name, string_types)
        assert isinstance(deep_domain_name, string_types)
        assert deep_domain_name.count('.') == 3
        self.assertRaises(ValueError, self.factory.domain_name, -1)

        user_name = self.factory.user_name()
        assert isinstance(user_name, string_types)

        tld = self.factory.tld()
        assert isinstance(tld, string_types)


class TestZhCN(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create(locale='zh_CN')

    def test_email(self):
        email = self.factory.email()
        validate_email(email, check_deliverability=False)


class testHuHU(unittest.TestCase):
    """ Tests internet module in the hu_HU locale. """

    def setUp(self):
        self.factory = Factory.create('hu')

    def test_internet(self):
        domain_name = self.factory.domain_name()
        assert isinstance(domain_name, string_types)
        tld = self.factory.tld()
        assert isinstance(tld, string_types)
        email = self.factory.email()
        assert isinstance(email, string_types)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('pl_PL')
        self.provider = self.factory.provider('faker.providers.internet')

    def test_free_email_domain(self):
        domain = self.factory.free_email_domain()
        assert domain in self.provider.free_email_domains

    def test_tld(self):
        tld = self.factory.tld()
        assert tld in self.provider.tlds
