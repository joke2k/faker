import logging

import pytest

from faker import Faker
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE
from faker.exceptions import UniquenessException

LOGGER = logging.getLogger(__name__)


class TestUniquenessClass:
    def test_uniqueness(self):
        fake = Faker("en_US")

        names = set()
        # There are (at time of writing 690) first names in the
        # US identity provider. Birthday paradox puts the chances of
        # no duplicates in 250 selections as low enough to be impossible
        for i in range(250):
            first_name = fake.unique.first_name()
            assert first_name not in names
            names.add(first_name)

    def test_sanity_escape(self):
        fake = Faker()

        # Those of you who are especially astute may realise
        # there are only 2 booleans, so the third boolean cannot
        # be unique.
        with pytest.raises(UniquenessException, match=r"Got duplicated values after [\d,]+ iterations."):
            for i in range(3):
                _ = fake.unique.boolean()

    def test_uniqueness_clear(self):
        fake = Faker()

        for i in range(2):
            fake.unique.boolean()

        fake.unique.clear()

        # Because we cleared the generated values, this will not
        # throw an exception
        fake.unique.boolean()

    def test_exclusive_arguments(self):
        """Calls through the "unique" portal will only affect
        calls with that specific function signature.
        """
        fake = Faker()

        for i in range(10):
            fake.unique.random_int(min=1, max=10)

        # Different signature, so new pool. If they shared a pool
        # this would throw a sanity exception
        fake.unique.random_int(min=2, max=10)

    def test_accessing_non_function(self):
        """Accessing non-functions through the `.unique` attribute
        is allowed."""

        fake = Faker()

        assert fake.unique.locales == [DEFAULT_LOCALE]

    def test_complex_return_types_is_supported(self):
        """The unique decorator supports complex return types
        like the ones used in the profile provider."""

        fake = Faker()

        for i in range(10):
            fake.unique.pydict()

        for i in range(10):
            fake.unique.pylist()

        for i in range(10):
            fake.unique.pyset()

    def test_unique_locale_access(self):
        """Accessing locales through UniqueProxy with subscript notation
        maintains global uniqueness across all locales."""

        fake = Faker(["en_US", "fr_FR", "ja_JP"])
        generated = set()

        for i in range(5):
            value = fake.unique["en_US"].random_int(min=1, max=10)
            assert value not in generated
            generated.add(value)

        for i in range(5):
            value = fake.unique["fr_FR"].random_int(min=1, max=10)
            assert value not in generated
            generated.add(value)

        with pytest.raises(UniquenessException, match=r"Got duplicated values after [\d,]+ iterations."):
            fake.unique["ja_JP"].random_int(min=1, max=10)

    def test_preferred_uniqueness(self, caplog):
        fake = Faker()

        with caplog.at_level(logging.WARNING):
            for i in range(3):
                _ = fake.preferred_unique.boolean()
        assert (
            'There seem to be no more unique values for generator "boolean". '
            "Resetting store of generated values as uniqueness is not being enforced."
        ) in caplog.text

    def test_current_values_exempt_from_unique_check(self):
        fake = Faker()

        country_first_attempt = fake.unique.current_country()
        assert country_first_attempt == fake.unique.current_country()

    def test_initial_current_values_with_multiple_locales_are_unique(self):
        fake = Faker(AVAILABLE_LOCALES)

        all_country_codes_with_locales = {Faker(locale).current_country_code() for locale in AVAILABLE_LOCALES}
        generated_country_codes = {fake.unique.current_country_code() for _ in range(len(AVAILABLE_LOCALES))}

        assert all_country_codes_with_locales == generated_country_codes

    def test_current_values_start_repeating_after_locales_exhausted(self):
        fake = Faker({"en_US": 1, "fr_FR": 2}, use_weighting=True)

        locale_count = len(fake.locales)
        generated_countries = {fake.unique.current_country() for _ in range(locale_count)}
        assert len(generated_countries) == locale_count
        assert fake.unique.current_country() in generated_countries

    def test_none_values_exempt_from_unique_check(self):
        fake = Faker()

        for _ in range(2):
            assert fake.unique.seed_locale("en_US", 0) is None
