from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '91'
    formats = (
        '##########',
        '### #######',
        '0##-########',
        '0##########',
        '0#### ######',
    )
