from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '###-##-##',
        '### ## ##',
        '0## ### ## ##',
        '0## ###-##-##',
        '+38 0## ###-##-##',
        '+38 0## ###-##-##',
        '+38 (0##) ###-##-##',
        '+38 0## ### ## ##',
    )
