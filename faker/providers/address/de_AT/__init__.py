from ..de import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{city_name}}",)

    city_with_postcode_formats = ("{{postcode}} {{city}}",)

    street_name_formats = (
        "{{first_name}}-{{last_name}}-{{street_suffix_long}}",
        "{{last_name}}{{street_suffix_short}}",
    )
    street_address_formats = ("{{street_name}} {{building_number}}",)
    address_formats = ("{{street_address}}\n{{postcode}} {{city}}",)

    building_number_formats = ("###", "##", "#", "#/#")

    street_suffixes_long = (
        "Gasse",
        "Platz",
        "Ring",
        "Straße",
        "Weg",
    )
    street_suffixes_short = (
        "gasse",
        "platz",
        "ring",
        "straße",
        "str.",
        "weg",
    )

    # https://en.wikipedia.org/wiki/List_of_postal_codes_in_Austria
    postcode_formats = (
        "1###",
        "2###",
        "3###",
        "4###",
        "5###",
        "6###",
        "7###",
        "8###",
        "9###",
    )

    # https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Austria
    cities = (
        "Allentsteig",
        "Altheim",
        "Althofen",
        "Amstetten",
        "Ansfelden",
        "Attnang-Puchheim",
        "Bad Aussee",
        "Bad Hall",
        "Bad Ischl",
        "Bad Leonfelden",
        "Bad Radkersburg",
        "Bad Sankt Leonhard im Lavanttal",
        "Bad Vöslau",
        "Baden",
        "Bärnbach",
        "Berndorf",
        "Bischofshofen",
        "Bleiburg",
        "Bludenz",
        "Braunau am Inn",
        "Bregenz",
        "Bruck an der Leitha",
        "Bruck an der Mur",
        "Deutsch-Wagram",
        "Deutschlandsberg",
        "Dornbirn",
        "Drosendorf-Zissersdorf 1",
        "Dürnstein",
        "Ebenfurth",
        "Ebreichsdorf",
        "Eferding",
        "Eggenburg",
        "Eisenerz",
        "Eisenstadt",
        "Enns",
        "Fehring",
        "Feldbach",
        "Feldkirch",
        "Feldkirchen",
        "Ferlach",
        "Fischamend",
        "Frauenkirchen",
        "Freistadt",
        "Friedberg",
        "Friesach",
        "Frohnleiten",
        "Fürstenfeld",
        "Gallneukirchen",
        "Gänserndorf",
        "Geras",
        "Gerasdorf bei Wien",
        "Gföhl",
        "Gleisdorf",
        "Gloggnitz",
        "Gmünd",
        "Gmünd in Kärnten",
        "Gmunden",
        "Graz",
        "Grein",
        "Grieskirchen",
        "Groß-Enzersdorf",
        "Groß-Gerungs",
        "Groß-Siegharts",
        "Güssing",
        "Haag",
        "Hainburg an der Donau",
        "Hainfeld",
        "Hall in Tirol",
        "Hallein",
        "Hardegg",
        "Hartberg",
        "Heidenreichstein",
        "Herzogenburg",
        "Imst",
        "Innsbruck",
        "Jennersdorf",
        "Judenburg",
        "Kapfenberg",
        "Kindberg",
        "Klagenfurt",
        "Klosterneuburg",
        "Knittelfeld",
        "Köflach",
        "Korneuburg",
        "Krems an der Donau",
        "Kufstein",
        "Laa an der Thaya",
        "Laakirchen",
        "Landeck",
        "Langenlois",
        "Leibnitz",
        "Leoben",
        "Lienz",
        "Liezen",
        "Lilienfeld",
        "Linz",
        "Litschau",
        "Maissau",
        "Mank",
        "Mannersdorf am Leithagebirge",
        "Marchegg",
        "Marchtrenk",
        "Mariazell",
        "Mattersburg",
        "Mattighofen",
        "Mautern an der Donau",
        "Melk",
        "Mistelbach an der Zaya",
        "Mödling",
        "Murau",
        "Mureck",
        "Mürzzuschlag",
        "Neulengbach",
        "Neumarkt am Wallersee",
        "Neunkirchen",
        "Neusiedl am See",
        "Oberndorf bei Salzburg",
        "Oberpullendorf",
        "Oberwart",
        "Oberwälz",
        "Perg",
        "Peuerbach",
        "Pinkafeld",
        "Pöchlarn",
        "Poysdorf",
        "Pregarten",
        "Pulkau",
        "Purbach am Neusiedler See",
        "Purkersdorf",
        "Raabs an der Thaya",
        "Radenthein",
        "Radstadt",
        "Rattenberg",
        "Retz",
        "Ried im Innkreis",
        "Rohrbach in Oberösterreich",
        "Rottenmann",
        "Rust",
        "Saalfelden am Steinernen Meer",
        "Salzburg",
        "Sankt Andrä im Lavanttal",
        "Sankt Johann im Pongau",
        "Sankt Pölten",
        "Sankt Valentin",
        "Sankt Veit an der Glan",
        "Schärding",
        "Scheibbs",
        "Schladming",
        "Schrattenthal",
        "Schrems",
        "Schwanenstadt",
        "Schwaz",
        "Schwechat",
        "Spittal an der Drau",
        "Stadtschlaining",
        "Steyr",
        "Steyregg",
        "Stockerau",
        "Straßburg",
        "Ternitz",
        "Traiskirchen",
        "Traismauer",
        "Traun",
        "Trieben",
        "Trofaiach",
        "Tulln an der Donau",
        "Villach",
        "Vils",
        "Vöcklabruck",
        "Voitsberg",
        "Völkermarkt",
        "Waidhofen an der Thaya",
        "Waidhofen an der Ybbs",
        "Weitra",
        "Weiz",
        "Wels",
        "Wien",
        "Wiener Neustadt",
        "Wieselburg",
        "Wilhelmsburg",
        "Wolfsberg",
        "Wolkersdorf",
        "Wörgl",
        "Ybbs an der Donau",
        "Zell am See",
        "Zeltweg",
        "Zistersdorf",
        "Zwettl",
    )

    # https://en.wikipedia.org/wiki/States_of_Austria
    states = (
        "Wien",
        "Steiermark",
        "Burgenland",
        "Tirol",
        "Niederösterreich",
        "Oberösterreich",
        "Salzburg",
        "Kärnten",
        "Vorarlberg",
    )

    # https://statoids.com/yat.html (using HASC codes)
    admin2_in_admin1 = {
        "Burgenland": [
            "Bezirk Eisenstadt",
            "Bezirk Rust",
            "Bezirk Eisenstadt Umgebung",
            "Bezirk Güssing",
            "Bezirk Jennersdorf",
            "Bezirk Mattersburg",
            "Bezirk Neusiedl am See",
            "Bezirk Oberpullendorf",
            "Bezirk Oberwart",
        ],
        "Kärnten": [
            "Bezirk Klagenfurt",
            "Bezirk Villach",
            "Bezirk Hermagor",
            "Bezirk Klagenfurt Land",
            "Bezirk Sankt Veit an der Glan",
            "Bezirk Spittal an der Drau",
            "Bezirk Villach Land",
            "Bezirk Völkermarkt",
            "Bezirk Wolfsberg",
            "Bezirk Feldkirchen",
        ],
        "Niederösterreich": [
            "Bezirk Krems an der Donau Stadt",
            "Bezirk Sankt Pölten",
            "Bezirk Waidhofen an der Ybbs",
            "Bezirk Wiener Neustadt",
            "Bezirk Amstetten",
            "Bezirk Baden",
            "Bezirk Bruck an der Leitha",
            "Bezirk Gänserndorf",
            "Bezirk Gmünd",
            "Bezirk Hollabrunn",
            "Bezirk Horn",
            "Bezirk Korneuburg",
            "Bezirk Krems an der Donau Land",
            "Bezirk Lilienfeld",
            "Bezirk Melk",
            "Bezirk Mistelbach",
            "Bezirk Mödling",
            "Bezirk Neunkirchen",
            "Bezirk Sankt Pölten Land",
            "Bezirk Scheibbs",
            "Bezirk Tulln",
            "Bezirk Waidhofen an der Thaya",
            "Bezirk Wiener Neustadt Land",
            "Bezirk Wien Umgebung",
            "Bezirk Zwettl",
        ],
        "Oberösterreich": [
            "Bezirk Linz",
            "Bezirk Steyr",
            "Bezirk Wels",
            "Bezirk Braunau am Inn",
            "Bezirk Eferding",
            "Bezirk Freistadt",
            "Bezirk Gmunden",
            "Bezirk Grieskirchen",
            "Bezirk Kirchdorf an der Krems",
            "Bezirk Linz Land",
            "Bezirk Perg",
            "Bezirk Ried im Innkreis",
            "Bezirk Rohrbach im Mühlkreis",
            "Bezirk Schärding",
            "Bezirk Steyr Land",
            "Bezirk Urfahr Umgebung",
            "Bezirk Vöcklabruck",
            "Bezirk Wels Land",
        ],
        "Salzburg": [
            "Bezirk Salzburg",
            "Bezirk Hallein",
            "Bezirk Salzburg Umgebung",
            "Bezirk Sankt Johann im Pongau",
            "Bezirk Tamsweg",
            "Bezirk Zell am See",
        ],
        "Steiermark": [
            "Bezirk Graz",
            "Bezirk Deutschlandsberg",
            "Bezirk Graz Umgebung",
            "Bezirk Leibnitz",
            "Bezirk Leoben",
            "Bezirk Liezen",
            "Bezirk Murau",
            "Bezirk Voitsberg",
            "Bezirk Weiz",
            "Bezirk Murtal",
            "Bezirk Bruck-Mürzzuschlag",
            "Bezirk Hartberg-Fürstenfeld",
            "Bezirk Südoststeiermark",
        ],
        "Tirol": [
            "Bezirk Innsbruck",
            "Bezirk Imst",
            "Bezirk Innsbruck Land",
            "Bezirk Kitzbühel",
            "Bezirk Kufstein",
            "Bezirk Landeck",
            "Bezirk Lienz",
            "Bezirk Reutte",
            "Bezirk Schwaz",
        ],
        "Vorarlberg": [
            "Bezirk Bludenz",
            "Bezirk Bregenz",
            "Bezirk Dornbirn",
            "Bezirk Feldkirch",
        ],
        "Wien": ["Bezirk Wien"],
    }
    municipality_key_formats = (
        "1####",
        "2####",
        "3####",
        "4####",
        "5####",
        "6####",
        "7####",
        "8####",
        "9####",
    )

    def street_suffix_short(self) -> str:
        return self.random_element(self.street_suffixes_short)

    def street_suffix_long(self) -> str:
        return self.random_element(self.street_suffixes_long)

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        return self.random_element(self.states)

    state = administrative_unit
    admin1 = administrative_unit

    def admin2(self) -> str:
        return self.random_element(
            tuple(
                admin2
                for admin2s in self.admin2_in_admin1.values()
                for admin2 in admin2s
            )
        )

    def admin2_from_admin1(self, admin1: str) -> str:
        return self.random_element(self.admin2_in_admin1[admin1])

    def admin2_with_admin1(self) -> str:
        admin1 = self.admin1()
        admin2 = self.admin2_from_admin1(admin1)
        return f"{admin2} {admin1}"

    def admin2_w_admin1(self, admin1: str) -> str:
        admin2 = self.admin2_from_admin1(admin1)
        return f"{admin2} {admin1}"

    def city_with_postcode(self) -> str:
        pattern: str = self.random_element(self.city_with_postcode_formats)
        return self.generator.parse(pattern)
