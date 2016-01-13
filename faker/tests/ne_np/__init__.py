from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.utils import text
from .. import string_types


class ne_NP_FactoryTestCase(unittest.TestCase):
  
    def setUp(self):
      self.factory = Factory.create('ne_NP')
        
    def test_address(self):
      from faker.providers.address.ne_NP import Provider
      countries = Provider.countries
      country   = self.factory.country()
      assert country
      assert isinstance(country, string_types)
      assert country in countries
      
      districts = Provider.districts
      district  = self.factory.district()
      assert district
      assert isinstance(district, string_types)
      assert district in districts

      cities = Provider.cities
      city   = self.factory.city()
      assert city
      assert isinstance(city, string_types)
      assert city in cities
      
    def test_names(self):
      from faker.providers.person.ne_NP import Provider
      first_names = Provider.first_names
      name = self.factory.name()
      first_name, last_name = name.split()
      assert first_name
      assert isinstance(first_name, string_types)
      assert first_name in first_names
      
      last_names = Provider.last_names
      assert last_names
      assert isinstance(last_name, string_types)
      assert last_name in last_names
      
      
      