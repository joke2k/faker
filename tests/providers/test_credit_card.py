import re

from faker.providers.bank.ru_RU import Provider as RuRuBankProvider
from faker.providers.credit_card import Provider as CreditCardProvider


class TestCreditCardProvider:
    """Test credit card provider methods"""
    mastercard_pattern = re.compile(
        r'(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}',
    )
    visa_pattern = re.compile(r'4[0-9]{12}([0-9]{3}){0,2}')
    discover_pattern = re.compile(r'6(?:011|5[0-9]{2})[0-9]{12}')
    diners_club_pattern = re.compile(r'3(?:0[0-5]|[68][0-9])[0-9]{11}')
    jcb_pattern = re.compile(r'(?:2131|1800|35\d{3})\d{11}')

    def test_mastercard(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_mastercard:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 16)
                assert len(number) == 16
                assert self.mastercard_pattern.fullmatch(number)

    def test_visa13(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_visa:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 13)
                assert len(number) == 13
                assert self.visa_pattern.fullmatch(number)

    def test_visa16(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_visa:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 16)
                assert len(number) == 16
                assert self.visa_pattern.fullmatch(number)

    def test_visa19(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_visa:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 19)
                assert len(number) == 19
                assert self.visa_pattern.fullmatch(number)

    def test_discover(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_discover:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 16)
                assert len(number) == 16
                assert self.discover_pattern.fullmatch(number)

    def test_diners_club(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_diners:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 14)
                assert len(number) == 14
                assert self.diners_club_pattern.fullmatch(number)

    def test_jcb16(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_jcb16:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 16)
                assert len(number) == 16
                assert self.jcb_pattern.fullmatch(number)

    def test_jcb15(self, faker, num_samples):
        provider = CreditCardProvider(faker)
        for prefix in provider.prefix_jcb15:
            for _ in range(num_samples):
                number = provider._generate_number(prefix, 15)
                assert len(number) == 15
                assert self.jcb_pattern.fullmatch(number)


class TestRuRu:
    """Test ru_RU credit card provider methods"""
    visa_pattern = re.compile(r'4[0-9]{15}')
    mastercard_pattern = re.compile(
        r'(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}',
    )
    mir_pattern = re.compile(r'220[0-4][0-9]{12}')
    maestro_pattern = re.compile(r'(?:50|5[6-9]|6[0-9])[0-9]{14}')
    amex_pattern = re.compile(r'3[4|7][0-9]{13}')
    unionpay_pattern = re.compile(r'(?:62|81)[0-9]{14}')

    def test_visa(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('visa')
            assert self.visa_pattern.fullmatch(number)

    def test_mastercard(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('mastercard')
            assert self.mastercard_pattern.fullmatch(number)

    def test_mir(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('mir')
            assert self.mir_pattern.fullmatch(number)

    def test_maestro(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('maestro')
            assert self.maestro_pattern.fullmatch(number)

    def test_amex(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('amex')
            assert self.amex_pattern.fullmatch(number)

    def test_unionpay(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('unionpay')
            assert self.unionpay_pattern.fullmatch(number)

    def test_credit_card_full(self, faker, num_samples):
        for _ in range(num_samples):
            card_data = faker.credit_card_full().split('\n')
            assert re.match('[A-Za-z]+', card_data[1])
            assert card_data[4] in RuRuBankProvider.banks


class TestPtPt:
    """Test pt_PT credit card provider methods"""

    visa_pattern = re.compile(r'4[0-9]{15}')
    mastercard_pattern = re.compile(r'5[1-5][0-9]{14}')
    maestro_pattern = re.compile(r'(50|67)[0-9]{14}')

    def test_visa(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('visa')
            assert self.visa_pattern.fullmatch(number)

    def test_mastercard(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('mastercard')
            assert self.mastercard_pattern.fullmatch(number)

    def test_maestro(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.credit_card_number('maestro')
            assert self.maestro_pattern.fullmatch(number)
