# coding=utf-8
from __future__ import unicode_literals
from ..fr_FR import Provider as AddressProvider


class Provider(AddressProvider):
    city_suffixes = ('-des-Bois', '-les-Bains', '-la-Ville', '-Dessus', 
        '-Dessous', ' am Rhein', ' am See', ' am Albis', ' an der Aare'
    )
    city_prefixes = ('Saint ', 'Sainte ', 'San ', 'Ober', 'Unter')
    city_formats = (
        '{{last_name}}',
        '{{last_name}}',
        '{{last_name}}',
        '{{last_name}}',
        '{{last_name}}{{city_suffix}}',
        '{{last_name}}{{city_suffix}}',
        '{{last_name}}{{city_suffix}}',
        '{{last_name}}-près-{{last_name}}',
        '{{last_name}}-sur-{{last_name}}',
        '{{city_prefix}}{{last_name}}',
        '{{last_name}} ({{canton_code}})',
    )

    street_address_formats = (
        '{{street_name}}',
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}}',
    )

    postcode_formats = ('1###', '2###', '3###', '4###', '5###', '6###', '7###',
        '8###', '9###'
    )
    
    cantons = (
        ('AG', 'Argovie'), ('AI', 'Appenzell Rhodes-Intérieures'), 
        ('AR', 'Appenzell Rhodes-Extérieures'), ('BE', 'Berne'), 
        ('BL', 'Bâle-Campagne'), ('BS', 'Bâle-Ville'), ('FR', 'Fribourg'),
        ('GE', 'Genève'), ('GL', 'Glaris'), ('GR', 'Grisons'), ('JU', 'Jura'),
        ('LU', 'Lucerne'), ('NE', 'Neuchâtel'), ('NW', 'Nidwald'), 
        ('OW', 'Obwald'), ('SG', 'Saint-Gall'), ('SH', 'Schaffhouse'), 
        ('SO', 'Soleure'), ('SZ', 'Schwytz'), ('TG', 'Thurgovie'), 
        ('TI', 'Tessin'), ('UR', 'Uri'), ('VD', 'Vaud'), ('VS', 'Valais'),
        ('ZG', 'Zoug'), ('ZH', 'Zurich')
    )

    @classmethod
    def street_prefix(cls):
        """
        :example 'rue'
        """
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def canton(cls):
        """
        Randomly returns a swiss canton ('Abbreviated' , 'Name').
        :example ('VD' . 'Vaud')
        """
        return cls.random_element(cls.cantons)

    @classmethod
    def canton_name(cls):
        """
        Randomly returns a Swiss canton name.
        :example 'Vaud'
        """
        return cls.canton()[1]

    @classmethod
    def canton_code(cls):
        """
        Randomly returns a Swiss canton code.
        :example 'VD'
        """
        return cls.canton()[0]



