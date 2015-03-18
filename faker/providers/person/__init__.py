localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    formats = ['{{first_name}} {{last_name}}', ]

    first_names = ['John', 'Jane']

    last_names = ['Doe', ]

    def name(self):
        """
        :example 'John Doe'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_name(cls):
        return cls.random_element(cls.first_names)

    @classmethod
    def last_name(cls):
        return cls.random_element(cls.last_names)

    def name_male(self):
        if hasattr(self, 'formats_male'):
            formats = self.formats_male
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_female(self):
        if hasattr(self, 'formats_female'):
            formats = self.formats_female
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    @classmethod
    def first_name_male(cls):
        if hasattr(cls, 'first_names_male'):
            return cls.random_element(cls.first_names_male)
        return cls.first_name()

    @classmethod
    def first_name_female(cls):
        if hasattr(cls, 'first_names_female'):
            return cls.random_element(cls.first_names_female)
        return cls.first_name()

    @classmethod
    def last_name_male(cls):
        if hasattr(cls, 'last_names_male'):
            return cls.random_element(cls.last_names_male)
        return cls.last_name()

    @classmethod
    def last_name_female(cls):
        if hasattr(cls, 'last_names_female'):
            return cls.random_element(cls.last_names_female)
        return cls.last_name()


    @classmethod
    def prefix(cls):
        if hasattr(cls, 'prefixes'):
            return cls.random_element(cls.prefixes)
        if hasattr(cls, 'prefixes_male') and hasattr(cls, 'prefixes_female'):
            prefixes = cls.random_element((cls.prefixes_male, cls.prefixes_female))
            return cls.random_element(prefixes)
        return ''

    @classmethod
    def prefix_male(cls):
        if hasattr(cls, 'prefixes_male'):
            return cls.random_element(cls.prefixes_male)
        return cls.prefix()

    @classmethod
    def prefix_female(cls):
        if hasattr(cls, 'prefixes_female'):
            return cls.random_element(cls.prefixes_female)
        return cls.prefix()

    @classmethod
    def suffix(cls):
        if hasattr(cls, 'suffixes'):
            return cls.random_element(cls.suffixes)
        if hasattr(cls, 'suffixes_male') and hasattr(cls, 'suffixes_female'):
            suffixes = cls.random_element((cls.suffixes_male, cls.suffixes_female))
            return cls.random_element(suffixes)
        return ''

    @classmethod
    def suffix_male(cls):
        if hasattr(cls, 'suffixes_male'):
            return cls.random_element(cls.suffixes_male)
        return cls.suffix()

    @classmethod
    def suffix_female(cls):
        if hasattr(cls, 'suffixes_female'):
            return cls.random_element(cls.suffixes_female)
        return cls.suffix()
