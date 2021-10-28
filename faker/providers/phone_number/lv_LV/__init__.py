from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "+371 ########",
        "+(371) ########",
        "+371########",
    )
