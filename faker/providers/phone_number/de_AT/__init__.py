# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '43'
    formats = (
        '316 ###',
        '463 ####',
        '512 #####',
        '662 ######',
        '732 #######',
        '2231 ########',
        '2246 #########',
    )
