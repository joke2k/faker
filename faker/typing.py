import platform

from datetime import date, datetime, timedelta
from typing import Sequence, TypeVar, Union

major, minor, patchlevel = (int(version) for version in platform.python_version_tuple())

if major > 3 or major == 3 and minor >= 10:  # Python 3.10 and above
    from collections import OrderedDict as OrderedDictType
elif major == 3 and (minor < 7 or minor == 7 and patchlevel < 2):  # Python 3.7.1 and below
    from typing import MutableMapping as OrderedDictType
else:
    from typing import OrderedDict as OrderedDictType

if major > 3 or major == 3 and minor >= 8:
    from typing import Literal
    GenderType = Literal['M', 'F']
else:
    GenderType = str

DateParseType = Union[date, datetime, timedelta, str, int]
HueType = TypeVar('HueType', str, float, Sequence[int])


__all__ = ['DateParseType', 'GenderType', 'HueType', 'OrderedDictType']
