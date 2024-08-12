import re

from typing import Pattern

from faker.providers.automotive import calculate_vin_str_weight
from faker.providers.automotive.de_DE import Provider as DeDeAutomotiveProvider
from faker.providers.automotive.es_ES import Provider as EsEsAutomotiveProvider
from faker.providers.automotive.ro_RO import Provider as RoRoAutomotiveProvider
from faker.providers.automotive.ru_RU import Provider as RuRuAutomotiveProvider
from faker.providers.automotive.sk_SK import Provider as SkSkAutomotiveProvider
from faker.providers.automotive.tr_TR import Provider as TrTrAutomotiveProvider
from faker.providers.automotive.uk_UA import Provider as UkUaAutomotiveProvider


class _SimpleAutomotiveTestMixin:
    """Use this test mixin for simple license plate validation"""

    def perform_extra_checks(self, license_plate, match):
        pass

    def test_license_plate(self, faker, num_samples):
        for _ in range(num_samples):
            license_plate = faker.license_plate()
            match = self.license_plate_pattern.fullmatch(license_plate)
            assert match is not None
            self.perform_extra_checks(license_plate, match)

    def test_vin(self, faker, num_samples):
        for _ in range(num_samples):
            vin_number = faker.vin()
            # length check: 17
            assert len(vin_number) == 17

            # verify checksum: vin_number[8]
            front_part_weight = calculate_vin_str_weight(vin_number[:8], [8, 7, 6, 5, 4, 3, 2, 10])
            rear_part_weight = calculate_vin_str_weight(vin_number[9:], [9, 8, 7, 6, 5, 4, 3, 2])
            checksum = (front_part_weight + rear_part_weight) % 11
            checksum_str = "X" if checksum == 10 else str(checksum)
            assert vin_number[8] == checksum_str


class TestArBh(_SimpleAutomotiveTestMixin):
    """Test ar_BH automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"\d{6}")


class TestAzAz(_SimpleAutomotiveTestMixin):
    """Test az_AZ automotive provider methods"""

    license_plate_pattern = re.compile(r"\d{2}-[A-Z]{2}-\d{3}")


class TestSkSk(_SimpleAutomotiveTestMixin):
    """Test sk_SK automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"(?P<prefix>[A-Z]{2})\d{3}[A-Z]{2}")

    def perform_extra_checks(self, license_plate, match):
        assert match.group("prefix") in SkSkAutomotiveProvider.license_plate_prefix


class TestPtBr(_SimpleAutomotiveTestMixin):
    """Test pt_BR automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{3}-\d{1}[A-Z]{1}\d{2}")


class TestPtPt(_SimpleAutomotiveTestMixin):
    """Test pt_PT automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(
        r"\d{2}-\d{2}-[A-Z]{2}|" r"\d{2}-[A-Z]{2}-\d{2}|" r"[A-Z]{2}-\d{2}-\d{2}|" r"[A-Z]{2}-\d{2}-[A-Z]{2}",
    )


class TestHeIl(_SimpleAutomotiveTestMixin):
    license_plate_pattern: Pattern = re.compile(r"(\d{3}-\d{2}-\d{3})|(\d{2}-\d{3}-\d{2})")


class TestHuHu(_SimpleAutomotiveTestMixin):
    """Test hu_HU automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{3}-\d{3}")


class TestDeDe(_SimpleAutomotiveTestMixin):
    """Test de_DE automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(
        r"(?P<prefix>[A-Z\u00D6\u00DC]{1,3})-[A-Z]{1,2}-[1-9]{1,4}",
        re.UNICODE,
    )

    def perform_extra_checks(self, license_plate, match):
        assert match.group("prefix") in DeDeAutomotiveProvider.license_plate_prefix


class TestSvSe(_SimpleAutomotiveTestMixin):
    """Test sv_SE automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{3} \d{2}[\dA-Z]")


class TestPlPl:
    def test_License_plate(self, faker, num_samples):
        pattern: Pattern = re.compile(r"{patterns}".format(patterns="|".join(faker.license_plate_regex_formats())))
        for _ in range(num_samples):
            plate = faker.license_plate()
            assert pattern.fullmatch(plate)


class TestEnPh(_SimpleAutomotiveTestMixin):
    """Test en_PH automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2}\d{4,5}|[A-Z]{3}\d{3,4}")
    motorcycle_pattern: Pattern = re.compile(r"[A-Z]{2}\d{4,5}")
    automobile_pattern: Pattern = re.compile(r"[A-Z]{3}\d{3,4}")

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

    _plate_letters = "".join(RuRuAutomotiveProvider.license_plate_letters)
    license_plate_pattern: Pattern = re.compile(
        r"(?:"
        r"(?P<private_plate_prefix>[{0}]\d\d\d[{0}][{0}])|"
        r"(?P<public_transport_plate_prefix>[{0}][{0}]\d\d\d)|"
        r"(?P<trailer_plate_prefix>[{0}][{0}]\d\d\d\d)|"
        r"(?P<police_plate_prefix>[{0}]\d\d\d\d)|"
        r"(?P<military_plate_prefix>\d\d\d\d[{0}][{0}])|"
        r"(?P<plate_number_special>00\dCD\d|00\dD\d\d\d|00\dT\d\d\d)"
        r") (?P<plate_suffix>.*)".format(_plate_letters),
    )

    def perform_extra_checks(self, license_plate, match):
        plate_suffix = match.group("plate_suffix")
        assert plate_suffix in RuRuAutomotiveProvider.license_plate_suffix

    def test_vehicle_category(self, faker, num_samples):
        for _ in range(num_samples):
            vehicle_category = faker.vehicle_category()
            assert isinstance(vehicle_category, str)
            assert vehicle_category in RuRuAutomotiveProvider.vehicle_categories


class TestFrFr(_SimpleAutomotiveTestMixin):
    """Test fr_FR automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"\d{3}-[A-Z]{3}-\d{2}|[A-Z]{2}-\d{3}-[A-Z]{2}")


class TestItIt(_SimpleAutomotiveTestMixin):
    """Test it_IT automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2}\d{3}[A-Z]{2}")


class TestNoNo(_SimpleAutomotiveTestMixin):
    """Test no_NO automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2} \d{5}")


class TestEsCo(_SimpleAutomotiveTestMixin):
    """Test es_CO automotive provider methods"""

    license_plate_pattern = re.compile(r"[A-Z]{3}\d{3}|[A-Z]{3}\d{2}[A-Z]|T\d{4}|[A-Z]{2}\d{4}|R\d{5}|S\d{5}")


class TestEsEs:
    """Test es_ES automotive provider methods"""

    new_format_pattern: Pattern = re.compile(r"\d{4}\s[A-Z]{3}")
    old_format_pattern: Pattern = re.compile(r"(?P<province_prefix>[A-Z]{1,2})\s\d{4}\s[A-Z]{2}")

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
            assert match.group("province_prefix") in EsEsAutomotiveProvider.province_prefix

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

    license_plate_pattern: Pattern = re.compile(
        r"(\d [ก-ฮ]{2} \d{1,4})|"  # car
        r"([ก-ฮ]{2} \d{1,4})|"  # car
        r"([ก-ฮ]{3} \d{1,3})|"  # motorcycle
        r"(\d{2}-\d{4})",  # truck
    )


class TestTrTr(_SimpleAutomotiveTestMixin):
    """Test tr_TR automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(
        r"\d{2} [A-Z] \d{4}|"
        r"\d{2} [A-Z] \d{5}|"
        r"\d{2} [A-Z]{2} \d{3}|"
        r"\d{2} [A-Z]{2} \d{4}|"
        r"\d{2} [A-Z]{3} \d{2}|"
        r"\d{2} [A-Z]{3} \d{3}",
    )

    def perform_extra_checks(self, license_plate, match):
        [city_code, letters, _] = license_plate.split(" ")
        assert int(city_code) in range(1, 82)
        assert all(letter in TrTrAutomotiveProvider.ascii_uppercase_turkish for letter in letters)


class TestRoRo(_SimpleAutomotiveTestMixin):
    """Test ro_RO automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"(?P<prefix>[A-Z]{1,2})-\d{2,3}-[A-Z]{3}")

    def perform_extra_checks(self, license_plate, match):
        assert match.group("prefix") in RoRoAutomotiveProvider.license_plate_prefix


class TestElGr(_SimpleAutomotiveTestMixin):
    """Test el_GR automotive provider methods"""

    license_plate_pattern = re.compile(r"^(?P<prefix>[A-Z]{2,3}) \d{4}$")


class TestNlNl(_SimpleAutomotiveTestMixin):
    """Test nl_NL automotive provider methods"""

    license_plate_car_pattern = re.compile(
        r"\d{2}-[BDFGHJKLNPRSTVXZ][A-Z]-[A-Z]{2}|"
        r"\d{2}-[BDFGHJKLNPRSTVXZ][A-Z]{2}-\d|"
        r"\d-[KSTVXZ][A-Z]{2}-\d{2}|"
        r"[BDFGHJKLNPRSTVXZ][A-Z]-\d{3}-[A-Z]|"
        r"[BDFGHJKLNPRSTVXZ]-\d{3}-[A-Z]{2}",
    )

    license_plate_motorbike_pattern = re.compile(
        r"M[A-Z]-[A-Z]{2}-\d{2}|" r"\d{2}-M[A-Z]-[A-Z]{2}",
    )

    license_plate_pattern = re.compile(
        license_plate_car_pattern.pattern + "|" + license_plate_motorbike_pattern.pattern,
    )

    def test_plate_car(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate_car()
            assert isinstance(plate, str)
            assert self.license_plate_car_pattern.match(plate)

    def test_plate_motorbike(self, faker, num_samples):
        for _ in range(num_samples):
            plate = faker.license_plate_motorbike()
            assert isinstance(plate, str)
            assert self.license_plate_motorbike_pattern.match(plate)


class TestViVn(_SimpleAutomotiveTestMixin):
    """Test vi_VN automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"\d{2}[ABCDĐEFGHKLMNPSTUVXYZ]-\d{5}")


class TestFiFi(_SimpleAutomotiveTestMixin):
    """Test fi_FI automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{3}-\d{3}")


class TestSqAl(_SimpleAutomotiveTestMixin):
    """Test sq_AL automotive providers methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2} \d{3}[A-Z]{2}")


class TestDeCh(_SimpleAutomotiveTestMixin):
    """Test de_CH automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2}-\d{1,3}\s?\d{0,3}")


class TestNlBe(_SimpleAutomotiveTestMixin):
    """Test nl_BE automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(r"(\d{3}-[A-Z]{3})|" r"([A-Z]{3}-\d{3})|" r"([1-2]-[A-Z]{3}-\d{3})")


class TestZhCn(_SimpleAutomotiveTestMixin):
    """Test zh_CN automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(
        r"^[京津冀晋蒙辽吉黑沪苏浙皖闽赣鲁豫鄂湘粤桂琼川贵云渝藏陕甘青宁新]{1}[A-Z]{1}-[A-Z0-9]{5}"
    )


class TestZhTw(_SimpleAutomotiveTestMixin):
    """Test zh_TW automotive provider methods"""

    license_plate_pattern: Pattern = re.compile(
        r"([A-Z]{2}-\d{4})|"  # prior 2012 v1
        r"(\d{4}-[A-Z]{2})|"  # prior 2012 v2
        r"([A-Z]{3}-\d{4})|"  # new format since 2014
        r"([A-Z]{3}-\d{3})",  # commercial cars since 2012
    )


class TestUkUa(_SimpleAutomotiveTestMixin):
    license_plate_pattern: Pattern = re.compile(r"[A-Z]{2}\d{4}[A-Z]{2}")

    def perform_extra_checks(self, license_plate, match):
        assert license_plate[-2:] in UkUaAutomotiveProvider.license_plate_suffix

    def test_temporary_plate(self, faker, num_samples):
        pattern = r"\d{2} [A-Z]{2}\d{4}"

        for _ in range(num_samples):
            temporary = faker.license_plate(temporary_plate=True)
            match = re.search(pattern, temporary)
            assert match is not None

    def test_diplomatic_plate(self, faker, num_samples):
        pattern = r"(CDP \d{3})|(DP|S) \d{3} \d{3}"

        for _ in range(num_samples):
            temporary = faker.diplomatic_license_plate()
            match = re.search(pattern, temporary)
            assert match is not None

    def test_prefix(self, faker):
        for _ in range(10):
            temporary = faker.plate_letter_prefix(region_name="Lviv")
            assert len(temporary) == 2
            assert temporary in UkUaAutomotiveProvider.license_region_data.get("Lviv")[0]

    def test_region_code(self, faker):
        assert "14" == faker.plate_region_code(region_name="Lviv")
