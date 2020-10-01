from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+90(###)#######',
        '+90 (###) #######',
        '0### ### ## ##',
        '0##########',
        '0###-### ####',
        '(###)### ####',
        '### # ###',
        '+90(###)###-####x###',
        '+90(###)###-####x####',
    )
