# coding=utf-8

from __future__ import unicode_literals
from ..es import Provider as AddressProvider


class Provider(AddressProvider):
    building_number_formats = ('%', '%#', '%#', '%#', '%##')
    street_prefixes = (
        'Plaza', 'Calle', 'Avenida', 'Urbanización', 'Callejón',
        'Pasaje', 'Paseo', 'Camino',
    )
    postcode_formats = ('####', )
    states = (
        'Amazonas', 'Anzoátegui', 'Apure', 'Aragua', 'Barinas', 'Bolívar', 'Carabobo',
        'Cojedes', 'Delta Amacuro', 'Falcón', 'Distrito Capital', 'Guárico', 'Lara', 'Mérida',
        'Miranda', 'Monagas', 'Nueva Esparta', 'Portuguesa', 'Sucre', 'Tachira', 'Trujillo',
        'Vargas', 'Yaracuy', 'Zulia'
    )

    city_formats = (
        '{{state_name}}',
    )

    street_name_formats = (
        '{{street_prefix}} {{first_name}} {{last_name}}',
        '{{street_prefix}} de {{first_name}} {{last_name}}',

    )
    street_address_formats = (
        '{{street_name}} {{building_number}}',
        '{{street_name}} {{building_number}} {{secondary_address}} ',
    )
    address_formats = (
        "{{street_address}}\n{{city}}, {{postcode}}",
    )
    secondary_address_formats = ('Apt. ##', 'Piso #', 'Calle #')

    @classmethod
    def state_name(cls):
        return cls.random_element(cls.states)

    @classmethod
    def street_prefix(cls):
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def secondary_address(cls):
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
