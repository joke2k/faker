from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``da_DK`` locale."""

    bban_format = "################"
    bank_country_code = "DK"
