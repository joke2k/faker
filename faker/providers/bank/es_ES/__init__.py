from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``es_ES`` locale."""

    bban_format = "####################"
    bank_country_code = "ES"
