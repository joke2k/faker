import pytest

from faker import Faker


@pytest.fixture()
def faker_locale():
    return "it_IT"


def test_faker_locale(faker, faker_locale):
    """Test faker fixture."""
    assert isinstance(faker, Faker)
    assert faker.name() != faker.name()
    assert faker.name()
    assert faker_locale == "it_IT"
    assert faker.providers[0].__lang__ == faker_locale
