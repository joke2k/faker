localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    formats = ('###-###-###',)

    def phone_number(self):
        return self.numerify(self.random_element(self.formats))
