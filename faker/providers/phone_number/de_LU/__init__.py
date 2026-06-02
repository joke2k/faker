from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # https://de.wikipedia.org/wiki/Telefonvorwahl_(Luxemburg)
    formats = (
        "22 ## ##",
        "23 ## ##",
        "24 $# ## ##",
        "25 ## ##",
        "26 $# ## ##",
        "27 $# ## ##",
        "28 ## ##",
        "29 ## ##",
        "3# ## ##",
        "4 ### ##",
        "71 ## ##",
        "72 ## ##",
        "74 ## ##",
        "75 ## ##",
        "76 ## ##",
        "78 ## ##",
        "80 ## ##",
        "81 ## ##",
        "83 ## ##",
        "87 ## ##",
        "88 ## ##",
        "89 ## ##",
        "92 ## ##",
        "95 ## ##",
        "99 ## ##",
    )

    prefixes = ("+352 ", "")

    def phone_number(self) -> str:
        return self.random_element(self.prefixes) + self.numerify(self.random_element(self.formats))
