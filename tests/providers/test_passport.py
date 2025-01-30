import re

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
