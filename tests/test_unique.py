import pytest

from faker import Faker
from faker.exceptions import UniquenessException


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

    def test_functions_only(self):
        """Accessing non-functions through the `.unique` attribute
        will throw a TypeError."""

        fake = Faker()

        with pytest.raises(TypeError, match="Accessing non-functions through .unique is not supported."):
            fake.unique.locales

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

    def test_unique_locale_clear(self):
        """Clearing either the root UniqueProxy or a locale-scoped UniqueProxy
        clears the shared seen state and keeps them synchronized."""

        fake = Faker(["en_US", "fr_FR"])

        # Clearing via a locale-scoped proxy clears the shared state
        assert fake.unique["en_US"].random_int(min=1, max=1) == 1
        fake.unique["en_US"].clear()
        assert fake.unique["en_US"].random_int(min=1, max=1) == 1

        # Shared state remains synchronized across locales after clear()
        with pytest.raises(UniquenessException):
            fake.unique["fr_FR"].random_int(min=1, max=1)

        # Clearing via the root proxy also clears held locale-scoped proxies
        en_unique = fake.unique["en_US"]
        fake.unique.clear()
        assert en_unique.random_int(min=1, max=1) == 1
        with pytest.raises(UniquenessException):
            fake.unique.random_int(min=1, max=1)
