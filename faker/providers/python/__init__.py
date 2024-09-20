import math
import string
import sys
import warnings

from decimal import Decimal
from enum import Enum
from typing import Any, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Type, TypeVar, Union, cast, no_type_check

from faker.typing import BasicNumber

from ...exceptions import BaseFakerException
from .. import BaseProvider, ElementsType

TypesNames = List[str]
TypesSpec = Union[List[Type], Tuple[Type, ...]]
TEnum = TypeVar("TEnum", bound=Enum)


class EmptyEnumException(BaseFakerException):
    pass


class Provider(BaseProvider):
    default_value_types: ElementsType[str] = (
        "str",
        "str",
        "str",
        "str",
        "float",
        "int",
        "int",
        "decimal",
        "date_time",
        "uri",
        "email",
    )

    def _check_signature(self, value_types: Optional[TypesSpec], allowed_types: Optional[TypesSpec]) -> TypesSpec:
        if value_types is not None and not isinstance(value_types, (list, tuple)):
            value_types = (value_types,)
            warnings.warn(
                "Passing `value_types` as positional arguments is going to be "
                "deprecated.  Pass them as a list or tuple instead.",
                PendingDeprecationWarning,
            )
        if allowed_types is not None and not isinstance(allowed_types, (list, tuple)):
            allowed_types = (allowed_types,)
            warnings.warn(
                "Passing `allowed_types` as positional arguments is going to be "
                "deprecated.  Pass them as a list or tuple instead.",
                PendingDeprecationWarning,
            )
        if value_types is None:
            value_types = ()
        if allowed_types is None:
            allowed_types = ()
        return tuple(value_types) + tuple(allowed_types)

    def pyobject(
        self,
        object_type: Optional[Type[Union[bool, str, float, int, tuple, set, list, Iterable, dict]]] = None,
    ) -> Optional[Union[bool, str, float, int, tuple, set, list, Iterable, dict]]:
        """
        Generates a random object passing the type desired.

        :object_type: the type of the object to generate.
        :return: the random object generated.
        :raises ValueError: if the object type passed is not supported
        """
        if object_type is None:
            return None
        elif object_type == bool:
            return self.pybool()
        elif object_type == str:
            return self.pystr()
        elif object_type == float:
            return self.pyfloat()
        elif object_type == int:
            return self.pyint()
        elif object_type == tuple:
            return self.pytuple()
        elif object_type == set:
            return self.pyset()
        elif object_type == list:
            return self.pylist()
        elif object_type == Iterable:
            return self.pyiterable()
        elif object_type == dict:
            return self.pydict()
        else:
            raise ValueError(f"Object type `{object_type}` is not supported by `pyobject` function")

    def pybool(self, truth_probability: int = 50) -> bool:
        """
        Generates a random boolean, optionally biased towards `True` or `False`.

        :truth_probability: Probability of generating a `True` value. Must be between `0` and `100` inclusive'.
        :return: Random boolean.
        :raises ValueError: If invalid `truth_probability` is provided.
        """
        if truth_probability < 0 or truth_probability > 100:
            raise ValueError("Invalid `truth_probability` value: must be between `0` and `100` inclusive")

        return self.random_int(1, 100) <= truth_probability

    def pystr(
        self,
        min_chars: Optional[int] = None,
        max_chars: int = 20,
        prefix: str = "",
        suffix: str = "",
    ) -> str:
        """
        Generates a random string of upper and lowercase letters.

        :param min_chars: minimum length of the random part.
        :param max_chars: maximum length of the random part.
        :param prefix: an optional prefix to prepend to the random string.
        :param suffix: an optional suffix to append to the random string.
        :return: Random of random length between min and max characters.
        """
        if min_chars is None:
            chars = "".join(self.random_letters(length=max_chars))
        else:
            assert max_chars >= min_chars, "Maximum length must be greater than or equal to minimum length"
            chars = "".join(
                self.random_letters(
                    length=self.generator.random.randint(min_chars, max_chars),
                ),
            )

        return prefix + chars + suffix

    def pystr_format(
        self,
        string_format: str = "?#-###{{random_int}}{{random_letter}}",
        letters: str = string.ascii_letters,
    ) -> str:
        return self.bothify(self.generator.parse(string_format), letters=letters)

    @no_type_check
    def pyfloat(
        self,
        left_digits: Optional[int] = None,
        right_digits: Optional[int] = None,
        positive: Optional[bool] = None,
        min_value: Optional[Union[float, int]] = None,
        max_value: Optional[Union[float, int]] = None,
    ) -> float:
        if left_digits is not None and left_digits < 0:
            raise ValueError("A float number cannot have less than 0 digits in its " "integer part")
        if right_digits is not None and right_digits < 0:
            raise ValueError("A float number cannot have less than 0 digits in its " "fractional part")
        if left_digits == 0 and right_digits == 0:
            raise ValueError("A float number cannot have less than 0 digits in total")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("Min value cannot be greater than max value")
        if None not in (min_value, max_value) and min_value == max_value:
            raise ValueError("Min and max value cannot be the same")
        if positive and min_value is not None and min_value <= 0:
            raise ValueError("Cannot combine positive=True with negative or zero min_value")
        if left_digits is not None and max_value and math.ceil(math.log10(abs(max_value))) > left_digits:
            raise ValueError("Max value must fit within left digits")
        if left_digits is not None and min_value and math.ceil(math.log10(abs(min_value))) > left_digits:
            raise ValueError("Min value must fit within left digits")

        # Make sure at least either left or right is set
        if left_digits is None and right_digits is None:
            needed_left_digits = max(1, math.ceil(math.log10(max(abs(max_value or 1), abs(min_value or 1)))))
            right_digits = self.random_int(1, sys.float_info.dig - needed_left_digits)

        # If only one side is set, choose #digits for other side
        if (left_digits is None) ^ (right_digits is None):
            if left_digits is None:
                left_digits = max(1, sys.float_info.dig - right_digits)
            else:
                right_digits = max(1, sys.float_info.dig - left_digits)

        # Make sure we don't ask for too many digits!
        if left_digits + right_digits > sys.float_info.dig:
            raise ValueError(
                f"Asking for too many digits ({left_digits} + {right_digits} == {left_digits + right_digits} > "
                f"{sys.float_info.dig})",
            )

        sign = ""
        if (min_value is not None) or (max_value is not None):
            # Copy values to ensure we're not modifying the original values and thus going out of bounds
            left_min_value = min_value
            left_max_value = max_value
            # Make sure left_digits still respected
            if left_digits is not None:
                if max_value is None:
                    left_max_value = 10**left_digits  # minus smallest representable, adjusted later
                if min_value is None:
                    left_min_value = -(10**left_digits)  # plus smallest representable, adjusted later

            if max_value is not None and max_value < 0:
                left_max_value += 1  # as the random_int will be generated up to max_value - 1
            if min_value is not None and min_value < 0:
                left_min_value += 1  # as we then append digits after the left_number
            left_number = self._safe_random_int(
                left_min_value,
                left_max_value,
                positive,
            )
        else:
            if positive is None:
                sign = self.random_element(("+", "-"))
            elif positive is True:
                sign = "+"
            else:
                sign = "-"

            left_number = self.random_number(left_digits)

        result = float(f"{sign}{left_number}.{self.random_number(right_digits)}")
        if positive and result == 0:
            if right_digits:
                result = float("0." + "0" * (right_digits - 1) + "1")
            else:
                result += sys.float_info.epsilon

        if right_digits:
            result = min(result, 10**left_digits - float(f'0.{"0" * (right_digits - 1)}1'))
            result = max(result, -(10**left_digits + float(f'0.{"0" * (right_digits - 1)}1')))
        else:
            result = min(result, 10**left_digits - 1)
            result = max(result, -(10**left_digits + 1))

        # It's possible for the result to end up > than max_value or < than min_value
        # When this happens we introduce some variance so we're not always the exactly the min_value or max_value.
        # Which can happen a lot depending on the difference of the values.
        # Ensure the variance is bound by the difference between the max and min
        if max_value is not None:
            if result > max_value:
                result = result - (result - max_value + self.generator.random.uniform(0, max_value - min_value))
        if min_value is not None:
            if result < min_value:
                result = result + (min_value - result + self.generator.random.uniform(0, max_value - min_value))

        return result

    def _safe_random_int(self, min_value: float, max_value: float, positive: bool) -> int:
        orig_min_value = min_value
        orig_max_value = max_value

        if min_value is None:
            min_value = max_value - self.random_int()
        if max_value is None:
            max_value = min_value + self.random_int()
        if positive:
            min_value = max(min_value, 0)

        if min_value == max_value:
            return self._safe_random_int(orig_min_value, orig_max_value, positive)
        else:
            min_value = int(min_value)
            max_value = int(max_value - 1)
            if max_value < min_value:
                max_value += 1
            return self.random_int(min_value, max_value)

    def pyint(self, min_value: int = 0, max_value: int = 9999, step: int = 1) -> int:
        return self.generator.random_int(min_value, max_value, step=step)

    def _random_int_of_length(self, length: int) -> int:
        """Generate a random integer of a given length

        If length is 0, so is the number. Otherwise the first digit must not be 0.
        """

        if length < 0:
            raise ValueError("Length must be a non-negative integer.")
        elif length == 0:
            return 0
        else:
            min_value = 10 ** (length - 1)
            max_value = (10**length) - 1
            return self.pyint(min_value=min_value, max_value=max_value)

    def pydecimal(
        self,
        left_digits: Optional[int] = None,
        right_digits: Optional[int] = None,
        positive: Optional[bool] = None,
        min_value: Optional[BasicNumber] = None,
        max_value: Optional[BasicNumber] = None,
    ) -> Decimal:
        if left_digits is not None and left_digits < 0:
            raise ValueError("A decimal number cannot have less than 0 digits in its " "integer part")
        if right_digits is not None and right_digits < 0:
            raise ValueError("A decimal number cannot have less than 0 digits in its " "fractional part")
        if (left_digits is not None and left_digits == 0) and (right_digits is not None and right_digits == 0):
            raise ValueError("A decimal number cannot have 0 digits in total")
        if min_value is not None and max_value is not None and min_value > max_value:
            raise ValueError("Min value cannot be greater than max value")
        if min_value is not None and max_value is not None and min_value == max_value:
            raise ValueError("Min and max value cannot be the same")
        if positive and min_value is not None and min_value <= 0:
            raise ValueError("Cannot combine positive=True with negative or zero min_value")
        if left_digits is not None and max_value and math.ceil(math.log10(abs(max_value))) > left_digits:
            raise ValueError("Max value must fit within left digits")
        if left_digits is not None and min_value and math.ceil(math.log10(abs(min_value))) > left_digits:
            raise ValueError("Min value must fit within left digits")

        # if either left or right digits are not specified we randomly choose a length
        max_random_digits = 100
        # Because if min_value is bigger than 10**100
        max_digits_from_value = max(
            math.ceil(math.log10(abs(min_value or 1))),
            math.ceil(math.log10(abs(max_value or 1))),
        )
        max_left_random_digits = max(max_random_digits, max_digits_from_value + 10)

        if min_value is not None and min_value >= 0:
            sign = "+"
        elif max_value is not None and max_value <= 0:
            sign = "-"
        else:
            if positive is None:
                sign = self.random_element(("+", "-"))
            else:
                sign = "+" if positive else "-"

        if sign == "+":
            if max_value is not None:
                left_number = str(self.random_int(int(max(min_value or 0, 0)), int(max_value)))
            else:
                min_left_digits = math.ceil(math.log10(max(min_value or 1, 1)))
                if left_digits is None:
                    left_digits = self.random_int(min_left_digits, max_left_random_digits)
                left_number = str(self._random_int_of_length(left_digits))
        else:
            if min_value is not None:
                left_number = str(self.random_int(int(abs(min(max_value or 0, 0))), int(abs(min_value))))
            else:
                min_left_digits = math.ceil(math.log10(abs(min(max_value or 1, 1))))
                if left_digits is None:
                    left_digits = self.random_int(min_left_digits, max_left_random_digits)
                left_number = str(self._random_int_of_length(left_digits))

        if right_digits is None:
            right_digits = self.random_int(0, max_random_digits)

        right_number = "".join([str(self.random_digit()) for _ in range(0, right_digits)])

        result = Decimal(f"{sign}{left_number}.{right_number}")

        # Because the random result might have the same number of decimals as max_value the random number
        # might be above max_value or below min_value
        if max_value is not None and result > max_value:
            result = Decimal(str(max_value))
        if min_value is not None and result < min_value:
            result = Decimal(str(min_value))

        return result

    def pytuple(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Tuple[Any, ...]:
        return tuple(
            self._pyiterable(
                nb_elements=nb_elements,
                variable_nb_elements=variable_nb_elements,
                value_types=value_types,
                allowed_types=allowed_types,
            )
        )

    def pyset(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Set[Any]:
        return set(
            self._pyiterable(
                nb_elements=nb_elements,
                variable_nb_elements=variable_nb_elements,
                value_types=value_types,
                allowed_types=allowed_types,
            )
        )

    def pylist(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> List[Any]:
        return list(
            self._pyiterable(
                nb_elements=nb_elements,
                variable_nb_elements=variable_nb_elements,
                value_types=value_types,
                allowed_types=allowed_types,
            )
        )

    @no_type_check
    def pyiterable(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Iterable[Any]:
        value_types: TypesSpec = self._check_signature(value_types, allowed_types)
        return self.random_element([self.pylist, self.pytuple, self.pyset])(
            nb_elements=nb_elements,
            variable_nb_elements=variable_nb_elements,
            value_types=value_types,
            allowed_types=allowed_types,
        )

    def _random_type(self, type_list: List[str]) -> str:
        value_type: str = self.random_element(type_list)

        method_name = f"py{value_type}"
        if hasattr(self, method_name):
            value_type = method_name

        return self.generator.format(value_type)

    def _pyiterable(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Iterator:
        value_types: TypesSpec = self._check_signature(value_types, allowed_types)

        value_types: TypesNames = [
            t if isinstance(t, str) else getattr(t, "__name__", type(t).__name__).lower()
            for t in value_types
            # avoid recursion
            if t not in ["iterable", "list", "tuple", "dict", "set"]
        ]
        if not value_types:
            value_types = self.default_value_types  # type: ignore

        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements, min=1)

        for _ in range(nb_elements):
            yield self._random_type(value_types)

    def pydict(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Dict[Any, Any]:
        """
        Returns a dictionary.

        :nb_elements: number of elements for dictionary
        :variable_nb_elements: is use variable number of elements for dictionary
        :value_types: type of dictionary values
        """

        words_list_count = len(self.generator.get_words_list())

        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements, min=1)

        if nb_elements > words_list_count:
            warnings.warn(
                f"Number of nb_elements is greater than the number of words in the list."
                f" {words_list_count} words will be used.",
                RuntimeWarning,
            )
            nb_elements = words_list_count

        return dict(
            zip(
                self.generator.words(nb_elements, unique=True),
                self._pyiterable(
                    nb_elements=nb_elements,
                    variable_nb_elements=False,
                    value_types=value_types,
                    allowed_types=allowed_types,
                ),
            )
        )

    def pystruct(
        self,
        count: int = 10,
        value_types: Optional[TypesSpec] = None,
        allowed_types: Optional[TypesSpec] = None,
    ) -> Tuple[List, Dict, Dict]:
        value_types: TypesSpec = self._check_signature(value_types, allowed_types)

        value_types: TypesNames = [
            t if isinstance(t, str) else getattr(t, "__name__", type(t).__name__).lower()
            for t in value_types
            # avoid recursion
            if t != "struct"
        ]
        if not value_types:
            value_types = self.default_value_types  # type: ignore

        types = []
        d = {}
        nd = {}
        for i in range(count):
            d[self.generator.word()] = self._random_type(value_types)
            types.append(self._random_type(value_types))
            nd[self.generator.word()] = {
                i: self._random_type(value_types),
                i
                + 1: [
                    self._random_type(value_types),
                    self._random_type(value_types),
                    self._random_type(value_types),
                ],
                i
                + 2: {
                    i: self._random_type(value_types),
                    i + 1: self._random_type(value_types),
                    i
                    + 2: [
                        self._random_type(value_types),
                        self._random_type(value_types),
                    ],
                },
            }
        return types, d, nd

    def enum(self, enum_cls: Type[TEnum]) -> TEnum:
        """
        Returns a random enum of the provided input `Enum` type.

        :param enum_cls: The `Enum` type to produce the value for.
        :returns: A randomly selected enum value.
        """

        if enum_cls is None:
            raise ValueError("'enum_cls' cannot be None")

        if not issubclass(enum_cls, Enum):
            raise TypeError("'enum_cls' must be an Enum type")

        members: List[TEnum] = list(cast(Iterable[TEnum], enum_cls))

        if len(members) < 1:
            raise EmptyEnumException(f"The provided Enum: '{enum_cls.__name__}' has no members.")

        return self.random_element(members)
