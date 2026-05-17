from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source: https://en.wikipedia.org/wiki/Telephone_numbers_in_Algeria

    cellphone_formats = (
        "0{{mobile_operator}}## ## ## ##",
        "+213 {{mobile_operator}}## ## ## ##",
    )

    telephone_formats = (
        "0{{area_code}} ## ## ##",
        "+213 {{area_code}} ## ## ##",
    )

    formats = cellphone_formats + telephone_formats

    def mobile_operator(self) -> str:
        return self.random_element(["5", "6", "7"])

    def area_code(self) -> str:
        return self.random_element(
            [
                "21",
                "23",
                "24",
                "25",
                "26",
                "27",
                "29",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
                "39",
                "41",
                "43",
                "45",
                "46",
                "48",
                "49",
            ]
        )

    def cellphone_number(self) -> str:
        pattern: str = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))

    def telephone_number(self) -> str:
        pattern: str = self.random_element(self.telephone_formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number(self) -> str:
        pattern: str = self.random_element(self.formats)
        return self.numerify(self.generator.parse(pattern))
