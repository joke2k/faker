from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_GB`` locale.

    Banks list sourced from:
    https://en.wikipedia.org/wiki/List_of_banks_in_the_United_Kingdom
    https://en.wikipedia.org/wiki/Banking_in_the_United_Kingdom
    Last checked: 2026-04-10
    """

    bban_format = "????##############"
    country_code = "GB"
    banks = (
        "Al Rayan Bank",
        "Aldermore Bank",
        "Atom Bank",
        "Bank of Ireland UK",
        "Bank of London and The Middle East",
        "Bank of Scotland",
        "Barclays Bank",
        "Chase UK",
        "Clydesdale Bank",
        "Co-operative Bank",
        "Gatehouse Bank",
        "Halifax",
        "Handelsbanken",
        "HSBC UK",
        "Investec Bank",
        "Kroo Bank",
        "Lloyds Bank",
        "Metro Bank",
        "Monzo Bank",
        "Nationwide Building Society",
        "NatWest",
        "OakNorth Bank",
        "Revolut Bank",
        "Royal Bank of Scotland",
        "Santander UK",
        "Shawbrook Bank",
        "Starling Bank",
        "Tandem Bank",
        "TSB Bank",
        "Ulster Bank",
        "Virgin Money",
        "Yorkshire Bank",
        "Zempler Bank",
        "Zopa Bank",
    )
