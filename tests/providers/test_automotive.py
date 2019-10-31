# coding=utf-8
from __future__ import unicode_literals

import re
import unittest

from faker import Faker
from six import string_types


class TestPtBR(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pt_BR')
        self.format = re.compile(r'[\w]{3}-[\d]{4}')

    def test_plate_has_been_generated(self):
        plate = self.factory.license_plate()
        assert isinstance(plate, string_types)
        assert self.format.match(plate), "%s is not in the correct format." % plate


class TestPtPT(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pt_PT')
        self.pattern = re.compile(r'^\d{2}-\d{2}-[aA-zZ]{2}$|^\d{2}-[aA-zZ]{2}-\d{2}$|^[aA-zZ]{2}-\d{2}-\d{2}$')

    def test_pt_PT_plate_format(self):
        plate = self.factory.license_plate()
        assert self.pattern.match(plate), "%s is not in the correct format." % plate


class TestHuHU(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_hu_HU_plate_format(self):
        plate = self.factory.license_plate()
        assert re.match(r"[A-Z]{3}-\d{3}", plate), "%s is not in the correct format." % plate


class TestDeDe(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('de_DE')

    def test_de_DE_plate_format(self):
        plate = self.factory.license_plate()
        assert re.match(r"[A-Z\u00D6\u00DC]{1,3}-[A-Z]{1,2}-\d{1,4}", plate, flags=re.UNICODE), \
            "%s is not in the correct format." % plate


class TestSvSE(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('sv_SE')

    def test_sv_SE_plate_format(self):
        plate = self.factory.license_plate()
        assert re.match(r"[A-Z]{3} \d{2}[\dA-Z]{1}", plate), "%s is not in the correct format." % plate


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_pl_PL_plate_format(self):
        plate = self.factory.license_plate()
        patterns = self.factory.license_plate_regex_formats()
        assert re.match(r'{patterns}'.format(patterns='|'.join(patterns)),
                        plate), '{plate} is not the correct format.'.format(plate=plate)


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.motorcycle_pattern = re.compile(r'^[A-Z]{2}\d{4,5}$')
        self.automobile_pattern = re.compile(r'^[A-Z]{3}\d{3,4}$')
        self.vehicle_pattern = re.compile(r'^(?:[A-Z]{2}\d{4,5}|[A-Z]{3}\d{3,4})$')
        self.setup_factory()

    def setup_factory(self):
        self.factory = Faker('en_PH')

    def test_PH_motorcycle_plate_format(self):
        for i in range(self.num_sample_runs):
            assert self.motorcycle_pattern.match(self.factory.motorcycle_license_plate())

    def test_PH_automobile_plate_format(self):
        for i in range(self.num_sample_runs):
            assert self.automobile_pattern.match(self.factory.automobile_license_plate())

    def test_PH_plate_format(self):
        for i in range(self.num_sample_runs):
            assert self.vehicle_pattern.match(self.factory.license_plate())

    def test_PH_protocol_plate_format(self):
        for i in range(self.num_sample_runs):
            assert int(self.factory.protocol_license_plate()) != 15


class TestFilPh(TestEnPh):

    def setup_factory(self):
        self.factory = Faker('fil_PH')


class TestTlPh(TestEnPh):

    def setup_factory(self):
        self.factory = Faker('tl_PH')
