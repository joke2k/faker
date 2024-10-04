from typing import Dict, List, Optional, Tuple

from typing_extensions import TypeAlias

from faker.providers.address import Provider as AddressProvider

Range: TypeAlias = Tuple[int, int]


class Provider(AddressProvider):
    # City and States names taken from wikipedia
    # Street format taken from some common famous places in India
    # Link for cities: https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population
    # Link for States: https://en.wikipedia.org/wiki/States_and_union_territories_of_India
    # Links for street name formats: https://www.mumbai77.com/city/3313/travel/old-new-street-names/

    city_formats = ("{{city_name}}",)

    street_name_formats = (
        "{{last_name}} Nagar",
        "{{last_name}} Zila",
        "{{last_name}} Street",
        "{{last_name}} Ganj",
        "{{last_name}} Road",
        "{{last_name}} Path",
        "{{last_name}} Marg",
        "{{last_name}} Chowk",
        "{{last_name}} Circle",
        "{{last_name}}",
    )

    street_address_formats = (
        "{{building_number}}, {{street_name}}",
        "{{building_number}}\n{{street_name}}",
    )

    address_formats = (
        "{{street_address}}\n{{city}} {{postcode}}",
        "{{street_address}}\n{{city}}-{{postcode}}",
        "{{street_address}}, {{city}} {{postcode}}",
        "{{street_address}}, {{city}}-{{postcode}}",
    )

    building_number_formats = ("H.No. ###", "###", "H.No. ##", "##", "##/##", "##/###")

    postcode_formats = ("######",)

    cities = (
        "Mumbai",
        "Delhi",
        "Kolkata",
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Ahmedabad",
        "Kanpur",
        "Pune",
        "Surat",
        "Jaipur",
        "Lucknow",
        "Nagpur",
        "Indore",
        "Bhopal",
        "Ludhiana",
        "Patna",
        "Visakhapatnam",
        "Vadodara",
        "Agra",
        "Thane",
        "Kalyan-Dombivli",
        "Varanasi",
        "Ranchi",
        "Nashik",
        "Dhanbad",
        "Faridabad",
        "Meerut",
        "Pimpri-Chinchwad",
        "Howrah",
        "Allahabad",
        "Ghaziabad",
        "Rajkot",
        "Amritsar",
        "Jabalpur",
        "Coimbatore",
        "Madurai",
        "Srinagar",
        "Aurangabad",
        "Solapur",
        "Vijayawada",
        "Jodhpur",
        "Gwalior",
        "Guwahati",
        "Chandigarh",
        "Hubli–Dharwad",
        "Mysore",
        "Tiruchirappalli",
        "Bareilly",
        "Jalandhar",
        "Navi Mumbai",
        "Salem",
        "Kota",
        "Vasai-Virar",
        "Aligarh",
        "Moradabad",
        "Bhubaneswar",
        "Gorakhpur",
        "Raipur",
        "Bhiwandi",
        "Kochi",
        "Jamshedpur",
        "Bhilai",
        "Amravati",
        "Cuttack",
        "Warangal",
        "Bikaner",
        "Mira-Bhayandar",
        "Guntur",
        "Bhavnagar",
        "Durgapur",
        "Kolhapur",
        "Ajmer",
        "Asansol",
        "Ulhasnagar",
        "Siliguri",
        "Jalgaon",
        "Saharanpur",
        "Jamnagar",
        "Bhatpara",
        "Sangli-Miraj & Kupwad",
        "Kozhikode",
        "Nanded",
        "Ujjain",
        "Dehradun",
        "Rourkela",
        "Gulbarga",
        "Tirunelveli",
        "Malegaon",
        "Akola",
        "Belgaum",
        "Mangalore",
        "Bokaro",
        "South Dumdum",
        "Udaipur",
        "Gaya",
        "Maheshtala",
        "Jhansi",
        "Nellore",
        "Jammu",
        "Thiruvananthapuram",
        "Davanagere",
        "Kollam",
        "Panihati",
        "Kurnool",
        "Tiruppur",
        "Dhule",
        "Bhagalpur",
        "Rajpur Sonarpur",
        "Kakinada",
        "Thrissur",
        "Bellary",
        "Muzaffarnagar",
        "Korba",
        "Rajahmundry",
        "Kamarhati",
        "Ambattur",
        "Berhampur",
        "Ahmednagar",
        "Muzaffarpur",
        "Noida",
        "Patiala",
        "Mathura",
        "New Delhi",
        "Latur",
        "Sambalpur",
        "Shahjahanpur",
        "Kulti",
        "Chandrapur",
        "Nizamabad",
        "Rohtak",
        "Bardhaman",
        "Rampur",
        "Bhilwara",
        "Firozabad",
        "Bilaspur",
        "Shimoga",
        "Agartala",
        "Gopalpur",
        "Darbhanga",
        "Panipat",
        "Bally",
        "Alwar",
        "Parbhani",
        "Ichalkaranji",
        "Anantapuram",
        "Baranagar",
        "Tumkur",
        "Ramagundam",
        "Jalna",
        "Durg",
        "Sagar",
        "Bihar Sharif",
        "Dewas",
        "Barasat",
        "Avadi",
        "Farrukhabad",
        "Aizawl",
        "Tirupati",
        "Bijapur",
        "Satara",
        "Satna",
        "Ratlam",
        "Imphal",
        "Pondicherry",
        "North Dumdum",
        "Anantapur",
        "Khammam",
        "Ozhukarai",
        "Bathinda",
        "Thoothukudi",
        "Thanjavur",
        "Naihati",
        "Sonipat",
        "Mau",
        "Tiruvottiyur",
        "Hapur",
        "Sri Ganganagar",
        "Karnal",
        "Etawah",
        "Nagercoil",
        "Raichur",
        "Raurkela Industrial Township",
        "Secunderabad",
        "Karimnagar",
        "Mirzapur",
        "Bharatpur",
        "Ambarnath",
        "Arrah",
        "Uluberia",
        "Serampore",
        "Dindigul",
        "Gandhinagar",
        "Burhanpur",
        "Nadiad",
        "Eluru",
        "Yamunanagar",
        "Kharagpur",
        "Munger",
        "Pali",
        "Katni",
        "Singrauli",
        "Tenali",
        "Sikar",
        "Silchar",
        "Rewa",
        "Sambhal",
        "Machilipatnam",
        "Vellore",
        "Alappuzha",
        "Bulandshahr",
        "Haridwar",
        "Vijayanagaram",
        "Erode",
        "Gurgaon",
        "Bidar",
        "Bhusawal",
        "Khandwa",
        "Purnia",
        "Haldia",
        "Chinsurah",
        "Bhiwani",
        "Raebareli",
        "Junagadh",
        "Bahraich",
        "Gandhidham",
        "Mango",
        "Raiganj",
        "Amroha",
        "Sultan Pur Majra",
        "Hospet",
        "Bidhannagar",
        "Malda",
        "Sirsa",
        "Berhampore",
        "Jaunpur",
        "Surendranagar Dudhrej",
        "Madhyamgram",
        "Kirari Suleman Nagar",
        "Bhind",
        "Nandyal",
        "Chittoor",
        "Bhalswa Jahangir Pur",
        "Fatehpur",
        "Morena",
        "Nangloi Jat",
        "Ongole",
        "Karawal Nagar",
        "Shivpuri",
        "Morbi",
        "Unnao",
        "Pallavaram",
        "Kumbakonam",
        "Shimla",
        "Mehsana",
        "Panchkula",
        "Orai",
        "Ambala",
        "Dibrugarh",
        "Guna",
        "Danapur",
        "Sasaram",
        "Anand",
        "Kottayam",
        "Hazaribagh",
        "Kadapa",
        "Saharsa",
        "Nagaon",
        "Loni",
        "Hajipur",
        "Dehri",
        "Bettiah",
        "Katihar",
        "Deoghar",
        "Jorhat",
        "Siwan",
        "Panvel",
        "Hosur",
        "Tinsukia",
        "Bongaigaon",
        "Motihari",
        "Jamalpur",
        "Suryapet",
        "Begusarai",
        "Miryalaguda",
        "Proddatur",
        "Karaikudi",
        "Kishanganj",
        "Phusro",
        "Buxar",
        "Tezpur",
        "Jehanabad",
        "Aurangabad",
        "Chapra",
        "Ramgarh",
        "Gangtok",
        "Adoni",
        "Amaravati",
        "Ballia",
        "Bhimavaram",
        "Dharmavaram",
        "Giridih",
        "Gudivada",
        "Guntakal",
        "Hindupur",
        "Kavali",
        "Khora ",
        "Ghaziabad",
        "Madanapalle",
        "Mahbubnagar",
        "Medininagar",
        "Narasaraopet",
        "Phagwara",
        "Pudukkottai",
        "Srikakulam",
        "Tadepalligudem",
        "Tadipatri",
        "Udupi",
    )

    states = (
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
    )

    states_abbr: Tuple[str, ...] = (
        "AP",
        "AR",
        "AS",
        "BR",
        "CG",
        "GA",
        "GJ",
        "HR",
        "HP",
        "JH",
        "KA",
        "KL",
        "MP",
        "MH",
        "MN",
        "ML",
        "MZ",
        "NL",
        "OD",
        "PB",
        "RJ",
        "SK",
        "TN",
        "TG",
        "TR",
        "UK",
        "UP",
        "WB",
    )

    union_territories = (
        ("Andaman and Nicobar Islands",),
        ("Chandigarh",),
        ("Dadra and Nagar Haveli, Dadra & Nagar Haveli",),
        ("Daman and Diu",),
        ("Delhi, National Capital Territory of Delhi",),
        ("Jammu and Kashmir",),
        ("Ladakh",),
        ("Lakshadweep",),
        ("Pondicherry",),
        ("Puducherry",),
    )

    union_territories_abbr = (
        "AN",
        "CH",
        "DN",
        "DD",
        "DL",
        "JK",
        "LA",
        "LD",
        "PY",
    )

    # https://en.wikipedia.org/wiki/Postal_Index_Number

    # FIXME: Some states such as `BR/JH` / `UK/UP` have similar PIN code ranges
    # FIXME: as mentioned in above link.

    state_pincode: Dict[str, List[Range]] = {
        "AP": [(510_000, 539_999)],
        "AR": [(790_000, 792_999)],
        "AS": [(780_000, 789_999)],
        "BR": [(800_000, 859_999)],
        "CG": [(490_000, 499_999)],
        "GA": [(403_000, 403_999)],
        "GJ": [(360_000, 399_999)],
        "HR": [(120_000, 139_999)],
        "HP": [(170_000, 179_999)],
        "JH": [(800_000, 859_999)],
        "KA": [(560_000, 599_999)],
        "KL": [(670_000, 681_999), (683_000, 699_999)],
        "MP": [(450_000, 489_999)],
        "MH": [(400_000, 402_999), (404_000, 449_999)],
        "MN": [(795_000, 795_999)],
        "ML": [(793_000, 794_999)],
        "MZ": [(796_000, 796_999)],
        "NL": [(797_000, 798_999)],
        "OD": [(750_000, 779_999)],
        "PB": [(140_000, 159_999)],
        "RJ": [(300_000, 349_999)],
        "SK": [(737_000, 737_999)],
        "TN": [(600_000, 669_999)],
        "TG": [(500_000, 509_999)],
        "TR": [(799_000, 799_999)],
        "UK": [(200_000, 289_999)],
        "UP": [(200_000, 289_999)],
        "WB": [(700_000, 736_999), (738_000, 743_999), (745_000, 749_999)],
    }

    union_territories_pincode: Dict[str, List[Range]] = {
        "AN": [(744_000, 744_999)],
        "CH": [(160_000, 169_999)],
        "DN": [(396_000, 396_999)],
        "DD": [(396_000, 396_999)],
        "DL": [(110_000, 119_999)],
        "JK": [(180_000, 199_999)],
        "LA": [(180_000, 199_999)],
        "LD": [(682_000, 682_999)],
        "PY": [(605_000, 605_999)],
    }

    army_pincode: Dict[str, Range] = {"APS": (900_000, 999_999)}

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        return self.random_element(self.states)

    state = administrative_unit

    def union_territory(self) -> str:
        """Returns random union territory name"""

        return self.random_element(self.union_territories)[0]

    def pincode_in_state(self, state_abbr: Optional[str] = None, include_union_territories: bool = False) -> int:
        """Random PIN Code within provided state abbreviation

        :param state_abbr: State Abbr, defaults to None
        :param include_union_territories: Include Union Territories ?, defaults to False
        :raises ValueError: If incorrect state abbr
        :return: PIN Code
        """

        known_abbrs = self.states_abbr
        if include_union_territories:
            known_abbrs += self.union_territories_abbr

        if state_abbr is None:
            state_abbr = self.random_element(known_abbrs)

        if state_abbr in known_abbrs:
            codes = self.state_pincode
            if include_union_territories:
                codes.update(self.union_territories_pincode)

            pincode_range = self.random_element(codes[state_abbr])

            return self.generator.random.randint(*pincode_range)

        raise ValueError("State Abbreviation not found in list")

    def pincode_in_military(self) -> int:
        """Random PIN Code within Army Postal Service range"""

        key: str = self.random_element(self.army_pincode.keys())

        return self.generator.random.randint(*self.army_pincode[key])

    # Aliases

    def zipcode_in_state(self, state_abbr: Optional[str] = None, include_union_territories: bool = False) -> int:
        return self.pincode_in_state(state_abbr, include_union_territories)

    def postcode_in_state(self, state_abbr: Optional[str] = None, include_union_territories: bool = False) -> int:
        return self.pincode_in_state(state_abbr, include_union_territories)

    def pincode_in_army(self) -> int:
        return self.pincode_in_military()

    def zipcode_in_military(self) -> int:
        return self.pincode_in_military()

    def zipcode_in_army(self) -> int:
        return self.pincode_in_military()

    def postcode_in_military(self) -> int:
        return self.pincode_in_military()

    def postcode_in_army(self) -> int:
        return self.pincode_in_military()
