from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "+36 ## ###-####",
        "(06)##/###-####",
        "(##)/###-####",
        "##/###-####",
        "##/### ####",
        "06-#/### ####",
        "06-##/### ####",
    )
