"""TEST NOTES:

The following tests cover cases where a ``faker_session_locale`` fixture was not
defined by the user, but an autouse ``faker_locale`` fixture was defined. In this
setup, the plugin's session level ``Faker`` instance will not be used, and each
test will instead generate a new instance using the value of ``faker_locale``.
These new instances will be still seeded in accordance to the plugin's seeding
rules.
"""

from random import Random

import pytest

from faker.contrib.pytest.plugin import DEFAULT_SEED

_CHANGED_LOCALE = ['it_IT']


@pytest.fixture(autouse=True)
def faker_locale():
    return _CHANGED_LOCALE


@pytest.fixture()
def faker_seed():
    return 4761


def test_no_injection(_session_faker, faker):
    random = Random(DEFAULT_SEED)
    assert faker != _session_faker
    assert faker.locales == _CHANGED_LOCALE
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()


def test_inject_faker_seed(_session_faker, faker, faker_seed):
    random = Random(faker_seed)
    assert faker != _session_faker
    assert faker.locales == _CHANGED_LOCALE
    assert faker.random != random
    assert faker.random.getstate() == random.getstate()
