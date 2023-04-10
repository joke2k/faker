from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = [
        "+51 9## ### ###",
        "519## ### ###",
        "519########",
        "9## ### ###",
        "9########",
    ]
