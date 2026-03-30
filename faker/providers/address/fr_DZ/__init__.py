from typing import Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """Address provider for fr_DZ locale."""

    # Source: https://fr.wikipedia.org/wiki/Wilayas_d%27Alg%C3%A9rie
    wilayas: Tuple[str, ...] = (
        "Adrar",
        "Chlef",
        "Laghouat",
        "Oum El Bouaghi",
        "Batna",
        "Béjaïa",
        "Biskra",
        "Béchar",
        "Blida",
        "Bouira",
        "Tamanrasset",
        "Tébessa",
        "Tlemcen",
        "Tiaret",
        "Tizi Ouzou",
        "Alger",
        "Djelfa",
        "Jijel",
        "Sétif",
        "Saïda",
        "Skikda",
        "Sidi Bel Abbès",
        "Annaba",
        "Guelma",
        "Constantine",
        "Médéa",
        "Mostaganem",
        "M'Sila",
        "Mascara",
        "Ouargla",
        "Oran",
        "El Bayadh",
        "Illizi",
        "Bordj Bou Arreridj",
        "Boumerdès",
        "El Tarf",
        "Tindouf",
        "Tissemsilt",
        "El Oued",
        "Khenchela",
        "Souk Ahras",
        "Tipaza",
        "Mila",
        "Aïn Defla",
        "Naâma",
        "Aïn Témouchent",
        "Ghardaïa",
        "Relizane",
        "Timimoun",
        "Bordj Badji Mokhtar",
        "Ouled Djellal",
        "Béni Abbès",
        "In Salah",
        "In Guezzam",
        "Touggourt",
        "Djanet",
        "El Meghaier",
        "El Menia",
    )

    # Source: https://github.com/othmanus/algeria-cities
    cities: Tuple[str, ...] = (
        # Wilaya 01 - Adrar
        "Adrar",
        "Reggane",
        "Aoulef",
        "Timimoun",
        # Wilaya 02 - Chlef
        "Chlef",
        "Ténès",
        "Boukadir",
        # Wilaya 03 - Laghouat
        "Laghouat",
        "Aflou",
        "Aïn Madhi",
        # Wilaya 04 - Oum El Bouaghi
        "Oum El Bouaghi",
        "Aïn Mlila",
        "Aïn Beïda",
        # Wilaya 05 - Batna
        "Batna",
        "Barika",
        "Aïn Touta",
        "Arris",
        "N'Gaous",
        # Wilaya 06 - Béjaïa
        "Béjaïa",
        "Akbou",
        "Kherrata",
        "Taklast",
        "Amizour",
        # Wilaya 07 - Biskra
        "Biskra",
        "Tolga",
        "Sidi Okba",
        "Zéribet El Oued",
        # Wilaya 08 - Béchar
        "Béchar",
        "Taghit",
        "Kenadsa",
        # Wilaya 09 - Blida
        "Blida",
        "Boufarik",
        "Larbaa",
        "Bouinan",
        # Wilaya 10 - Bouira
        "Bouira",
        "Sour El Ghozlane",
        "Aïn Bessem",
        # Wilaya 11 - Tamanrasset
        "Tamanrasset",
        "Ablessa",
        # Wilaya 12 - Tébessa
        "Tébessa",
        "Bir El Ater",
        "El Aouinet",
        # Wilaya 13 - Tlemcen
        "Tlemcen",
        "Maghnia",
        "Ghazaouet",
        "Nedroma",
        "Marsa Ben M'Hidi",
        # Wilaya 14 - Tiaret
        "Tiaret",
        "Sougueur",
        "Frenda",
        "Takhmaret",
        # Wilaya 15 - Tizi Ouzou
        "Tizi Ouzou",
        "Draa Ben Khedda",
        "Azeffoun",
        "Boughni",
        "Tigzirt",
        # Wilaya 16 - Alger
        "Alger Centre",
        "Bab El Oued",
        "La Casbah",
        "Sidi M'Hamed",
        "Hussein Dey",
        "El Harrach",
        "Rouiba",
        "Zéralda",
        "Bir Mourad Raïs",
        "Bouzaréah",
        "Chéraga",
        "Draria",
        "Bab Ezzouar",
        "Bordj El Kiffan",
        "Dar El Beïda",
        "Aïn Taya",
        # Wilaya 17 - Djelfa
        "Djelfa",
        "Messaad",
        "Aïn Oussera",
        "Hassi Bahbah",
        # Wilaya 18 - Jijel
        "Jijel",
        "El Milia",
        "Taher",
        "Ziama Mansouriah",
        # Wilaya 19 - Sétif
        "Sétif",
        "El Eulma",
        "Djemila",
        "Aïn Arnat",
        "Bougaa",
        # Wilaya 20 - Saïda
        "Saïda",
        "Aïn El Hadjar",
        # Wilaya 21 - Skikda
        "Skikda",
        "Azzaba",
        "El Harrouch",
        "Collo",
        # Wilaya 22 - Sidi Bel Abbès
        "Sidi Bel Abbès",
        "Aïn El Berd",
        "Marhoum",
        "Tlemnia",
        # Wilaya 23 - Annaba
        "Annaba",
        "El Bouni",
        "Aïn Berda",
        "Sidi Amar",
        # Wilaya 24 - Guelma
        "Guelma",
        "Bouchegouf",
        "Hammam Debagh",
        # Wilaya 25 - Constantine
        "Constantine",
        "El Khroub",
        "Didouche Mourad",
        "Zighoud Youcef",
        "Aïn Abid",
        # Wilaya 26 - Médéa
        "Médéa",
        "Ksar El Boukhari",
        "Berrouaghia",
        "Boughzoul",
        # Wilaya 27 - Mostaganem
        "Mostaganem",
        "Sidi Ali",
        "Aïn Tédeles",
        "Mazagran",
        # Wilaya 28 - M'Sila
        "M'Sila",
        "Bou Saâda",
        "Sidi Aïssa",
        "Aïn El Melh",
        # Wilaya 29 - Mascara
        "Mascara",
        "Tighennif",
        "Bouhanifia",
        "Sig",
        # Wilaya 30 - Ouargla
        "Ouargla",
        "Hassi Messaoud",
        "Aïn El Beïda",
        # Wilaya 31 - Oran
        "Oran",
        "Arzew",
        "Aïn El Turk",
        "Bir El Djir",
        "Mers El Hadjadj",
        "Es Sénia",
        # Wilaya 32 - El Bayadh
        "El Bayadh",
        "Brezina",
        # Wilaya 33 - Illizi
        "Illizi",
        "In Amenas",
        # Wilaya 34 - Bordj Bou Arreridj
        "Bordj Bou Arreridj",
        "Ras El Oued",
        "Aïn Taghrout",
        # Wilaya 35 - Boumerdès
        "Boumerdès",
        "Khemis El Khechna",
        "Bordj Menaïel",
        "Dellys",
        # Wilaya 36 - El Tarf
        "El Tarf",
        "El Kala",
        "Ben M'Hidi",
        # Wilaya 37 - Tindouf
        "Tindouf",
        # Wilaya 38 - Tissemsilt
        "Tissemsilt",
        "Khemisti",
        # Wilaya 39 - El Oued
        "El Oued",
        "Guemar",
        "Hassi Khalifa",
        "Reguiba",
        # Wilaya 40 - Khenchela
        "Khenchela",
        "Babar",
        # Wilaya 41 - Souk Ahras
        "Souk Ahras",
        "Mdaourouch",
        "Sedrata",
        # Wilaya 42 - Tipaza
        "Tipaza",
        "Cherchell",
        "Bou Ismaïl",
        "Koléa",
        # Wilaya 43 - Mila
        "Mila",
        "Ferdjioua",
        "Chelghoum Laïd",
        # Wilaya 44 - Aïn Defla
        "Aïn Defla",
        "Khemis Miliana",
        "El Attaf",
        "Miliana",
        # Wilaya 45 - Naâma
        "Naâma",
        "Mecheria",
        "Aïn Sefra",
        # Wilaya 46 - Aïn Témouchent
        "Aïn Témouchent",
        "Béni Saf",
        "Hammam Bou Hadjar",
        # Wilaya 47 - Ghardaïa
        "Ghardaïa",
        "Guerrara",
        "Metlili",
        "El Atteuf",
        # Wilaya 48 - Relizane
        "Relizane",
        "Mazouna",
        "Oued Rhiou",
        # New wilayas
        "Timimoun",
        "Bordj Badji Mokhtar",
        "Ouled Djellal",
        "Béni Abbès",
        "In Salah",
        "In Guezzam",
        "Touggourt",
        "Djanet",
        "El Meghaier",
        "El Menia",
    )

    street_prefixes: Tuple[str, ...] = (
        "rue",
        "avenue",
        "boulevard",
        "chemin",
    )

    building_number_formats: Tuple[str, ...] = ("%", "%#", "%#", "%##")

    postcode_formats: Tuple[str, ...] = tuple(f"{i:02d}###" for i in range(1, 49))

    street_name_formats: Tuple[str, ...] = (
        "{{street_prefix}} {{last_name}}",
        "{{street_prefix}} {{first_name}} {{last_name}}",
        "{{street_prefix}} de {{last_name}}",
    )

    street_address_formats: Tuple[str, ...] = (
        "{{building_number}} {{street_name}}",
        "{{building_number}}, {{street_name}}",
    )

    address_formats: Tuple[str, ...] = (
        "{{street_address}} {{city}}",
        "{{street_address}} - {{city}}",
        "{{street_address}} {{city}}, {{administrative_unit}}",
        "{{street_address}}, {{city}}, {{administrative_unit}}",
        "{{street_address}} {{city}} - {{administrative_unit}}",
    )

    def street_prefix(self) -> str:
        return self.random_element(self.street_prefixes)

    def city(self) -> str:
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        return self.random_element(self.wilayas)

    wilaya = administrative_unit
