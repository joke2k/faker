from .. import Provider as BaseProvider
from collections import OrderedDict


localized = True


class Bill:
    def __init__(
            self,
            name,
            provider,
            provider_code,
            company_code,
            
            ):
        self.name = name
        self.provider = provider
        self.provider_code = provider_code
        self.company_code = company_code


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
