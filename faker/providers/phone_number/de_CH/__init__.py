from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """Phone number provider for `de_CH` locale.

    Sources:
    - https://de.wikipedia.org/wiki/Telefonnummer_(Schweiz)

    """

    dialing_codes = (
        "75",
        "76",
        "77",
        "78",
        "79",
    )

    landline_codes = (
        "21",
        "22",
        "24",
        "26",
        "27",
        "31",
        "32",
        "33",
        "34",
        "43",
        "41",
        "44",
        "52",
        "55",
        "56",
        "61",
        "62",
        "71",
        "81",
        "91",
    )

    cellphone_formats = (
        "+41 {{dialing_code}} ### ## ##",
        "0{{dialing_code}} ### ## ##",
    )

    landline_formats = (
        "+41 {{landline_code}} ### ## ##",
        "0{{landline_code}} ### ## ##",
    )

    """
        Get dialing code for cellphone numbers.
    """

    def dialing_code(self) -> str:
        return self.random_element(self.dialing_codes)

    """
        Get dialing code for landlines.
    """

    def landline_code(self) -> str:
        return self.random_element(self.landline_codes)

    """
        Get a landline phone number.
    """

    def phone_number(self) -> str:
        pattern: str = self.random_element(self.landline_formats)
        return self.numerify(self.generator.parse(pattern))

    """
        Get a cellphone number.
    """

    def cellphone_number(self) -> str:
        pattern: str = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))
