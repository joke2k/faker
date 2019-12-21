# coding=utf-8
from __future__ import unicode_literals
import re

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source:
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Saudi_Arabia

    cellphone_formats = (
        '{{country_code}} {{provider_code}} ### ####',
        '{{country_code}} {{provider_code}}#######',
        '{{country_code}}{{provider_code}}#######',
        '0{{provider_code}} ### ####',
        '0{{provider_code}}#######',
    )

    telephone_formats = (
        '{{country_code}} {{area_code}} ### ####',
        '{{country_code}} {{area_code}}#######',
        '{{country_code}}{{area_code}}#######',
        '0{{area_code}} ### ####',
        '0{{area_code}}#######',
    )

    cellphone_msisdn_formats = (
        '966{{provider_code}}#######',
    )

    telephone_msisdn_formats = (
        '966{{area_code}}#######',
    )

    def provider_code(self):
        return self.random_element((
            '50',
            '53',
            '55',
            '51',
            '58',
            '59',
            '54',
            '56',
            '570',
            '571',
            '572',
            '576',
            '577',
            '578',
        ))

    def country_code(self):
        return self.random_element((
            '00966',
            '+966',
            '966',
        ))

    def area_code(self):
        return self.random_element((
            '11',
            '12',
            '13',
            '14',
            '16',
            '17',
        ))

    def cellphone_number(self):
        pattern = self.random_element(self.cellphone_formats)
        text = self.generator.parse(pattern)
        provider_code = re.search(r'5\d+', text).group()

        # Slice text if provider code is more than two digits, since phone number must be 10 digits long
        if len(provider_code) > 2:
            text = text[:2-len(provider_code)]

        return self.numerify(text)

    def cellphone_msisdn(self):
        pattern = self.random_element(self.cellphone_msisdn_formats)
        text = self.generator.parse(pattern)
        provider_code = re.search(r'5\d+', text).group()

        # Slice text if provider code is more than two digits, since phone number must be 10 digits long
        if len(provider_code) > 2:
            text = text[:2 - len(provider_code)]

        return self.numerify(text)

    def telephone_number(self):
        pattern = self.random_element(self.telephone_formats)
        return self.numerify(self.generator.parse(pattern))

    def telephone_msisdn(self):
        pattern = self.random_element(self.telephone_msisdn_formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number(self):
        phone_number = self.random_element((
            self.telephone_number,
            self.cellphone_number,
        ))
        return phone_number()

    def msisdn(self):
        msisdn = self.random_element((
            self.telephone_msisdn,
            self.cellphone_msisdn,
        ))
        return msisdn()
