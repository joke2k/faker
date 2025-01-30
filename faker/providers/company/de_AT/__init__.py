from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    # Source: https://www.wko.at/wirtschaftsrecht/gesellschaftsformen-oesterreich

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}} & {{last_name}} {{company_suffix}}",
    )

    company_suffixes = (
        "AG",
        "AG",
        "AG",
        "GesbR",
        "GmbH",
        "GmbH",
        "GmbH",
        "KG",
        "KG",
        "KG",
        "OG",
        "e.V.",
    )
