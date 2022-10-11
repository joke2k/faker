from datetime import date, datetime, timedelta
from typing import Sequence, TypeVar, Union

try:
    from typing import Literal  # type: ignore
except ImportError:
    from typing_extensions import Literal  # type: ignore

DateParseType = Union[date, datetime, timedelta, str, int]
HueType = TypeVar("HueType", str, float, Sequence[int])
SexLiteral = Literal["M", "F"]
SeedType = Union[int, float, str, bytes, bytearray, None]
