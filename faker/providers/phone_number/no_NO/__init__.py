from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '47'
    formats = (
        '#########',
        '## ## ## ##',
        '########',
        '9## ## ###',
        '4## ## ###',
        '9#######',
        '4#######',
    )
