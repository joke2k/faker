from typing import Optional

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}}",
    )

    company_suffixes = (
        "SRL",
        "SA",
        "SCA",
        "SNC",
        "SCS",
        "AFJ",
        "ASF",
        "CON",
        "CRL",
        "INC",
        "LOC",
        "OC1",
        "OC2",
        "OC3",
        "PFA",
        "RA",
        "SCS",
        "SPI",
        "URL",
    )

    def company_suffix(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.company_suffixes, min_length, max_length)
