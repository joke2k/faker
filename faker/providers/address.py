from decimal import Decimal
import random
from . import BaseProvider
from . import date_time


class Provider(BaseProvider):
    city_suffixes = ['Ville', ]
    street_suffixes = ['Street', ]
    city_formats = ['{{first_name}} {{city_suffix}}', ]
    street_name_formats = ['{{last_name}} {{street_suffix}}', ]
    street_address_formats = ['{{building_number}} {{street_name}}', ]
    address_formats = ['{{street_address}} {{postcode}} {{city}}', ]
    building_number_formats = ['##', ]
    postcode_formats = ['#####', ]
    countries = [tz['name'] for tz in date_time.Provider.countries]

    @classmethod
    def city_suffix(cls):
        """
        :example 'town'
        """
        return cls.randomElement(cls.city_suffixes)

    @classmethod
    def street_suffix(cls):
        """
        :example 'Avenue'
        """
        return cls.randomElement(cls.street_suffixes)

    @classmethod
    def building_number(cls):
        """
        :example '791'
        """
        return cls.numerify(cls.randomElement(cls.building_number_formats))

    def city(self):
        """
        :example 'Sashabury'
        """
        pattern = self.randomElement(self.city_formats)
        return self.generator.parse(pattern)

    def street_name(self):
        """
        :example 'Crist Parks'
        """
        pattern = self.randomElement(self.street_name_formats)
        return self.generator.parse(pattern)

    def street_address(self):
        """
        :example '791 Crist Parks'
        """
        pattern = self.randomElement(self.street_address_formats)
        return self.generator.parse(pattern)

    @classmethod
    def postcode(cls):
        """
        :example 86039-9874
        """
        return cls.bothify(cls.randomElement(cls.postcode_formats)).upper()

    def address(self):
        """
        :example '791 Crist Parks, Sashabury, IL 86039-9874'
        """
        pattern = self.randomElement(self.address_formats)
        return self.generator.parse(pattern)

    @classmethod
    def country(cls):
        return cls.randomElement(cls.countries)

    @classmethod
    def geo_coordinate(cls):
        return Decimal(random.randint(-180000000, 180000000) / 1000000.0).quantize(Decimal('.000001'))

    @classmethod
    def latitude(cls):
        return cls.geo_coordinate()

    @classmethod
    def longitude(cls):
        return cls.geo_coordinate()
