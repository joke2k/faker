# coding=utf-8

import re
import unittest

from faker import Faker


class TestNoNO(unittest.TestCase):
    """ Tests the bban in no_NO locale """

    def setUp(self):
        self.fake = Faker('no_NO')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"\d{11}", bban)


class TestFiFi(unittest.TestCase):
    """ Tests the iban in fi_FI locale """

    def setUp(self):
        self.fake = Faker('fi_FI')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"\d{16}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"FI\d{16}", iban)


class TestPlPL(unittest.TestCase):
    """Tests the bank provider for pl_PL locale"""

    def setUp(self):
        self.fake = Faker('pl_PL')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"\d{26}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"PL\d{26}", iban)


class TestEnGB(unittest.TestCase):
    """Tests the bank provider for en_GB locale"""

    def setUp(self):
        self.fake = Faker('en_GB')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"[A-Z]{4}\d{14}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"GB\d{2}[A-Z]{4}\d{14}", iban)
