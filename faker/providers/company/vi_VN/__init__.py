from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}} và {{last_name}} {{company_suffix}}",
        "{{last_name}} và đối tác {{company_suffix}}",
    )

    company_suffixes = (
        "Công ty TNHH",
        "Công ty Cổ phần",
        "Doanh nghiệp tư nhân",
        "Công ty TNHH MTV",
        "Công ty Hợp danh",
        "Công ty Trách nhiệm hữu hạn",
    )

    def company_suffix(self) -> str:
        return self.random_element(self.company_suffixes)
