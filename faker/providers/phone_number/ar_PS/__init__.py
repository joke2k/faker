from typing import Optional

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source:
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_the_State_of_Palestine

    cellphone_formats = (
        "{{area_code}} {{provider_code}} ### ####",
        "{{area_code}}{{provider_code}}#######",
        "0{{provider_code}} ### ####",
        "0{{provider_code}}#######",
    )

    telephone_formats = (
        "{{area_code}} 4 24# ####",
        "{{area_code}}424#####",
        "04 24# ####",
        "0424#####",
        "{{area_code}} 9 25# ####",
        "{{area_code}}925#####",
        "09 25# ####",
        "0925#####",
        "{{area_code}} 4 26# ####",
        "{{area_code}}426#####",
        "04 26# ####",
        "0426#####",
        "{{area_code}} 4 23# ####",
        "{{area_code}}423#####",
        "04 23# ####",
        "0423#####",
        "{{area_code}} 4 29# ####",
        "{{area_code}}429#####",
        "04 29# ####",
        "0429#####",
        "{{area_code}} 2 29# ####",
        "{{area_code}}229#####",
        "02 29# ####",
        "0229#####",
        "{{area_code}} 2 23# ####",
        "{{area_code}}223#####",
        "02 23# ####",
        "0223#####",
        "{{area_code}} 2 22# ####",
        "{{area_code}}222#####",
        "02 22# ####",
        "0222#####",
        "{{area_code}} 2 27# ####",
        "{{area_code}}227#####",
        "02 27# ####",
        "0227#####",
        "{{area_code}} 8 20# ####",
        "{{area_code}}820#####",
        "08 20# ####",
        "0820#####",
        "{{area_code}} 8 21# ####",
        "{{area_code}}821#####",
        "08 21# ####",
        "0821#####",
        "{{area_code}} 8 24# ####",
        "{{area_code}}824#####",
        "08 24# ####",
        "0824#####",
        "{{area_code}} 8 25# ####",
        "{{area_code}}825#####",
        "08 25# ####",
        "0825#####",
        "{{area_code}} 8 26# ####",
        "{{area_code}}826#####",
        "08 26# ####",
        "0826#####",
        "{{area_code}} 8 28# ####",
        "{{area_code}}828#####",
        "08 28# ####",
        "0828#####",
    )

    toll_formats = (
        "1 700 ### ###",
        "1-700-###-###",
        "1 800 ### ###",
        "1-800-###-###",
    )

    services_phones_formats = (
        "100",
        "101",
        "102",
    )

    formats = cellphone_formats + telephone_formats + services_phones_formats + toll_formats

    def provider_code(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(
            [
                "59",
                "56",
            ],
            min_length,
            max_length,
        )

    def area_code(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(
            [
                "00972",
                "+972",
                "00970",
                "+970",
            ],
            min_length,
            max_length,
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
