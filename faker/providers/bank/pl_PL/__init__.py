from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``pl_PL`` locale."""

    bban_format = "#" * 26
    country_code = "PL"
