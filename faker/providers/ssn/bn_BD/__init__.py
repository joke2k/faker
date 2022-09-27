from .. import Provider as SsnProvider


class Provider(SsnProvider):
    """
    Implement SSN provider for ``bn_BD`` locale.
    National ID Card Number is considered the SSN number for
    Bangladeshi people.
    :example: '1882824588423'
    """

    ssn_formats = (
        "%############",
        "%## ### ####",
    )
