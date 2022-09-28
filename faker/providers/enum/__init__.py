from enum import Enum
from typing import TypeVar, Type, List, Iterable, cast


from .. import BaseProvider
from ...exceptions import BaseFakerException

localized = False

TEnum = TypeVar("TEnum", bound=Enum)


class EmptyEnumException(BaseFakerException):
    pass


class Provider(BaseProvider):
    """
    Implements a Provider for Enum types.
    """

    def enum(self, enum_cls: Type[TEnum]) -> TEnum:
        """
        Returns a random enum of the provided input `Enum` type.

        :param enum_cls: The `Enum` type to produce the value for.
        :returns: A randomly selected enum value.
        """

        if enum_cls is None:
            raise ValueError("'enum_cls' cannot be None")

        if not issubclass(enum_cls, Enum):
            raise TypeError(f"'enum_cls' must be an Enum type")

        members: List[TEnum] = list(cast(Iterable[TEnum], enum_cls))

        if len(members) < 1:
            raise EmptyEnumException(
                f"The provided Enum: '{enum_cls.__name__}' has no members."
            )

        return self.random_element(members)
