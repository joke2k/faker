from . import BaseProvider


class Provider(BaseProvider):
    formats = ['{{first_name}} {{last_name}}', ]

    first_names = ['John', 'Jane']

    last_names = ['Doe', ]

    def name(self):
        """
        :example 'Jhon Doe'
        """
        pattern = self.randomElement(self.formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_name(cls):
        return cls.randomElement(cls.first_names)

    @classmethod
    def last_name(cls):
        return cls.randomElement(cls.last_names)
