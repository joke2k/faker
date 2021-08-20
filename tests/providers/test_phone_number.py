import re

from faker.providers.phone_number import Provider as PhoneNumberProvider
from faker.providers.phone_number.en_PH import Provider as EnPhPhoneNumberProvider


class TestPhoneNumber:
    """Test phone number provider methods"""

    def test_country_calling_code(self, faker, num_samples):
        for _ in range(num_samples):
            cc = faker.country_calling_code()
            assert cc in PhoneNumberProvider.country_calling_codes

    def test_msisdn(self, faker, num_samples):
        for _ in range(num_samples):
            msisdn = faker.msisdn()
            assert isinstance(msisdn, str)
            assert len(msisdn) == 13
            assert msisdn.isdigit()


class TestJaJp:
    """Test ja_JP phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        for _ in range(num_samples):
            pattern = re.compile(r'(?:0[789]0|\d{2})-\d{4}-\d{4}')
            phone_number = faker.phone_number()
            assert pattern.fullmatch(phone_number)


class TestPtBr:
    """Test pt_BR phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            r'(?:\+55 )?'
            r'(?:[1-8]1|84|\((?:0[1-8]1|084)\))'
            r' \d{4}[ -]\d{4}|'
            r'\d{4}?[ -]\d{3}[ -]\d{4}',
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert pattern.fullmatch(phone_number)

    def test_msisdn(self, faker, num_samples):
        pattern = re.compile(r'55(?:[1-8]19|849)\d{8}')
        for _ in range(num_samples):
            msisdn = faker.msisdn()
            assert pattern.fullmatch(msisdn)

    def test_cellphone(self, faker, num_samples):
        pattern = re.compile(
            r'(?:\+55 )?'
            r'(?:\d{2}|\(0?\d{2}\))'
            r' 9 ?\d{4}[ -]\d{4}',
        )
        for _ in range(num_samples):
            cellphone = faker.cellphone_number()
            assert pattern.fullmatch(cellphone)

    def test_service_phone(self, faker, num_samples):
        pattern = re.compile(r'1(?:0|2|5|8|9)?(?:[0-9])')
        for _ in range(num_samples):
            service = faker.service_phone_number()
            assert pattern.fullmatch(service)


class TestHuHu:
    """Test hu_HU phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            r'(?:'
            r'\+36 \d{2} |'
            r'\(06\)\d{2}/|'
            r'\(\d{2}\)/|'
            r'\d{2}/|'
            r'06-\d{1,2}/'
            r')\d{3}[- ]\d{4}',
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert isinstance(phone_number, str)
            assert pattern.fullmatch(phone_number)


class TestThTh:
    """Test th_TH phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            # leading zero or internaional code
            r'((\+66)|\+66[ -]?\(0\)|0)[ -]?'
            # landline or mobile
            r'([23457][ -]?(\d[ -]?){6}\d|[689][ -]?(\d[ -]?){7}\d)'
            # extension
            r'([ ]?(x|ext|ต่อ)[\.]?[ ]?\d{1,5})?',
            re.IGNORECASE,
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert isinstance(phone_number, str)
            assert pattern.fullmatch(phone_number)


class TestHyAm:
    """Test hy_AM phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            r'(?:[23]\d{2}-|\([23]\d{2}\) |[23]\d{2}\.)\d{5}|'
            r'(?:(?:10|9\d)-|\((?:10|9\d)\) |(?:10|9\d)\.)\d{6}',
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert isinstance(phone_number, str)
            assert pattern.fullmatch(phone_number)


class TestEnPh:
    """Test en_PH phone number provider methods"""

    @classmethod
    def setup_class(cls):
        cls.mobile_number_pattern = re.compile(r'^(?:0|\+63)(\d+)-\d{3}-\d{4}$')
        cls.area2_landline_number_pattern = re.compile(r'^(?:0|\+63)2-(\d{4})-\d{4}')
        cls.non_area2_landline_number_pattern = re.compile(r'^(?:0|\+63)(\d{2})-(\d{3})-\d{4}')
        cls.globe_mobile_number_prefixes = EnPhPhoneNumberProvider.globe_mobile_number_prefixes
        cls.smart_mobile_number_prefixes = EnPhPhoneNumberProvider.smart_mobile_number_prefixes
        cls.sun_mobile_number_prefixes = EnPhPhoneNumberProvider.sun_mobile_number_prefixes
        cls.mobile_number_prefixes = (
            cls.globe_mobile_number_prefixes + cls.smart_mobile_number_prefixes + cls.sun_mobile_number_prefixes
        )
        cls.bayantel_landline_identifiers = EnPhPhoneNumberProvider.bayantel_landline_identifiers
        cls.misc_landline_identifiers = EnPhPhoneNumberProvider.misc_landline_identifiers
        cls.non_area2_landline_area_codes = EnPhPhoneNumberProvider.non_area2_landline_area_codes

    def test_globe_mobile_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.globe_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.globe_mobile_number_prefixes

    def test_smart_mobile_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.smart_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.smart_mobile_number_prefixes

    def test_sun_mobile_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.sun_mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.sun_mobile_number_prefixes

    def test_mobile_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.mobile_number()
            match = self.mobile_number_pattern.match(number)
            assert match and match.group(1) in self.mobile_number_prefixes

    def test_globe_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.globe_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1).startswith('7')

    def test_pldt_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.pldt_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1).startswith('8')

    def test_bayantel_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.bayantel_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.bayantel_landline_identifiers

    def test_misc_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.misc_area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.misc_landline_identifiers

    def test_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.area2_landline_number()
            match = self.area2_landline_number_pattern.match(number)
            assert match and any([
                match.group(1).startswith('7'),
                match.group(1).startswith('8'),
                match.group(1) in self.bayantel_landline_identifiers,
                match.group(1) in self.misc_landline_identifiers,
            ])

    def test_non_area2_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.non_area2_landline_number()
            match = self.non_area2_landline_number_pattern.match(number)
            assert match and match.group(1) in self.non_area2_landline_area_codes

    def test_landline_number(self, faker, num_samples):
        for _ in range(num_samples):
            number = faker.landline_number()
            area2_match = self.area2_landline_number_pattern.match(number)
            non_area2_match = self.non_area2_landline_number_pattern.match(number)
            assert area2_match or non_area2_match
            if area2_match:
                assert any([
                    area2_match.group(1).startswith('7'),
                    area2_match.group(1).startswith('8'),
                    area2_match.group(1) in self.bayantel_landline_identifiers,
                    area2_match.group(1) in self.misc_landline_identifiers,
                ])
            elif non_area2_match:
                assert non_area2_match.group(1) in self.non_area2_landline_area_codes


class TestFilPh(TestEnPh):
    """Test fil_PH phone number provider methods"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH phone number provider methods"""
    pass


class TestTaIn:
    """Test ta_IN phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            r'\+91 \d{3} ?\d{7}|'
            r'0\d{2}(-)?\d{2}(?(1)| ?)\d{6}',
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert pattern.fullmatch(phone_number)


class TestEsEs:
    """Test es_ES phone number provider methods"""

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            r'\+34 ?(?:7[0-4]|[689]\d)\d'
            r'(?: \d{3} \d{3}|\d{6}| \d{2} \d{2} \d{2})',
        )
        for _ in range(num_samples):
            phone_number = faker.phone_number()
            assert pattern.fullmatch(phone_number)


class TestArAe:
    """Test ar_AE phone number provider methods"""

    cellphone_pattern = (
        r'(?:\+|00)971\s?5[024568]\s?\d{3}\s?\d{4}|'
        r'05[024568]\s?\d{3}\s?\d{4}'
    )
    telephone_pattern = (
        r'(?:\+|00)971\s?[1234679]\s?\d{3}\s?\d{4}|'
        r'0[1234679]\s?\d{3}\s?\d{4}'
    )
    toll_pattern = (
        r'200\d{4}|'
        r'600\d{6}|'
        r'800\d{3,7}'
    )
    service_phone_pattern = (
        r'9(?:9(?:9|8|7|6|1)|01|22)'
    )

    def test_cellphone_number(self, faker, num_samples):
        pattern = re.compile(self.cellphone_pattern)
        for _ in range(num_samples):
            cellphone = faker.cellphone_number()
            assert pattern.fullmatch(cellphone)

    def test_telephone_number(self, faker, num_samples):
        pattern = re.compile(self.telephone_pattern)
        for _ in range(num_samples):
            telephone = faker.telephone_number()
            assert pattern.fullmatch(telephone)

    def test_toll_number(self, faker, num_samples):
        pattern = re.compile(self.toll_pattern)
        for _ in range(num_samples):
            toll = faker.toll_number()
            assert pattern.fullmatch(toll)

    def test_service_phone_number(self, faker, num_samples):
        pattern = re.compile(self.service_phone_pattern)
        for _ in range(num_samples):
            service = faker.service_phone_number()
            assert pattern.fullmatch(service)

    def test_phone_number(self, faker, num_samples):
        pattern = re.compile(
            rf'{self.cellphone_pattern}|'
            rf'{self.telephone_pattern}|'
            rf'{self.toll_pattern}|'
            rf'{self.service_phone_pattern}',
        )
        for _ in range(num_samples):
            phone = faker.phone_number()
            assert pattern.fullmatch(phone)
