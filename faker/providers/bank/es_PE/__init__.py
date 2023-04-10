from .. import Provider as BankProvider


class Provider(BankProvider):
    #Implement bank provider for ``es_PE`` locale.
    #Source: <https://www.bcrp.gob.pe/sitios-de-interes/entidades-financieras.html>
    country_code = "PE"

    banks = (
        "Banco de la Nación",
        "Banco de Comercio",
        "Banco de Crédito del Perú",
        "Banco Interamericano de Finanzas (BanBif)",
        "Banco Pichincha",
        "BBVA",
        "Citibank Perú",
        "Interbank",
        "MiBanco",
        "Scotiabank Perú",
        "Banco GNB Perú",
        "Banco Falabella",
        "Banco Ripley",
        "Banco Santander Perú",
        "Alfin Banco",
        "Bank of China",
        "Bci Perú",
        "ICBC PERU BANK",
        "Agrobanco",
    )

    def bank(self) -> str:
        #Generate a bank name
        return self.random_element(self.banks)
