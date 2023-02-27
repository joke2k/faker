"""
This module exists solely to figure how long a registrant/publication
number may be within an SBN. It's the same as the ISBN implementation
for ean 978, reg_group 0.
"""

from collections import namedtuple
from typing import List

RegistrantRule = namedtuple("RegistrantRule", ["min", "max", "registrant_length"])

# Structure: RULES = [Rule1, Rule2, ...]
RULES: List[RegistrantRule] = [
    RegistrantRule("0000000", "1999999", 2),
    RegistrantRule("2000000", "2279999", 3),
    RegistrantRule("2280000", "2289999", 4),
    RegistrantRule("2290000", "6479999", 3),
    RegistrantRule("6480000", "6489999", 7),
    RegistrantRule("6490000", "6999999", 3),
    RegistrantRule("7000000", "8499999", 4),
    RegistrantRule("8500000", "8999999", 5),
    RegistrantRule("9000000", "9499999", 6),
    RegistrantRule("9500000", "9999999", 7),
]
