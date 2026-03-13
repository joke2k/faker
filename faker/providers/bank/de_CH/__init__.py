from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``de_CH`` locale."""

    bban_format = "#################"
    country_code = "CH"

    # Major Swiss banks - Source: https://de.wikipedia.org/wiki/Schweizer_Bankwesen
    banks = (
        "UBS",
        "Credit Suisse",
        "Raiffeisen Schweiz",
        "Zürcher Kantonalbank",
        "PostFinance",
        "Julius Bär",
        "Banque Cantonale Vaudoise",
        "Migros Bank",
        "Basler Kantonalbank",
        "Luzerner Kantonalbank",
        "Union Bancaire Privée",
        "Vontobel",
    )
