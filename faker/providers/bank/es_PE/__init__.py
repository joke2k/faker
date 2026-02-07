# faker/providers/bank/es_PE/__init__.py

from .. import Provider as BankProvider


class Provider(BankProvider):
    """
    Implement bank provider for ``es_PE`` locale.

    Sources:
    - CCI format and documentation: https://www.bcrp.gob.pe/sistema-de-pagos/codigo-de-cuenta-interbancario.html
    - List of financial institutions: https://www.sbs.gob.pe/sistema-financiero-y-de-seguros/
    Accessed: 2026-02-07
    """

    bban_format = "####################"
    country_code = "PE"
