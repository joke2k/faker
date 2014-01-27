from __future__ import unicode_literals
from ..address import Provider as AddressProvider


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
    ## States and abbrs from Mexico from INEGI
    ## http://www.inegi.org.mx/geo/contenidos/geoestadistica/CatalogoClaves.aspx
    states = (
        'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche',
        'Coahuila de Zaragoza', 'Colima', 'Chiapas', 'Chihuahua',
        'Distrito Federal', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo',
        'Jalisco', 'México', 'Michoacán de Ocampo', 'Morelos', 'Nayarit',
        'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo',
        'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas',
        'Tlaxcala', 'Veracruz de Ignacio de la Llave', 'Yucatán', 'Zacatecas')
    states_abbr = (
        'AGS', 'BC', 'BCS', 'CAMP', 'COAH', 'COL', 'CHIS', 'CHIH', 'DF',
        'DGO', 'GTO', 'GRO', 'HGO', 'JAL', 'MEX', 'MICH', 'MOR', 'NAY',
        'NL', 'OAX', 'PUE', 'QRO', 'Q. ROO', 'SLP', 'SIN', 'SON', 'TAB',
        'TAMPS', 'TLAX', 'VER', 'YUC', 'ZAC')
    ## List of Countries https://www.un.org/es/members/
    countries = (
        'Afganistán', 'Albania', 'Alemania', 'Andorra', 'Angola',
        'Antigua y Barbuda', 'Arabia Saudita', 'Argelia', 'Argentina',
        'Armenia', 'Australia', 'Austria', 'Azerbaiyán',
        'Bahamas', 'Bahrein', 'Bangladesh', 'Barbados', 'Belarús',
        'Bélgica', 'Belice', 'Benin', 'Bhután', 'Bolivia',
        'Bosnia y Herzegovina', 'Botswana', 'Brasil', 'Brunei Darussalam',
        'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Camboya',
        'Camerún', 'Canadá', 'Chad', 'Chile', 'China', 'Chipre','Colombia',
        'Comoras', 'Congo', 'Costa Rica', 'Côte d\'Ivoire', 'Croacia',
        'Cuba', 'Dinamarca', 'Djibouti', 'Dominicana', 'Ecuador', 'Egipto',
        'El Salvador', 'Emiratos Árabes Unidos', 'Eritrea', 'Eslovaquia',
        'Eslovenia', 'España', 'Estados Unidos de América', 'Estonia',
        'Etiopía', 'ex República Yugoslava de Macedonia',
        'Federación de Rusia', 'Fiji', 'Filipinas', 'Finlandia', 'Francia',
        'Gabón', 'Gambia', 'Georgia', 'Ghana', 'Granada', 'Grecia',
        'Guatemala', 'Guinea', 'Guinea Bissau', 'Guinea Ecuatorial',
        'Guyana', 'Haití', 'Honduras', 'Hungría', 'India', 'Indonesia',
        'Irán', 'Iraq', 'Irlanda', 'Islandia', 'Islas Marshall',
        'Islas Salomón', 'Israel', 'Italia', 'Jamaica', 'Japón',
        'Jordania', 'Kazajstán', 'Kenya', 'Kirguistán', 'Kiribati',
        'Kuwait', 'Lesotho', 'Letonia', 'Líbano', 'Liberia', 'Libia',
        'Liechtenstein', 'Lituania', 'Luxemburgo', 'Madagascar',
        'Malasia', 'Malawi', 'Maldivas', 'Mali', 'Malta','Marruecos',
        'Mauricio', 'Mauritania', 'México', 'Micronesia', 'Mónaco',
        'Mongolia', 'Montenegro','Mozambique','Myanmar', 'Namibia',
        'Nauru', 'Nicaragua', 'Niger', 'Nigeria', 'Noruega',
        'Nueva Zelandia', 'Omán', 'Países Bajos', 'Pakistán', 'Palau',
        'Panamá', 'Papua Nueva Guinea', 'Paraguay', 'Perú', 'Polonia',
        'Portugal', 'Qatar',
        'Reino Unido de Gran Bretaña e Irlanda del Norte',
        'República Árabe Siria', 'República Centroafricana',
        'República Checa', 'República de Corea', 'República de Moldova',
        'República Democrática del Congo',
        'República Democrática Popular Lao',
        'República Dominicana',
        'República Federal Democrática de Nepal',
        'República Popular Democrática de Corea',
        'República Unida de Tanzanía', 'Rumania', 'Rwanda',
        'Saint Kitts y Nevis', 'Samoa', 'San Marino', 'Santa Lucía',
        'Santo Tomé y Príncipe', 'San Vicente y las Granadinas',
        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leona', 'Singapur',
        'Somalia', 'Sri Lanka', 'Sudáfrica', 'Sudán', 'Sudán del Sur',
        'Suecia', 'Suiza', 'Suriname', 'Swazilandia', 'Tailandia',
        'Tayikistán', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad y Tabago',
        'Túnez', 'Turkmenistán', 'Turquía', 'Tuvalu', 'Ucrania', 'Uganda',
        'Uruguay', 'Uzbekistán', 'Vanuatu', 'Venezuela', 'Vietman',
        'Yemen', 'Zambia', 'Zimbabwe'
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
        '{{building_number}} {{street_name}} {{secondary_address}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}, {{state_abbr}} {{postcode}}",
    )
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
