from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    Phone number provider for es_PE locale.

    Sources:
    - Telephone numbers in Peru: https://en.wikipedia.org/wiki/Telephone_numbers_in_Peru
    - Ministry of Transport and Communications (MTC) official pages
    Accessed: 2026-02-07
    """

    # Mobile numbers in Peru are 9 digits and start with 9.
    mobile_formats = (
        "9## ### ###",
        "9########",
        "+51 9## ### ###",
    )
