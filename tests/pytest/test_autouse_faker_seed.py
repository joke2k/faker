"""TEST NOTES:

The following tests cover cases where a ``faker_session_locale`` fixture was not
defined by the user, but an autouse ``faker_seed`` fixture was defined. In this
setup, the plugin's ``DEFAULT_SEED`` will be ignored, and ``Faker`` instances will
be seeded using the value of ``faker_seed``. Said instances are still chosen in
accordance to how ``faker_locale`` and ``faker_session_locale`` interact with
each other.
"""

from random import Random

import pytest

from faker.contrib.pytest.plugin import DEFAULT_LOCALE

_CHANGED_SEED = 4761


@pytest.fixture()
def faker_locale():
    return ['it_IT']


@pytest.fixture(autouse=True)
def faker_seed():
    return _CHANGED_SEED


def test_no_injection(_session_faker, faker):
    random = Random(_CHANGED_SEED)
    assert faker == _session_faker
    assert faker.locales == [DEFAULT_LOCALE]
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()


def test_inject_faker_locale(_session_faker, faker, faker_locale):
    random = Random(_CHANGED_SEED)
    assert faker != _session_faker
    assert faker.locales == faker_locale
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()
