from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``de_CH`` locale."""

    bban_format = "#################"
    bank_country_code = "CH"
