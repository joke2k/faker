from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``it_IT`` locale."""

    bban_format = "?######################"
    bank_country_code = "IT"
