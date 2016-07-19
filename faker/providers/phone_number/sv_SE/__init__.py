# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '46'
    formats = (
        '08-### ### ##',
        '08-### ## ##',
        '08-## ## ##',
        '0##-### ## ##',
        '0##-## ## ##',
        '0###-## ## ##',
        '0###-### ##',
        '(0)8 ### ### ##',
        '(0)## ## ## ##',
        '(0)### ### ##',
    )
