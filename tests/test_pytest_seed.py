import pytest

from faker import Faker


@pytest.fixture()
def faker_seed():
    return 0


def test_faker_seed_instance(faker):
    assert isinstance(faker, Faker)
    assert faker.name()
    compare = Faker()
    compare.seed_instance(0)
    compare.name() == faker.name()
