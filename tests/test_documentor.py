import warnings

import pytest

from faker import Faker
from faker.documentor import Documentor

LOCALES_WITHOUT_BANK_NAMES = ["cs_CZ", "de_DE", "es_ES", "fr_FR"]


@pytest.mark.parametrize("locale", LOCALES_WITHOUT_BANK_NAMES)
def test_get_formatters_skips_not_implemented_providers(locale):
    fake = Faker(locale)
    doc = Documentor(fake)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        formatters = doc.get_formatters(locale=locale)

    assert formatters
    assert any("banks" in str(w.message) for w in caught)
