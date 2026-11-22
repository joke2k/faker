from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """Implement phone number provider for ``en_IN`` locale.

    Mobile numbers have ten digits and start with 6, 7, 8 or 9. Landline
    numbers are dialled with the trunk prefix 0, then the STD code (which
    starts with 1 to 8) and the subscriber number, ten digits after the 0.
    Source: https://en.wikipedia.org/wiki/Telephone_numbers_in_India
    """

    formats = (
        # Mobile, international
        "+916#########",
        "+917#########",
        "+918#########",
        "+919#########",
        # Mobile, national
        "6#########",
        "7#########",
        "8#########",
        "9#########",
        # Landline, national
        "01#########",
        "02#########",
        "03#########",
        "04#########",
        "05#########",
        "06#########",
        "07#########",
        "08#########",
    )
