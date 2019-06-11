# coding=utf-8
from __future__ import unicode_literals

import random
import string

from .. import Provider as BaseProvider


def _reduce_digits(n):
    """
    Sum of digits of a number until sum becomes single digit.

    Example:
        658 => 6 + 5 + 8 = 19 => 1 + 9 = 10 => 1
    """
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    else:
        return n % 9


def ssn_checksum(digits):
    """
    Calculate the checksum for the mexican SSN (IMSS).
    """
    return -sum(
        _reduce_digits(n * (i % 2 + 1))
        for i, n in enumerate(digits)
    ) % 10


class Provider(BaseProvider):
    """
    A Faker provider for the Mexican SSN, RFC and CURP
    """
    ssn_formats = ("###########",)

    def ssn(self):
        """
        Mexican Social Security Number, as given by IMSS.

        :return: a random Mexican SSN
        """
        office = self.random_int(min=1, max=99)
        birth_year = self.random_int(min=0, max=99)
        start_year = self.random_int(min=0, max=99)
        serial = self.random_int(min=1, max=9999)

        num = "{0:02d}{1:02d}{2:02d}{3:04d}".format(
            office,
            start_year,
            birth_year,
            serial,
        )

        check = ssn_checksum(map(int, num))
        num += str(check)

        return num
