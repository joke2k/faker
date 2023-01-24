from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    cellphone_formats = (
        "+994{{provider_code}}{{start_digit}}######",
        "0{{provider_code}} {{start_digit}}## ## ##",
        "0{{provider_code}}-{{start_digit}}##-##-##",
    )

    telephone_formats = ("{{area_code}}## ## ##",)

    provider_codes = ["50", "51", "55", "60", "70", "77", "99"]

    start_digits = ["2", "3", "4", "5", "6", "7", "8", "9"]

    area_codes = [
        "012 3",
        "012 4",
        "012 5",
        "018 6",
        "020 2",
        "021 2",
        "021 4",
        "022 2",
        "022 3",
        "022 4",
        "023 3",
        "024 2",
        "025 2",
        "026 2",
        "026 3",
        "036 5",
    ]

    formats = cellphone_formats + telephone_formats

    def start_digit(self) -> str:
        return self.random_element(self.start_digits)

    def provider_code(self) -> str:
        return self.random_element(self.provider_codes)

    def area_code(self) -> str:
        return self.random_element(self.area_codes)

    def cellphone_number(self) -> str:
        pattern: str = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))

    def landline_number(self) -> str:
        pattern: str = self.random_element(self.telephone_formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number(self) -> str:
        pattern: str = self.random_element(self.formats)
        return self.numerify(self.generator.parse(pattern))
