from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "+45 ########",
        "+45 #### ####",
        "+45 ## ## ## ##",
        "########",
        "#### ####",
        "## ## ## ##",
    )
