from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '351'
    formats = (
        '91# ### ###',
        '92# ### ###',
        '93# ### ###',
        '96# ### ###',
        '2## ### ###',
        '2########',
        '91# ### ###',
        '91#######',
        '92# ### ###',
        '92#######',
        '93# ### ###',
        '93#######',
        '96# ### ###',
        '96#######',
    )
