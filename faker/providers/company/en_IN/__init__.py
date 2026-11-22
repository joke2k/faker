from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """Implement company provider for ``en_IN`` locale.

    Company suffixes follow the business structures defined by the Companies
    Act, 2013 and the Limited Liability Partnership Act, 2008, plus the trade
    names commonly used by sole proprietorships and partnership firms.
    Source: https://www.mca.gov.in/
    """

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} & {{last_name}} {{company_suffix}}",
        "{{last_name}} & Sons",
        "{{last_name}} Industries",
        "{{last_name}} Industries {{company_suffix}}",
        "{{last_name}} Enterprises",
        "{{last_name}} Enterprises {{company_suffix}}",
        "{{last_name}} Traders",
        "{{last_name}} Traders {{company_suffix}}",
        "{{last_name}} Textiles",
        "{{last_name}} Textiles {{company_suffix}}",
        "{{last_name}} Steels",
        "{{last_name}} Steels {{company_suffix}}",
        "{{last_name}} Chemicals",
        "{{last_name}} Chemicals {{company_suffix}}",
        "{{last_name}} Pharmaceuticals",
        "{{last_name}} Pharmaceuticals {{company_suffix}}",
        "{{last_name}} Motors",
        "{{last_name}} Motors {{company_suffix}}",
        "{{last_name}} Infotech",
        "{{last_name}} Infotech {{company_suffix}}",
        "{{last_name}} Constructions",
        "{{last_name}} Constructions {{company_suffix}}",
        "{{last_name}} Agencies",
        "{{last_name}} Agencies {{company_suffix}}",
        "{{last_name}} Logistics",
        "{{last_name}} Logistics {{company_suffix}}",
        "{{last_name}} Foods",
        "{{last_name}} Foods {{company_suffix}}",
        "{{last_name}} Exports",
        "{{last_name}} Exports {{company_suffix}}",
    )

    company_suffixes = (
        "Pvt. Ltd.",
        "Pvt. Ltd.",
        "Pvt. Ltd.",
        "Private Limited",
        "Private Limited",
        "Ltd.",
        "Limited",
        "LLP",
    )
