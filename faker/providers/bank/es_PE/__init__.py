from .. import Provider as BankProvider


class Provider(BankProvider):
    # Implement bank provider for 'es_PE' locale.
    # Source: <https://www.bcrp.gob.pe/sitios-de-interes/entidades-financieras.html>
    bban_format = "????##################"
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
        "Alfin Banco"
        "Banco central de Reserva del Perú",
        "Scotiabank Perú",
        "Banco GNB Perú",
        "Banco Falabella",
        "Banco Ripley",
        "Banco Santander Perú",
        "Bank of China",
        "Bci Perú",
        "ICBC PERU BANK",
        "Agrobanco",
    )
    swift_bank_codes = (
        "BANC",
        "BDCM",
        "BCPL",
        "BIFS",
        "FINA",
        "BCON",
        "CITI",
        "BINP",
        "AIFN",
        "CRPE",
        "BSUD",
        "HBPE",
        "BSAP",
        "BKCH",
        "CRED",
        "ICBK",
    )
    swift_location_codes = (
        "PL",
    )
    swift_branch_codes = (
        "XXX",
        "000",
    )
    def bank(self) -> str:
        # Generate a bank name
        return self.random_element(self.banks)
