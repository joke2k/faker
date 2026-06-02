from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    # Source: https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_c%C3%B4ng_ty_Vi%E1%BB%87t_Nam
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
        "Tập Đoàn",
    )

    def company_suffix(self) -> str:
        return self.random_element(self.company_suffixes)
