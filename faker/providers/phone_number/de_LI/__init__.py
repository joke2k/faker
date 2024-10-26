from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Liechtenstein
    formats = ("%## ## ##", "+423 %## ## ##")
