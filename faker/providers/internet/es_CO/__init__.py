from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """Implement internet provider for ``es_CO`` locale.

    Source:
        - Colombian domain statistics: Ministerio de Tecnologías de la Información
        y las Comunicaciones
        https://gobernanzadeinternet.mintic.gov.co/752/w3-propertyvalue-198729.html
    """

    tlds = (
        "com",
        "com",
        "com",
        "net",
        "org",
        "co",
        "co",
        "co",
        "co",
        "com.co",
        "net.co",
        "nom.co",
    )
