from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source references (accessed 2026-04-18):
    # - https://dot.gov.in/numbering-resources (India numbering resources)
    # - Faker locale patterns in `phone_number/hi_IN` and `phone_number/ta_IN`
    # Patterns are intended for structurally valid synthetic Indian numbers.
    formats = (
        "+91 ##########",
        "+91 ### #######",
        "0##-########",
        "0##########",
        "0#### ######",
    )
