from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):

    # From: https://pt.wikipedia.org/wiki/Matr%C3%ADculas_de_autom%C3%B3veis_em_Portugal
    license_formats = (
        '##-##-??',
        '##-??-##',
        '??-##-##',
    )
