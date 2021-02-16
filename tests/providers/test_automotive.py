import re

from faker.providers.automotive.de_DE import Provider as DeDeAutomotiveProvider
from faker.providers.automotive.es_ES import Provider as EsEsAutomotiveProvider
from faker.providers.automotive.ru_RU import Provider as RuRuAutomotiveProvider
from faker.providers.automotive.sk_SK import Provider as SkSkAutomotiveProvider
from faker.providers.automotive.tr_TR import Provider as TrTrAutomotiveProvider


class _SimpleAutomotiveTestMixin:
    """Use this test mixin for simple license plate validation"""

    def perform_extra_checks(self, license_plate, match):
        pass

    def test_license_plate(self, faker, num_samples):
        for _ in range(num_samples):
            license_plate = faker.license_plate()
            match = self.license_plate_pattern.fullmatch(license_plate)
            assert match
            self.perform_extra_checks(license_plate, match)


class TestSkSk(_SimpleAutomotiveTestMixin):
    """Test sk_SK automotive provider methods"""
    license_plate_pattern = re.compile(r'(?P<prefix>[A-Z]{2})\d{3}[A-Z]{2}')

    def perform_extra_checks(self, license_plate, match):
        assert match.group('prefix') in SkSkAutomotiveProvider.license_plate_prefix


class TestPtBr(_SimpleAutomotiveTestMixin):
    """Test pt_BR automotive provider methods"""
    license_plate_pattern = re.compile(r'[A-Z]{3}-\d{4}')


class TestPtPt(_SimpleAutomotiveTestMixin):
    """Test pt_PT automotive provider methods"""
    license_plate_pattern = re.compile(
        r'\d{2}-\d{2}-[A-Z]{2}|'
        r'\d{2}-[A-Z]{2}-\d{2}|'
        r'[A-Z]{2}-\d{2}-\d{2}|'
        r'[A-Z]{2}-\d{2}-[A-Z]{2}',
    )


class TestHuHu(_SimpleAutomotiveTestMixin):
    """Test hu_HU automotive provider methods"""
    license_plate_pattern = re.compile(r'[A-Z]{3}-\d{3}')


class TestDeDe(_SimpleAutomotiveTestMixin):
    """Test de_DE automotive provider methods"""
    license_plate_pattern = re.compile(
        r'(?P<prefix>[A-Z\u00D6\u00DC]{1,3})-[A-Z]{1,2}-[1-9]{1,4}',
        re.UNICODE,
    )

    def perform_extra_checks(self, license_plate, match):
        assert match.group('prefix') in DeDeAutomotiveProvider.license_plate_prefix


class TestSvSe(_SimpleAutomotiveTestMixin):
    """Test sv_SE automotive provider methods"""
    license_plate_pattern = re.compile(r'[A-Z]{3} \d{2}[\dA-Z]')


class TestPlPl:

    def test_License_plate(self, faker, num_samples):
        pattern = re.compile(r'{patterns}'.format(patterns='|'.join(faker.license_plate_regex_formats())))
        for _ in range(num_samples):
            plate = faker.license_plate()
            assert pattern.fullmatch(plate)


class TestEnPh(_SimpleAutomotiveTestMixin):
    """Test en_PH automotive provider methods"""
    license_plate_pattern = re.compile(r'[A-Z]{2}\d{4,5}|[A-Z]{3}\d{3,4}')
    motorcycle_pattern = re.compile(r'[A-Z]{2}\d{4,5}')
    automobile_pattern = re.compile(r'[A-Z]{3}\d{3,4}')

    def test_motorcycle_plate(self, faker, num_samples):
        for _ in range(num_samples):
            assert self.motorcycle_pattern.match(faker.motorcycle_license_plate())

    def test_automobile_plate(self, faker, num_samples):
        for _ in range(num_samples):
            assert self.automobile_pattern.match(faker.automobile_license_plate())

    def test_protocol_plate(self, faker, num_samples):
        for _ in range(num_samples):
            protocol_plate = faker.protocol_license_plate()
            assert int(protocol_plate) != 15 and 1 <= int(protocol_plate) <= 17


class TestFilPh(TestEnPh):
    """Test fil_PH automotive provider methods"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH automotive provider methods"""
    pass


class TestRuRu(_SimpleAutomotiveTestMixin):
    """Test ru_RU automotive provider methods"""
    _plate_letters = ''.join(RuRuAutomotiveProvider.license_plate_letters)
    license_plate_pattern = re.compile(
        r'(?:'
        r'(?P<private_plate_prefix>[{0}]\d\d\d[{0}][{0}])|'
        r'(?P<public_transport_plate_prefix>[{0}][{0}]\d\d\d)|'
        r'(?P<trailer_plate_prefix>[{0}][{0}]\d\d\d\d)|'
        r'(?P<police_plate_prefix>[{0}]\d\d\d\d)|'
        r'(?P<military_plate_prefix>\d\d\d\d[{0}][{0}])|'
        r'(?P<plate_number_special>00\dCD\d|00\dD\d\d\d|00\dT\d\d\d)'
        r') (?P<plate_suffix>.*)'.format(_plate_letters),
    )

    def perform_extra_checks(self, license_plate, match):
        plate_suffix = match.group('plate_suffix')
        assert plate_suffix in RuRuAutomotiveProvider.license_plate_suffix

    def test_vehicle_category(self, faker, num_samples):
        for _ in range(num_samples):
            vehicle_category = faker.vehicle_category()
            assert isinstance(vehicle_category, str)
            assert vehicle_category in RuRuAutomotiveProvider.vehicle_categories


class TestFrFr(_SimpleAutomotiveTestMixin):
    """Test fr_FR automotive provider methods"""
    license_plate_pattern = re.compile(r'\d{3}-[A-Z]{3}-\d{2}|[A-Z]{2}-\d{3}-[A-Z]{2}')


class TestNoNo(_SimpleAutomotiveTestMixin):
    """Test no_NO automotive provider methods"""
    license_plate_pattern = re.compile(r'[A-Z]{2} \d{5}')


class TestEsEs:
    """Test es_ES automotive provider methods"""
    new_format_pattern = re.compile(r'\d{4}\s[A-Z]{3}')
    old_format_pattern = re.compile(r'(?P<province_prefix>[A-Z]{1,2})\s\d{4}\s[A-Z]{2}')

    def test_plate_new_format(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate_unified()
            assert isinstance(plate, str)
            assert self.new_format_pattern.match(plate)

    def test_plate_old_format(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate_by_province()
            assert isinstance(plate, str)
            match = self.old_format_pattern.match(plate)
            assert match
            assert match.group('province_prefix') in EsEsAutomotiveProvider.province_prefix

    def test_plate_old_format_explicit_province_prefix(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate_by_province(province_prefix="CA")
            assert isinstance(plate, str)
            assert self.old_format_pattern.match(plate)
            assert plate[:2] == "CA"

    def test_plate_format(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate()
            assert isinstance(plate, str)
            assert self.new_format_pattern.match(plate) or self.old_format_pattern.match(plate)


class TestThTh(_SimpleAutomotiveTestMixin):
    """Test th_TH automotive provider methods"""
    license_plate_pattern = re.compile(
        r'(\d [ก-ฮ]{2} \d{1,4})|'  # car
        r'([ก-ฮ]{2} \d{1,4})|'  # car
        r'([ก-ฮ]{3} \d{1,3})|'  # motorcycle
        r'(\d{2}-\d{4})',  # truck
        )


class TestTrTr(_SimpleAutomotiveTestMixin):
    """Test tr_TR automotive provider methods"""
    license_plate_pattern = re.compile(
        r'\d{2} [A-Z] \d{4}|'
        r'\d{2} [A-Z] \d{5}|'
        r'\d{2} [A-Z]{2} \d{3}|'
        r'\d{2} [A-Z]{2} \d{4}|'
        r'\d{2} [A-Z]{3} \d{2}|'
        r'\d{2} [A-Z]{3} \d{3}',
    )

    def perform_extra_checks(self, license_plate, match):
        [city_code, letters, _] = license_plate.split(' ')
        assert int(city_code) in range(1, 82)
        assert all(letter in TrTrAutomotiveProvider.ascii_uppercase_turkish for letter in letters)
