# coding=utf-8

import re
import unittest

from faker import Faker

class TestNoNO(unittest.TestCase):
    """ Tests the bban in no_NO locale """

    def setUp(self):
        self.factory = Faker('no_NO')

    def test_bban(self):
        bban = self.factory.bban()
        assert re.match("\d{11}", bban)
