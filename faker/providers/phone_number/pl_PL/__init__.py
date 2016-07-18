from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '48'
    formats = (
        # Mobile
        # Government website: http://www.uke.gov.pl/numeracja-843
        '22 ### ## ##',
        '32 ### ## ##',
        '50# ### ###',
        '51# ### ###',
        '53# ### ###',
        '57# ### ###',
        '60# ### ###',
        '66# ### ###',
        '69# ### ###',
        '72# ### ###',
        '73# ### ###',
        '78# ### ###',
        '79# ### ###',
        '88# ### ###',
    )
