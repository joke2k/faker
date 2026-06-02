from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    # Source: https://de.wikipedia.org/wiki/Firma#Schweizerisches_Recht

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
    )

    company_suffixes = (
        "AG",
        "AG",
        "AG",
        "GmbH",
        "GmbH",
        "GmbH",
        "& Co.",
        "& Partner",
        "& Cie.",
        "& Söhne",
    )
