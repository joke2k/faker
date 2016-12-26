# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as SsnProvider
from faker.generator import random
import datetime


class Provider(SsnProvider):

    @classmethod
    def ssn(cls):
        """
        Returns 11 character Finnish personal identity code (Henkilötunnus,
        HETU, Swedish: Personbeteckning). Age of person is between 18 and 90
        years, based on local computer date. This function assigns random
        sex to person.

        HETU consists of eleven characters of the form DDMMYYCZZZQ, where
        DDMMYY is the date of birth, C the century sign, ZZZ the individual
        number and Q the control character (checksum). The sign for the
        century is either + (1800–1899), - (1900–1999), or A (2000–2099).
        The individual number ZZZ is odd for males and even for females.
        For people born in Finland its range is 002-899
        (larger numbers may be used in special cases).
        An example of a valid code is 311280-888Y.

        https://en.wikipedia.org/wiki/National_identification_number#Finland
        """
        def _checksum(hetu):
            checksum_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
            return checksum_characters[int(hetu) % 31]

        min_age = 18 * 365
        max_age = 90 * 365
        age = datetime.timedelta(days=random.randrange(min_age, max_age))
        birthday = datetime.date.today() - age
        hetu_date = "%02d%02d%s" % (birthday.day, birthday.month, str(birthday.year)[-2:])
        if birthday.year < 2000:
            separator = '-'
        else:
            separator = 'A'
        suffix = str(random.randrange(2, 899)).zfill(3)
        checksum = _checksum(hetu_date + suffix)
        hetu = "".join([hetu_date, separator, suffix, checksum])
        return hetu
