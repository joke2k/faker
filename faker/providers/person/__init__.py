from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    formats = ['{{first_name}} {{last_name}}']

    first_names = ['John', 'Jane']

    last_names = ['Doe']

    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    language_names = [
        'Afar', 'Abkhazian', 'Avestan', 'Afrikaans', 'Akan', 'Amharic',
        'Aragonese', 'Arabic', 'Assamese', 'Avaric', 'Aymara', 'Azerbaijani',
        'Bashkir', 'Belarusian', 'Bulgarian', 'Bihari languages', 'Bislama',
        'Bambara', 'Bengali', 'Tibetan', 'Breton', 'Bosnian', 'Catalan',
        'Chechen', 'Chamorro', 'Corsican', 'Cree', 'Czech', 'Church Slavic',
        'Chuvash', 'Welsh', 'Danish', 'German', 'Divehi', 'Dzongkha', 'Ewe',
        'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque',
        'Persian', 'Fulah', 'Finnish', 'Fijian', 'Faroese', 'French',
        'Western Frisian', 'Irish', 'Gaelic', 'Galician', 'Guarani',
        'Gujarati', 'Manx', 'Hausa', 'Hebrew', 'Hindi', 'Hiri Motu',
        'Croatian', 'Haitian', 'Hungarian', 'Armenian', 'Herero',
        'Interlingua', 'Indonesian', 'Interlingue', 'Igbo', 'Sichuan Yi',
        'Inupiaq', 'Ido', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese',
        'Javanese', 'Georgian', 'Kongo', 'Kikuyu', 'Kuanyama', 'Kazakh',
        'Kalaallisut', 'Central Khmer', 'Kannada', 'Korean', 'Kanuri',
        'Kashmiri', 'Kurdish', 'Komi', 'Cornish', 'Kirghiz', 'Latin',
        'Luxembourgish', 'Ganda', 'Limburgan', 'Lingala', 'Lao', 'Lithuanian',
        'Luba-Katanga', 'Latvian', 'Malagasy', 'Marshallese', 'Maori',
        'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese',
        'Burmese', 'Nauru', 'North Ndebele', 'Nepali',
        'Ndonga', 'Dutch', 'Norwegian Nynorsk', 'Norwegian', 'South Ndebele',
        'Navajo', 'Chichewa', 'Occitan', 'Ojibwa', 'Oromo', 'Oriya',
        'Ossetian', 'Panjabi', 'Pali', 'Polish', 'Pushto', 'Portuguese',
        'Quechua', 'Romansh', 'Rundi', 'Romanian', 'Russian', 'Kinyarwanda',
        'Sanskrit', 'Sardinian', 'Sindhi', 'Northern Sami', 'Sango', 'Sinhala',
        'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Somali', 'Albanian',
        'Serbian', 'Swati', 'Sotho, Southern', 'Sundanese', 'Swedish',
        'Swahili', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tigrinya', 'Turkmen',
        'Tagalog', 'Tswana', 'Tonga', 'Turkish', 'Tsonga', 'Tatar', 'Twi',
        'Tahitian', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda',
        'Vietnamese', 'Walloon', 'Wolof', 'Xhosa', 'Yiddish',
        'Yoruba', 'Zhuang', 'Chinese', 'Zulu',
    ]

    def name(self):
        """
        :example 'John Doe'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    def first_name(self):
        return self.random_element(self.first_names)

    def last_name(self):
        return self.random_element(self.last_names)

    def name_male(self):
        if hasattr(self, 'formats_male'):
            formats = self.formats_male
        else:
            formats = self.formats
        pattern = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_nonbinary(self):
        if hasattr(self, 'formats_nonbinary'):
            formats = self.formats_nonbinary
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

    def first_name_male(self):
        if hasattr(self, 'first_names_male'):
            return self.random_element(self.first_names_male)
        return self.first_name()

    def first_name_nonbinary(self):
        if hasattr(self, 'first_names_nonbinary'):
            return self.random_element(self.first_names_nonbinary)
        return self.first_name()

    def first_name_female(self):
        if hasattr(self, 'first_names_female'):
            return self.random_element(self.first_names_female)
        return self.first_name()

    def last_name_male(self):
        if hasattr(self, 'last_names_male'):
            return self.random_element(self.last_names_male)
        return self.last_name()

    def last_name_nonbinary(self):
        if hasattr(self, 'last_names_nonbinary'):
            return self.random_element(self.last_names_nonbinary)
        return self.last_name()

    def last_name_female(self):
        if hasattr(self, 'last_names_female'):
            return self.random_element(self.last_names_female)
        return self.last_name()

    def prefix(self):
        if hasattr(self, 'prefixes'):
            return self.random_element(self.prefixes)
        if hasattr(self, 'prefixes_male') and hasattr(self, 'prefixes_female') and hasattr(self, 'prefixes_nonbinary'):
            prefixes = self.random_element(
                (self.prefixes_male, self.prefixes_female, self.prefixes_nonbinary))
            return self.random_element(prefixes)
        if hasattr(self, 'prefixes_male') and hasattr(self, 'prefixes_female'):
            prefixes = self.random_element(
                (self.prefixes_male, self.prefixes_female))
            return self.random_element(prefixes)
        return ''

    def prefix_male(self):
        if hasattr(self, 'prefixes_male'):
            return self.random_element(self.prefixes_male)
        return self.prefix()

    def prefix_nonbinary(self):
        if hasattr(self, 'prefixes_nonbinary'):
            return self.random_element(self.prefixes_nonbinary)
        return self.prefix()

    def prefix_female(self):
        if hasattr(self, 'prefixes_female'):
            return self.random_element(self.prefixes_female)
        return self.prefix()

    def suffix(self):
        if hasattr(self, 'suffixes'):
            return self.random_element(self.suffixes)
        if hasattr(self, 'suffixes_male') and hasattr(self, 'suffixes_female') and hasattr(self, 'suffixes_nonbinary'):
            suffixes = self.random_element(
                (self.suffixes_male, self.suffixes_female, self.suffixes_nonbinary))
            return self.random_element(suffixes)
        if hasattr(self, 'suffixes_male') and hasattr(self, 'suffixes_female'):
            suffixes = self.random_element(
                (self.suffixes_male, self.suffixes_female))
            return self.random_element(suffixes)
        return ''

    def suffix_male(self):
        if hasattr(self, 'suffixes_male'):
            return self.random_element(self.suffixes_male)
        return self.suffix()

    def suffix_nonbinary(self):
        if hasattr(self, 'suffixes_nonbinary'):
            return self.random_element(self.suffixes_nonbinary)
        return self.suffix()

    def suffix_female(self):
        if hasattr(self, 'suffixes_female'):
            return self.random_element(self.suffixes_female)
        return self.suffix()

    def language_name(self):
        """Generate a random i18n language name (e.g. English)."""
        return self.random_element(self.language_names)
