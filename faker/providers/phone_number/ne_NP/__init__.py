from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '977'
    formats = (
        '##########',
        '### #######',
        '984#######',
        '985#######',
        '980#######',
    )
