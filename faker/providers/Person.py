from . import BaseProvider



class Provider(BaseProvider):

    formats = ['{{firstName}} {{lastName}}',]

    firstNames = ['John','Jane']

    lastNames = ['Doe',]

    def name(self):
        """
        :example 'Jhon Doe'
        """
        format = self.randomElement( self.formats )
        return self.generator.parse( format )

    @classmethod
    def firstName(cls):
        return cls.randomElement( cls.firstNames )

    @classmethod
    def lastName(cls):
        return cls.randomElement( cls.lastNames )
