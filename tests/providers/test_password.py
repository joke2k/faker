import string

import pytest

from faker import Faker
from faker.providers.password import Provider as PasswordProvider

SYMBOLS = set("!@#$%^&*()-_=+[]{};:,.?/")
AMBIGUOUS = set("O0oIl1|`'\"")


def make_fake(seed=0):
    fake = Faker()
    fake.add_provider(PasswordProvider)
    fake.seed_instance(seed)
    return fake


def counts_by_class(password: str):
    up = sum(1 for c in password if c in string.ascii_uppercase)
    low = sum(1 for c in password if c in string.ascii_lowercase)
    dig = sum(1 for c in password if c in string.digits)
    sym = sum(1 for c in password if c in SYMBOLS)
    return up, low, dig, sym


def test_basic_constraints():
    """Ensures password meets length and all minimum counts."""
    fake = make_fake(42)
    password = fake.strong_password(length=20, min_upper=2, min_lower=3, min_digits=4, min_symbols=5)
    assert len(password) == 20
    up, low, dig, sym = counts_by_class(password)
    assert up >= 2 and low >= 3 and dig >= 4 and sym >= 5


def test_no_ambiguous_by_default():
    """Verifies ambiguous characters are excluded by default."""
    fake = make_fake(1)
    password = fake.strong_password(length=64)
    # Should exclude ambiguous characters unless allow_ambiguous=True
    assert not (set(password) & AMBIGUOUS)


def test_minimums_cannot_exceed_length():
    """Confirms error when sum of minimums exceeds total length."""
    fake = make_fake(0)
    with pytest.raises(ValueError):
        fake.strong_password(length=3, min_upper=1, min_lower=1, min_digits=1, min_symbols=1)


def test_minimums_must_be_nonnegative():
    """Confirms error when any minimum is negative."""
    fake = make_fake(0)
    with pytest.raises(ValueError):
        fake.strong_password(length=10, min_upper=-1)


def test_reproducible_with_seed():
    """Checks deterministic output when using the same seed."""
    f1 = make_fake(123)
    f2 = make_fake(123)
    password1 = f1.strong_password()
    password2 = f2.strong_password()
    assert password1 == password2


def test_exact_sum_of_minimums_only():
    """When length == sum(minimums), output must be exactly the required counts."""
    fake = make_fake(77)
    password = fake.strong_password(length=10, min_upper=2, min_lower=3, min_digits=4, min_symbols=1)
    assert len(password) == 10
    assert counts_by_class(password) == (2, 3, 4, 1)


def test_zero_symbol_requirement_is_allowed():
    """Ensure no symbols appear when min_symbols=0 and length == sum of others."""
    fake = make_fake(78)
    password = fake.strong_password(length=12, min_upper=4, min_lower=4, min_digits=4, min_symbols=0)
    up, low, dig, sym = counts_by_class(password)
    assert len(password) == 12
    assert sym == 0


def test_only_digits_when_min_digits_equals_length():
    """If digits minimum equals length, password should be all digits (with ambiguous digits excluded by default)."""
    fake = make_fake(79)
    password = fake.strong_password(length=8, min_upper=0, min_lower=0, min_digits=8, min_symbols=0)
    assert len(password) == 8
    # Ambiguous digits 0 and 1 should be excluded by default
    assert set(password).issubset(set("23456789"))


def test_no_whitespace_anywhere():
    """Ensures no whitespace characters."""
    fake = make_fake(80)
    password = fake.strong_password(length=48)
    assert not any(char.isspace() for char in password)
