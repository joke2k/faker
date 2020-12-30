from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+91##########',
        '0##########',
        '##########',
    )
