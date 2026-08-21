from datetime import datetime

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """Company provider for the ``en_IN`` locale.

    Company names combine common Indian surnames and business-sector words with
    the legal-form suffixes used by Indian companies (``Pvt Ltd``, ``LLP`` and
    so on). The provider also exposes :meth:`cin`, which returns a Corporate
    Identification Number - the 21-character identifier the Ministry of
    Corporate Affairs assigns to every registered company.
    """

    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{company_sector}} {{company_suffix}}",
        "{{last_name}} and {{last_name}} {{company_suffix}}",
        "{{last_name}} {{company_sector}}",
    )

    company_suffixes = (
        "Pvt Ltd",
        "Private Limited",
        "Limited",
        "Ltd",
        "LLP",
        "and Sons",
        "and Co",
        "Industries",
        "Enterprises",
        "Corporation",
    )

    # Business-sector words that commonly appear in Indian company names.
    company_sectors = (
        "Technologies",
        "Industries",
        "Textiles",
        "Motors",
        "Pharma",
        "Steel",
        "Cements",
        "Chemicals",
        "Infotech",
        "Systems",
        "Solutions",
        "Exports",
        "Trading",
        "Agro",
        "Power",
    )

    # State / union-territory codes used in the Registrar of Companies portion
    # of a CIN.
    cin_states = (
        "AP",
        "AR",
        "AS",
        "BR",
        "CH",
        "CT",
        "DL",
        "GA",
        "GJ",
        "HR",
        "HP",
        "JK",
        "JH",
        "KA",
        "KL",
        "MP",
        "MH",
        "MN",
        "ML",
        "MZ",
        "NL",
        "OR",
        "PB",
        "PY",
        "RJ",
        "SK",
        "TN",
        "TG",
        "TR",
        "UP",
        "UT",
        "WB",
        "AN",
        "DN",
        "DD",
        "LD",
    )

    # Company-classification codes used in a CIN.
    cin_classifications = (
        "PTC",  # Private company
        "PLC",  # Public company
        "OPC",  # One Person Company
        "GOI",  # Government of India company
        "SGC",  # State Government company
        "NPL",  # Not-for-profit (Section 8) company
        "ULL",  # Unlimited liability company
        "FTC",  # Subsidiary of a foreign company
    )

    def company_sector(self) -> str:
        """Return a business-sector word used in Indian company names."""
        return self.random_element(self.company_sectors)

    def cin(self) -> str:
        """Return a Corporate Identification Number (CIN).

        The 21-character identifier issued by the Ministry of Corporate Affairs
        has the structure (shown spaced for clarity)::

            L 17110 MH 1973 PLC 019786

        - listing status (``L`` listed / ``U`` unlisted)
        - a 5-digit industry code
        - a 2-letter state code
        - the 4-digit year of incorporation
        - a 3-letter company classification
        - a 6-digit registration number
        """
        listing = self.random_element(("L", "U"))
        industry = self.numerify("#####")
        state = self.random_element(self.cin_states)
        year = self.random_int(1900, datetime.now().year)
        classification = self.random_element(self.cin_classifications)
        registration = self.numerify("######")
        return f"{listing}{industry}{state}{year}{classification}{registration}"
