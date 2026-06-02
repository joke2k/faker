from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """
    Address Provider for the zu_ZA locale (Zulu, South Africa).

    Data sourced from:
    - South African cities and towns: https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_South_Africa
    - South African postal codes: https://en.wikipedia.org/wiki/List_of_postal_codes_in_South_Africa
    - Languages of South Africa: https://en.wikipedia.org/wiki/Languages_of_South_Africa
    """

    city_formats = ("{{city_name}}",)
    building_number_formats = ("%#", "%##", "%###")
    postcode_formats = ("%###",)  # Güncellendi: 4 haneli posta kodu için
    section_formats = ("",)
    street_address_formats = ("{{building_number}} {{street_name}} {{street_suffix}}",)
    address_formats = ("{{street_address}}, {{city}}, {{postcode}}",)
    secondary_address_formats = ("Flat #%#", "Unit #%#", "Suite #%#")

    street_names = (
        "Main",
        "Church",
        "President",
        "Voortrekker",
        "Nelson Mandela",
        "Albertina Sisulu",
        "Rivonia",
        "Jan Smuts",
        "Commissioner",
        "Long",
        "High",
        "Short",
        "Victoria",
        "Queen",
        "King",
        "Oxford",
        "George",
        "William",
        "York",
        "Smith",
        "Adelaide",
        "Charles",
        "Churchill",
        "Cecil",
        "Clarence",
        "Edward",
        "Elizabeth",
        "Frere",
        "Gandhi",
        "Grey",
        "James",
        "Joseph",
        "Milner",
        "Napier",
        "Paul Kruger",
        "Prince",
        "Somerset",
        "Stanley",
        "Thomas",
        "Walter Sisulu",
        "West",
    )

    street_suffixes = ("Umgwaqo", "Indlela", "Isitaladi", "Ithafa", "Indawo")

    cities = (
        "eGoli",
        "eThekwini",
        "iBhayi",
        "iKapa",
        "uMgungundlovu",
        "Polokwane",
        "Mbombela",
        "Mahikeng",
        "Kimberley",
        "Bloemfontein",
        "Rustenburg",
        "Soweto",
        "Benoni",
        "Tembisa",
        "Welkom",
        "Vereeniging",
        "Chatsworth",
        "Uitenhage",
        "Middelburg",
        "Springs",
        "Randfontein",
        "Boksburg",
        "Witbank",
        "Klerksdorp",
        "Bethlehem",
        "George",
        "Upington",
        "Musina",
        "Vanderbijlpark",
        "Stellenbosch",
        "Krugersdorp",
        "Sasolburg",
        "Centurion",
        "Newcastle",
        "Thohoyandou",
        "Potchefstroom",
        "Kathu",
        "Paarl",
    )

    city_suffixes = ("",)

    countries = (
        "iNingizimu Afrika",
        "Botswana",
        "Lesotho",
        "Namibia",
        "Eswatini",
        "Zimbabwe",
        "Mozambique",
        "Angola",
        "Zambia",
        "Malawi",
        "Madagascar",
        "Tanzania",
        "Kenya",
        "Nigeria",
        "Ghana",
        "Egypt",
        "Morocco",
        "Tunisia",
        "Algeria",
        "Ethiopia",
        "Sudan",
        "Somalia",
        "Uganda",
        "Cameroon",
        "DR Congo",
        "Rwanda",
        "Burundi",
        "Senegal",
        "Mali",
        "Ivory Coast",
        "Niger",
        "Chad",
        "Mauritania",
        "Eritrea",
        "Djibouti",
        "Cape Verde",
        "Seychelles",
        "Mauritius",
        "Comoros",
        "Gambia",
        "Liberia",
        "Sierra Leone",
        "Benin",
        "Togo",
        "Equatorial Guinea",
        "Gabon",
        "Congo",
        "Central African Republic",
        "Sao Tome and Principe",
        "Guinea",
        "Guinea-Bissau",
        "Burkina Faso",
    )

    provinces = (
        "iMpuma-Kapa",
        "Freistata",
        "eGoli",
        "iKwaZulu-Natali",
        "Limpopo",
        "iMpumalanga",
        "Bokone Bophirima",
        "Noord-Kaap",
        "Wes-Kaap",
    )

    def secondary_address(self) -> str:
        """
        :sample:
        """
        return self.numerify(self.random_element(self.secondary_address_formats))

    def building_number(self) -> str:
        """
        :sample:
        """
        return self.numerify(self.random_element(self.building_number_formats))

    def street_name(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.street_names)

    def street_suffix(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.street_suffixes)

    def city_name(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.cities)

    def city_name_suffix(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.city_suffixes)

    def section_number(self) -> str:
        """
        :sample:
        """
        return self.numerify(self.random_element(self.section_formats))

    def province(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.provinces)

    def administrative_unit(self) -> str:
        """
        :sample:
        """
        return self.random_element(self.provinces)
