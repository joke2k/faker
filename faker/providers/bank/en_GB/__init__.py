from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_GB`` locale."""

    bban_format = "????##############"
    country_code = "GB"

    # Major UK banks
    banks = (
        "Barclays",
        "HSBC UK",
        "Lloyds Bank",
        "NatWest",
        "Santander UK",
        "Halifax",
        "Bank of Scotland",
        "Royal Bank of Scotland",
        "Nationwide Building Society",
        "TSB Bank",
        "Virgin Money",
        "Metro Bank",
        "Monzo",
        "Revolut",
        "Starling Bank",
        "Co-operative Bank",
        "Yorkshire Bank",
        "Clydesdale Bank",
    )
