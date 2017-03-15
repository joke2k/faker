from __future__ import unicode_literals

import unittest

from faker import Factory
from .. import string_types


class NeNPFactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('ne_NP')
        
    def test_address(self):
        from faker.providers.address.ne_NP import Provider
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in Provider.countries

        district = self.factory.district()
        assert isinstance(district, string_types)
        assert district in Provider.districts

        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in Provider.cities

    def test_names(self):
        from faker.providers.person.ne_NP import Provider
        for _ in range(10000):
            name = self.factory.name().split()
            assert all(isinstance(n, string_types) for n in name)
            # name should always be 2-3 words. If 3, first word
            # should be a prefix.
            assert name[-2] in Provider.first_names
            assert name[-1] in Provider.last_names
            prefixes = Provider.prefixes_male + Provider.prefixes_female
            if len(name) == 3:
                assert name[0] in prefixes
