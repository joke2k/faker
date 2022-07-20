from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``pt_BR`` locale."""
    # New format since March 2017

    license_formats = ("???-####",)
