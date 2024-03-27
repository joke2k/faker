from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``no_NO`` locale."""

    bban_format = "###########"
    bank_country_code = "NO"
