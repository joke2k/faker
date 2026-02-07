# faker/providers/automotive/es_PE/__init__.py

from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """
    Implement automotive provider for ``es_PE`` locale.

    Sources:
    - Vehicle registration plates of Peru: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Peru
    Accessed: 2026-02-07
    """

    # Common formats (examples):
    license_format_modern = "???-###"
    license_format_previous = "??-####"
