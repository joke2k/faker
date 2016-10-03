# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    cities = (
        'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk',
        'Szczecin',
        'Bydgoszcz', 'Lublin', 'Katowice', 'Białystok', 'Gdynia',
        'Częstochowa', 'Radom', 'Sosnowiec', 'Toruń', 'Kielce', 'Gliwice',
        'Rzeszów', 'Zabrze', 'Bytom', 'Olsztyn', 'Bielsko-Biała',
        'Ruda Śląska',
        'Rybnik', 'Tychy', 'Dąbrowa Górnicza', 'Gorzów Wielkopolski',
        'Elbląg',
        'Płock', 'Opole', 'Wałbrzych', 'Zielona Góra', 'Włocławek', 'Tarnów',
        'Chorzów', 'Koszalin', 'Kalisz', 'Legnica', 'Grudziądz', 'Słupsk',
        'Jaworzno', 'Jastrzębie-Zdrój', 'Nowy Sącz', 'Jelenia Góra', 'Konin',
        'Piotrków Trybunalski', 'Siedlce', 'Inowrocław', 'Mysłowice', 'Piła',
        'Lubin', 'Ostrów Wielkopolski', 'Ostrowiec Świętokrzyski', 'Gniezno',
        'Stargard Szczeciński', 'Siemianowice Śląskie', 'Suwałki', 'Głogów',
        'Pabianice', 'Chełm', 'Zamość', 'Tomaszów Mazowiecki', 'Leszno',
        'Przemyśl', 'Stalowa Wola', 'Kędzierzyn-Koźle', 'Łomża', 'Żory',
        'Mielec', 'Tarnowskie Góry', 'Tczew', 'Bełchatów', 'Świdnica',
        'Ełk', 'Pruszków', 'Będzin', 'Biała Podlaska', 'Zgierz',
        'Piekary Śląskie', 'Racibórz', 'Legionowo', 'Ostrołęka',
        'Świętochłowice', 'Starachowice', 'Zawiercie', 'Wejherowo',
        'Puławy', 'Wodzisław Śląski', 'Starogard Gdański', 'Skierniewice',
        'Tarnobrzeg', 'Skarżysko-Kamienna', 'Radomsko', 'Krosno', 'Rumia',
        'Dębica', 'Kołobrzeg', 'Kutno', 'Nysa', 'Ciechanów', 'Otwock',
        'Piaseczno', 'Zduńska Wola', 'Sieradz', 'Świnoujście', 'Żyrardów',
        'Szczecinek', 'Świdnik', 'Chojnice', 'Nowa Sól', 'Oświęcim',
        'Bolesławiec', 'Mińsk Mazowiecki', 'Mikołów', 'Jarosław', 'Sanok',
        'Knurów', 'Malbork', 'Żary', 'Kwidzyn', 'Chrzanów', 'Sopot',
        'Sochaczew', 'Wołomin', 'Oleśnica', 'Brzeg', 'Olkusz', 'Jasło',
        'Cieszyn', 'Kraśnik', 'Lębork', 'Czechowice-Dziedzice', 'Dzierżoniów',
        'Ostróda', 'Police', 'Nowy Targ', 'Iława', 'Czeladź', 'Myszków',
        'Żywiec', 'Zgorzelec', 'Oława', 'Bielawa', 'Swarzędz', 'Mława',
        'Ząbki', 'Łuków', 'Augustów', 'Śrem', 'Bochnia', 'Luboń', 'Giżycko',
        'Grodzisk Mazowiecki', 'Łowicz', 'Krotoszyn', 'Września',
        'Turek', 'Pruszcz Gdański', 'Brodnica', 'Gorlice',
        'Czerwionka-Leszczyny', 'Kłodzko', 'Marki', 'Nowy Dwór Mazowiecki',
        'Kętrzyn', 'Zakopane', 'Wyszków', 'Biłgoraj', 'Żagań',
        'Bielsk Podlaski', 'Świecie', 'Wałcz', 'Jarocin', 'Pszczyna',
        'Wągrowiec', 'Szczytno', 'Białogard', 'Sandomierz', 'Bartoszyce',
        'Kluczbork', 'Lubliniec', 'Skawina', 'Jawor', 'Kościan', 'Wieluń',
        'Kościerzyna', 'Nowa Ruda', 'Świebodzice', 'Koło', 'Piastów',
        'Goleniów', 'Ostrów Mazowiecka', 'Polkowice', 'Lubartów', 'Zambrów',
        'Płońsk', 'Reda', 'Łaziska Górne', 'Środa Wielkopolska'
    )

    street_prefixes = (
        'ulica', 'aleja', 'plac',
    )

    streets = (
        'Polna', 'Lesna', 'Sloneczna', 'Krótka', 'Szkolna', 'Ogrodowa',
        'Lipowa', 'Brzozowa', 'Lakowa', 'Kwiatowa', 'Sosnowa', 'Koscielna',
        'Akacjowa', 'Parkowa', 'Zielona', 'Kolejowa', 'Sportowa', 'Debowa',
        'Kosciuszki', 'Maja', 'Mickiewicza', 'Cicha', 'Spokojna', 'Klonowa',
        'Spacerowa', 'Swierkowa', 'Kasztanowa', 'Nowa', 'Piaskowa',
        'Sienkiewicza', 'Rózana', 'Topolowa', 'Wisniowa', 'Dworcowa',
        'Wiejska', 'Graniczna', 'Slowackiego', 'Dluga', 'Wrzosowa',
        'Konopnickiej', 'Boczna', 'Waska', 'Wierzbowa', 'Jasminowa',
        'Wspólna', 'Modrzewiowa', 'Kopernika', 'Jana Pawla II',
        'Poprzeczna', 'Wesola', 'Pogodna', 'Zeromskiego', 'Rynek', 'Bukowa',
        'Wojska Polskiego', 'Sadowa', 'Górna', 'Jodlowa', 'Wolnosci',
        'Glówna', 'Mlynska', 'Strazacka', 'Prusa', 'Jesionowa', 'Przemyslowa',
        'Osiedlowa', 'Wiosenna', 'Sikorskiego', 'Chopina', 'Poludniowa',
        'Malinowa', 'Stawowa', 'Reymonta', 'Pilsudskiego', 'Zacisze',
        'Cmentarna', 'Okrezna', 'Kochanowskiego', 'Armii Krajowej', 'Mila',
        'Jasna', 'Wodna', 'Zamkowa', 'Witosa', 'Reja', 'Warszawska',
        'Miodowa', 'Partyzantów', 'Krzywa', 'Kilinskiego', 'Dolna',
        'Podgórna', 'Kreta', 'Jarzebinowa', 'Moniuszki', 'Targowa', 'Prosta',
        'Orzeszkowej', 'Spóldzielcza', 'Jagodowa', 'Dzialkowa', 'Staszica',
        'Orzechowa', 'Rzemieslnicza', 'Rzeczna', 'Boleslawa Chrobrego',
        'Fabryczna', 'Teczowa', 'Chabrowa', 'Poziomkowa', 'Konwaliowa',
        'Wyszynskiego', 'Kalinowa', 'Pólnocna', 'Matejki', 'Grunwaldzka',
        'Cisowa', 'Nadrzeczna', 'Pocztowa', 'Zachodnia', 'Dabrowskiego',
        'Grabowa', 'Norwida', 'Zródlana', 'Asnyka', 'Gajowa', 'Paderewskiego',
        'Listopada', 'Wyspianskiego', 'Mostowa', 'Broniewskiego', 'Tuwima',
        'Wschodnia', 'Jaworowa', 'Poznanska', 'Makowa', 'Bema', 'Jeziorna',
        'Piekna', 'Czeresniowa', 'Mala', 'Krakowska', 'Radosna',
        'Leszczynowa', 'Traugutta', 'Jadwigi', 'Rolna', 'Wyzwolenia',
        'Piastowska', 'Grzybowa', 'Krasickiego', 'Podlesna', 'Zytnia',
        'Zlota', 'Bursztynowa', 'Zwirowa', 'Stycznia', 'Widokowa',
        'Kazimierza Wielkiego', 'Kamienna', 'Jalowcowa', 'Morelowa',
        'Mieszka I', 'Mysliwska', 'Laczna', 'Szpitalna', 'Wczasowa',
        'Zurawia', 'Fiolkowa', 'Glowackiego', 'Rolnicza', 'Tulipanowa',
        'Wladyslawa Jagielly', 'Dworska', 'Letnia', 'Liliowa', 'Owocowa',
        'Pulaskiego', 'Stefana Batorego', 'Harcerska', 'Kollataja',
        'Strzelecka', 'Kraszewskiego', 'Wladyslawa Lokietka',
        'Zwirki i Wigury', 'Wroclawska', 'Gdanska', 'Turystyczna',
        'Niepodleglosci', 'Poniatowskiego', 'Korczaka', 'Rybacka',
        'Narutowicza', 'Okrzei', 'Krucza', 'Jagiellonska', 'Swierczewskiego',
        'Kasprowicza', 'Szeroka', 'Jana III Sobieskiego', 'Mlynarska',
        'Olchowa', 'Powstanców Slaskich', 'Rumiankowa', 'Stroma',
        'Starowiejska', 'Mazowiecka',
        'Lawendowa', 'Robotnicza', 'Zbozowa', 'Mokra',
        'Powstanców Wielkopolskich', 'Towarowa', 'Dobra', 'Srodkowa',
        'Willowa', 'Zielna', 'Zdrojowa', 'Opolska', 'Agrestowa', 'Ksiezycowa',
        'Zwyciestwa', 'Fredry', 'Letniskowa', 'Andersa', 'Baczynskiego',
        'Batalionów Chlopskich', 'Dabrowskiej', 'Orla', 'Sklodowskiej-Curie',
        'Blekitna', 'Rubinowa', 'Brzoskwiniowa', 'Urocza', 'Galczynskiego',
        'Krasinskiego', 'Pomorska', 'Szymanowskiego', 'Jezynowa',
        'Czarnieckiego', 'Nalkowskiej', 'Zaciszna', 'Porzeczkowa',
        'Krancowa', 'Jesienna', 'Klasztorna', 'Irysowa', 'Niecala',
        'Wybickiego', 'Nadbrzezna', 'Szarych Szeregów', 'Walowa',
        'Slowicza', 'Strumykowa', 'Drzymaly', 'Golebia', 'Torowa',
        'Cegielniana', 'Cyprysowa', 'Slowianska', 'Diamentowa', 'Warynskiego',
        'Czestochowska', 'Dojazdowa', 'Przechodnia', 'Hallera', 'Lubelska',
        'Plater', 'Popieluszki', 'Borówkowa', 'Chelmonskiego', 'Daszynskiego',
        'Plazowa', 'Tartaczna', 'Jabloniowa', 'Kossaka', 'Skargi', 'Ludowa',
        'Sokola', 'Azaliowa', 'Szmaragdowa', 'Lipca', 'Staffa', 'Tysiaclecia',
        'Brzechwy', 'Jastrzebia', 'Kusocinskiego', 'Storczykowa', 'Wilcza',
        'Górnicza', 'Szafirowa', 'Dlugosza', 'Handlowa', 'Krokusowa',
        'Skladowa', 'Widok', 'Perlowa', 'Skosna', 'Wypoczynkowa', 'Chmielna',
        'Jaskólcza', 'Nowowiejska', 'Piwna', 'Slaska', 'Zaulek', 'Glogowa',
        'Górska', 'Truskawkowa', 'Kaszubska', 'Kosynierów', 'Mazurska',
        'Srebrna', 'Bociania', 'Ptasia', 'Cedrowa', 'Rycerska',
        'Wieniawskiego', 'Zabia', 'Torunska', 'Podmiejska', 'Slonecznikowa',
        'Sowia', 'Stolarska', 'Powstanców', 'Sucharskiego',
        'Boleslawa Krzywoustego', 'Konarskiego',
        'Szczesliwa', 'Lazurowa', 'Miarki', 'Narcyzowa', 'Browarna',
        'Konstytucji 3 Maja', 'Majowa', 'Milosza', 'Malczewskiego', 'Orkana',
        'Skrajna', 'Bankowa', 'Bydgoska', 'Piekarska', 'Zeglarska', 'Jana',
        'Turkusowa', 'Tylna', 'Wysoka', 'Zakatek', 'Maczka', 'Morska',
        'Rataja', 'Szewska', 'Podwale', 'Palacowa', 'Magnoliowa', 'Ceglana',
        'Sawickiej', 'Sciegiennego', 'Wiklinowa', 'Zakole', 'Borowa',
        'Kolorowa', 'Lisia', 'Lotnicza', 'Sarnia', 'Wiazowa', 'Grottgera',
        'Kolonia', 'Królewska', 'Promienna', 'Daleka', 'Jana Sobieskiego',
        'Rejtana', 'Wiatraczna', 'Kaliska', 'Lanowa', 'Srednia', 'Wislana',
        'Wróblewskiego', 'Koralowa', 'Kruczkowskiego', 'Lelewela',
        'Makuszynskiego', 'Sybiraków', 'Kowalska', 'Morcinka', 'Odrzanska',
        'Okulickiego', 'Solidarnosci', 'Zapolskiej', 'Labedzia', 'Wojciecha',
        'Baltycka', 'Lwowska', 'Rajska', 'Korfantego', 'Pszenna', 'Ciasna',
        'Floriana', 'Hutnicza', 'Kielecka'
    )

    regions = (
        "Dolnośląskie", "Kujawsko - pomorskie", "Lubelskie", "Lubuskie",
        "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie",
        "Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie",
        "Warmińsko - mazurskie", "Wielkopolskie", "Zachodniopomorskie",
    )

    building_number_formats = ('##', '###', "##/##",)
    postcode_formats = ('##-###',)
    street_address_formats = (
        '{{street_prefix}} {{street_name}} {{building_number}}',
        '{{street_prefix_short}} {{street_name}} {{building_number}}',
    )
    address_formats = (
        "{{street_address}}\n{{postcode}} {{city}}",
    )

    @classmethod
    def street_prefix(cls):
        """
        Randomly returns a street prefix
        :example 'aleja'
        """
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def street_prefix_short(cls):
        """
        Randomly returns an abbreviation of the street prefix.
        :example 'al.'
        """
        return cls.random_element(cls.street_prefixes)[:2]+'.'

    @classmethod
    def street_name(cls):
        """
        Randomly returns a street name
        :example 'Wróblewskiego'
        """
        return cls.random_element(cls.streets)

    @classmethod
    def city(cls):
        """
        Randomly returns a street name
        :example 'Konin'
        """
        return cls.random_element(cls.cities)

    @classmethod
    def region(cls):
        """
        :example 'Wielkopolskie'
        """
        return cls.random_element(cls.regions)
