from enum import Enum, auto

import pytest

from faker.providers.python import EmptyEnumException


class _TestEnumWithNoElements(Enum):
    pass


class _TestEnumWithSingleElement(Enum):
    Single = auto


class _TestEnum(Enum):
    A = auto
    B = auto
    C = auto


class TestEnumProvider:
    num_samples = 100

    def test_enum(self, faker, num_samples):
        # (1/3) ** 100 ~ 1.94e-48 probability of this test failing because a specific
        # value was not sampled
        for _ in range(num_samples):
            actual = faker.enum(_TestEnum)
            assert actual in (_TestEnum.A, _TestEnum.B, _TestEnum.C)

    def test_enum_single(self, faker):
        assert faker.enum(_TestEnumWithSingleElement) == _TestEnumWithSingleElement.Single
        assert faker.enum(_TestEnumWithSingleElement) == _TestEnumWithSingleElement.Single

    def test_empty_enum_raises(self, faker):
        with pytest.raises(
            EmptyEnumException,
            match="The provided Enum: '_TestEnumWithNoElements' has no members.",
        ):
            faker.enum(_TestEnumWithNoElements)

    def test_none_raises(self, faker):
        with pytest.raises(ValueError):
            faker.enum(None)

    def test_incorrect_type_raises(self, faker):
        not_an_enum_type = str
        with pytest.raises(TypeError):
            faker.enum(not_an_enum_type)
