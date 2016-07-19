from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '30'
    formats = (
        '2### ######',
        '2#########',
        '2###0 ## ###',
        '2###0#####',
        '2##0 ### ###',
        '2##0 ######',
        '2##0######',
        '210 ### ####',
        '210 #######',
        '210#######',
        '69## ### ###',
        '69## ######',
        '69########',
    )
