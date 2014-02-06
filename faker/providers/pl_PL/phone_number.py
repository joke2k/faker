from __future__ import unicode_literals
from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+48 5## ### ###',
        '+48 6## ### ###',
        '+48 7## ### ###',
        '+48 8## ### ###',
        '+48 ## ### ## ##',
    )