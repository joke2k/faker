from decimal import Decimal
import random
from . import BaseProvider
from . import DateTime



class Provider( BaseProvider ):

    citySuffixes = ['Ville',]
    streetSuffixes = ['Street',]
    cityFormats = ['{{firstName}} {{citySuffix}}',]
    streetNameFormats = ['{{lastName}} {{streetSuffix}}',]
    streetAddressFormats = ['{{buildingNumber}} {{streetName}}',]
    addressFormats = ['{{streetAddress}} {{postcode}} {{city}}',]
    buildingNumberFormats = ['##',]
    postcodeFormats = ['#####',]
    countries = [tz['name'] for tz in DateTime.Provider.countries]

    @classmethod
    def citySuffix(cls):
        """
        :example 'town'
        """
        return cls.randomElement( cls.citySuffixes )

    @classmethod
    def streetSuffix(cls):
        """
        :example 'Avenue'
        """
        return cls.randomElement( cls.streetSuffixes )

    @classmethod
    def buildingNumber(cls):
        """
        :example '791'
        """
        return cls.numerify( cls.randomElement( cls.buildingNumberFormats ) )

    def city(self):
        """
        :example 'Sashabury'
        """
        format = self.randomElement( self.cityFormats )
        return self.generator.parse( format )

    def streetName(self):
        """
        :example 'Crist Parks'
        """
        format = self.randomElement( self.streetNameFormats )
        return self.generator.parse( format )

    def streetAddress(self):
        """
        :example '791 Crist Parks'
        """
        format = self.randomElement( self.streetAddressFormats )
        return self.generator.parse( format )

    @classmethod
    def postcode(cls):
        """
        :example 86039-9874
        """
        return cls.bothify( cls.randomElement( cls.postcodeFormats ) ).upper()

    def address(self):
        """
        :example '791 Crist Parks, Sashabury, IL 86039-9874'
        """
        format = self.randomElement( self.addressFormats )
        return self.generator.parse( format )

    @classmethod
    def country(cls):
        return cls.randomElement( cls.countries )

    @classmethod
    def geo_coordinate(cls):
        return Decimal( random.randint(-180000000,180000000)/1000000.0 ).quantize(Decimal('.000001'))

    @classmethod
    def latitude(cls): return cls.geo_coordinate()

    @classmethod
    def longitude(cls): return cls.geo_coordinate()