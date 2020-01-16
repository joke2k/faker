import pytest

from faker import Faker


@pytest.fixture()
def faker_seed():
    """Faker seed.
    None by default which means faker's default random seed.
    """
    return None


@pytest.fixture()
def faker_locale():
    """Faker locale.
    None by default which means faker's default locale.
    """
    return None


@pytest.fixture()
def faker(faker_locale, faker_seed):
    """Faker factory object."""
    faker = Faker(faker_locale)
    if faker_seed is not None:
        faker.seed_instance(faker_seed)
    return faker
