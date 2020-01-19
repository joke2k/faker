from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+34 ### ### ###',
        '+34 #########',
        '+34 ### ## ## ##',
        '+34### ### ###',
        '+34#########',
        '+34### ## ## ##',
    )
