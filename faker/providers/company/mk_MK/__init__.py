from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """Company provider for mk_MK locale (Macedonian)."""

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}}",
        "{{last_name}} и {{last_name}} {{company_suffix}}",
    )

    company_suffixes = (
        "АД",
        "ДОО",
        "ДООЕЛ",
        "ЕД",
        "КД",
        "ТД",
        "ЈП",
        "ООД",
    )
