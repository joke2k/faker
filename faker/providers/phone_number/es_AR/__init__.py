from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    According to official specs:
    https://es.wikipedia.org/wiki/N%C3%BAmeros_telef%C3%B3nicos_en_Argentina
    https://www.argentina.gob.ar/pais/codigo-telefonia
    """

    formats = (
        "+54 15 2%## ####",  # National telephone to mobile phone
        "+54 9 3%## ####",  # International phone}
    )

    landline_codes = (
        "351",  # Córdoba (capital city of Córdoba province)
        "379",  # Corrientes (capital city of Corrientes province)
        "221",  # La Plata (capital city of Buenos Aires province)
        "380",  # La Rioja (capital city of La Rioja province)
        "261",  # Mendoza (capital city of Mendoza province)
        "299",  # Neuquén (capital city of Neuquén province)
        "343",  # Paraná (capital city of Entre Ríos province)
        "376",  # Posadas (capital city of Misiones province)
        "280",  # Rawson (capital city of Chubut province)
        "362",  # Resistencia (capital city of Chaco province)
        "2966",  # Río Gallegos (capital city of Santa Cruz province)
        "387",  # Salta (capital city of Salta province)
        "383",  # San Fernando del Valle de Catamarca (capital city of Catamarca province)
        "264",  # San Juan (capital city of San Juan province)
        "266",  # San Luis (capital city of San Luis province)
        "381",  # San Miguel de Tucumán (capital city of Tucumán province)
        "388",  # San Salvador de Jujuy (capital city of Jujuy province)
        "342",  # Santa Fe (capital city of Santa Fe province)
        "2954",  # Santa Rosa (capital city of La Pampa province)
        "385",  # Santiago del Estero (capital city of Santiago del Estero province)
        "391",  # Ushuaia (capital city of Tierra del Fuego province)
        "2920",  # Viedma (capital city of Rio Negro province)
    )

    special_codes = (
        "600",  # Nationalwide
        "800",  # Nationalwide, toll-free
    )

    cellphone_blocks = ("2", "3", "4", "5", "6", "7", "8", "9")
