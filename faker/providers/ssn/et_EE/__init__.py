# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as SsnProvider
from faker.generator import random
import datetime
import operator


def checksum(digits):
    """Calculate checksum of Estonian personal identity code.

    Checksum is calculated with "Modulo 11" method using level I or II scale:
    Level I scale: 1 2 3 4 5 6 7 8 9 1
    Level II scale: 3 4 5 6 7 8 9 1 2 3

    The digits of the personal code are multiplied by level I scale and summed;
    if remainder of modulo 11 of the sum is less than 10, checksum is the
    remainder.
    If remainder is 10, then level II scale is used; checksum is remainder if
    remainder < 10 or 0 if remainder is 10.

    See also https://et.wikipedia.org/wiki/Isikukood
    """
    sum_mod11 = sum(map(operator.mul, digits, Provider.scale1)) % 11
    if sum_mod11 < 10:
        return sum_mod11
    sum_mod11 = sum(map(operator.mul, digits, Provider.scale2)) % 11
    return 0 if sum_mod11 == 10 else sum_mod11


class Provider(SsnProvider):
    min_age = 16 * 365
    max_age = 90 * 365
    scale1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    scale2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)

    @classmethod
    def ssn(cls):
        """
        Returns 11 character Estonian personal identity code (isikukood, IK).

        Age of person is between 16 and 90 years, based on local computer date.
        This function assigns random sex to person.
        An Estonian Personal identification code consists of 11 digits,
        generally given without any whitespace or other delimiters.
        The form is GYYMMDDSSSC, where G shows sex and century of birth (odd
        number male, even number female, 1-2 19th century, 3-4 20th century,
        5-6 21st century), SSS is a serial number separating persons born on
        the same date and C a checksum.

        https://en.wikipedia.org/wiki/National_identification_number#Estonia
        """
        age = datetime.timedelta(days=random.randrange(Provider.min_age,
                                                       Provider.max_age))
        birthday = datetime.date.today() - age
        if birthday.year < 2000:
            ik = random.choice(('3', '4'))
        elif birthday.year < 2100:
            ik = random.choice(('5', '6'))
        else:
            ik = random.choice(('7', '8'))

        ik += "%02d%02d%02d" % ((birthday.year % 100), birthday.month,
                                birthday.day)
        ik += str(random.randrange(0, 999)).zfill(3)
        return ik + str(checksum([int(ch) for ch in ik]))
