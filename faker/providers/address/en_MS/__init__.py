from collections import OrderedDict
from typing import Dict, List, Optional

from ... import ElementsType
from ..en import Provider as AddressProvider

# https://en.wikipedia.org/wiki/Addresses_in_Malaysia


class Provider(AddressProvider):
    # 'Bandar' and 'Taman' are the most common township prefix
    # https://en.wikipedia.org/wiki/Template:Greater_Kuala_Lumpur > Townships
    # https://en.wikipedia.org/wiki/Template:Johor > Townships
    # https://en.wikipedia.org/wiki/Template:Kedah > Townships
    # https://en.wikipedia.org/wiki/Template:Kelantan > Townships
    # https://en.wikipedia.org/wiki/Template:Melaka > Townships
    # https://en.wikipedia.org/wiki/Template:Negeri_Sembilan > Townships
    # https://en.wikipedia.org/wiki/Template:Perak > Townships
    # https://en.wikipedia.org/wiki/Template:Penang > Townships
    # https://en.wikipedia.org/wiki/Template:Selangor > Townships
    # https://en.wikipedia.org/wiki/Template:Terengganu > Townships

    city_prefixes = (
        "Alam",
        "Apartment",
        "Ara",
        "Bandar",
        "Bandar",
        "Bandar",
        "Bandar",
        "Bandar",
        "Bandar",
        "Bandar Bukit",
        "Bandar Seri",
        "Bandar Sri",
        "Bandar Baru",
        "Batu",
        "Bukit",
        "Desa",
        "Damansara",
        "Kampung",
        "Kampung Baru",
        "Kampung Baru",
        "Kondominium",
        "Kota",
        "Laman",
        "Lembah",
        "Medan",
        "Pandan",
        "Pangsapuri",
        "Petaling",
        "Puncak",
        "Seri",
        "Sri",
        "Taman",
        "Taman",
        "Taman",
        "Taman",
        "Taman",
        "Taman",
        "Taman Desa",
    )

    city_suffixes = (
        "Aman",
        "Amanjaya",
        "Anggerik",
        "Angkasa",
        "Antarabangsa",
        "Awan",
        "Bahagia",
        "Bangsar",
        "Baru",
        "Belakong",
        "Bendahara",
        "Bestari",
        "Bintang",
        "Brickfields",
        "Casa",
        "Changkat",
        "Country Heights",
        "Damansara",
        "Damai",
        "Dato Harun",
        "Delima",
        "Duta",
        "Flora",
        "Gembira",
        "Genting",
        "Harmoni",
        "Hartamas",
        "Impian",
        "Indah",
        "Intan",
        "Jasa",
        "Jaya",
        "Keramat",
        "Kerinchi",
        "Kiara",
        "Kinrara",
        "Kuchai",
        "Laksamana",
        "Mahkota",
        "Maluri",
        "Manggis",
        "Maxwell",
        "Medan",
        "Melawati",
        "Menjalara",
        "Meru",
        "Mulia",
        "Mutiara",
        "Pahlawan",
        "Perdana",
        "Pertama",
        "Permai",
        "Pelangi",
        "Petaling",
        "Pinang",
        "Puchong",
        "Puteri",
        "Putra",
        "Rahman",
        "Rahmat",
        "Raya",
        "Razak",
        "Ria",
        "Saujana",
        "Segambut",
        "Selamat",
        "Selatan",
        "Semarak",
        "Sentosa",
        "Seputeh",
        "Setapak",
        "Setia Jaya",
        "Sinar",
        "Sungai Besi",
        "Sungai Buaya",
        "Sungai Long",
        "Suria",
        "Tasik Puteri",
        "Tengah",
        "Timur",
        "Tinggi",
        "Tropika",
        "Tun Hussein Onn",
        "Tun Perak",
        "Tunku",
        "Ulu",
        "Utama",
        "Utara",
        "Wangi",
    )

    # https://en.wikipedia.org/wiki/States_and_federal_territories_of_Malaysia
    states: Dict[str, List[str]] = {
        "JHR": ["Johor Darul Ta'zim", "Johor"],
        "KDH": ["Kedah Darul Aman", "Kedah"],
        "KTN": ["Kelantan Darul Naim", "Kelantan"],
        "KUL": ["KL", "Kuala Lumpur", "WP Kuala Lumpur"],
        "LBN": ["Labuan"],
        "MLK": ["Malacca", "Melaka"],
        "NSN": ["Negeri Sembilan Darul Khusus", "Negeri Sembilan"],
        "PHG": ["Pahang Darul Makmur", "Pahang"],
        "PNG": ["Penang", "Pulau Pinang"],
        "PRK": ["Perak Darul Ridzuan", "Perak"],
        "PLS": ["Perlis Indera Kayangan", "Perlis"],
        "PJY": ["Putrajaya"],
        "SBH": ["Sabah"],
        "SWK": ["Sarawak"],
        "SGR": ["Selangor Darul Ehsan", "Selangor"],
        "TRG": ["Terengganu Darul Iman", "Terengganu"],
    }

    states_postcode = {
        "PLS": [(1000, 2800)],
        "KDH": [(5000, 9810)],
        "PNG": [(10000, 14400)],
        "KTN": [(15000, 18500)],
        "TRG": [(20000, 24300)],
        "PHG": [
            (25000, 28800),
            (39000, 39200),
            (49000, 69000),
        ],
        "PRK": [(30000, 36810)],
        "SGR": [(40000, 48300), (63000, 68100)],
        "KUL": [(50000, 60000)],
        "PJY": [(62000, 62988)],
        "NSN": [(70000, 73509)],
        "MLK": [(75000, 78309)],
        "JHR": [(79000, 86900)],
        "LBN": [(87000, 87033)],
        "SBH": [(88000, 91309)],
        "SWK": [(93000, 98859)],
    }

    city_prefix_abbrs: ElementsType[str] = (
        "SS",
        "Seksyen ",
        "PJS",
        "PJU",
        "USJ ",
    )

    def city_prefix_abbr(self) -> str:
        return self.random_element(self.city_prefix_abbrs)

    city_formats: ElementsType[str] = (
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix}} {{city_suffix}}",
        "{{city_prefix_abbr}}%",
        "{{city_prefix_abbr}}%#",
        "{{city_prefix_abbr}}%#?",
    )

    def city(self) -> str:
        pattern: str = self.bothify(self.random_element(self.city_formats))
        return self.generator.parse(pattern)

    # https://en.wikipedia.org/wiki/List_of_roads_in_Kuala_Lumpur#Standard_translations
    street_prefixes: ElementsType[str] = [
        "Jln",
        "Jln",
        "Jalan",
        "Jalan",
        "Jalan",
        "Lorong",
    ]

    def street_prefix(self) -> str:
        return self.random_element(self.street_prefixes)

    # https://en.wikipedia.org/wiki/List_of_roads_in_Kuala_Lumpur
    # https://en.wikipedia.org/wiki/List_of_roads_in_Ipoh
    # https://en.wikipedia.org/wiki/Transportation_in_Seremban#Inner_city_roads
    # https://en.wikipedia.org/wiki/List_of_streets_in_George_Town,_Penang
    street_suffixes: ElementsType[str] = [
        "Air Itam",
        "Alor",
        "Ampang",
        "Ampang Hilir",
        "Anson",
        "Ariffin",
        "Bangsar",
        "Baru",
        "Bellamy",
        "Birch",
        "Bijih Timah",
        "Bukit Aman",
        "Bukit Bintang",
        "Bukit Petaling",
        "Bukit Tunku",
        "Cantonment",
        "Cenderawasih",
        "Chan Sow Lin",
        "Chow Kit",
        "Cinta",
        "Cochrane",
        "Conlay",
        "D. S. Ramanathan",
        "Damansara",
        "Dang Wangi",
        "Davis",
        "Dewan Bahasa",
        "Dato Abdul Rahman",
        "Dato'Keramat",
        "Dato' Maharaja Lela",
        "Doraisamy",
        "Eaton",
        "Faraday",
        "Galloway",
        "Genting Klang",
        "Gereja",
        "Hang Jebat",
        "Hang Kasturi",
        "Hang Lekir",
        "Hang Lekiu",
        "Hang Tuah",
        "Hospital",
        "Imbi",
        "Istana",
        "Jelutong",
        "Kampung Attap",
        "Kebun Bunga",
        "Kedah",
        "Keliling",
        "Kia Peng",
        "Kinabalu",
        "Kuala Kangsar",
        "Kuching",
        "Ledang",
        "Lembah Permai",
        "Loke Yew",
        "Lt. Adnan",
        "Lumba Kuda",
        "Madras",
        "Magazine",
        "Maharajalela",
        "Masjid",
        "Maxwell",
        "Mohana Chandran",
        "Muda",
        "P. Ramlee",
        "Padang Kota Lama",
        "Pahang",
        "Pantai Baharu",
        "Parlimen",
        "Pasar",
        "Pasar Besar",
        "Perak",
        "Perdana",
        "Petaling",
        "Prangin",
        "Pudu",
        "Pudu Lama",
        "Raja",
        "Raja Abdullah",
        "Raja Chulan",
        "Raja Laut",
        "Rakyat",
        "Residensi",
        "Robson",
        "S.P. Seenivasagam",
        "Samarahan 1",
        "Selamat",
        "Sempadan",
        "Sentul",
        "Serian 1",
        "Sasaran",
        "Sin Chee",
        "Sultan Abdul Samad",
        "Sultan Azlan Shah",
        "Sultan Iskandar",
        "Sultan Ismail",
        "Sultan Sulaiman",
        "Sungai Besi",
        "Syed Putra",
        "Tan Cheng Lock",
        "Thambipillay",
        "Tugu",
        "Tuanku Abdul Halim",
        "Tuanku Abdul Rahman",
        "Tun Abdul Razak",
        "Tun Dr Ismail",
        "Tun H S Lee",
        "Tun Ismail",
        "Tun Perak",
        "Tun Razak",
        "Tun Sambanthan",
        "U-Thant",
        "Utama",
        "Vermont",
        "Vivekananda",
        "Wan Kadir",
        "Wesley",
        "Wisma Putra",
        "Yaacob Latif",
        "Yap Ah Loy",
        "Yap Ah Shak",
        "Yap Kwan Seng",
        "Yew",
        "Zaaba",
        "Zainal Abidin",
    ]

    street_name_formats: ElementsType[str] = (
        "{{street_prefix}} %",
        "{{street_prefix}} %/%",
        "{{street_prefix}} %/%#",
        "{{street_prefix}} %/%?",
        "{{street_prefix}} %/%#?",
        "{{street_prefix}} %?",
        "{{street_prefix}} %#?",
        "{{street_prefix}} {{street_suffix}}",
        "{{street_prefix}} {{street_suffix}} %",
        "{{street_prefix}} {{street_suffix}} %/%",
        "{{street_prefix}} {{street_suffix}} %/%#",
        "{{street_prefix}} {{street_suffix}} %/%?",
        "{{street_prefix}} {{street_suffix}} %/%#?",
        "{{street_prefix}} {{street_suffix}} %?",
        "{{street_prefix}} {{street_suffix}} %#?",
    )

    def street_name(self) -> str:
        """
        :example: 'Crist Parks'
        """
        pattern: str = self.bothify(self.random_element(self.street_name_formats))
        return self.generator.parse(pattern)

    building_prefixes: ElementsType[str] = [
        "",
        "",
        "",
        "",
        "",
        "",
        "No. ",
        "No. ",
        "No. ",
        "Lot ",
    ]

    def building_prefix(self) -> str:
        return self.random_element(self.building_prefixes)

    building_number_formats: ElementsType[str] = (
        "%",
        "%",
        "%",
        "%#",
        "%#",
        "%#",
        "%#",
        "%##",
        "%-%",
        "?-##-##",
        "%?-##",
    )

    def building_number(self) -> str:
        return self.bothify(self.random_element(self.building_number_formats))

    street_address_formats: ElementsType[str] = ("{{building_prefix}}{{building_number}}, {{street_name}}",)

    def city_state(self) -> str:
        """Return the complete city address with matching postcode and state

        Example: 55100 Bukit Bintang, Kuala Lumpur
        """
        state: str = self.random_element(self.states.keys())
        postcode = self.postcode_in_state(state)
        city = self.city()
        state_name: str = self.random_element(self.states[state])

        return f"{postcode} {city}, {state_name}"

    # https://en.wikipedia.org/wiki/Addresses_in_Malaysia
    # street number, street name, region, and town/city, state.
    address_formats = OrderedDict((("{{street_address}}, {{city}}, {{city_state}}", 100.0),))

    def city_prefix(self) -> str:
        return self.random_element(self.city_prefixes)

    def administrative_unit(self) -> str:
        return self.random_element(self.states[self.random_element(self.states.keys())])

    state = administrative_unit

    def postcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        """
        :returns: A random postcode within the provided state

        :param state: A state

        Example: 55100
        https://en.wikipedia.org/wiki/Postal_codes_in_Malaysia#States
        """

        if state_abbr is None:
            state_abbr = self.random_element(self.states.keys())

        try:
            # some states have multiple ranges so first pick one, then generate a random postcode
            range = self.generator.random.choice(self.states_postcode[state_abbr])
            postcode = "%d" % (self.generator.random.randint(*range))

            # zero left pad up until desired length (some have length 3 or 4)
            target_postcode_len = 5
            current_postcode_len = len(postcode)
            if current_postcode_len < target_postcode_len:
                pad = target_postcode_len - current_postcode_len
                postcode = f"{'0'*pad}{postcode}"

            return postcode
        except KeyError as e:
            raise KeyError("State Abbreviation not found in list") from e

    def postcode(self) -> str:
        return self.postcode_in_state(None)
