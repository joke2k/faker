# coding=utf-8
from __future__ import unicode_literals
from decimal import Decimal

from .. import BaseProvider
from .. import date_time

localized = True


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
    country_codes = [tz['code'] for tz in date_time.Provider.countries]

    def city_suffix(self):
        """
        :example 'town'
        """
        return self.random_element(self.city_suffixes)

    def street_suffix(self):
        """
        :example 'Avenue'
        """
        return self.random_element(self.street_suffixes)

    def building_number(self):
        """
        :example '791'
        """
        return self.numerify(self.random_element(self.building_number_formats))

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

    def postcode(self):
        """
        :example 86039-9874
        """
        return self.bothify(self.random_element(self.postcode_formats)).upper()

    def address(self):
        """
        :example '791 Crist Parks, Sashabury, IL 86039-9874'
        """
        pattern = self.random_element(self.address_formats)
        return self.generator.parse(pattern)

    def country(self):
        return self.random_element(self.countries)

    def country_code(self):
        return self.random_element(self.country_codes)

    def geo_coordinate(self, center=None, radius=0.001):
        """
        Optionally center the coord and pick a point within radius.
        """
        if center is None:
            return Decimal(str(self.generator.random.randint(-180000000, 180000000) / 1000000.0)).quantize(Decimal('.000001'))
        else:
            center = float(center)
            radius = float(radius)
            geo = self.generator.random.uniform(center - radius, center + radius)
            return Decimal(str(geo)).quantize(Decimal('.000001'))

    def latitude(self):
        # Latitude has a range of -90 to 90, so divide by two.
        return self.geo_coordinate() / 2

    def longitude(self):
        return self.geo_coordinate()
