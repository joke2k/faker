"""TEST NOTES:

The following tests cover cases where a ``faker_session_locale`` fixture was not
defined by the user, but non-autouse ``faker_locale`` and ``faker_seed`` fixtures
were defined. The resulting behavior of the ``faker`` fixture will vary dependening
on which fixtures are injected.
"""


from random import Random

import pytest

from faker.contrib.pytest.plugin import DEFAULT_LOCALE, DEFAULT_SEED


@pytest.fixture()
def faker_locale():
    return ['it_IT']


@pytest.fixture()
def faker_seed():
    return 4761


def test_no_injection(_session_faker, faker):
    random = Random(DEFAULT_SEED)
    assert faker == _session_faker
    assert faker.locales == [DEFAULT_LOCALE]
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()


def test_inject_faker_locale(_session_faker, faker, faker_locale):
    random = Random(DEFAULT_SEED)
    assert faker != _session_faker
    assert faker.locales == faker_locale
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()


def test_inject_faker_seed(_session_faker, faker, faker_seed):
    random = Random(faker_seed)
    assert faker == _session_faker
    assert faker.locales == [DEFAULT_LOCALE]
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()


def test_inject_faker_seed_and_locale(_session_faker, faker, faker_locale, faker_seed):
    random = Random(faker_seed)
    assert faker != _session_faker
    assert faker.locales == faker_locale
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()
