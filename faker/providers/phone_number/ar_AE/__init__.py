from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source: https://en.wikipedia.org/wiki/Telephone_numbers_in_the_United_Arab_Emirates

    cellphone_formats = (
        "{{area_code}} {{cellphone_provider_code}} ### ####",
        "{{area_code}}{{cellphone_provider_code}}#######",
        "0{{cellphone_provider_code}} ### ####",
        "0{{cellphone_provider_code}}#######",
    )

    telephone_formats = (
        "{{area_code}} {{telephone_provider_code}} ### ####",
        "{{area_code}}{{telephone_provider_code}}#######",
        "0{{telephone_provider_code}} ### ####",
        "0{{telephone_provider_code}}#######",
    )

    toll_formats = (
        "200####",
        "600######",
        "800###",
        "800####",
        "800#####",
        "800######",
        "800#######",
    )

    services_phones_formats = (
        "999",
        "901",
        "998",
        "997",
        "996",
        "991",
        "922",
    )

    formats = (
        cellphone_formats + telephone_formats + services_phones_formats + toll_formats
    )

    def cellphone_provider_code(self) -> str:
        return self.random_element(
            [
                "50",
                "52",
                "54",
                "55",
                "56",
                "58",
            ]
        )

    def telephone_provider_code(self) -> str:
        return self.random_element(
            [
                "1",
                "2",
                "3",
                "4",
                "6",
                "7",
                "9",
            ]
        )

    def area_code(self) -> str:
        return self.random_element(
            [
                "00971",
                "+971",
            ]
        )

    def cellphone_number(self) -> str:
        pattern: str = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))

    def telephone_number(self) -> str:
        pattern: str = self.random_element(self.telephone_formats)
        return self.numerify(self.generator.parse(pattern))

    def service_phone_number(self) -> str:
        pattern: str = self.random_element(self.services_phones_formats)
        return self.numerify(self.generator.parse(pattern))

    def toll_number(self) -> str:
        pattern: str = self.random_element(self.toll_formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number(self) -> str:
        pattern: str = self.random_element(self.formats)
        return self.numerify(self.generator.parse(pattern))
