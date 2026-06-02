from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "+998 (##) ###-##-##",
        "+998 (##) ### ## ##",
        "+998 (##) ### ####",
        "+998 (##) ###-####",
        "+998 ## ###-##-##",
        "+998 ## ### ## ##",
        "+998 ## ### ####",
        "+998 ## ###-####",
        "+998#########",
    )
