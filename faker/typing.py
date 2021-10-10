from datetime import date, datetime, timedelta
from typing import Any, Dict, Sequence, Union

try:
    from typing import OrderedDict
except ImportError:
    from typing import MutableMapping
    OrderedDict = MutableMapping

DateTime = Union[datetime, date, timedelta, str]
Elements = Union[Sequence[Any], Dict[str, Any], OrderedDict[str, Any]]
Seed = Union[int, float, str, bytes, bytearray]
