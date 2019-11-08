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
        assert re.match(r"\d{11}", bban)


class TestFiFi(unittest.TestCase):
    """ Tests the iban in fi_FI locale """

    def setUp(self):
        self.factory = Faker('fi_FI')

    def test_bban(self):
        bban = self.factory.bban()
        assert re.match(r"\d{16}", bban)

    def test_iban(self):
        iban = self.factory.iban()
        assert re.match(r"FI\d{16}", iban)


class TestPlPL(unittest.TestCase):
    """Tests the bank provider for pl_PL locale"""

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_bban(self):
        bban = self.factory.bban()
        assert re.match(r"\d{26}", bban)

    def test_iban(self):
        iban = self.factory.iban()
        assert re.match(r"PL\d{26}", iban)


class TestEnGB(unittest.TestCase):
    """Tests the bank provider for en_GB locale"""

    def setUp(self):
        self.factory = Faker('en_GB')

    def test_bban(self):
        bban = self.factory.bban()
        assert re.match(r"[A-Z]{4}\d{14}", bban)

    def test_iban(self):
        iban = self.factory.iban()
        assert re.match(r"GB\d{2}[A-Z]{4}\d{14}", iban)
