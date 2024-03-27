from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_GB`` locale."""

    bban_format = "????##############"
    bank_country_code = "GB"
