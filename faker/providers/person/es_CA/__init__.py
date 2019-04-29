# coding=utf-8
from __future__ import unicode_literals
from ..es_ES import Provider as PersonProvider


class Provider(PersonProvider):
    """
    Adds popular Catalan names to the spanish ones.
    https://www.idescat.cat/pub/?id=aec&n=946&lang=es
    """
    first_names_male = tuple(set(PersonProvider.first_names_male + (
        'Marc',
        'Àlex',
        'Álex',
        'Pol',
        'Nil',
        'Jan',
        'Hugo',
        'Martí',
        'Èric',
        'Eric',
        'Lucas',
        'Biel',
        'Pau',
        'Leo',
        'Arnau',
        'Aleix',
        'Bruno',
        'Enzo',
        'Daniel',
        'Adam',
        'Max',
        'David')))

    first_names_female = tuple(set(PersonProvider.first_names_male + (
        'Júlia',
        'Julia',
        'Martina',
        'Emma',
        'Maria',
        'María',
        'Lucia',
        'Laia',
        'Paula',
        'Sofía',
        'Sofia',
        'Ona',
        'Carla',
        'Noa',
        'Aina',
        'Abril',
        'Arlet',
        'Mia',
        'Chloe',
        'Chlóe',
        'Clàudia',
        'Claudia',
        'Sara',
        'Valèria',
        'Valeria',
        'Jana'
        'María',
        'Begoña')))

    first_names = first_names_male + first_names_female
