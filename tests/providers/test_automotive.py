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
        assert self.format.match(plate)

class TestHuHU(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_hu_HU_plate_format(self):
        plate = self.factory.license_plate()

        assert re.match("[A-Z]{3}-\d{3}", plate)

class TestDeDe(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('de_DE')

    def test_de_DE_plate_format(self):
        plate = self.factory.license_plate()

        assert re.match("[A-Z]{1,3}-[A-Z]{1,2}-\d{1,4}", plate)
