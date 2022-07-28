from typing import Optional

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}} és {{last_name}} {{company_suffix}}",
        "{{last_name}} és társa {{company_suffix}}",
    )

    company_suffixes = ("Kft.", "Kht.", "Zrt.", "Bt.", "Nyrt.", "Kkt.")

    def company_suffix(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.company_suffixes, min_length, max_length)
