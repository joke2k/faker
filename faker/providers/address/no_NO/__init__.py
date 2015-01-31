# coding=utf-8
from __future__ import unicode_literals

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_suffixes = ['berg', 'borg', 'by', 'bø', 'dal', 'eid', 'fjell',
                     'fjord', 'foss', 'grunn', 'hamn', 'havn', 'helle', 'mark',
                     'nes', 'odden', 'sand', 'sjøen', 'stad', 'strand',
                     'strøm', 'sund', 'vik', 'vær', 'våg', 'ø', 'øy', 'ås']
    street_suffixes = ['alléen', 'bakken', 'berget', 'bråten', 'eggen',
                       'engen', 'ekra', 'faret', 'flata', 'gata', 'gjerdet',
                       'grenda', 'gropa', 'hagen', 'haugen', 'havna', 'holtet',
                       'høgda', 'jordet', 'kollen', 'kroken', 'lia', 'lunden',
                       'lyngen', 'løkka', 'marka', 'moen', 'myra', 'plassen',
                       'ringen', 'roa', 'røa', 'skogen', 'skrenten',
                       'spranget', 'stien', 'stranda', 'stubben', 'stykket',
                       'svingen', 'tjernet', 'toppen', 'tunet', 'vollen',
                       'vika', 'åsen']
    city_formats = [
        '{{first_name}}{{city_suffix}}', '{{last_name}}']
    street_name_formats = [
        '{{last_name}}{{street_suffix}}', 
    ]
    street_address_formats = ['{{street_name}} {{building_number}}',]
    address_formats = ['{{street_address}}, {{postcode}} {{city}}', ]
    building_number_formats = ['#', '#', '#', '#?', '##', '##', '##?']
    postcode_formats = ['####', ]

    @classmethod
    def postcode(cls):
        """
        :example 0234
        """
        return cls.random_element(cls.postcode_formats)

