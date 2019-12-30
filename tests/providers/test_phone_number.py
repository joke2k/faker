# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

import six

from faker import Faker


class TestPhoneNumber(unittest.TestCase):
    """ Tests phone_number in the ja_JP locale """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_phone_number(self):
        pn = self.fake.phone_number()

        assert pn
        assert isinstance(pn, six.string_types)

    def test_msisdn(self):
        msisdn = self.fake.msisdn()

        assert msisdn is not None
        assert isinstance(msisdn, six.string_types)
        assert len(msisdn) == 13
        assert msisdn.isdigit()


class TestJa(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('ja')
        Faker.seed(0)

    def test_phone_number(self):
        pn = self.fake.phone_number()
        formats = ('070', '080', '090')

        assert pn
        assert isinstance(pn, six.string_types)
        first, second, third = pn.split('-')
        assert first
        assert first.isdigit()
        assert second
        assert second.isdigit()
        assert third
        assert third.isdigit()
        if len(first) == 2:
            assert len(second) == 4
            assert len(third) == 4
        else:
            assert len(first) == 3
            assert len(second) == 4
            assert len(third) == 4
            assert first in formats


class TestPtBr(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pt_br')
        Faker.seed(0)

    def test_msisdn(self):
        msisdn = self.fake.msisdn()
        formats = ('5511', '5521', '5531', '5541', '5551', '5561', '5571', '5581')

        assert msisdn is not None
        assert isinstance(msisdn, six.string_types)
        assert len(msisdn) == 13
        assert msisdn.isdigit()
        assert msisdn[0:4] in formats

    def test_cellphone(self):
        cellphone = self.fake.cellphone_number()
        assert cellphone is not None
        assert len(cellphone) == 14


class TestHuHU(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('hu_HU')
        Faker.seed(0)

    def test_phone_number(self):
        phone_number = self.fake.phone_number()
        re.match(r"[1-9]\d/\d{3} \d{4}", phone_number)


class TestThTH(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('th_TH')
        Faker.seed(0)

    def test_phone_number_should_be_in_defined_format(self):
        phone_number = self.fake.phone_number()

        first, second, third = phone_number.split(' ')

        formats = ('+66', '+668')
        self.assertTrue(first in formats)

        if len(first) == 3:
            self.assertEqual(first, '+66')
        elif len(first) == 4:
            self.assertEqual(first, '+668')

        self.assertEqual(len(second), 4)
        self.assertEqual(len(third), 4)


class TestHyAm(unittest.TestCase):
    """ Tests phone_number in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_phone_number(self):
        pn = self.fake.phone_number()
        assert isinstance(pn, six.string_types)


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.mobile_number_pattern = re.compile(r'^(?:0|\+63)(\d+)-\d{3}-\d{4}$')
        self.area2_landline_number_pattern = re.compile(r'^(?:0|\+63)2-(\d{4})-\d{4}')
        self.non_area2_landline_number_pattern = re.compile(r'^(?:0|\+63)(\d{2})-(\d{3})-\d{4}')
        self.setup_constants()
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker('en_PH')
        Faker.seed(0)

    def setup_constants(self):
        from faker.providers.phone_number.en_PH import Provider
        self.globe_mobile_number_prefixes = Provider.globe_mobile_number_prefixes
        self.smart_mobile_number_prefixes = Provider.smart_mobile_number_prefixes
        self.sun_mobile_number_prefixes = Provider.sun_mobile_number_prefixes
        self.mobile_number_prefixes = (
            self.globe_mobile_number_prefixes + self.smart_mobile_number_prefixes + self.sun_mobile_number_prefixes
        )
        self.bayantel_landline_identifiers = Provider.bayantel_landline_identifiers
        self.misc_landline_identifiers = Provider.misc_landline_identifiers
        self.non_area2_landline_area_codes = Provider.non_area2_landline_area_codes

    def test_PH_globe_mobile_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.globe_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.globe_mobile_number_prefixes

    def test_PH_smart_mobile_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.smart_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.smart_mobile_number_prefixes

    def test_PH_sun_mobile_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.sun_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.sun_mobile_number_prefixes

    def test_PH_mobile_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.mobile_number_prefixes

    def test_PH_globe_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.globe_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1).startswith('7')

    def test_PH_pldt_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.pldt_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1).startswith('8')

    def test_PH_bayantel_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.bayantel_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.bayantel_landline_identifiers

    def test_PH_misc_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.misc_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.misc_landline_identifiers

    def test_PH_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and any([
                match.group(1).startswith('7'),
                match.group(1).startswith('8'),
                match.group(1) in self.bayantel_landline_identifiers,
                match.group(1) in self.misc_landline_identifiers,
            ])

    def test_PH_non_area2_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.non_area2_landline_number()
            match = self.non_area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.non_area2_landline_area_codes

    def test_PH_landline_number(self):
        for i in range(self.num_sample_runs):
            number = self.fake.landline_number()
            area2_match = self.area2_landline_number_pattern.match(number)
            non_area2_match = self.non_area2_landline_number_pattern.match(number)
            assert area2_match or non_area2_match
            if area2_match:
                assert any([
                    area2_match.group(1).startswith('7'),
                    area2_match.group(1).startswith('8'),
                    area2_match.group(1) in self.bayantel_landline_identifiers,
                    area2_match.group(1) in self.misc_landline_identifiers,
                ])
            elif non_area2_match:
                assert non_area2_match.group(1) in self.non_area2_landline_area_codes


class TestFilPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('fil_PH')
        Faker.seed(0)


class TestTlPh(TestEnPh):

    def setup_faker(self):
        self.fake = Faker('tl_PH')
        Faker.seed(0)


class TestTaIN(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('ta_IN')
        Faker.seed(0)

    def test_phone_number(self):
        phone_number = self.fake.phone_number()
        re.match(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$", phone_number)
