# faker/providers/bank/es_PE/__init__.py

from .. import Provider as BankProvider


class Provider(BankProvider):
    """
    Implement bank provider for ``es_PE`` locale.

    Sources:
    - CCI Format: https://www.bcrp.gob.pe/sistema-de-pagos/codigo-de-cuenta-interbancario.html
    - Bank Names: https://www.sbs.gob.pe/sistema-financiero-y-de-seguros/sistema-financiero/empresas-en-el-sistema-financiero/
    Accessed: 2026-02-07
    """

    # The Peruvian "Código de Cuenta Interbancario" (CCI) has 20 digits.
    bban_format = "####################"
    country_code = "PE"

    # List of major banks operating in Peru
    banks = (
        "Banco de Crédito del Perú (BCP)",
        "Interbank",
        "Scotiabank Perú",
        "BBVA Perú",
        "Banco de la Nación",
        "MiBanco",
        "Banco Pichincha",
        "BanBif",
        "Banco Ripley",
        "Banco Falabella",
        "Banco GNB Perú",
        "Banco de Comercio",
    )

    def bank(self) -> str:
        """
        Returns a random Peruvian bank name.
        """
        return self.random_element(self.banks)

