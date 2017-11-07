from .. import Provider as BankProvider


class Provider(BankProvider):
    # no IBAN in en_US! but need to provide a class for the tests!
    bban_format = '??##'
    country_code = 'US'
