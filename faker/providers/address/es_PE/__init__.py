from ..es import Provider as AddressProvider


class Provider(AddressProvider):
    """
    A Faker provider for the Spanish-Peru (es_PE) locale.

    Sources:
    - Departments: https://en.wikipedia.org/wiki/Departments_of_Peru
    - Cities: https://en.wikipedia.org/wiki/List_of_cities_in_Peru
    - Official statistics and administrative divisions: https://www.inei.gob.pe
    Accessed: 2026-02-07
    """

    # Postcode format for Peru is 5 digits (kept from base provider if applicable)
    postcode_formats = ("#####",)
