from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``nl_NL`` locale."""

    bban_format = "????##########"
    bank_country_code = "NL"
