from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '386'
    formats = (
        '040 ### ###',
        '041 ### ###',
        '031 ### ###',
        '030 ### ###',
        '070 ### ###',
        '01 #### ###',
        '02 #### ###',
        '04 #### ###',
        '05 #### ###',
        '06 #### ###',
        '08 #### ###',
    )
