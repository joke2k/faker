from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``de_AT`` locale."""

    bban_format = "################"
    bank_country_code = "AT"
