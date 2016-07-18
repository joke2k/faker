localized = True
import random
from .. import BaseProvider


class Provider(BaseProvider):
    formats = ('###-###-###',)
    country_code = '1'

    @classmethod
    def phone_number(cls):
        return cls.numerify(random.choice(['+' + cls.country_code + ' ', '']) + cls.random_element(cls.formats))

    @classmethod
    def phone_number_with_country_code(cls):
        return cls.numerify('+' + cls.country_code + cls.random_element(cls.formats))

    @classmethod
    def phone_number_without_country_code(cls):
        return cls.numerify(cls.random_element(cls.formats))
