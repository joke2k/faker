from __future__ import unicode_literals
from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+371 ########',
        '+(371) ########',
        '+371########'
    )
