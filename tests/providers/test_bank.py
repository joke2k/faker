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


class TestRuRU(unittest.TestCase):
    """Tests the bank provider for ru_RU locale"""

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"[A-Z]{4}\d{13}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"RU\d{2}[A-Z]{4}\d{13}", iban)

    def test_bic(self):
        bic = self.fake.bic()
        assert re.match(r"04\d{7,9}", bic)

    def test_correspondent_account(self):
        correspondent_account = self.fake.correspondent_account()
        assert re.match(r"301\d{17}", correspondent_account)

    def test_checking_account(self):
        checking_account = self.fake.checking_account()
        assert re.match(r"\d{3}0\d{16}", checking_account)

    def test_bank(self):
        bank = self.fake.bank()
        assert re.match(r"\D{3,41}", bank)


class TestPtPt(unittest.TestCase):
    """Tests the bank provider for pt_PT locale"""

    def setUp(self):
        self.fake = Faker('pt_PT')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"\d{21}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"PT\d{21}", iban)


class TestEsES(unittest.TestCase):
    """Tests the bank provider for es_ES locale"""

    def setUp(self):
        self.fake = Faker('es_ES')
        Faker.seed(0)

    def test_bban(self):
        bban = self.fake.bban()
        assert re.match(r"\d{20}", bban)

    def test_iban(self):
        iban = self.fake.iban()
        assert re.match(r"ES\d{22}", iban)
