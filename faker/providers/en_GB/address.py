from __future__ import unicode_literals 
from ..address import Provider as AddressProvider


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

    countries = (
        'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
        'Antarctica (the territory South of 60 deg S)', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
        'Australia', 'Austria', 'Azerbaijan',
        'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
        'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island (Bouvetoya)', 'Brazil',
        'British Indian Ocean Territory (Chagos Archipelago)', 'British Virgin Islands', 'Brunei Darussalam',
        'Bulgaria', 'Burkina Faso', 'Burundi',
        'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile',
        'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo', 'Cook Islands',
        'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
        'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
        'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
        'Faroe Islands', 'Falkland Islands (Malvinas)', 'Fiji', 'Finland', 'France', 'French Guiana',
        'French Polynesia', 'French Southern Territories',
        'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',
        'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana',
        'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong',
        'Hungary',
        'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy',
        'Jamaica', 'Japan', 'Jersey', 'Jordan',
        'Kazakhstan', 'Kenya', 'Kiribati', 'Korea', 'Korea', 'Kuwait', 'Kyrgyz Republic',
        'Lao People\'s Democratic Republic', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya',
        'Liechtenstein', 'Lithuania', 'Luxembourg',
        'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
        'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
        'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar',
        'Namibia', 'Nauru', 'Nepal', 'Netherlands Antilles', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
        'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway',
        'Oman',
        'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
        'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico',
        'Qatar',
        'Reunion', 'Romania', 'Russian Federation', 'Rwanda',
        'Saint Barthelemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin',
        'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe',
        'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia (Slovak Republic)',
        'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands',
        'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard & Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland',
        'Syrian Arab Republic',
        'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',
        'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu',
        'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America',
        'United States Minor Outlying Islands', 'United States Virgin Islands', 'Uruguay', 'Uzbekistan',
        'Vanuatu', 'Venezuela', 'Vietnam',
        'Wallis and Futuna', 'Western Sahara',
        'Yemen',
        'Zambia', 'Zimbabwe'
    )

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
