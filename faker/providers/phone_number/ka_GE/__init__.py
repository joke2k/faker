from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Sourse: https://en.wikipedia.org/wiki/Telephone_numbers_in_Georgia_(country)
    formats = (
        "+995 ### ### ###",
        "+995 (###) ### ###",
        "+995#########",
        "0 ### ### ###",
        "+995 32 ### ## ##",
        "+995 34# ### ###",
        "+995 (34#) ### ###",
        "0 32 ### ## ##",
        "0 34# ### ###",
    )
