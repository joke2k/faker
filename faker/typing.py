import platform

from datetime import date, datetime, timedelta
from typing import Any, Dict, Sequence, Union

major, minor, patchlevel = (int(version) for version in platform.python_version_tuple())

if major > 3 or major == 3 and minor >= 10:  # Python 3.10 and above
    from collections import OrderedDict
elif major == 3 and (minor < 7 or minor == 7 and patchlevel < 2):  # Python 3.7.1 and below
    from typing import MutableMapping as OrderedDict
else:
    from typing import OrderedDict

DateTime = Union[datetime, date, timedelta, str]
Elements = Union[Sequence[Any], Dict[str, Any], OrderedDict[str, Any]]
Seed = Union[int, float, str, bytes, bytearray]
