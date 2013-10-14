from . import BaseProvider



class Provider( BaseProvider ):

    formats = ['{{lastName}} {{companySuffix}}',]

    companySuffixes = ['Ltd',]

    def company(self):
        """
        :example 'Acme Ltd'
        """
        format = self.randomElement( self.formats )
        return self.generator.parse( format )

    @classmethod
    def companySuffix(cls):
        """
        :example 'Ltd'
        """
        return cls.randomElement( cls.companySuffixes )
