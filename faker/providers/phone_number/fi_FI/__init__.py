from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '358'
    formats = (
        '## #######',
        '#########',
        '0#########',
        '0## ### ####'
    )
