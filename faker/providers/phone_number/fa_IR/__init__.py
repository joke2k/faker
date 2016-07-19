from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '98'
    formats = (
        # Mobile
        '91# ### ####',
        '091# ### ####',
        '920 ### ####',
        '0920 ### ####',
        '921 ### ####',
        '0921 ### ####',
        '93# ### ####',
        '093# ### ####',
        # Land lines
        '21 #### ####',
        '021 #### ####',
        '25 #### ####',
        '025 #### ####',
        '26 #### ####',
        '026 #### ####',
        '### #### ####',
        '0### #### ####'
    )
