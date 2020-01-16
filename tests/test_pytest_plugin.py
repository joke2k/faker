from faker import Faker


def test_faker(faker, faker_locale, faker_seed):
    """Test faker fixture."""
    assert isinstance(faker, Faker)
    assert faker.name() != faker.name()
    assert faker.name()
    assert faker_locale is None
    assert faker_seed is None
