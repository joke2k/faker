# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

import six

from faker import Faker


class TestPhoneNumber(unittest.TestCase):
    """ Tests phone_number in the ja_JP locale """

    def setUp(self):
        self.factory = Faker()

    def test_phone_number(self):
        pn = self.factory.phone_number()

        assert pn
        assert isinstance(pn, six.string_types)

    def test_phone_number_ja(self):
        factory = Faker('ja')
        pn = factory.phone_number()
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

    def test_msisdn(self):
        msisdn = self.factory.msisdn()

        assert msisdn is not None
        assert isinstance(msisdn, six.string_types)
        assert len(msisdn) == 13
        assert msisdn.isdigit()

    def test_msisdn_pt_br(self):
        factory = Faker('pt_br')
        msisdn = factory.msisdn()
        formats = ('5511', '5521', '5531', '5541', '5551', '5561', '5571', '5581')

        assert msisdn is not None
        assert isinstance(msisdn, six.string_types)
        assert len(msisdn) == 13
        assert msisdn.isdigit()
        assert msisdn[0:4] in formats

    def test_cellphone_pt_br(self):
        factory = Faker('pt_BR')
        cellphone = factory.cellphone_number()
        assert cellphone is not None
        assert len(cellphone) == 14


class TestHuHU(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_phone_number(self):
        phone_number = self.factory.phone_number()
        re.match(r"[1-9]\d/\d{3} \d{4}", phone_number)


class TestThTH(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('th_TH')

    def test_phone_number_should_be_in_defined_format(self):
        phone_number = self.factory.phone_number()

        first, second, third = phone_number.split(' ')

        formats = ('+66', '+668')
        self.assertTrue(first in formats)

        if len(first) == 3:
            self.assertEqual(first, '+66')
        elif len(first) == 4:
            self.assertEqual(first, '+668')

        self.assertEqual(len(second), 4)
        self.assertEqual(len(third), 4)
