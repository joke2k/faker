import re
import unittest

from faker import Faker
from faker.providers.bank.ru_RU import Provider as RuBank


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


class TestRuRu(unittest.TestCase):
    """ Tests credit card in the ru_RU locale """

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)
        self.visa_pattern = r'^4[0-9]{15}$'
        self.mastercard_pattern = r'^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'
        self.mir_pattern = r'^220[0-4][0-9]{12}$'
        self.maestro_pattern = r'^50|5[6-9]|6[0-9][0-9]{14}$'
        self.amex_pattern = r'^3[4|7][0-9]{13}$'
        self.unionpay_pattern = r'^62|81[0-9]{14}$'

    def test_visa(self):
        number = self.fake.credit_card_number('visa')
        assert re.match(self.visa_pattern, number)

    def test_mastercard(self):
        number = self.fake.credit_card_number('mastercard')
        assert re.match(self.mastercard_pattern, number)

    def test_mir(self):
        number = self.fake.credit_card_number('mir')
        assert re.match(self.mir_pattern, number)

    def test_maestro(self):
        number = self.fake.credit_card_number('maestro')
        assert re.match(self.maestro_pattern, number)

    def test_amex(self):
        number = self.fake.credit_card_number('amex')
        assert re.match(self.amex_pattern, number)

    def test_unionpay(self):
        number = self.fake.credit_card_number('unionpay')
        assert re.match(self.unionpay_pattern, number)

    def test_owner(self):
        card_data = self.fake.credit_card_full().split('\n')
        assert re.match('[A-Za-z]+', card_data[1])

    def test_issuer(self):
        card_data = self.fake.credit_card_full().split('\n')
        assert card_data[4] in RuBank.banks
