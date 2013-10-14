from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+## ### ## ## ####',
        '+## ## #######',
        '+## ## ########',
        '+## ### #######',
        '+## ### ########',
        '+## #### #######',
        '+## #### ########'
    )