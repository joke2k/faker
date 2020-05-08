from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # Source: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Norway
    license_formats = (
        # Classic format
        '?? #####',
    )
