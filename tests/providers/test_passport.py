import re
import pytest
from faker.providers.passport.it_IT import Provider as ItPassportProvider

from typing import Pattern


class TestPassport:
    """Test passport provider methods"""

    def test_passport_number(self, faker, num_samples):
        for _ in range(num_samples):
            passport_number = faker.passport_number()
            assert isinstance(passport_number, str)


class TestDeAt:
    """Test de_AT passport provider methods"""

    def test_passport_number(self, faker, num_samples):
        for _ in range(num_samples):

            pattern: Pattern = re.compile(r"[A-Z]{1,2}\d{7}")
            passport_number = faker.passport_number()
            assert pattern.fullmatch(passport_number)


@pytest.mark.parametrize("faker", ["it_IT"], indirect=True)
class TestItIT:
    """Test it_IT passport provider methods"""

    def test_passport_number(self, faker, num_samples):
        faker.add_provider(ItPassportProvider)

        pattern = re.compile(r"^[A-Z]{2}\d{7}$")

        for _ in range(num_samples):
            passport_number = faker.passport_number()
            assert pattern.fullmatch(passport_number)
