import dataclasses

from collections import OrderedDict as OrderedDictType
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import List, Literal, Sequence, TypeVar, Union


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


BasicNumber = Union[float, int, Decimal]
CardType = TypeVar("CardType", "CreditCard", str)
DateParseType = Union[date, datetime, timedelta, str, int]
HueType = Union[str, float, int, Sequence[int]]
SexLiteral = Literal["M", "F", "X"]
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
