from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "###-##-##",
        "### ## ##",
        "0## ### ## ##",
        "0## ###-##-##",
        "+380 ## ###-##-##",
        "+380 ## ###-##-##",
        "+380 (##) ###-##-##",
        "+380 ## ### ## ##",
    )
