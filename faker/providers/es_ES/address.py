# coding=utf-8

from __future__ import unicode_literals
from ..address import Provider as AddressProvider


class Provider(AddressProvider):
    building_number_formats = ('%', '%#', '%#', '%#', '%##')
    street_prefixes = (
        'Plaza', 'Calle', 'Avenida', 'Via', 'Vial', 'Rambla', 'Glorieta', 'Urbanización', 'Callejón', 'Cañada',
        'Alameda', 'Acceso', 'C.', 'Ronda', 'Pasaje', 'Cuesta', 'Pasadizo', 'Paseo', 'Camino'
    )
    postcode_formats = ('#####', )
    states = (
        'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz',
        'Baleares', 'Barcelona', 'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón',
        'Ceuta', 'Ciudad', 'Córdoba', 'Cuenca', 'Girona', 'Granada', 'Guadalajara',
        'Guipúzcoa', 'Huelva', 'Huesca', 'Jaén', 'La Coruña', 'La Rioja', 'Las Palmas',
        'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga', 'Melilla', 'Murcia', 'Navarra',
        'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife',
        'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia',
        'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza'
    )
    countries = (
        'Afganistán', 'Akrotiri', 'Albania', 'Alemania', 'Andorra', 'Angola', 'Anguila',
        'Antártida', 'Antigua y Barbuda', 'Antillas Neerlandesas', 'Arabia Saudí',
        'Arctic Ocean', 'Argelia', 'Argentina', 'Armenia', 'Aruba', 'Ashmore and Cartier Islands',
        'Atlantic Ocean', 'Australia', 'Austria', 'Azerbaiyán', 'Bahamas',
        'Bahráin', 'Bangladesh', 'Barbados', 'Bélgica', 'Belice', 'Benín', 'Bermudas',
        'Bielorrusia', 'Birmania Myanmar', 'Bolivia', 'Bosnia y Hercegovina',
        'Botsuana', 'Brasil', 'Brunéi', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Bután',
        'Cabo Verde', 'Camboya', 'Camerún', 'Canadá', 'Chad', 'Chile', 'China',
        'Chipre', 'Clipperton Island', 'Colombia', 'Comoras', 'Congo', 'Coral Sea Islands',
        'Corea del Norte', 'Corea del Sur', 'Costa de Marfil', 'Costa Rica',
        'Croacia', 'Cuba', 'Dhekelia', 'Dinamarca', 'Dominica', 'Ecuador', 'Egipto', 'El Salvador',
        'El Vaticano', 'Emiratos Árabes Unidos', 'Eritrea', 'Eslovaquia',
        'Eslovenia', 'España', 'Estados Unidos', 'Estonia', 'Etiopía', 'Filipinas',
        'Finlandia', 'Fiyi', 'Francia', 'Gabón', 'Gambia', 'Gaza Strip', 'Georgia',
        'Ghana', 'Gibraltar', 'Granada', 'Grecia', 'Groenlandia', 'Guam', 'Guatemala',
        'Guernsey', 'Guinea', 'Guinea Ecuatorial', 'Guinea-Bissau', 'Guyana', 'Haití',
        'Honduras', 'Hong Kong', 'Hungría', 'India', 'Indian Ocean', 'Indonesia',
        'Irán', 'Iraq', 'Irlanda', 'Isla Bouvet', 'Isla Christmas', 'Isla Norfolk',
        'Islandia', 'Islas Caimán', 'Islas Cocos', 'Islas Cook', 'Islas Feroe', 'Islas Georgia del Sur y Sandwich del Sur',
        'Islas Heard y McDonald', 'Islas Malvinas', 'Islas Marianas del Norte', 'Islas Marshall',
        'Islas Pitcairn', 'Islas Salomón', 'Islas Turcas y Caicos', 'Islas Vírgenes Americanas',
        'Islas Vírgenes Británicas', 'Israel', 'Italia', 'Jamaica', 'Jan Mayen', 'Japón', 'Jersey',
        'Jordania', 'Kazajistán', 'Kenia', 'Kirguizistán', 'Kiribati', 'Kuwait', 'Laos',
        'Lesoto', 'Letonia', 'Líbano', 'Liberia', 'Libia', 'Liechtenstein', 'Lituania',
        'Luxemburgo', 'Macao', 'Macedonia', 'Madagascar', 'Malasia', 'Malaui',
        'Maldivas', 'Malí', 'Malta', 'Man, Isle of', 'Marruecos', 'Mauricio',
        'Mauritania', 'Mayotte', 'México', 'Micronesia', 'Moldavia', 'Mónaco',
        'Mongolia', 'Montserrat', 'Mozambique', 'Namibia', 'Nauru', 'Navassa Island',
        'Nepal', 'Nicaragua', 'Níger', 'Nigeria', 'Niue', 'Noruega', 'Nueva Caledonia',
        'Nueva Zelanda', 'Omán', 'Pacific Ocean', 'Países Bajos', 'Pakistán', 'Palaos',
        'Panamá', 'Papúa-Nueva Guinea', 'Paracel Islands', 'Paraguay', 'Perú',
        'Polinesia Francesa', 'Polonia', 'Portugal', 'Puerto Rico', 'Qatar', 'Reino Unido',
        'República Centroafricana', 'República Checa', 'República Democrática del Congo',
        'República Dominicana', 'Ruanda', 'Rumania', 'Rusia', 'Sáhara Occidental', 'Samoa',
        'Samoa Americana', 'San Cristóbal y Nieves', 'San Marino',
        'San Pedro y Miquelón', 'San Vicente y las Granadinas', 'Santa Helena', 'Santa Lucía',
        'Santo Tomé y Príncipe', 'Senegal', 'Seychelles', 'Sierra Leona',
        'Singapur', 'Siria', 'Somalia', 'Southern Ocean', 'Spratly Islands', 'Sri Lanka',
        'Suazilandia', 'Sudáfrica', 'Sudán', 'Suecia', 'Suiza', 'Surinam',
        'Svalbard y Jan Mayen', 'Tailandia', 'Taiwán', 'Tanzania', 'Tayikistán',
        'TerritorioBritánicodel Océano Indico', 'Territorios Australes Franceses',
        'Timor Oriental', 'Togo', 'Tokelau', 'Tonga', 'Trinidad y Tobago', 'Túnez',
        'Turkmenistán', 'Turquía', 'Tuvalu', 'Ucrania', 'Uganda', 'Unión Europea',
        'Uruguay', 'Uzbekistán', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wake Island',
        'Wallis y Futuna', 'West Bank', 'World', 'Yemen', 'Yibuti', 'Zambia', 'Zimbabue'
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
    secondary_address_formats = ('Apt. ##', 'Piso #', 'Puerta #')

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

