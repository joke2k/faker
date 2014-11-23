from __future__ import unicode_literals 
from ..en import Provider as AddressProvider


class Provider(AddressProvider):
    city_prefixes = ('North', 'East', 'West', 'South', 'New', 'Lake', 'Port')
    city_suffixes = (
        'town', 'ton', 'land', 'ville', 'berg', 'burgh', 'borough', 'bury', 'view', 'port', 'mouth', 'stad', 'furt',
        'chester', 'mouth', 'fort', 'haven', 'side', 'shire')
    building_number_formats = ('#', '##', '###')
    street_suffixes = (
        'alley', 'avenue', 'branch', 'bridge', 'brook', 'brooks', 'burg', 'burgs', 'bypass', 'camp', 'canyon', 'cape',
        'causeway', 'center', 'centers', 'circle', 'circles', 'cliff', 'cliffs', 'club', 'common', 'corner', 'corners',
        'course', 'court', 'courts', 'cove', 'coves', 'creek', 'crescent', 'crest', 'crossing', 'crossroad', 'curve',
        'dale', 'dam', 'divide', 'drive', 'drive', 'drives', 'estate', 'estates', 'expressway', 'extension',
        'extensions',
        'fall', 'falls', 'ferry', 'field', 'fields', 'flat', 'flats', 'ford', 'fords', 'forest', 'forge', 'forges',
        'fork',
        'forks', 'fort', 'freeway', 'garden', 'gardens', 'gateway', 'glen', 'glens', 'green', 'greens', 'grove',
        'groves',
        'harbor', 'harbors', 'haven', 'heights', 'highway', 'hill', 'hills', 'hollow', 'inlet', 'inlet', 'island',
        'island',
        'islands', 'islands', 'isle', 'isle', 'junction', 'junctions', 'key', 'keys', 'knoll', 'knolls', 'lake',
        'lakes',
        'land', 'landing', 'lane', 'light', 'lights', 'loaf', 'lock', 'locks', 'locks', 'lodge', 'lodge', 'loop',
        'mall',
        'manor', 'manors', 'meadow', 'meadows', 'mews', 'mill', 'mills', 'mission', 'mission', 'motorway', 'mount',
        'mountain', 'mountain', 'mountains', 'mountains', 'neck', 'orchard', 'oval', 'overpass', 'park', 'parks',
        'parkway',
        'parkways', 'pass', 'passage', 'path', 'pike', 'pine', 'pines', 'place', 'plain', 'plains', 'plains', 'plaza',
        'plaza', 'point', 'points', 'port', 'port', 'ports', 'ports', 'prairie', 'prairie', 'radial', 'ramp', 'ranch',
        'rapid', 'rapids', 'rest', 'ridge', 'ridges', 'river', 'road', 'road', 'roads', 'roads', 'route', 'row', 'rue',
        'run', 'shoal', 'shoals', 'shore', 'shores', 'skyway', 'spring', 'springs', 'springs', 'spur', 'spurs',
        'square',
        'square', 'squares', 'squares', 'station', 'station', 'stravenue', 'stravenue', 'stream', 'stream', 'street',
        'street', 'streets', 'summit', 'summit', 'terrace', 'throughway', 'trace', 'track', 'trafficway', 'trail',
        'trail',
        'tunnel', 'tunnel', 'turnpike', 'turnpike', 'underpass', 'union', 'unions', 'valley', 'valleys', 'via',
        'viaduct',
        'view', 'views', 'village', 'village', 'villages', 'ville', 'vista', 'vista', 'walk', 'walks', 'wall', 'way',
        'ways', 'well', 'wells')

    postcode_formats = ('??#? #??', '?#? #??', '?# #??', '?## #??', '??# #??', '??## #??',)

    city_formats = (
        '{{city_prefix}} {{first_name}}{{city_suffix}}',
        '{{city_prefix}} {{first_name}}',
        '{{first_name}}{{city_suffix}}',
        '{{last_name}}{{city_suffix}}',
    )
    street_name_formats = (
        '{{first_name}} {{street_suffix}}',
        '{{last_name}} {{street_suffix}}'
    )
    street_address_formats = (
        '{{building_number}} {{street_name}}',
        '{{secondary_address}}\n{{street_name}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}\n{{postcode}}",
    )
    secondary_address_formats = ('Flat #', 'Flat ##', 'Flat ##?', 'Studio #', 'Studio ##', 'Studio ##?')

    @classmethod
    def city_prefix(cls):
        return cls.random_element(cls.city_prefixes)

    @classmethod
    def secondary_address(cls):
        return cls.bothify(cls.random_element(cls.secondary_address_formats))
