from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        # Mobile
        '+98 91# ### ####',
        '091# ### ####',
        '+98 920 ### ####',
        '0920 ### ####',
        '+98 921 ### ####',
        '0921 ### ####',
        '+98 93# ### ####',
        '093# ### ####',
        # Land lines
        '+98 21 #### ####',
        '021 #### ####',
        '+98 25 #### ####',
        '025 #### ####',
        '+98 26 #### ####',
        '026 #### ####',
        '+98 ### #### ####',
        '0### #### ####'
    )