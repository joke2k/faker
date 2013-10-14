from . import BaseProvider

class Provider(BaseProvider):

    formats = ('###-###-###',)

    @classmethod
    def phoneNumber(cls):
        return cls.numerify( cls.randomElement( cls.formats ) )