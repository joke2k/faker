from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # Source (english): https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_France
    # Source (french gov) : https://immatriculation.ants.gouv.fr/Tout-savoir-sur-le-SIV/Le-Systeme-d-Immatriculation-des-Vehicules-SIV/Numero-logo-et-plaque
    license_formats = (
        # New format
        '??-###-??',
        # Old format for plates < 2009
        '###-???-##',
    )
