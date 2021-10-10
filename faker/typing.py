from datetime import date, datetime, timedelta
from typing import Any, Dict, OrderedDict, Sequence, Union

DateTime = Union[datetime, date, timedelta, str]
Elements = Union[Sequence[Any], Dict[str, Any], OrderedDict[str, Any]]
Seed = Union[int, float, str, bytes, bytearray]
