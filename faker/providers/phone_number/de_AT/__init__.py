from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """Phone number provider for `de_AT` locale.

    Sources:
    - https://de.wikipedia.org/wiki/Telefonvorwahl_(%C3%96sterreich)

    """

    dialing_codes = (
        "650",
        "655",
        "660",
        "661",
        "663",
        "664",
        "665",
        "667",
        "670",
        "676",
        "677",
        "678",
        "680",
        "681",
        "688",
        "690",
        "699",
    )

    area_code_formats = (
        "1",  # Wien
        "316",  # Graz
        "463",  # Klagenfurt
        "512",  # Innsbruck
        "662",  # Salzburg
        "732",  # Linz
        "21##",
        "22##",
        "25##",
        "26##",
        "27##",
        "28##",
        "29##",
        "31##",
        "33##",
        "34##",
        "35##",
        "36##",
        "38##",
        "42##",
        "43##",
        "47##",
        "48##",
        "52##",
        "53##",
        "54##",
        "55##",
        "56##",
        "61##",
        "62##",
        "64##",
        "65##",
        "72##",
        "73##",
        "74##",
        "75##",
        "76##",
        "77##",
        "79##",
    )

    cellphone_formats = (
        "+43 (0) {{dialing_code}} ########",
        "+43 {{dialing_code}} ### ### ##",
        "+43 {{dialing_code}}########",
        "0{{dialing_code}} ### ### ##",
        "0{{dialing_code}}/########",
    )

    landline_formats = (
        "+43 (0) {{area_code}} ########",
        "+43 {{area_code}} ##### ###",
        "+43 {{area_code}}########",
        "0{{area_code}} ##### ###",
        "(0{{area_code}}) ##### ###",
        "0{{area_code}}/########",
    )

    """
        Get dialing code for cellphone numbers.
    """

    def dialing_code(self) -> str:
        return self.random_element(self.dialing_codes)

    """
        Get area code for landlines.
    """

    def area_code(self) -> str:
        area_code: str = self.random_element(self.area_code_formats)
        return self.numerify(area_code)

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
