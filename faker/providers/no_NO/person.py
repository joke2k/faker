# coding=utf-8
from __future__ import unicode_literals
from ..person import Provider as PersonProvider

class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{prefix}} {{first_name_male}} {{last_name}}',
        '{{prefix}} {{first_name_female}} {{last_name}}',
    )

    first_names_male = (
'Adrian',
'Aksel',
'Alexander',
'Anders',
'Andreas',
'Benjamin',
'Daniel',
'Eirik',
'Elias',
'Emil',
'Erik',
'Even',
'Filip',
'Fredrik',
'Håkon',
'Henrik',
'Herman',
'Isak',
'Jakob',
'Joakim',
'Johannes',
'Jonas',
'Jonathan',
'Jørgen',
'Kasper',
'Kristian',
'Kristoffer',
'Lars',
'Lucas',
'Magnus',
'Marius',
'Markus',
'Martin',
'Mathias',
'Mats',
'Mikkel',
'Nikolai',
'Noah',
'Ole',
'Oliver',
'Oskar',
'Sander',
'Sebastian',
'Simen',
'Sindre',
'Sondre',
'Theodor',
'Thomas',
'Tobias',
'William',
    )

    first_names_female = (
'Amalie',
'Andrea',
'Anna',
'Aurora',
'Camilla',
'Celine',
'Eline',
'Elise',
'Emilie',
'Emma',
'Frida',
'Hanna',
'Hedda',
'Helene',
'Ida',
'Ingrid',
'Jenny',
'Julie',
'Kaja',
'Karoline',
'Kristine',
'Leah',
'Linnea',
'Madeleine'
'Maja',
'Malin',
'Maren',
'Mari',
'Maria',
'Marie',
'Marte',
'Martine',
'Mathilde',
'Mia',
'Mina',
'Natalie',
'Nora',
'Oda',
'Sandra',
'Sara',
'Selma',
'Silje',
'Sofie',
'Sunniva',
'Synne',
'Thea',
'Tiril',
'Tuva',
'Victoria',
'Vilde',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Aalerud', 'Aas', 'Aasen', 'Amundsen', 'Andersen', 'Andreassen',
        'Andresen', 'Arnesen', 'Bakke', 'Bakken', 'Berg', 'Berge', 'Berntsen',
        'Bjerke', 'Bjørnstad', 'Borge', 'Carlsen', 'Christiansen', 'Dahl',
        'Danielsen', 'Edvardsen', 'Eide', 'Eriksen', 'Evensen', 'Finstad',
        'Fjeld', 'Fossum', 'Fredriksen', 'Glosli', 'Gran', 'Gundersen',
        'Hagen', 'Halvorsen', 'Hansen', 'Haugen', 'Haukelidsæter', 'Henriksen',
        'Holm', 'Hopland', 'Huseby', 'Jacobsen', 'Jakobsen', 'Jensen',
        'Johannessen', 'Johansen', 'Johnsen', 'Jørgensen', 'Karlsen', 'Kleven',
        'Kristensen', 'Kristiansen', 'Kristoffersen', 'Krogh', 'Kvarme',
        'Larsen', 'Lie', 'Løken', 'Lunde', 'Martinsen', 'Mathisen', 'Moe',
        'Moen', 'Myhrer', 'Nguyen', 'Nielsen', 'Nilsen', 'Nordby', 'Nordskaug',
        'Nygård', 'Ødegård', 'Olsen', 'Olstad', 'Østby', 'Østli', 'Pedersen',
        'Pettersen', 'Rasmussen', 'Røed', 'Ruud', 'Ryan', 'Sæther', 'Skoglund',
        'Skuterud', 'Smedsrud', 'Smogeli', 'Solberg', 'Solheim', 'Solli',
        'Sørensen', 'Sørlie', 'Stensrud', 'Strand', 'Svendsen', 'Tangen',
        'Thoresen', 'Torgersen', 'Torp', 'Vedvik', 'Vegge', 'Vik', 'Wold',
    )

    prefixes = (
        'Dr.', 'Prof.',
    )

    @classmethod
    def first_name(cls):
        return cls.random_element(cls.first_names)

    @classmethod
    def first_name_male(cls):
        return cls.random_element(cls.first_names_male)

    @classmethod
    def first_name_female(cls):
        return cls.random_element(cls.first_names_female)

    @classmethod
    def prefix(cls):
        return cls.random_element(cls.prefixes)

    @classmethod
    def prefix_male(cls):
        return cls.random_element(cls.prefixes)

    @classmethod
    def prefix_female(cls):
        return cls.random_element(cls.prefixes)

