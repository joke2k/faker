from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``fi_FI`` locale."""

    bban_format = "##############"
    bank_country_code = "FI"
