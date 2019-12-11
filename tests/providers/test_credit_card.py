# coding=utf-8

import re
import unittest

from faker import Faker


class TestCreditCardProvider(unittest.TestCase):

    def setUp(self):
        self.fake = Faker(locale='en_US')
        Faker.seed(0)
        self.provider = self.fake.provider('faker.providers.credit_card')
        self.mastercard_pattern = r'^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'
        self.visa_pattern = r'^4[0-9]{12}([0-9]{3}){0,2}$'
        self.discover_pattern = r'^6(?:011|5[0-9]{2})[0-9]{12}$'
        self.diners_club_pattern = r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'
        self.jcb_pattern = r'^(?:2131|1800|35\d{3})\d{11}$'

    def test_mastercard(self):
        for prefix in self.provider.prefix_mastercard:
            number = self.provider._generate_number(prefix, 16)
            assert re.match(self.mastercard_pattern, number)

    def test_visa13(self):
        for prefix in self.provider.prefix_visa:
            number = self.provider._generate_number(prefix, 13)
            assert re.match(self.visa_pattern, number)

    def test_visa16(self):
        for prefix in self.provider.prefix_visa:
            number = self.provider._generate_number(prefix, 16)
            assert re.match(self.visa_pattern, number)

    def test_visa19(self):
        for prefix in self.provider.prefix_visa:
            number = self.provider._generate_number(prefix, 19)
            assert re.match(self.visa_pattern, number)

    def test_discover(self):
        for prefix in self.provider.prefix_discover:
            number = self.provider._generate_number(prefix, 16)
            assert re.match(self.discover_pattern, number)

    def test_diners_club(self):
        for prefix in self.provider.prefix_diners:
            number = self.provider._generate_number(prefix, 14)
            assert re.match(self.diners_club_pattern, number)

    def test_jcb16(self):
        for prefix in self.provider.prefix_jcb16:
            number = self.provider._generate_number(prefix, 16)
            assert re.match(self.jcb_pattern, number)

    def test_jcb15(self):
        for prefix in self.provider.prefix_jcb15:
            number = self.provider._generate_number(prefix, 15)
            assert re.match(self.jcb_pattern, number)
