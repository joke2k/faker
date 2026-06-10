import pytest


class TestPaAFLocale:

    # ---------------- PERSON ----------------
    def test_person(self, faker):
        value = faker.name()
        assert isinstance(value, str)

        value = faker.first_name()
        assert isinstance(value, str)

        value = faker.last_name()
        assert isinstance(value, str)

        value = faker.prefix()
        assert isinstance(value, str)

        value = faker.suffix()
        assert isinstance(value, str)

    # ---------------- ADDRESS ----------------
    def test_address(self, faker):
        assert isinstance(faker.city(), str)
        assert isinstance(faker.street_name(), str)
        assert isinstance(faker.street_address(), str)
        assert isinstance(faker.postcode(), str)
        assert isinstance(faker.state(), str)
        assert isinstance(faker.country(), str)

    # ---------------- PHONE ----------------
    def test_phone_number(self, faker):
        assert isinstance(faker.phone_number(), str)


    # ---------------- CREDIT CARD ----------------
    def test_credit_card(self, faker):
        assert isinstance(faker.credit_card_number(), str)
        assert isinstance(faker.credit_card_expire(), str)
        assert isinstance(faker.credit_card_provider(), str)

    # ---------------- BARCODE ----------------
    def test_barcode(self, faker):
        assert isinstance(faker.ean13(), str)
        assert isinstance(faker.upc_a(), str)

    # ---------------- COLOR ----------------
    def test_color(self, faker):
        assert isinstance(faker.color_name(), str)
        assert isinstance(faker.color(), str)

    # ---------------- COMPANY ----------------
    def test_company(self, faker):
        assert isinstance(faker.company(), str)

    # ---------------- CURRENCY ----------------
    def test_currency(self, faker):
        assert isinstance(faker.currency_code(), str)
        assert isinstance(faker.currency_name(), str)

    # ---------------- DATE TIME ----------------
    def test_date_time(self, faker):
        assert faker.date_time() is not None
        assert isinstance(faker.day_of_week(), str)
        assert isinstance(faker.month_name(), str)

    # ---------------- GEO ----------------
    def test_geo(self, faker):
        latlng = faker.local_latlng()
        assert isinstance(latlng, (list, tuple))
        assert len(latlng) == 3

        assert faker.local_latitude()
        assert faker.local_longitude()

    # ---------------- INTERNET ----------------
    def test_internet(self, faker):
        assert isinstance(faker.domain_name(), str)
        assert isinstance(faker.email(), str)
        assert isinstance(faker.url(), str)
        assert isinstance(faker.ipv4(), str)
        assert isinstance(faker.ipv6(), str)

    # ---------------- ISBN ----------------
    def test_isbn(self, faker):
        assert isinstance(faker.isbn10(), str)
        assert isinstance(faker.isbn13(), str)

    # ---------------- JOB ----------------
    def test_job(self, faker):
        assert isinstance(faker.job(), str)

    # ---------------- LOREM ----------------
    def test_lorem(self, faker):
        assert isinstance(faker.word(), str)
        assert isinstance(faker.words(), list)
        assert isinstance(faker.sentence(), str)
        assert isinstance(faker.paragraph(), str)

    # ---------------- PHONE (duplicate removed style) ----------------
    def test_phone(self, faker):
        assert isinstance(faker.phone_number(), str)

    # # ---------------- SSN (AFGHAN ID) ----------------
    # def test_afghan_id(self, faker):
    #     value = faker.afghan_id(separator="-")
    #     assert isinstance(value, str)
    #     assert "-" in value
    #     assert len(value.replace("-", "")) > 0