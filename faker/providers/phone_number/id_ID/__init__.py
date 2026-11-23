from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Currently this is my own work
    # The trunk prefix 0 is dropped after the +62 country code, so the digit
    # that follows +62 is never 0 (e.g. 021 becomes +62 21, 0812 becomes +62 812).
    formats = (
        "+62-%#-###-####",
        "+62 (%#) ### ####",
        "+62 (%#) ###-####",
        "+62-%##-###-####",
        "+62 (%##) ### ####",
        "+62 (%##) ###-####",
        "(0%#) ### ####",
        "(0%#) ###-####",
        "(0%##) ### ####",
        "(0%##) ###-####",
        "08# ### ####",
        "08########",
    )
