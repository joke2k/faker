import pytest

from faker.generator import Generator


@pytest.fixture(scope="session")
def faker_locale():
    return "it_IT"


def test_faker(faker, faker_locale):
    """Test faker fixture."""
    assert isinstance(faker, Generator)
    assert faker.name() != faker.name()
    assert faker.name()
    assert faker_locale == "it_IT"
    assert faker.providers[0].__lang__ == faker_locale
