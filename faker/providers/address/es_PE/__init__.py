from ..es import Provider as AddressProvider

class Provider(AddressProvider):
    """
    A Faker provider for the Spanish-Peru (es_PE) locale.
    This inherits from the base 'es' provider and adds Peru-specific data.
    
    Sources:
    - Departments: https://en.wikipedia.org/wiki/Departments_of_Peru
    - Cities: https://en.wikipedia.org/wiki/List_of_cities_in_Peru
    - Street Prefixes: Common knowledge of Peruvian addresses.
    """
    
    # Define the structure of addresses in Peru
    city_formats = ('{{city_name}}',)
    street_name_formats = (
        '{{street_prefix}} {{first_name}} {{last_name}}',
        '{{street_prefix}} {{last_name}}',
        '{{street_prefix}} de {{last_name}}',
    )
    street_address_formats = (
        '{{street_name}} #{{building_number}}',
        '{{street_name}} #{{building_number}}, {{secondary_address}}',
    )
    address_formats = (
        '{{street_address}}\n{{city}}, {{department}}',
    )
    
    # Postcode format for Peru is 5 digits
    postcode_formats = ('#####',)

    # Common secondary address indicators
    secondary_address_formats = (
        'Dpto. ###', 'Of. ###', 'Int. ##', 'Piso #',
    )

    # Common street prefixes in Peru
    street_prefixes = (
        'Avenida', 'Av.', 'Jirón', 'Jr.', 'Calle', 'Paseo', 'Alameda', 'Malecón',
    )

    # Building number formats
    building_number_formats = ('###', '####', '##')

    # The 24 Departments of Peru + the Constitutional Province of Callao
    departments = (
        'Amazonas', 'Áncash', 'Apurímac', 'Arequipa', 'Ayacucho', 'Cajamarca',
        'Callao', 'Cusco', 'Huancavelica', 'Huánuco', 'Ica', 'Junín',
        'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios',
        'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna',
        'Tumbes', 'Ucayali',
    )

    # A list of major cities in Peru
    cities = (
        'Arequipa', 'Ayacucho', 'Cajamarca', 'Callao', 'Chiclayo', 'Chimbote',
        'Cusco', 'Huancayo', 'Huánuco', 'Huaraz', 'Ica', 'Iquitos', 'Juliaca',
        'Lima', 'Piura', 'Pucallpa', 'Puno', 'Tacna', 'Trujillo', 'Tumbes',
    )

    # Methods to be called by Faker
    def department(self) -> str:
        """
        Returns a random Peruvian department.
        """
        return self.random_element(self.departments)

    def city_name(self) -> str:
        """
        Returns a random Peruvian city name.
        """
        return self.random_element(self.cities)

    def street_prefix(self) -> str:
        """
        Returns a random street prefix.
        """
        return self.random_element(self.street_prefixes)

    def secondary_address(self) -> str:
        """
        Returns a random secondary address (apartment, office, etc.).
        """
        return self.numerify(self.random_element(self.secondary_address_formats))
