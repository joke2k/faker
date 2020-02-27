from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # Source (english): https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_France
    license_formats = (
        # New format
        '??-###-??',
        # Old format for plates < 2009
        '###-???-##',
    )
