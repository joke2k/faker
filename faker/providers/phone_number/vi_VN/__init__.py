from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """Implement phone_number provider for ``vi_VN`` locale.
    # Source : https://vi.wikipedia.org/wiki/M%C3%A3_%C4%91i%E1%BB%87n_tho%E1%BA%A1i_Vi%E1%BB%87t_Nam
    """

    formats = (
        "+84 ## #######",
        "(0#) #### ####",
        "0# #### ####",
        "0# #######",
        "+84-##-######",
        "+84-##-### ####",
        "(0#)###-####",
    )
