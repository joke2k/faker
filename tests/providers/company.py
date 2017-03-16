# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Factory
from faker.providers.company.ja_JP import Provider as JaProvider
from .. import string_types


class TestJaJP(unittest.TestCase):
    """ Tests companies in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_company(self):
        prefixes = JaProvider.company_prefixes

        prefix = self.factory.company_prefix()
        assert isinstance(prefix, string_types)
        assert prefix in prefixes

        company = self.factory.company()
        assert isinstance(company, string_types)
        assert any(prefix in company for prefix in prefixes)
        assert any(company.startswith(prefix) for prefix in prefixes)
