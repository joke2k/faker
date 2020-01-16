import pytest

from faker import Factory


@pytest.fixture(scope="session")
def faker_locale():
    """Faker locale.
    None by default which means faker's default locale.
    """
    return None


@pytest.fixture(scope="session")
def faker(faker_locale):
    """Faker factory object."""
    return Factory.create(faker_locale)
