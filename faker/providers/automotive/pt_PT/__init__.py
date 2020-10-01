from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``pt_PT`` locale.

    Sources:

    - https://pt.wikipedia.org/wiki/Matr%C3%ADculas_de_autom%C3%B3veis_em_Portugal
    """

    license_formats = (
        '##-##-??',
        '##-??-##',
        '??-##-##',
    )
