from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``es_CO`` locale.

    Sources:
    - Bank names: Superintendencia Financiera de Colombia
      https://www.superfinanciera.gov.co/publicaciones/61694/

    - SWIFT bank codes: BBVA
      https://www.bbva.com/es/salud-financiera/los-codigos-de-las-entidades-bancarias-en-colombia/
    """

    country_code = "CO"

    banks = (
        "Banco de Bogotá",
        "Banco Popular",
        "Itaú",
        "Bancolombia",
        "Citibank",
        "Banco GNB Sudameris",
        "BBVA Colombia",
        "Banco de Occidente",
        "Banco Caja Social",
        "Banco Davivienda",
        "Davibank",
        "Banco Agrario de Colombia",
        "AV Villas",
        "Ban100",
        "Bancamía",
        "Banco W",
        "Bancoomeva",
        "Banco Finandina",
        "Banco Falabella",
        "Banco Pichincha",
        "Coopcentral",
        "Banco Santander Colombia",
        "Banco Mundo Mujer",
        "Mibanco",
        "Banco Serfinanza",
        "Banco J.P. Morgan Colombia",
        "Lulo Bank",
        "Banco BTG Pactual Colombia",
        "Banco Unión",
        "Banco Contactar",
        "Revolut Bank Colombia",
    )

    swift_bank_codes = (
        "AGRA",
        "AVVI",
        "BBVA",
        "BCOM",
        "BCSC",
        "BFAL",
        "BNMA",
        "BOCC",
        "BOGO",
        "BSNT",
        "BWSA",
        "CITI",
        "COLO",
        "COOP",
        "CRED",
        "DAVI",
        "FDNA",
        "GNBS",
        "ITAU",
        "MIBA",
        "PICH",
        "POPU",
        "SCOL",
        "SERF",
        "UNIO",
    )
