from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '421'
    formats = (
        '2 ########',
        '3# ### ####',
        '4# ### ####',
        '5# ### ####',
        '90# ### ###',
        '91# ### ###',
        '940 ### ###',
        '944 ### ###',
        '948 ### ###',
        '949 ### ###',
    )
