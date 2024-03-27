from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``el_GR`` locale."""

    bban_format = "#######################"
    bank_country_code = "GR"
