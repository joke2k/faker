from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``mk_MK`` locale."""

    bban_format = "###??????????##"
    country_code = "MK"
