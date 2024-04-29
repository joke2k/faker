import dataclasses
import sys

from datetime import date, datetime, timedelta
from typing import Sequence, Union

try:
    from typing import List, Literal, TypeVar  # type: ignore
except ImportError:
    from typing import List

    from typing_extensions import Literal, TypeVar  # type: ignore

if sys.version_info >= (3, 9):
    from collections import OrderedDict as OrderedDictType
else:
    from typing import OrderedDict as OrderedDictType


class CreditCard:
    def __init__(
        self,
        name: str,
        prefixes: List[str],
        length: int = 16,
        security_code: str = "CVC",
        security_code_length: int = 3,
    ) -> None:
        self.name = name
        self.prefixes = prefixes
        self.length = length
        self.security_code = security_code
        self.security_code_length = security_code_length


CardType = TypeVar("CardType", "CreditCard", str)
DateParseType = Union[date, datetime, timedelta, str, int]
HueType = Union[str, float, int, Sequence[int]]
SexLiteral = Literal["M", "F"]
SeedType = Union[int, float, str, bytes, bytearray, None]


@dataclasses.dataclass
class Country:
    name: str
    timezones: Sequence[str]
    alpha_2_code: str
    alpha_3_code: str
    continent: str
    capital: str


__all__ = ["OrderedDictType", "CreditCard", "CardType", "Country", "DateParseType", "HueType", "SexLiteral", "SeedType"]
