# coding=utf-8
from __future__ import unicode_literals

import re
import unittest

from faker import Faker
from six import string_types


class TestPtBR(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pt_BR')
        self.format = re.compile('[\w]{3}-[\d]{4}')

    def test_plate_has_been_generated(self):
        plate = self.factory.license_plate()
        assert isinstance(plate, string_types)
        assert self.format.match(plate)
