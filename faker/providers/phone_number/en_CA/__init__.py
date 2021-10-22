from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "%##-###-####",
        "%##.###.####",
        "%## ### ####",
        "(%##) ###-####",
        "1-%##-###-####",
        "1 (%##) ###-####",
        "+1 (%##) ###-####",
        "%##-###-#### x###",
        "(%##) ###-#### x###",
    )
