import pytest

from faker import Faker


class TestOptionalClass:
    def test_optional(self) -> None:
        fake = Faker()
        Faker.seed(0)

        # 100 draws make it astronomically unlikely to miss any of the three
        # outcomes (True, False, None) even under worst-case probability splits.
        # 10 draws had a ~12% empirical failure rate (see GH-2366).
        values = {fake.optional.boolean() for _ in range(100)}
        assert values == {True, False, None}

    def test_optional_probability(self) -> None:
        """The probability is configurable."""
        fake = Faker()

        fake.optional.name(prob=0.1)

    def test_optional_arguments(self) -> None:
        """Other arguments are passed through to the function."""
        fake = Faker()

        fake.optional.pyint(1, 2, prob=0.4)

    def test_optional_valid_range(self) -> None:
        """Only probabilities in the range (0, 1]."""
        fake = Faker()

        with pytest.raises(ValueError, match=""):
            fake.optional.name(prob=0)

        with pytest.raises(ValueError, match=""):
            fake.optional.name(prob=1.1)

        with pytest.raises(ValueError, match=""):
            fake.optional.name(prob=-3)

    def test_functions_only(self):
        """Accessing non-functions through the `.optional` attribute
        will throw a TypeError."""

        fake = Faker()

        with pytest.raises(TypeError, match="Accessing non-functions through .optional is not supported."):
            fake.optional.locales
