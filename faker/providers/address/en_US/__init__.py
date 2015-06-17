from __future__ import unicode_literals

from ..en import Provider as AddressProvider
from faker.generator import random


class Provider(AddressProvider):
    city_prefixes = ('North', 'East', 'West', 'South', 'New', 'Lake', 'Port')
    
    city_suffixes = (
        'town', 'ton', 'land', 'ville', 'berg', 'burgh', 'borough', 'bury', 'view', 'port', 'mouth', 'stad', 'furt',
        'chester', 'mouth', 'fort', 'haven', 'side', 'shire')
    
    building_number_formats = ('#####', '####', '###')
    
    street_suffixes = (
        'Alley', 'Avenue', 'Branch', 'Bridge', 'Brook', 'Brooks', 'Burg', 'Burgs', 'Bypass', 'Camp', 'Canyon', 'Cape',
        'Causeway', 'Center', 'Centers', 'Circle', 'Circles', 'Cliff', 'Cliffs', 'Club', 'Common', 'Corner', 'Corners',
        'Course', 'Court', 'Courts', 'Cove', 'Coves', 'Creek', 'Crescent', 'Crest', 'Crossing', 'Crossroad', 'Curve',
        'Dale', 'Dam', 'Divide', 'Drive', 'Drive', 'Drives', 'Estate', 'Estates', 'Expressway', 'Extension',
        'Extensions',
        'Fall', 'Falls', 'Ferry', 'Field', 'Fields', 'Flat', 'Flats', 'Ford', 'Fords', 'Forest', 'Forge', 'Forges',
        'Fork',
        'Forks', 'Fort', 'Freeway', 'Garden', 'Gardens', 'Gateway', 'Glen', 'Glens', 'Green', 'Greens', 'Grove',
        'Groves',
        'Harbor', 'Harbors', 'Haven', 'Heights', 'Highway', 'Hill', 'Hills', 'Hollow', 'Inlet', 'Inlet', 'Island',
        'Island',
        'Islands', 'Islands', 'Isle', 'Isle', 'Junction', 'Junctions', 'Key', 'Keys', 'Knoll', 'Knolls', 'Lake',
        'Lakes',
        'Land', 'Landing', 'Lane', 'Light', 'Lights', 'Loaf', 'Lock', 'Locks', 'Locks', 'Lodge', 'Lodge', 'Loop',
        'Mall',
        'Manor', 'Manors', 'Meadow', 'Meadows', 'Mews', 'Mill', 'Mills', 'Mission', 'Mission', 'Motorway', 'Mount',
        'Mountain', 'Mountain', 'Mountains', 'Mountains', 'Neck', 'Orchard', 'Oval', 'Overpass', 'Park', 'Parks',
        'Parkway',
        'Parkways', 'Pass', 'Passage', 'Path', 'Pike', 'Pine', 'Pines', 'Place', 'Plain', 'Plains', 'Plains', 'Plaza',
        'Plaza', 'Point', 'Points', 'Port', 'Port', 'Ports', 'Ports', 'Prairie', 'Prairie', 'Radial', 'Ramp', 'Ranch',
        'Rapid', 'Rapids', 'Rest', 'Ridge', 'Ridges', 'River', 'Road', 'Road', 'Roads', 'Roads', 'Route', 'Row', 'Rue',
        'Run', 'Shoal', 'Shoals', 'Shore', 'Shores', 'Skyway', 'Spring', 'Springs', 'Springs', 'Spur', 'Spurs',
        'Square',
        'Square', 'Squares', 'Squares', 'Station', 'Station', 'Stravenue', 'Stravenue', 'Stream', 'Stream', 'Street',
        'Street', 'Streets', 'Summit', 'Summit', 'Terrace', 'Throughway', 'Trace', 'Track', 'Trafficway', 'Trail',
        'Trail',
        'Tunnel', 'Tunnel', 'Turnpike', 'Turnpike', 'Underpass', 'Union', 'Unions', 'Valley', 'Valleys', 'Via',
        'Viaduct',
        'View', 'Views', 'Village', 'Village', 'Villages', 'Ville', 'Vista', 'Vista', 'Walk', 'Walks', 'Wall', 'Way',
        'Ways', 'Well', 'Wells')
    
    postcode_formats = ('#####', '#####-####')
    
    states = (
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
        'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
        'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
        'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
        'Virginia',
        'Washington', 'West Virginia', 'Wisconsin', 'Wyoming' )
    
    states_abbr = (
        'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN',
        'IA',
        'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
        'NC',
        'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA',
        'WV',
        'WI', 'WY')

    military_state_abbr = ('AE', 'AA', 'AP')

    military_ship_prefix = ('USS', 'USNS', 'USNV', 'USCGC')

    military_apo_format = ("PSC ####, Box ####")

    military_dpo_format = ("Unit #### Box ####")
    
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
        '{{building_number}} {{street_name}} {{secondary_address}}',
    )

    address_formats = (
        "{{street_address}}\n{{city}}, {{state_abbr}} {{postcode}}",
    )

    address_formats = {
    "{{street_address}}\n{{city}}, {{state_abbr}} {{postcode}}": 25,
    #military address formatting.
    "{{military_apo}}\nAPO {{military_state}} {{postcode}}": 1,
    "{{military_ship}} {{last_name}}\nFPO {{military_state}} {{postcode}}": 1,
    "{{military_dpo}}\nDPO {{military_state}} {{postcode}}": 1
    }

    secondary_address_formats = ('Apt. ###', 'Suite ###')

    @classmethod
    def city_prefix(cls):
        return cls.random_element(cls.city_prefixes)

    @classmethod
    def secondary_address(cls):
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)

    @classmethod
    def state_abbr(cls):
        return cls.random_element(cls.states_abbr)

    @classmethod
    def zipcode(cls):
        return "%05d" % random.randint(501, 99950)

    @classmethod
    def zipcode_plus4(cls):
        return "%s-%04d" % (cls.zipcode(), random.randint(1, 9999))

    @classmethod
    def military_ship(cls):
        """
        :example 'USS'
        """
        return cls.random_element(cls.military_ship_prefix)

    @classmethod
    def military_state(cls):
         """
         :example 'APO'
         """
         return cls.random_element(cls.military_state_abbr)

    @classmethod
    def military_apo(cls):
        """
        :example 'PSC 5394 Box 3492
        """
        return cls.numerify(cls.military_apo_format)

    @classmethod
    def military_dpo(cls):
        """
        :example 'Unit 3333 Box 9342'
        """
        return cls.numerify(cls.military_dpo_format)
 

    # Aliases
    @classmethod
    def postalcode(cls):
        return cls.zipcode()

    @classmethod
    def postalcode_plus4(cls):
        return cls.zipcode_plus4()
