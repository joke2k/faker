from typing import Dict, Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """Address provider for Turkey.

    Provinces (il) are listed with their official plate codes, which are also
    the first two digits of every postal code in that province. Districts
    (ilçe) are given for the most populous provinces, so that a full
    ``address()`` always combines a district with its own province and a
    matching postal code.

    Sources:
    - https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_illeri
    - https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_il%C3%A7eleri
    """

    city_formats = ("{{city_name}}",)
    street_name_formats = ("{{street}} {{street_suffix}}",)
    street_address_formats = (
        "{{street_name}} No: {{building_number}}",
        "{{street_name}} No: {{building_number}} Daire: {{apartment_number}}",
    )
    building_number_formats = ("%", "%#", "%##", "%/%", "%#/%")
    apartment_number_formats = ("%", "%#")

    street_suffixes = ("Caddesi", "Sokak", "Bulvarı")

    # Plate code -> province name, in official order (01-81).
    provinces: Dict[str, str] = {
        "01": "Adana",
        "02": "Adıyaman",
        "03": "Afyonkarahisar",
        "04": "Ağrı",
        "05": "Amasya",
        "06": "Ankara",
        "07": "Antalya",
        "08": "Artvin",
        "09": "Aydın",
        "10": "Balıkesir",
        "11": "Bilecik",
        "12": "Bingöl",
        "13": "Bitlis",
        "14": "Bolu",
        "15": "Burdur",
        "16": "Bursa",
        "17": "Çanakkale",
        "18": "Çankırı",
        "19": "Çorum",
        "20": "Denizli",
        "21": "Diyarbakır",
        "22": "Edirne",
        "23": "Elazığ",
        "24": "Erzincan",
        "25": "Erzurum",
        "26": "Eskişehir",
        "27": "Gaziantep",
        "28": "Giresun",
        "29": "Gümüşhane",
        "30": "Hakkari",
        "31": "Hatay",
        "32": "Isparta",
        "33": "Mersin",
        "34": "İstanbul",
        "35": "İzmir",
        "36": "Kars",
        "37": "Kastamonu",
        "38": "Kayseri",
        "39": "Kırklareli",
        "40": "Kırşehir",
        "41": "Kocaeli",
        "42": "Konya",
        "43": "Kütahya",
        "44": "Malatya",
        "45": "Manisa",
        "46": "Kahramanmaraş",
        "47": "Mardin",
        "48": "Muğla",
        "49": "Muş",
        "50": "Nevşehir",
        "51": "Niğde",
        "52": "Ordu",
        "53": "Rize",
        "54": "Sakarya",
        "55": "Samsun",
        "56": "Siirt",
        "57": "Sinop",
        "58": "Sivas",
        "59": "Tekirdağ",
        "60": "Tokat",
        "61": "Trabzon",
        "62": "Tunceli",
        "63": "Şanlıurfa",
        "64": "Uşak",
        "65": "Van",
        "66": "Yozgat",
        "67": "Zonguldak",
        "68": "Aksaray",
        "69": "Bayburt",
        "70": "Karaman",
        "71": "Kırıkkale",
        "72": "Batman",
        "73": "Şırnak",
        "74": "Bartın",
        "75": "Ardahan",
        "76": "Iğdır",
        "77": "Yalova",
        "78": "Karabük",
        "79": "Kilis",
        "80": "Osmaniye",
        "81": "Düzce",
    }
    cities = tuple(provinces.values())

    # Plate code -> all districts of that province.
    districts: Dict[str, Tuple[str, ...]] = {
        "01": (
            "Aladağ",
            "Ceyhan",
            "Çukurova",
            "Feke",
            "İmamoğlu",
            "Karaisalı",
            "Karataş",
            "Kozan",
            "Pozantı",
            "Saimbeyli",
            "Sarıçam",
            "Seyhan",
            "Tufanbeyli",
            "Yumurtalık",
            "Yüreğir",
        ),
        "06": (
            "Akyurt",
            "Altındağ",
            "Ayaş",
            "Bala",
            "Beypazarı",
            "Çamlıdere",
            "Çankaya",
            "Çubuk",
            "Elmadağ",
            "Etimesgut",
            "Evren",
            "Gölbaşı",
            "Güdül",
            "Haymana",
            "Kahramankazan",
            "Kalecik",
            "Keçiören",
            "Kızılcahamam",
            "Mamak",
            "Nallıhan",
            "Polatlı",
            "Pursaklar",
            "Sincan",
            "Şereflikoçhisar",
            "Yenimahalle",
        ),
        "07": (
            "Akseki",
            "Aksu",
            "Alanya",
            "Demre",
            "Döşemealtı",
            "Elmalı",
            "Finike",
            "Gazipaşa",
            "Gündoğmuş",
            "İbradı",
            "Kaş",
            "Kemer",
            "Kepez",
            "Konyaaltı",
            "Korkuteli",
            "Kumluca",
            "Manavgat",
            "Muratpaşa",
            "Serik",
        ),
        "16": (
            "Büyükorhan",
            "Gemlik",
            "Gürsu",
            "Harmancık",
            "İnegöl",
            "İznik",
            "Karacabey",
            "Keles",
            "Kestel",
            "Mudanya",
            "Mustafakemalpaşa",
            "Nilüfer",
            "Orhaneli",
            "Orhangazi",
            "Osmangazi",
            "Yenişehir",
            "Yıldırım",
        ),
        "26": (
            "Alpu",
            "Beylikova",
            "Çifteler",
            "Günyüzü",
            "Han",
            "İnönü",
            "Mahmudiye",
            "Mihalgazi",
            "Mihalıççık",
            "Odunpazarı",
            "Sarıcakaya",
            "Seyitgazi",
            "Sivrihisar",
            "Tepebaşı",
        ),
        "27": (
            "Araban",
            "İslahiye",
            "Karkamış",
            "Nizip",
            "Nurdağı",
            "Oğuzeli",
            "Şahinbey",
            "Şehitkamil",
            "Yavuzeli",
        ),
        "33": (
            "Akdeniz",
            "Anamur",
            "Aydıncık",
            "Bozyazı",
            "Çamlıyayla",
            "Erdemli",
            "Gülnar",
            "Mezitli",
            "Mut",
            "Silifke",
            "Tarsus",
            "Toroslar",
            "Yenişehir",
        ),
        "34": (
            "Adalar",
            "Arnavutköy",
            "Ataşehir",
            "Avcılar",
            "Bağcılar",
            "Bahçelievler",
            "Bakırköy",
            "Başakşehir",
            "Bayrampaşa",
            "Beşiktaş",
            "Beykoz",
            "Beylikdüzü",
            "Beyoğlu",
            "Büyükçekmece",
            "Çatalca",
            "Çekmeköy",
            "Esenler",
            "Esenyurt",
            "Eyüpsultan",
            "Fatih",
            "Gaziosmanpaşa",
            "Güngören",
            "Kadıköy",
            "Kağıthane",
            "Kartal",
            "Küçükçekmece",
            "Maltepe",
            "Pendik",
            "Sancaktepe",
            "Sarıyer",
            "Silivri",
            "Sultanbeyli",
            "Sultangazi",
            "Şile",
            "Şişli",
            "Tuzla",
            "Ümraniye",
            "Üsküdar",
            "Zeytinburnu",
        ),
        "35": (
            "Aliağa",
            "Balçova",
            "Bayındır",
            "Bayraklı",
            "Bergama",
            "Beydağ",
            "Bornova",
            "Buca",
            "Çeşme",
            "Çiğli",
            "Dikili",
            "Foça",
            "Gaziemir",
            "Güzelbahçe",
            "Karabağlar",
            "Karaburun",
            "Karşıyaka",
            "Kemalpaşa",
            "Kınık",
            "Kiraz",
            "Konak",
            "Menderes",
            "Menemen",
            "Narlıdere",
            "Ödemiş",
            "Seferihisar",
            "Selçuk",
            "Tire",
            "Torbalı",
            "Urla",
        ),
        "41": (
            "Başiskele",
            "Çayırova",
            "Darıca",
            "Derince",
            "Dilovası",
            "Gebze",
            "Gölcük",
            "İzmit",
            "Kandıra",
            "Karamürsel",
            "Kartepe",
            "Körfez",
        ),
        "55": (
            "19 Mayıs",
            "Alaçam",
            "Asarcık",
            "Atakum",
            "Ayvacık",
            "Bafra",
            "Canik",
            "Çarşamba",
            "Havza",
            "İlkadım",
            "Kavak",
            "Ladik",
            "Salıpazarı",
            "Tekkeköy",
            "Terme",
            "Vezirköprü",
            "Yakakent",
        ),
        "61": (
            "Akçaabat",
            "Araklı",
            "Arsin",
            "Beşikdüzü",
            "Çarşıbaşı",
            "Çaykara",
            "Dernekpazarı",
            "Düzköy",
            "Hayrat",
            "Köprübaşı",
            "Maçka",
            "Of",
            "Ortahisar",
            "Sürmene",
            "Şalpazarı",
            "Tonya",
            "Vakfıkebir",
            "Yomra",
        ),
    }

    # Common neighbourhood (mahalle) names found in many Turkish cities.
    neighborhoods = (
        "Akıncılar",
        "Atatürk",
        "Bahçelievler",
        "Barbaros",
        "Cumhuriyet",
        "Çamlık",
        "Dumlupınar",
        "Esentepe",
        "Fatih",
        "Fevzi Çakmak",
        "Gazi",
        "Güzelyalı",
        "Hürriyet",
        "İnönü",
        "İstiklal",
        "Kazım Karabekir",
        "Kocatepe",
        "Kurtuluş",
        "Mevlana",
        "Mimar Sinan",
        "Sakarya",
        "Selimiye",
        "Yeşilyurt",
        "Yıldıztepe",
        "Yunus Emre",
        "Zafer",
    )

    # Common street name stems, combined with a street suffix.
    streets = (
        "Akasya",
        "Atatürk",
        "Bahçe",
        "Barış",
        "Cumhuriyet",
        "Çiçek",
        "Çınar",
        "Değirmen",
        "Erguvan",
        "Fevzi Çakmak",
        "Gazi",
        "Gül",
        "Güneş",
        "Hastane",
        "Ihlamur",
        "İnönü",
        "İstasyon",
        "İstiklal",
        "Kavak",
        "Lale",
        "Manolya",
        "Menekşe",
        "Mevlana",
        "Mimar Sinan",
        "Nergis",
        "Okul",
        "Papatya",
        "Pınar",
        "Sedir",
        "Söğüt",
        "Yıldız",
        "Yunus Emre",
        "Zambak",
    )

    def street(self) -> str:
        """
        :example: "Lale"
        """
        return self.random_element(self.streets)

    def neighborhood(self) -> str:
        """
        :example: "Cumhuriyet Mahallesi"
        """
        return self.random_element(self.neighborhoods) + " Mahallesi"

    def apartment_number(self) -> str:
        """
        :example: "4"
        """
        return self.numerify(self.random_element(self.apartment_number_formats))

    def city_name(self) -> str:
        """
        :example: "Ankara"
        """
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        """
        :example: "Ankara"
        """
        return self.random_element(self.cities)

    province = administrative_unit

    def province_plate_code(self) -> str:
        """
        :example: "06"
        """
        return self.random_element(tuple(self.provinces.keys()))

    def district(self) -> str:
        """
        :example: "Çankaya"
        """
        plate_code: str = self.random_element(tuple(self.districts.keys()))
        return self.random_element(self.districts[plate_code])

    def postcode(self) -> str:
        """
        Postal codes are five digits; the first two are the province plate code.

        :example: "06420"
        """
        return self.province_plate_code() + self.numerify("###")

    def address(self) -> str:
        """
        :example: "Cumhuriyet Mahallesi, Lale Sokak No: 12 Daire: 4, 06420 Çankaya/Ankara"
        """
        plate_code: str = self.random_element(tuple(self.districts.keys()))
        district: str = self.random_element(self.districts[plate_code])
        postcode = plate_code + self.numerify("###")
        return f"{self.neighborhood()}, {self.street_address()}, " f"{postcode} {district}/{self.provinces[plate_code]}"
