# coding=utf-8

import re
import unittest

import faker
from faker.providers import credit_card


class MastercardGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.base_provider = credit_card.Provider(faker.generator.Generator())
        self.factory = faker.Faker(locale='en_US')
        self.pattern = r'^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'

    def test_mastercard(self):
        prefix_all = ['51', '52', '53', '54', '55', '222%', '223', '224', '225',
                      '226', '227', '228', '229', '23', '24', '25', '26', '270',
                      '271', '2720']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 16)
            assert re.match(self.pattern, number)


class VisaGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.base_provider = credit_card.Provider(faker.generator.Generator())
        self.factory = faker.Faker(locale='en_US')
        self.pattern = r'^4[0-9]{12}([0-9]{3}){0,2}$'

    def test_visa13(self):
        prefix_all = ['4']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 13)
            assert re.match(self.pattern, number)

    def test_visa16(self):
        prefix_all = ['4']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 16)
            assert re.match(self.pattern, number)

    def test_visa19(self):
        prefix_all = ['4']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 19)
            assert re.match(self.pattern, number)


class DiscoverGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.base_provider = credit_card.Provider(faker.generator.Generator())
        self.factory = faker.Faker(locale='en_US')
        self.pattern = r'^6(?:011|5[0-9]{2})[0-9]{12}$'

    def test_discover(self):
        prefix_all = ['6011', '65']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 16)
            assert re.match(self.pattern, number)


class DinersClubGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.base_provider = credit_card.Provider(faker.generator.Generator())
        self.factory = faker.Faker(locale='en_US')
        self.pattern = r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'

    def test_diners_club(self):
        prefix_all = ['300', '301', '302', '303', '304', '305', '36', '38']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 14)
            assert re.match(self.pattern, number)


class JCBGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.base_provider = credit_card.Provider(faker.generator.Generator())
        self.factory = faker.Faker(locale='en_US')
        self.pattern = r'^(?:2131|1800|35\d{3})\d{11}$'

    def test_jcb16(self):
        prefix_all = ['35']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 16)
            assert re.match(self.pattern, number)

    def test_jcb15(self):
        prefix_all = ['2131', '1800']
        for prefix in prefix_all:
            number = credit_card.Provider._generate_number(self.base_provider, prefix, 15)
            assert re.match(self.pattern, number)
