from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "+84 ## #######",
        "(0#) #### ####",
        "0# #### ####",
        "0# #######",
        "+84-##-######",
        "+84-##-### ####",
        "(0#)###-####",
    )
