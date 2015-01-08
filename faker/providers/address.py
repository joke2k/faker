# coding=utf-8

from __future__ import unicode_literals
from decimal import Decimal
import random
from . import BaseProvider
from . import date_time


class Provider(BaseProvider):
    city_suffixes = ['Ville', ]
    street_suffixes = ['Street', ]
    city_formats = ('{{first_name}} {{city_suffix}}', )
    street_name_formats = ('{{last_name}} {{street_suffix}}', )
    street_address_formats = ('{{building_number}} {{street_name}}', )
    address_formats = ('{{street_address}} {{postcode}} {{city}}', )
    building_number_formats = ('##', )
    postcode_formats = ('#####', )
    countries = [tz['name'] for tz in date_time.Provider.countries]
    country_codes = [u'AF', u'AX', u'AL', u'DZ', u'AS', u'AD', u'AO', u'AI', u'AQ', u'AG', u'AR', u'AM', u'AW', u'AU',
                     u'AT', u'AZ', u'BS', u'BH', u'BD', u'BB', u'BY', u'BE', u'BZ', u'BJ', u'BM', u'BT', u'BO', u'BA',
                     u'BW', u'BV', u'BR', u'IO', u'BN', u'BG', u'BF', u'BI', u'KH', u'CM', u'CA', u'CV', u'KY', u'CF',
                     u'TD', u'CL', u'CN', u'CX', u'CC', u'CO', u'KM', u'CG', u'CD', u'CK', u'CR', u'CI', u'HR', u'CU',
                     u'CY', u'CZ', u'DK', u'DJ', u'DM', u'DO', u'EC', u'EG', u'SV', u'GQ', u'ER', u'EE', u'ET', u'FK',
                     u'FO', u'FJ', u'FI', u'FR', u'GF', u'PF', u'TF', u'GA', u'GM', u'GE', u'DE', u'GH', u'GI', u'GR',
                     u'GL', u'GD', u'GP', u'GU', u'GT', u'GG', u'GN', u'GW', u'GY', u'HT', u'HM', u'VA', u'HN', u'HK',
                     u'HU', u'IS', u'IN', u'ID', u'IR', u'IQ', u'IE', u'IM', u'IL', u'IT', u'JM', u'JP', u'JE', u'JO',
                     u'KZ', u'KE', u'KI', u'KP', u'KR', u'KW', u'KG', u'LA', u'LV', u'LB', u'LS', u'LR', u'LY', u'LI',
                     u'LT', u'LU', u'MO', u'MK', u'MG', u'MW', u'MY', u'MV', u'ML', u'MT', u'MH', u'MQ', u'MR', u'MU',
                     u'YT', u'MX', u'FM', u'MD', u'MC', u'MN', u'MS', u'MA', u'MZ', u'MM', u'NA', u'NR', u'NP', u'NL',
                     u'AN', u'NC', u'NZ', u'NI', u'NE', u'NG', u'NU', u'NF', u'MP', u'NO', u'OM', u'PK', u'PW', u'PS',
                     u'PA', u'PG', u'PY', u'PE', u'PH', u'PN', u'PL', u'PT', u'PR', u'QA', u'RE', u'RO', u'RU', u'RW',
                     u'SH', u'KN', u'LC', u'PM', u'VC', u'WS', u'SM', u'ST', u'SA', u'SN', u'CS', u'SC', u'SL', u'SG',
                     u'SK', u'SI', u'SB', u'SO', u'ZA', u'GS', u'ES', u'LK', u'SD', u'SR', u'SJ', u'SZ', u'SE', u'CH',
                     u'SY', u'TW', u'TJ', u'TZ', u'TH', u'TL', u'TG', u'TK', u'TO', u'TT', u'TN', u'TR', u'TM', u'TC',
                     u'TV', u'UG', u'UA', u'AE', u'GB', u'US', u'UM', u'UY', u'UZ', u'VU', u'VE', u'VN', u'VG', u'VI',
                     u'WF', u'EH', u'YE', u'ZM', u'ZW']

    @classmethod
    def city_suffix(cls):
        """
        :example 'town'
        """
        return cls.random_element(cls.city_suffixes)

    @classmethod
    def street_suffix(cls):
        """
        :example 'Avenue'
        """
        return cls.random_element(cls.street_suffixes)

    @classmethod
    def building_number(cls):
        """
        :example '791'
        """
        return cls.numerify(cls.random_element(cls.building_number_formats))

    def city(self):
        """
        :example 'Sashabury'
        """
        pattern = self.random_element(self.city_formats)
        return self.generator.parse(pattern)

    def street_name(self):
        """
        :example 'Crist Parks'
        """
        pattern = self.random_element(self.street_name_formats)
        return self.generator.parse(pattern)

    def street_address(self):
        """
        :example '791 Crist Parks'
        """
        pattern = self.random_element(self.street_address_formats)
        return self.generator.parse(pattern)

    @classmethod
    def postcode(cls):
        """
        :example 86039-9874
        """
        return cls.bothify(cls.random_element(cls.postcode_formats)).upper()

    def address(self):
        """
        :example '791 Crist Parks, Sashabury, IL 86039-9874'
        """
        pattern = self.random_element(self.address_formats)
        return self.generator.parse(pattern)

    @classmethod
    def country(cls):
        return cls.random_element(cls.countries)

    @classmethod
    def country_code(cls):
        return cls.random_element(cls.country_codes)

    @classmethod
    def geo_coordinate(cls, center=None, radius=0.001):
        """
        Optionally center the coord and pick a point within radius.
        """
        if not center:
            return Decimal(str(random.randint(-180000000, 180000000) / 1000000.0)).quantize(Decimal('.000001'))
        else:
            geo = random.uniform(center - radius, center + radius)
            return Decimal(str(geo))

    @classmethod
    def latitude(cls):
        # Latitude has a range of -90 to 90, so divide by two.
        return cls.geo_coordinate() / 2

    @classmethod
    def longitude(cls):
        return cls.geo_coordinate()
