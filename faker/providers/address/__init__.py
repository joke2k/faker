# coding=utf-8
from __future__ import unicode_literals
from decimal import Decimal
import random

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
