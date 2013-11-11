from __future__ import unicode_literals
from . import BaseProvider


class Provider(BaseProvider):
    formats = ['{{first_name}} {{last_name}}', ]

    first_names = ['John', 'Jane']

    last_names = ['Doe', ]

    def name(self):
        """
        :example 'Jhon Doe'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_name(cls):
        return cls.random_element(cls.first_names)

    @classmethod
    def last_name(cls):
        return cls.random_element(cls.last_names)
