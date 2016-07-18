from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '39'
    formats = (
        '### ## ## ####',
        '## #######',
        '## ########',
        '### #######',
        '### ########',
        '#### #######',
        '#### ########'
    )
