from .. import Provider as BaseProvider
from collections import OrderedDict


localized = True


class Bill:
    def __init__(
            self,
            name,
            provider,
            provider_code,
            company_codes,
            ):
        self.name = name
        self.provider = provider
        self.provider_code = provider_code
        self.company_codes = company_codes


class Provider(BaseProvider):

    water_company_codes = []
    electricity_company_codes = []
    gas_company_codes = []
    phone_company_codes = []
    mobile_company_codes = []
    municipality_company_codes = []

    # https://www.tavanir.org.ir/dm/dmmoshtarekin/doc/bill850530.pdf
    bill_types = OrderedDict((
        ('water', Bill('قبض آب', 'آبفا', 1, water_company_codes)),
        ('electricity', Bill('قبض برق', 'توانیر', 2, electricity_company_codes)),
        ('gas', Bill('قبض گاز', 'شرکت گاز', 3, gas_company_codes)),
        ('phone', Bill('قبض تلفن', 'مخابرات', 4, phone_company_codes)),
        ('mobile', Bill('قبض موبایل', 'همراه اول', 5, mobile_company_codes)),
        ('municipality', Bill('قبض عوارض شهرداری', 'شهرداری', 6, municipality_company_codes)),
    ))

    def bill_provider(self, bill_type=None):
        """ Returns the name of the bill. """
        if bill_type is None:
            bill_type = self.random_element(self.bill_types.keys())
        return self._bill_types(bill_type).provider

    def bill_name(self, bill_type=None):
        """ Returns the provider's name of the bill. """
        if bill_type is None:
            bill_type = self.random_element(self.bill_types.keys())
        return self._bill_types(bill_type).name

    def _bill_types(self, bill_type=None):
        """ Returns a random bill instance. """
        if bill_type is None:
            bill_type = self.random_element(self.bill_types.keys())
        elif isinstance(bill_type, Bill):
            return bill_type
        return self.bill_types[bill_type]
