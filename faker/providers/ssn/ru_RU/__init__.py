from .. import Provider as SsnProvider


class Provider(SsnProvider):
    """
    A Faker provider for the Russian SSN
    """
    ssn_formats = ("############",)
