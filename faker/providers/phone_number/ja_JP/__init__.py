from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '070-####-####',
        '080-####-####',
        '090-####-####',
        '##-####-####',
    )
