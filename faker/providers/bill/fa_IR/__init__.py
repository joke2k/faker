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

    water_company_codes = ["028"]
    electricity_company_codes = ["042"]
    gas_company_codes = ["062"]
    phone_company_codes = ["211"]
    mobile_company_codes = ["301"]
    municipality_company_codes = ["009"]

    # https://www.tavanir.org.ir/dm/dmmoshtarekin/doc/bill850530.pdf
    bill_types = OrderedDict((
        ('water', Bill('قبض آب', 'آبفا', "1", water_company_codes)),
        ('electricity', Bill('قبض برق', 'توانیر', "2", electricity_company_codes)),
        ('gas', Bill('قبض گاز', 'شرکت گاز', "3", gas_company_codes)),
        ('phone', Bill('قبض تلفن', 'مخابرات', "4", phone_company_codes)),
        ('mobile', Bill('قبض موبایل', 'همراه اول', "5", mobile_company_codes)),
        ('municipality', Bill('قبض عوارض شهرداری', 'شهرداری', "6", municipality_company_codes)),
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

    def bill_id(self, bill_type=None, company_code=None, client_case_code=None, provider_code=None):
        """ Returns a bill_id instance. """
        bill_id = self._bill_id(
            bill_type=bill_type, company_code=company_code,
            client_case_code=client_case_code, provider_code=provider_code
        )
        return bill_id + str(self._make_control_number(bill_id))

    def _bill_types(self, bill_type=None):
        """ Returns a random bill instance. """
        if bill_type is None:
            bill_type = self.random_element(self.bill_types.keys())
        elif isinstance(bill_type, Bill):
            return bill_type
        return self.bill_types[bill_type]

    def _bill_id(self, bill_type=None, company_code=None, client_case_code=None, provider_code=None):
        bill = self._bill_types(bill_type)
        if not company_code:
            company_code = self.random_element(bill.company_codes)
        if not client_case_code:
            client_case_code = str(self.random_int(100, 10000000))
        if not provider_code:
            provider_code = bill.provider_code
        bill_id = client_case_code + company_code + provider_code
        return bill_id

    @staticmethod
    def _make_control_number(bill_id):
        sum_number = 0
        ctrl_number = 2
        for number in bill_id[::-1]:
            sum_number += int(number) * ctrl_number
            if ctrl_number == 7:
                ctrl_number = 2
                continue
            ctrl_number += 1
        sum_number = sum_number % 11
        return 11 - sum_number if sum_number > 1 else 0
