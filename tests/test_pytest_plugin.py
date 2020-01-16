from faker.generator import Generator


def test_faker(faker, faker_locale):
    """Test faker fixture."""
    assert isinstance(faker, Generator)
    assert faker.name() != faker.name()
    assert faker.name()
    assert faker_locale is None
