# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


def checksum_identity_card_number(characters):
    """
    Calculates and returns a control digit for given list of characters basing on Identity Card Number standards.
    """
    weights_for_check_digit = [7, 3, 1, 0, 7, 3, 1, 7, 3]
    check_digit = 0

    for i in range(3):
        check_digit += weights_for_check_digit[i] * (ord(characters[i]) - 55)

    for i in range(4, 9):
        check_digit += weights_for_check_digit[i] * characters[i]

    check_digit %= 10

    return check_digit


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name_female}}',
        '{{first_name}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name_male}}',
    )

    first_names_male = (
        'Jakub',
        'Jan',
        'Mateusz',
        'Bartek',
        'Kacper',
        'Michał',
        'Szymon',
        'Antoni',
        'Filip',
        'Piotr',
        'Maciej',
        'Aleksander',
        'Franciszek',
        'Mikołaj',
        'Adam',
        'Stanisław',
        'Wiktor',
        'Krzysztof',
        'Wojciech',
        'Igor',
        'Maksymilian',
        'Karol',
        'Dawid',
        'Tomasz',
        'Patryk',
        'Oskar',
        'Paweł',
        'Dominik',
        'Kamil',
        'Oliwier',
        'Ignacy',
        'Marcel',
        'Hubert',
        'Adrian',
        'Łukasz',
        'Sebastian',
        'Julian',
        'Tymon',
        'Krystian',
        'Marcin',
        'Damian',
        'Miłosz',
        'Leon',
        'Alan',
        'Tymoteusz',
        'Kajetan',
        'Grzegorz',
        'Daniel',
        'Rafał',
        'Eryk',
        'Konrad',
        'Ksawery',
        'Gabriel',
        'Nikodem',
        'Bruno',
        'Przemysław',
        'Borys',
        'Artur',
        'Olaf',
        'Jerzy',
        'Marek',
        'Tadeusz',
        'Andrzej',
        'Witold',
        'Iwo',
        'Juliusz',
        'Robert',
        'Błażej',
        'Cezary',
        'Jeremi',
        'Jacek',
        'Konstanty',
        'Ryszard',
        'Stefan',
        'Aleks',
        'Gustaw',
        'Radosław',
        'Emil',
        'Norbert',
        'Fabian',
        'Jędrzej',
        'Alex',
        'Kazimierz',
        'Arkadiusz',
        'Kornel',
        'Józef',
        'Natan',
        'Cyprian',
        'Mieszko',
        'Nataniel',
        'Maks',
        'Maurycy',
        'Olgierd',
        'Dariusz',
        'Leonard',
        'Mariusz',
        'Albert',
        'Fryderyk',
        'Ernest',
        'Tobiasz')

    first_names_female = (
        'Kamila',
        'Ewa',
        'Blanka',
        'Olga',
        'Kalina',
        'Klara',
        'Urszula',
        'Sandra',
        'Kaja',
        'Marianna',
        'Kornelia',
        'Justyna',
        'Monika',
        'Sara',
        'Adrianna',
        'Aniela',
        'Agnieszka',
        'Róża',
        'Marcelina',
        'Roksana',
        'Natasza',
        'Lidia',
        'Malwina',
        'Karina',
        'Ada',
        'Marika',
        'Anastazja',
        'Sonia',
        'Nela',
        'Dorota',
        'Apolonia',
        'Ida',
        'Eliza',
        'Angelika',
        'Anna Maria',
        'Liwia',
        'Ewelina',
        'Julita',
        'Rozalia',
        'Inga',
        'Krystyna',
        'Bianka',
        'Dagmara',
        'Melania',
        'Sylwia',
        'Nicole',
        'Anita',
        'Aurelia',
        'Elżbieta',
        'Janina',
        'Julianna',
        'Tola',
        'Gaja')

    unisex_last_names = (
        'Wandzel', 'Pajda', 'Dzienis', 'Borysewicz', 'Szlaga', 'Krzysiek', 'Iwańczyk', 'Cierpisz',
        'Borczyk', 'Szymula', 'Pietrasiak', 'Minkiewicz', 'Hojka', 'Goral', 'Staś', 'Smoter',
        'Bosek', 'Bitner', 'Kondej', 'Furgał', 'Durlik', 'Kusa', 'Pacewicz', 'Masiak', 'Kucz',
        'Cichowlas', 'Anders', 'Wawszczak', 'Słupek', 'Pych', 'Piszcz', 'Opoka', 'Lorenz',
        'Grochowina', 'Wicha', 'Pawliczek', 'Kus', 'Zysk', 'Sroga', 'Rychel', 'Patora', 'Maciocha',
        'Rozmiarek', 'Pesta', 'Działak', 'Godyń', 'Chmara', 'Jakubaszek', 'Bałazy', 'Rykała',
        'Wika', 'Kotala', 'Fikus', 'Sus', 'Kunc', 'Mateusiak', 'Kusyk', 'Romańczyk', 'Makieła',
        'Lejman', 'Kołaczek', 'Kurzak', 'Bondyra', 'Podkowa', 'Paśnik', 'Oleszko', 'Marcol',
        'Szybiak', 'Ruszczak', 'Zbroja', 'Stosik', 'Gruchot', 'Boś', 'Wożniak', 'Gniewek', 'Buława',
        'Wiatrak', 'Talaśka', 'Patalas', 'Kwoka', 'Krzempek', 'Danilczuk', 'Ważny', 'Sidorczuk',
        'Legutko', 'Kobos', 'Tylek', 'Szkoda', 'Przerwa', 'Linek', 'Galik', 'Dulewicz', 'Drozda',
        'Nowek', 'Matulewicz', 'Karpeta', 'Jurczuk', 'Buśko', 'Słomian', 'Drywa', 'Rybus', 'Langa',
        'Kluczek', 'Orkisz', 'Ziemkiewicz', 'Siara', 'Para', 'Kwasek', 'Januszko', 'Hejduk',
        'Łuszczak', 'Sprawka', 'Kiełek', 'Jop', 'Faryna', 'Zimoń', 'Utrata', 'Mirga', 'Kozaczuk',
        'Wojtyna', 'Rzońca', 'Madejczyk', 'Glapiak', 'Dziadkowiec', 'Ochnio', 'Sieja', 'Malewicz',
        'Bachanek', 'Mirocha', 'Domżał', 'Tworzydło', 'Płaneta', 'Feret', 'Witas', 'Figat', 'Muc',
        'Kuciel', 'Kielan', 'Hałat', 'Tecław', 'Loba', 'Klucznik', 'Bielas', 'Rajczyk', 'Myszak',
        'Muniak', 'Michalczak', 'Kochanowicz', 'Szołtysik', 'Rychert', 'Pyda', 'Janowiak', 'Janiga',
        'Grądziel', 'Wdowczyk', 'Pytlarz', 'Kuzia', 'Dziewa', 'Bernatowicz', 'Ostapiuk', 'Rejniak',
        'Kotlarek', 'Gajownik', 'Brach', 'Tatarek', 'Szyc', 'Masny', 'Drop', 'Saternus',
        'Podsiadła', 'Patyna', 'Kargol', 'Truchan', 'Pietrusiak', 'Kolbusz', 'Kalota', 'Hołubowicz',
        'Andrzejuk', 'Zdziech', 'Szymonik', 'Sych', 'Strojna', 'Seta', 'Orman', 'Hermanowicz',
        'Denkiewicz', 'Bulanda', 'Szwaja', 'Jankowicz', 'Pochopień', 'Kobza', 'Karwot', 'Kałek',
        'Laszuk', 'Aleksiejuk', 'Witaszek', 'Wawryniuk', 'Jacak', 'Bugla', 'Wejman', 'Jaroch',
        'Janiszek', 'Gorzelańczyk', 'Zieja', 'Krochmal', 'Filas', 'Wawrzynowicz', 'Szałas',
        'Machoń', 'Labus', 'Irzyk', 'Gomuła', 'Wesoły', 'Solarek', 'Kośka', 'Myszk', 'Moryc',
        'Lizoń', 'Lesisz', 'Kiełbowicz', 'Serwa', 'Piórek', 'Majdak', 'Bruzda', 'Bakun', 'Subocz',
        'Stypuła', 'Gołek', 'Fik', 'Wołczyk', 'Waniek', 'Parzyszek', 'Oszust', 'Burza', 'Żbik',
        'Misztela', 'Kurant', 'Drygas', 'Łaciak', 'Franczuk', 'Rycerz', 'Żok', 'Zeman', 'Mejer',
        'Kanarek', 'Jędruch', 'Saj', 'Nieroda', 'Juśkiewicz', 'Surdyk', 'Paliga', 'Makaruk',
        'Hamera', 'Łukowicz', 'Barcz', 'Witos', 'Strzelczak', 'Siedlaczek', 'Pakosz', 'Burchardt',
        'Nurek', 'Morys', 'Korbel', 'Kokosza', 'Kijanka', 'Bobak', 'Samson', 'Jarosiewicz',
        'Szelest', 'Stanisławek', 'Perka', 'Ciepłuch', 'Bryja', 'Świątkiewicz', 'Samul', 'Rohde',
        'Prucnal', 'Miszkiewicz', 'Kuropatwa', 'Gajdzik', 'Mućka', 'Misiaszek', 'Fornalik',
        'Wiszowaty', 'Thiel', 'Osiadacz', 'Miśko', 'Mielcarz', 'Drózd', 'Oleksiuk', 'Matyka',
        'Łyczak', 'Cabała', 'Ośka', 'Bereś', 'Armatys', 'Szmajda', 'Młyńczak', 'Kupidura', 'Kijas',
        'Chomiuk', 'Gowin', 'Dybka', 'Bródka', 'Wziątek', 'Ślęczka', 'Koj', 'Drabczyk', 'Buczko',
        'Sawko', 'Kłysz', 'Karpiel', 'Jarczyk', 'Flaga', 'Fiedorczuk', 'Tomalak', 'Nałęcz',
        'Choroś', 'Brańka', 'Rajchel', 'Kiedrowicz', 'Gąbka', 'Fiołek', 'Drozdowicz', 'Stypa',
        'Kawala', 'Mazanek', 'Kwinta', 'Koczy', 'Hyży', 'Grzejszczak', 'Wywiał', 'Sacharczuk',
        'Jaroszuk', 'Golon', 'Chachuła', 'Malarczyk', 'Kawula', 'Bohdanowicz', 'Bartocha', 'Lewko',
        'Igras', 'Damps', 'Tlałka', 'Niechciał', 'Łyskawa', 'Goś', 'Więckiewicz', 'Leśko', 'Konsek',
        'Juszczuk', 'Szczudło', 'Poniedziałek', 'Palus', 'Bodziony', 'Śmieszek', 'Rej', 'Pietryga',
        'Mieszała', 'Malcher', 'Kopij', 'Kaczan', 'Janasik', 'Watras', 'Stojak', 'Strzyż',
        'Siemieniec', 'Kośnik', 'Kasperczak', 'Woszczyna', 'Wiech', 'Stefanik', 'Miara', 'Łodyga',
        'Walo', 'Oleksiewicz', 'Mainka', 'Baka', 'Trybuś', 'Samol', 'Jamroży', 'Gruszczyk',
        'Deluga', 'Trzos', 'Sinkiewicz', 'Lesik', 'Kroczak', 'Klamka', 'Grzelczyk', 'Dycha',
        'Ciesielczyk', 'Armata', 'Wawrzyczek', 'Prokopczyk', 'Hampel', 'Grzech', 'Rzucidło', 'Rawa',
        'Kręcisz', 'Karyś', 'Rodzeń', 'Karalus', 'Mikosz', 'Kazimierczuk', 'Hajda', 'Berg', 'Teper',
        'Słabosz', 'Dziechciarz', 'Dmoch', 'Śleziak', 'Pietrek', 'Martyka', 'Wołk', 'Smętek',
        'Kroll', 'Grab', 'Dziedzina', 'Noszczyk', 'Kazek', 'Jędrusiak', 'Cebo', 'Tokarek', 'Małota',
        'Hanc', 'Uliasz', 'Pysz', 'Piłka', 'Błaszyk', 'Wyrobek', 'Trybus', 'Szlęk', 'Pindor', 'Łuc',
        'Baszak', 'Majak', 'Łój', 'Szczypek', 'Łuczkiewicz', 'Łaszcz', 'Froń', 'Dybaś', 'Budner',
        'Ostasz', 'Siekierka', 'Pilipczuk', 'Kandzia', 'Gieroń', 'Drost', 'Chwała', 'Malesza',
        'Fiedler', 'Suszko', 'Kurnik', 'Bereda', 'Nalewajko', 'Duczmal', 'Sieradzan', 'Pietrasz',
        'Cecot', 'Tomaszkiewicz', 'Rabiej', 'Staniaszek', 'Mikusek', 'Kuryłowicz', 'Herda',
        'Brzykcy', 'Początek', 'Ochal', 'Koral', 'Kaźmierczyk', 'Kandziora', 'Sycz', 'Reich',
        'Lindner', 'Fulara', 'Przybycień', 'Hermann', 'Forysiak', 'Strzępek', 'Sondej', 'Pyć',
        'Piaścik', 'Grygo', 'Wita', 'Szynkiewicz', 'Piesik', 'Nasiadka', 'Murach', 'Kostro',
        'Hinca', 'Engler', 'Tułacz', 'Przewoźny', 'Pizoń', 'Łapacz', 'Hajduga', 'Bulczak', 'Bubel',
        'Smutek', 'Samoraj', 'Plaskota', 'Fraś', 'Becker', 'Baranowicz', 'Trznadel', 'Topa',
        'Stanisławczyk', 'Lato', 'Kołton', 'Uryga', 'Tomaszczyk', 'Szymanik', 'Stochmal',
        'Kiszczak', 'Dylong', 'Chruszcz', 'Byra', 'Friedrich', 'Cyganik', 'Pacocha', 'Jonczyk',
        'Szymańczyk', 'Radko', 'Meler', 'Kuran', 'Koman', 'Błądek', 'Banachowicz', 'Babiuch',
        'Kruszka', 'Fijoł', 'Zatoń', 'Włodarz', 'Trepka', 'Świerszcz', 'Strzała', 'Opioła', 'Kursa',
        'Dyś', 'Broś', 'Tyka', 'Syroka', 'Grys', 'Szczepaniuk', 'Marcińczyk', 'Leks', 'Kubina',
        'Janke', 'Dąbrowicz', 'Hulbój', 'Cieciura', 'Chochół', 'Szpila', 'Samiec', 'Rduch',
        'Nabiałek', 'Margol', 'Kopa', 'Engel', 'Czerepak', 'Rosłon', 'Pusz', 'Matla', 'Wołoch',
        'Pazik', 'Nazimek', 'Kuśka', 'Karczmarz', 'Gajzler', 'Sławik', 'Lalak', 'Grabias', 'Gągała',
        'Chwedoruk', 'Wasil', 'Pachołek', 'Wichłacz', 'Walentynowicz', 'Tylus', 'Kosz', 'Iwanow',
        'Garczarek', 'Dorociak', 'Boguta', 'Betka', 'Widuch', 'Wawrzynek', 'Szymajda', 'Stanaszek',
        'Klama', 'Goj', 'Dzierżak', 'Walasik', 'Skwira', 'Luks', 'Kujawiak', 'Dworczak', 'Tofil',
        'Rurarz', 'Pachla', 'Lenarcik', 'Kusztal', 'Chaber', 'Skała', 'Radzewicz', 'Kramer',
        'Kochel', 'Dukat', 'Naglik', 'Szurek', 'Litwiniuk', 'Halama', 'Grzela', 'Wojaczek',
        'Popielarczyk', 'Krysik', 'Dawidczyk', 'Barteczko', 'Balik', 'Warych', 'Miodek', 'Madera',
        'Leszczyk', 'Kolanek', 'Fijak', 'Furgała', 'Faruga', 'Poleszak', 'Kusek', 'Herok', 'Golda',
        'Rymarz', 'Pociask', 'Kowalak', 'Czupryna', 'Trzcionka', 'Sulik', 'Matulka', 'Herbut',
        'Stosio', 'Kurtyka', 'Ciuk', 'Szczerbiak', 'Snoch', 'Budniak', 'Boruc', 'Tylka', 'Kwak',
        'Garncarz', 'Szuta', 'Miśkowiec', 'Sykut', 'Jarosik', 'Golus', 'Chmielak', 'Abramczuk',
        'Skrobek', 'Patrzałek', 'Linkiewicz', 'Jereczek', 'Jarema', 'Flasza', 'Fiedoruk',
        'Budkiewicz', 'Świgoń', 'Przewoźnik', 'Parada', 'Heller', 'Gierak', 'Ferdyn', 'Sumera',
        'Bik', 'Kamela', 'Ciereszko', 'Świtaj', 'Pastuszko', 'Łobacz', 'Kuba', 'Krzywonos',
        'Granat', 'Szóstak', 'Płoskonka', 'Kumorek', 'Komuda', 'Klinkosz', 'Falba', 'Szczechowicz',
        'Rozum', 'Moroń', 'Matynia', 'Greszta', 'Łuczka', 'Dziewit', 'Mueller', 'Kapral',
        'Hrynkiewicz', 'Gonsior', 'Forma', 'Ciesiółka', 'Bors', 'Siwa', 'Niemczuk', 'Nazar',
        'Liśkiewicz', 'Jarczak', 'Felisiak', 'Fedorczyk', 'Wilusz', 'Pastor', 'Gierek', 'Romaniak',
        'Oleszczak', 'Juras', 'Zachwieja', 'Szmurło', 'Smektała', 'Przewoźna', 'Nikel', 'Chlebek',
        'Balas', 'Latuszek', 'Ambrozik', 'Janczura', 'Aleksandrzak', 'Wojtalik', 'Rok', 'Nagórka',
        'Latoszek', 'Kubowicz', 'Domian', 'Ciemięga', 'Soliwoda', 'Komsta', 'Filus', 'Wierzchoń',
        'Skotarczak', 'Cader', 'Trzmiel', 'Jagieło', 'Wawszczyk', 'Troć', 'Swatek', 'Bączkiewicz',
        'Ulewicz', 'Tutka', 'Pałac', 'Mydlarz', 'Molka', 'Janiuk', 'Guziak', 'Frycz', 'Drzał',
        'Zacharek', 'Wiencek', 'Szłapka', 'Kurach', 'Bareja', 'Pawlukiewicz', 'Moździerz', 'Mich',
        'Lisik', 'Kałwa', 'Dadej', 'Matela', 'Lenda', 'Wolff', 'Wojnicz', 'Sendor', 'Mrózek',
        'Łągiewka', 'Kulisz', 'Kolarz', 'Walus', 'Mikoda', 'Kral', 'Darul', 'Warczak', 'Kunysz',
        'Kidoń', 'Ciuła', 'Chomiak', 'Rzeźniczak', 'Przeniosło', 'Chomik', 'Zimoląg', 'Wojtyś',
        'Mędrala', 'Hennig', 'Handzel', 'Twardzik', 'Śmieja', 'Solarczyk', 'Mendak', 'Lemieszek',
        'Kiryluk', 'Wrześniak', 'Kwarciak', 'Gasik', 'Borysiewicz', 'Sierota', 'Mysiak',
        'Kraszkiewicz', 'Hyjek', 'Polaszek', 'Pazera', 'Kubisz', 'Kościukiewicz', 'Kopczyk',
        'Kliber', 'Kaczmar', 'Kaczka', 'Bicz', 'Augustynek', 'Straszak', 'Sajewicz', 'Glanc',
        'Bzymek', 'Zieniewicz', 'Pagacz', 'Gortat', 'Bubak', 'Warwas', 'Skoneczna', 'Nestorowicz',
        'Dziopa', 'Danisz', 'Bazydło', 'Garncarek', 'Albin', 'Szeszko', 'Naczk', 'Łukowiak',
        'Kopciuch', 'Jakoniuk', 'Węgrzynowicz', 'Walencik', 'Turlej', 'Leonowicz', 'Kierepka',
        'Hendzel', 'Fronczek', 'Zarzeczna', 'Zagrodnik', 'Wałęsa', 'Trzepizur', 'Tereszkiewicz',
        'Szczubełek', 'Magier', 'Działo', 'Drygała', 'Czesak', 'Majorek', 'Wlizło', 'Skutnik',
        'Radke', 'Piątkiewicz', 'Oślizło', 'Kansy', 'Szela', 'Mol', 'Kuświk', 'Karpik', 'Janczarek',
        'Hajdukiewicz', 'Mzyk', 'Kostera', 'Leszkiewicz', 'Hutnik', 'Glaza', 'Fydrych', 'Piegza',
        'Matusewicz', 'Matus', 'Kluczyk', 'Drobnik', 'Połom', 'Okraska', 'Neska', 'Kozłowicz',
        'Wołos', 'Wacławczyk', 'Ochnik', 'Maruszczak', 'Lesner', 'Kuncewicz', 'Kieszek', 'Betlej',
        'Wałdoch', 'Szarejko', 'Smalec', 'Łosiewicz', 'Lisak', 'Walkusz', 'Owsiak', 'Kowaluk',
        'Simon', 'Rup', 'Neubauer', 'Muskała', 'Kucharzyk', 'Gabryel', 'Zimniak', 'Warmuz', 'Opas',
        'Michniak', 'Cieloch', 'Wójcikiewicz', 'Świech', 'Powierża', 'Olko', 'Miękus', 'Kutnik',
        'Kustosz', 'Kochman', 'Trąbka', 'Szyja', 'Młynarz', 'Wojtak', 'Dzierwa', 'Zyguła', 'Taciak',
        'Koziatek', 'Koss', 'Walenciak', 'Twardosz', 'Pakos', 'Mamcarz', 'Burzawa', 'Lenik',
        'Franc', 'Sadza', 'Mądrzak', 'Mak', 'Bobel', 'Szajna', 'Proch', 'Kosela', 'Guźniczak',
        'Radziewicz', 'Olchawa', 'Morcinek', 'Bastek', 'Ragan', 'Podeszwa', 'Mitek', 'Janoszka',
        'Słaba', 'Rusnak', 'Płócienniczak', 'Hanke', 'Gosek', 'Wujek', 'Warchał', 'Starzak',
        'Prochownik', 'Molak', 'Duszkiewicz', 'Sztaba', 'Piwek', 'Nowotnik', 'Kiljan', 'Dubel',
        'Brodowicz', 'Tylec', 'Pik', 'Pastucha', 'Księżak', 'Gumieniak', 'Ufnal', 'Stawinoga',
        'Słoń', 'Kolarczyk', 'John', 'Fleszar', 'Lemke', 'Kurc', 'Kamieniarz', 'Jaskóła', 'Jaremko',
        'Gogacz', 'Dudała', 'Chlipała', 'Szłapa', 'Seidel', 'Kopyt', 'Karłowicz', 'Gębura',
        'Frączkiewicz', 'Frankowicz', 'Dybiec', 'Drobny', 'Brózda', 'Boruń', 'Pelka', 'Macias',
        'Ruszel', 'Pabis', 'Krefta', 'Ćwierz', 'Bieleń', 'Szyca', 'Pronobis', 'Dreszer', 'Bryzek',
        'Ambrożewicz', 'Słobodzian', 'Mrozowicz', 'Wojak', 'Szklarek', 'Paw', 'Kościelak',
        'Kalarus', 'Wylegała', 'Powązka', 'Młot', 'Krekora', 'Bilewicz', 'Pyszka', 'Niedźwiadek',
        'Lubera', 'Chodak', 'Breguła', 'Synak', 'Supeł', 'Suda', 'Roczniak', 'Matuszyk', 'Helak',
        'Gubernat', 'Wojtera', 'Wiszowata', 'Świętoń', 'Deryło', 'Szałaj', 'Rzeszutko', 'Matejczuk',
        'Żołądź', 'Suchta', 'Pokrzywa', 'Piguła', 'Litwińczuk', 'Kik', 'Gula', 'Geisler', 'Micał',
        'Maszota', 'Kurzyna', 'Feliksiak', 'Cybul', 'Wiaderek', 'Śnieg', 'Linka', 'Fidler',
        'Fabiszak', 'Cibor', 'Ryczko', 'Rudolf', 'Jędrzejek', 'Bekus', 'Bek', 'Wolan', 'Radzio',
        'Kuliberda', 'Kolanko', 'Szykuła', 'Skowyra', 'Porwoł', 'Kosiak', 'Kasica', 'Jakiel',
        'Piejko', 'Owczarczak', 'Michnik', 'Linke', 'Kutera', 'Bobryk', 'Szabla', 'Powała',
        'Marciniszyn', 'Gorgol', 'Czerwionka', 'Ledzion', 'Dykas', 'Zygmuntowicz', 'Listwan',
        'Bobrowicz', 'Żurawik', 'Migała', 'Merchel', 'Bogumił', 'Wojsa', 'Sadura', 'Łyjak', 'Giers',
        'Gałat', 'Parafiniuk', 'Kryszkiewicz', 'Wyrostek', 'Wałek', 'Rembisz', 'Paściak', 'Maksym',
        'Kusio', 'Kostek', 'Kalisiak', 'Bździuch', 'Szlufik', 'Pogorzelec', 'Pielech', 'Kafel',
        'Gmur', 'Glazer', 'Borysiuk', 'Białk', 'Adamaszek', 'Wiesiołek', 'Wakuła', 'Rogula',
        'Leszczuk', 'Kapciak', 'Gul', 'Buszka', 'Sklorz', 'Parda', 'Miszkiel', 'Latek', 'Kurzydło',
        'Kucharz', 'Giec', 'Wajdzik', 'Mazik', 'Klimko', 'Kleina', 'Dorawa', 'Perczak', 'Lang',
        'Grunt', 'Cywka', 'Batóg', 'Widłak', 'Miszta', 'Kość', 'Kosidło', 'Aleksander',
        'Marchlewicz', 'Korkosz', 'Beśka', 'Bak', 'Stoch', 'Makles', 'Hudzik', 'Hornik', 'Bujko',
        'Ziętal', 'Zawal', 'Sochaj', 'Podpora', 'Małyszek', 'Maćków', 'Latacz', 'Kozdra', 'Kosno',
        'Gogół', 'Fit', 'Bienia', 'Wendt', 'Szyda', 'Suchoń', 'Sobel', 'Lesiewicz', 'Koleśnik',
        'Kinder', 'Kasper', 'Jaszczyszyn', 'Weremczuk', 'Steinke', 'Sądej', 'Puła', 'Nowrot',
        'Nowotny', 'Majorczyk', 'Kunert', 'Jerzyk', 'Capała', 'Bartoś', 'Wojciech', 'Stelmasiak',
        'Portka', 'Pietrak', 'Łuksza', 'Kulma', 'Jeske', 'Góraj', 'Fyda', 'Siemion', 'Rusiniak',
        'Flisiak', 'Cherek', 'Bryndza', 'Zioła', 'Zapaśnik', 'Raszkiewicz', 'Pszczółka', 'Pałgan',
        'Kozar', 'Gumienny', 'Fedak', 'Erdmann', 'Matura', 'Kapera', 'Golan', 'Szczesiak',
        'Szambelan', 'Półchłopek', 'Łuszczyk', 'Szymocha', 'Pielka', 'Macioł', 'Brudny', 'Babij',
        'Zacharczuk', 'Pilarek', 'Owsianka', 'Harasimiuk', 'Durlak', 'Długajczyk', 'Wijata',
        'Szyndler', 'Morka', 'Mendyka', 'Kubiaczyk', 'Kij', 'Gaudyn', 'Bok', 'Posłuszny', 'Plich',
        'Pacyga', 'Miętus', 'Ficner', 'Świerkosz', 'Krzywoń', 'Kojder', 'Kiepura', 'Godzisz',
        'Ciuba', 'Bukowiec', 'Wlaźlak', 'Teterycz', 'Ścibisz', 'Sobkiewicz', 'Raczkiewicz',
        'Konrad', 'Kohut', 'Gonet', 'Frydel', 'Dyka', 'Siemek', 'Ośko', 'Gospodarek', 'Stryjek',
        'Labudda', 'Kosiec', 'Indyk', 'Franik', 'Fiołka', 'Strycharz', 'Ostapczuk', 'Laszczyk',
        'Lament', 'Korzekwa', 'Kędziorek', 'Dziuban', 'Biegała', 'Witoń', 'Szpara', 'Padło',
        'Otremba', 'Mierzwiak', 'Kordus', 'Bojczuk', 'Szmelter', 'Rudzik', 'Madzia', 'Grabara',
        'Górkiewicz', 'Bartel', 'Śliz', 'Sura', 'Skrzecz', 'Puto', 'Pułka', 'Piotrowiak', 'Mazan',
        'Kobryń', 'Klatka', 'Januchta', 'Grubba', 'Zaucha', 'Sularz', 'Siergiej', 'Pianka',
        'Jędruszczak', 'Groth', 'Sobisz', 'Siejak', 'Rećko', 'Lorens', 'Cegła', 'Wochnik', 'Kuryś',
        'Gregorowicz', 'Filek', 'Salawa', 'Piekarek', 'Pabisiak', 'Glonek', 'Butrym', 'Przewoźniak',
        'Macek', 'Konstanty', 'Kolber', 'Jędrasiak', 'Wężyk', 'Szaj', 'Malara', 'Kłoczko',
        'Karsznia', 'Golenia', 'Zajko', 'Wudarczyk', 'Stanuch', 'Niklewicz', 'Matejczyk', 'Kopyto',
        'Grygorowicz', 'Szajda', 'Stachelek', 'Słyk', 'Loska', 'Job', 'Dziadura', 'Dworniczak',
        'Skubis', 'Obst', 'Kazimierczyk', 'Cymer', 'Ciak', 'Chudoba', 'Achtelik', 'Tytko', 'Skupin',
        'Skierka', 'Panuś', 'Pabiś', 'Folta', 'Bogaczyk', 'Basa', 'Trzpil', 'Morek', 'Kloska',
        'Kapustka', 'Gzyl', 'Gołoś', 'Danel', 'Borkiewicz', 'Araszkiewicz', 'Miotke', 'Rezler',
        'Potyrała', 'Pacholak', 'Herba', 'Grzenia', 'Giezek', 'Gajowiak', 'Filak', 'Fechner',
        'Droździk', 'Cyman', 'Wieczerzak', 'Stróż', 'Staciwa', 'Ruchała', 'Rogal', 'Reszke',
        'Kurpisz', 'Gryga', 'Stempniak', 'Matraszek', 'Kózka', 'Elsner', 'Boba', 'Barłóg',
        'Kiliszek', 'Jessa', 'Ignatiuk', 'Gogola', 'Drobek', 'Lica', 'Larysz', 'Kalka', 'Dziczek',
        'Czupryn', 'Żołna', 'Pytko', 'Misiarz', 'Majnusz', 'Kaszkowiak', 'Jonak', 'Basista',
        'Potęga', 'Natanek', 'Matyszczak', 'Majerczyk', 'Łapaj', 'Korzonek', 'Jaśko', 'Futyma',
        'Duszczyk', 'Antończak', 'Wysota', 'Dela', 'Stawowczyk', 'Milczarczyk', 'Malisz',
        'Andrearczyk', 'Żynda', 'Swaczyna', 'Ryndak', 'Moskalik', 'Mitoraj', 'Łyś', 'Łepek',
        'Knieć', 'Janisz', 'Gorol', 'Ciężka', 'Żyrek', 'Zmarzły', 'Wojtaszczyk', 'Szyguła',
        'Szalast', 'Rząd', 'Nicewicz', 'Danieluk', 'Bulak', 'Wojtasiewicz', 'Pleskot', 'Materek',
        'Kurczak', 'Dytko', 'Świstek', 'Szafarz', 'Litwa', 'Kreczmer', 'Idec', 'Grabczak',
        'Goliszek', 'Flieger', 'Filiks', 'Dyszy', 'Błażejczak', 'Maksimowicz', 'Komisarczyk',
        'Jewuła', 'Hallmann', 'Gabara', 'Budzyń', 'Andruszko', 'Pałyga', 'Moj', 'Koterba', 'Gruza',
        'Gamoń', 'Pasierbek', 'Kuchciak', 'Kanik', 'Cis', 'Zegar', 'Sadlik', 'Paprotny', 'Nalazek',
        'Mikita', 'Kucab', 'Kranc', 'Godzik', 'Sip', 'Powałka', 'Penkala', 'Pachuta', 'Nagel',
        'Litwinowicz', 'Kukuczka', 'Knysak', 'Fojt', 'Brejnak', 'Tasarz', 'Zielke', 'Zaraś',
        'Zaranek', 'Waleczek', 'Rubaj', 'Bazylewicz', 'Banyś', 'Balawender', 'Zmuda', 'Wojcik',
        'Łabno', 'Gęsiarz', 'Frost', 'Bany', 'Żero', 'Rudowicz', 'Nyk', 'Milcarz', 'Lipowicz',
        'Kycia', 'Kościołek', 'Korda', 'Berus', 'Wiese', 'Olkowicz', 'Dzieża', 'Doroszkiewicz',
        'Cetera', 'Pazdan', 'Pacia', 'Kempka', 'Dydak', 'Ścibior', 'Szyjka', 'Pyziak', 'Pleśniak',
        'Maszczyk', 'Ludwiniak', 'Zadora', 'Strug', 'Mokwa', 'Łasak', 'Kulczak', 'Kruszona',
        'Zacharewicz', 'Miękina', 'Klaus', 'Glegoła', 'Wyderka', 'Maleszka', 'Malcherek', 'Lew',
        'Kulis', 'Bodzak', 'Błaziak', 'Bartłomiejczyk', 'Toś', 'Kubasiak', 'Dorobisz', 'Cukier',
        'Ciećko', 'Zapadka', 'Kłosowicz', 'Kasak', 'Czubaszek', 'Baumgart', 'Szemraj', 'Nogieć',
        'Burczak', 'Pietraś', 'Ostafin', 'Noculak', 'Kukieła', 'Fogel', 'Duczek', 'Cylwik',
        'Biernacik', 'Wydrych', 'Szajek', 'Siwczak', 'Majewicz', 'Łosiak', 'Karkut', 'Durys',
        'Chwalisz', 'Bembenek', 'Bartkowicz', 'Piskor', 'Mikus', 'Księżyk', 'Goss', 'Drewniok',
        'Bąkiewicz', 'Wódka', 'Wota', 'Prażmo', 'Kiwior', 'Bogdał', 'Rubacha', 'Hanus', 'Wasiewicz',
        'Trochimiuk', 'Szwiec', 'Suszka', 'Palak', 'Ziemann', 'Maćczak', 'Kruzel', 'Kołaczyk',
        'Kapka', 'Jodko', 'Jeszke', 'Gros', 'Gendek', 'Dubik', 'Ważna', 'Pierchała', 'Nieszporek',
        'Kandora', 'Janasz', 'Gryszkiewicz', 'Drobik', 'Ciołczyk', 'Wołkowicz', 'Tylman', 'Pituła',
        'Pioch', 'Pilich', 'Marach', 'Malon', 'Lepa', 'Kaliciak', 'Joszko', 'Hejna', 'Gryta',
        'Frelich', 'Bełz', 'Bakalarczyk', 'Nóżka', 'Holewa', 'Fierek', 'Żuchowicz', 'Wojtunik',
        'Trzop', 'Masłoń', 'Linda', 'Kurp', 'Gryka', 'Draus', 'Rezmer', 'Mizak', 'Makurat',
        'Kościk', 'Helman', 'Gendera', 'Dydo', 'Bondaruk', 'Bodek', 'Wujec', 'Sady', 'Przekwas',
        'Postawa', 'Polasik', 'Plebanek', 'Lejk', 'Kacperek', 'Gołofit', 'Tomys', 'Świadek',
        'Mizgała', 'Kubrak', 'Ernst', 'Wielgos', 'Martynowicz', 'Drela', 'Ziarnik', 'Stasica',
        'Semik', 'Mytych', 'Melka', 'Marat', 'Dąbrówka', 'Wyroba', 'Siudek', 'Senator',
        'Ryszkiewicz', 'Podsiedlik', 'Małys', 'Lepianka', 'Giersz', 'Zugaj', 'Procek', 'Makosz',
        'Kunda', 'Ziółko', 'Trzyna', 'Stroka', 'Rzeszut', 'Pyza', 'Krężołek', 'Kazior', 'Fidos',
        'Sołek', 'Gordon', 'Dubis', 'Ciochoń', 'Bieszke', 'Żołnierczyk', 'Sobstyl', 'Skalik',
        'Namysło', 'Litewka', 'Krzysztofek', 'Grycz', 'Feluś', 'Downar', 'Szram', 'Oleksik',
        'Milej', 'Kudela', 'Klaja', 'Giedrojć', 'Getka', 'Durma', 'Dudko', 'Dębosz', 'Browarczyk',
        'Sąsiadek', 'Picheta', 'Peciak', 'Niećko', 'Midura', 'Maciejko', 'Gregorek', 'Wąsiewicz',
        'Twardy', 'Szachniewicz', 'Sypek', 'Sojda', 'Saran', 'Mosiołek', 'Guściora', 'Golak',
        'Ellwart', 'Drewicz', 'Barszczak', 'Wójt', 'Strawa', 'Sereda', 'Rejmer', 'Prostak', 'Kołak',
        'Klekot', 'Gerlach', 'Ciepła', 'Barankiewicz', 'Welc', 'Skotarek', 'Sadłocha',
        'Roszkiewicz', 'Połetek', 'Ofiara', 'Kiełbus', 'Kałwak', 'Jas', 'Jarkiewicz', 'Jambor',
        'Hartman', 'Graś', 'Raźniak', 'Janc', 'Doroz', 'Baster', 'Banak', 'Spólnik', 'Poreda',
        'Orwat', 'Matyjas', 'Laskus', 'Bajak', 'Witko', 'Ślimak', 'Sapeta', 'Sadownik', 'Roszko',
        'Nazarewicz', 'Mrotek', 'Gnyp', 'Dziarmaga', 'Zaniewicz', 'Walusiak', 'Toborek', 'Szulim',
        'Pawliczak', 'Nikołajuk', 'Myszor', 'Mila', 'Liedtke', 'Korpal', 'Jaźwiec', 'Groborz',
        'Świerkot', 'Sabała', 'Kluj', 'Żach', 'Wawrzyńczyk', 'Szumiło', 'Sulich', 'Stępak',
        'Rutowicz', 'Krzyszczak', 'Kiełbik', 'Gogol', 'Buszkiewicz', 'Basaj', 'Bartuś', 'Samulak',
        'Ryfa', 'Potoczna', 'Panicz', 'Leśny', 'Lada', 'Kuska', 'Gleba', 'Folga', 'Barczuk',
        'Ślebioda', 'Olma', 'Kuśnierek', 'Krzan', 'Hubert', 'Grzebyk', 'Fras', 'Durlej', 'Pielach',
        'Klin', 'Jędrak', 'Frelek', 'Brząkała', 'Borysiak', 'Zagozda', 'Śliż', 'Szkopek', 'Raźny',
        'Olearczyk', 'Mirończuk', 'Chyb', 'Żybura', 'Żelazo', 'Kunka', 'Kosałka', 'Gosz', 'Dulas',
        'Żelazek', 'Terka', 'Sośniak', 'Pikor', 'Pezda', 'Hadam', 'Groń', 'Fal', 'Chalimoniuk',
        'Karnas', 'Uziębło', 'Grochola', 'Gawliczek', 'Freitag', 'Ćmiel', 'Wacław', 'Symonowicz',
        'Strzoda', 'Sterna', 'Spadło', 'Rajtar', 'Krzykała', 'Holc', 'Gronostaj', 'Barej',
        'Wasilewicz', 'Podgórny', 'Łapot', 'Lepak', 'Hojda', 'Dziuda', 'Klupś', 'Brzeźniak',
        'Bojarczuk', 'Tryka', 'Nalewajek', 'Kudłacik', 'Kubasiewicz', 'Bazyluk', 'Bartoszak',
        'Zbylut', 'Tołoczko', 'Szaruga', 'Obuchowicz', 'Gryska', 'Bociek', 'Wowra', 'Szramka',
        'Spychaj', 'Roj', 'Musiolik', 'Franas', 'Dłubak', 'Cholewka', 'Bobko', 'Białous', 'Osial',
        'Nieborak', 'Minta', 'Kozica', 'Kowara', 'Gwara', 'Tekieli', 'Pancerz', 'Mleczak', 'Celuch',
        'Zapiór', 'Graboś', 'Fidura', 'Cyrek', 'Bracha', 'Gradek', 'Noras', 'Mulawa', 'Moniuszko',
        'Kapcia', 'Gumienna', 'Graj', 'Gilewicz', 'Żółtek', 'Wojtalewicz', 'Szumny', 'Opyrchał',
        'Macha', 'Łuczyk', 'Hus', 'Czak', 'Borzym', 'Wojtczuk', 'Winnik', 'Kuk', 'Kubanek',
        'Dziełak', 'Dudziec', 'Cimoch', 'Ciapa', 'Buchalik', 'Zbróg', 'Węgrzyniak', 'Wawrzkiewicz',
        'Teodorowicz', 'Szkoła', 'Sutor', 'Kapuścik', 'Hajdas', 'Fołta', 'Burkiewicz', 'Aleksa',
        'Wajer', 'Siembab', 'Kozon', 'Wojewódka', 'Wenda', 'Majos', 'Huczek', 'Domoń', 'Zubel',
        'Szymaniuk', 'Salomon', 'Mikiciuk', 'Grodek', 'Wielądek', 'Szymańczak', 'Sommer', 'Saczuk',
        'Pastuszek', 'Mroczko', 'Łokaj', 'Deptuch', 'Wawak', 'Szczepaniec', 'Romejko', 'Rogacz',
        'Poczta', 'Nowotka', 'Jaszcz', 'Jany', 'Hewelt', 'Stachów', 'Smykla', 'Sędek', 'Niemira',
        'Młodzik', 'Łyczek', 'Kleban', 'Fura', 'Fudalej', 'Cyroń', 'Zagożdżon', 'Kenig',
        'Górnisiewicz', 'Wołoszyk', 'Szatanik', 'Sajda', 'Pyrkosz', 'Misiejuk', 'Mikołajewicz',
        'Kołsut', 'Glenc', 'Eckert', 'Dziadowicz', 'Waszczyk', 'Szyba', 'Steckiewicz', 'Kloch',
        'Kabala', 'Zamora', 'Tabiś', 'Sobków', 'Pupek', 'Neugebauer', 'Kołtuniak', 'Galek', 'Stój',
        'Rajda', 'Pruchnik', 'Kuza', 'Karaśkiewicz', 'Judek', 'Jędryczka', 'Grzegorzak', 'Drobniak',
        'Chowaniak', 'Wąsek', 'Smagacz', 'Pędzik', 'Klinger', 'Klęczar', 'Wochna', 'Rejek',
        'Krakowczyk', 'Kobak', 'Kawiak', 'Grosz', 'Czubaj', 'Chorążewicz', 'Zadka', 'Wietecha',
        'Sass', 'Męcik', 'Gustaw', 'Furga', 'Frącz', 'Dawiec', 'Wypchło', 'Tarasek', 'Szmaj',
        'Ornat', 'Huszcza', 'Dudczak', 'Ułanowicz', 'Rubin', 'Pich', 'Makoś', 'Krępa', 'Korek',
        'Jonik', 'Andrejczuk', 'Wiertel', 'Soroko', 'Składanek', 'Mortka', 'Małocha', 'Majsterek',
        'Lemanowicz', 'Lelito', 'Krystkowiak', 'Krasa', 'Kierat', 'Jędraszczyk', 'Handke',
        'Dymarczyk', 'Doruch', 'Beker', 'Peszko', 'Osik', 'Łyp', 'Karmelita', 'Herdzik', 'Brzęk',
        'Białczyk', 'Uss', 'Pitura', 'Łusiak', 'Knapek', 'Gumuła', 'Darłak', 'Znojek', 'Wilkos',
        'Rut', 'Przekop', 'Kręcichwost', 'Korab', 'Józwik', 'Jagiełka', 'Chylak', 'Zbiciak',
        'Wasążnik', 'Tłuczek', 'Syldatk', 'Parkitny', 'Juroszek', 'Wisz', 'Wiciak', 'Palonek',
        'Kusik', 'Kocurek', 'Kacperczyk', 'Bluszcz', 'Wydmuch', 'Wereda', 'Trybała', 'Sito',
        'Pietraszkiewicz', 'Nojek', 'Madziar', 'Kazana', 'Szulczyk', 'Rosołek', 'Roskosz', 'Proć',
        'Mazek', 'Koniecko', 'Horbacz', 'Zastawny', 'Orszulik', 'Mesjasz', 'Margas', 'Koźlak',
        'Dzidek', 'Damek', 'Zinkiewicz', 'Sznura', 'Sapała', 'Piaseczna', 'Osada', 'Koziarz',
        'Korta', 'Kłosiewicz', 'Klyszcz', 'Janoszek', 'Deszcz', 'Okła', 'Matacz', 'Hankiewicz',
        'Front', 'Daraż', 'Czura', 'Bylina', 'Bugiel', 'Anioła', 'Amanowicz', 'Zach', 'Starościak',
        'Kliszcz', 'Hadała', 'Czopik', 'Bytner', 'Wośko', 'Wawrzyn', 'Świt', 'Sanetra', 'Pyszczek',
        'Potaczek', 'Osman', 'Materka', 'Madura', 'Kniaź', 'Gryciuk', 'Fidor', 'Dunal', 'Dobroń',
        'Chlebda', 'Słupik', 'Osica', 'Oleksak', 'Maraszek', 'Kręgiel', 'Kopytko', 'Gomoła',
        'Droździel', 'Szott', 'Szkup', 'Posmyk', 'Młotek', 'Klejna', 'Jałowiec', 'Heinrich',
        'Haraburda', 'Grupa', 'Dziadkiewicz', 'Zaczyk', 'Rapa', 'Łodej', 'Lempart', 'Lamch',
        'Głuszko', 'Cudzich', 'Brojek', 'Ziemak', 'Tusk', 'Kieloch', 'Dziduch', 'Dudkowiak',
        'Czerner', 'Sommerfeld', 'Migoń', 'Macheta', 'Dusik', 'Ćwirko', 'Bilik', 'Sydor', 'Swiątek',
        'Sporek', 'Olesiejuk', 'Kutek', 'Jaszczur', 'Jarmuż', 'Gronkiewicz', 'Witan', 'Staniczek',
        'Rząca', 'Roter', 'Pracz', 'Hnat', 'Cydzik', 'Szatko', 'Styrna', 'Podleśna', 'Oleksa',
        'Nieścior', 'Matyjaszek', 'Łasica', 'Kwapień', 'Koronkiewicz', 'Hołota', 'Elert',
        'Czochara', 'Toczko', 'Święs', 'Słysz', 'Salach', 'Leśna', 'Głownia', 'Galica', 'Cieniuch',
        'Szulist', 'Pedrycz', 'Królczyk', 'Zyzik', 'Zaborek', 'Skałka', 'Sankiewicz', 'Pleban',
        'Martin', 'Lewek', 'Jędrys', 'Guzdek', 'Dumała', 'Wszoła', 'Rębiś', 'Pośnik', 'Porzucek',
        'Hawro', 'Dziób', 'Zwara', 'Wiraszka', 'Romankiewicz', 'Roch', 'Paleń', 'Ogonek', 'Makar',
        'Majdan', 'Kozdrój', 'Kozdroń', 'Jachna', 'Duniec', 'Dułak', 'Wojtanowicz', 'Waloch',
        'Ubysz', 'Stożek', 'Małycha', 'Kmak', 'Hass', 'Frydrychowicz', 'Domka', 'Żugaj', 'Zubowicz',
        'Wyrwał', 'Mordal', 'Kordys', 'Gozdur', 'Gabrych', 'Zbrożek', 'Zbroszczyk', 'Wojtoń',
        'Tórz', 'Torbus', 'Letkiewicz', 'Lampart', 'Superson', 'Sopata', 'Sobiło', 'Sapa', 'Salwin',
        'Pera', 'Organiściak', 'Matwiejczyk', 'Matejuk', 'Mały', 'Krüger', 'Dyszkiewicz', 'Basak',
        'Ankiewicz', 'Adamiuk', 'Sykała', 'Skonieczka', 'Pawełko', 'Nojman', 'Iskierka', 'Zięcik',
        'Trojanek', 'Sadlak', 'Nieradko', 'Behrendt', 'Wojewodzic', 'Polewka', 'Zasępa', 'Szczerek',
        'Szałata', 'Sot', 'Mleczek', 'Kukawka', 'Kaczmarkiewicz', 'Dorobek', 'Burchard', 'Blaut',
        'Witka', 'Sasak', 'Pasiak', 'Panasiewicz', 'Motak', 'Lizurej', 'Kuboń', 'Jędraszek',
        'Dylik', 'Cal', 'Buszko', 'Burnat', 'Wyskiel', 'Winek', 'Wiertelak', 'Wiak', 'Roś',
        'Orzeszek', 'Ochota', 'Mijas', 'Maculewicz', 'Kaja', 'Ciesielka', 'Bejm', 'Szmuc', 'Sygut',
        'Siarkiewicz', 'Ryznar', 'Patoka', 'Miszkurka', 'Kudełka', 'Krzyśko', 'Galon', 'Buczma',
        'Ziegler', 'Uroda', 'Turczyk', 'Tolak', 'Sypuła', 'Sadowy', 'Rasała', 'Kazubek', 'Han',
        'Wasiuk', 'Stempin', 'Stawczyk', 'Prokopiak', 'Pospiech', 'Polakiewicz', 'Olas',
        'Maruszczyk', 'Kapinos', 'Kabza', 'Szwałek', 'Smagała', 'Musiała', 'Miksza', 'Lampa',
        'Kulon', 'Koczara', 'Drynda', 'Szczypiór', 'Pawełkiewicz', 'Myk', 'Kuczak', 'Kołata',
        'Żywica', 'Tondera', 'Szmalec', 'Szczap', 'Sypień', 'Sołtysek', 'Mosur', 'Kościesza',
        'Kosowicz', 'Kolendo', 'Huber', 'Giel', 'Gałęza', 'Dyja', 'Cacko', 'Apanowicz', 'Wandas',
        'Siebert', 'Moneta', 'Ziajka', 'Sieg', 'Paluszak', 'Lichoń', 'Kastelik', 'Gwizdek', 'Drewa',
        'Andrys', 'Zbrzeźniak', 'Wlazły', 'Wittbrodt', 'Niksa', 'Habdas', 'Fryś', 'Doktór', 'Detka',
        'Cieplucha', 'Ciarka', 'Witkowicz', 'Wardzała', 'Stąpór', 'Pniak', 'Pierzak', 'Kryk',
        'Kożuszek', 'Kohnke', 'Kapałka', 'Domino', 'Czuj', 'Boksa', 'Wocial', 'Stuglik', 'Steciuk',
        'Smela', 'Plona', 'Piwowarek', 'Pernak', 'Minkina', 'Klos', 'Halik', 'Dzika', 'Dargacz',
        'Damian', 'Adrian', 'Węgrzynek', 'Tomal', 'Świerad', 'Szkatuła', 'Sajnóg', 'Kudlak',
        'Golczyk', 'Fronczyk', 'Czapiga', 'Błażejak', 'Bejma', 'Bartela', 'Tadeusiak', 'Nędzi',
        'Kurcz', 'Jasionek', 'Heleniak', 'Ziarek', 'Zera', 'Sarniak', 'Różak', 'Ligas', 'Kuzior',
        'Kuder', 'Korzeniak', 'Fac', 'Domowicz', 'Dębniak', 'Cieciora', 'Chaberek', 'Bogusiewicz',
        'Block', 'Wardziak', 'Prawdzik', 'Niebudek', 'Jeszka', 'Szpyrka', 'Szkaradek', 'Starek',
        'Pasich', 'Lademann', 'Jantos', 'Grzelec', 'Zapora', 'Wnuczek', 'Wąsala', 'Pompa', 'Małas',
        'Janka', 'Gałaj', 'Dybał', 'Chromy', 'Szpyt', 'Senger', 'Prygiel', 'Pawela', 'Łakota',
        'Jama', 'Graban', 'Fogt', 'Cebulak', 'Boryczko', 'Bojdo', 'Biesek', 'Arendarczyk',
        'Schubert', 'Namysł', 'Milewczyk', 'Hetmańczyk', 'Dyczko', 'Dankiewicz', 'Czerniec',
        'Staśko', 'Rochowiak', 'Misiuk', 'Markiel', 'Ksel', 'Krzyżostaniak', 'Elwart', 'Delekta',
        'Zębik', 'Siatka', 'Niewiara', 'Miozga', 'Mętel', 'Korgul', 'Karwan', 'Franków', 'Domek',
        'Ciepluch', 'Chojna', 'Surmiak', 'Strama', 'Stein', 'Siewiera', 'Robaszkiewicz', 'Piksa',
        'Kociemba', 'Klyta', 'Gromala', 'Gill', 'Broszkiewicz', 'Zontek', 'Stiller', 'Rosada',
        'Mieloch', 'Kornak', 'Goworek', 'Gadzała', 'Fitas', 'Uzar', 'Siedlarz', 'Rorat', 'Oskroba',
        'Mitera', 'Grygorcewicz', 'Gmurczyk', 'Dylak', 'Zybura', 'Wojtaszak', 'Wisła', 'Wasyluk',
        'Szałkiewicz', 'Krzysztoszek', 'Kościuszko', 'Kasiak', 'Wyrwich', 'Wołoszczuk', 'Śledzik',
        'Smorąg', 'Satora', 'Pochroń', 'Melaniuk', 'Jajko', 'Czajor', 'Bajko', 'Wojsław', 'Szumiec',
        'Nehring', 'Naumiuk', 'Luberda', 'Kęsek', 'Jaśkowiec', 'Foit', 'Fita', 'Fedyk', 'Działa',
        'Cygal', 'Zdancewicz', 'Walocha', 'Toma', 'Soczewka', 'Monkiewicz', 'Majtyka', 'Hynek',
        'Dynia', 'Czuryło', 'Bernatek', 'Apostel', 'Zawiasa', 'Piersa', 'Megger', 'Kukier', 'Jarka',
        'Glazik', 'Dyjas', 'Buś', 'Bona', 'Bandyk', 'Zięciak', 'Krajniak', 'Koperek', 'Kazberuk',
        'Dziewior', 'Chachaj', 'Sołoducha', 'Słomiany', 'Skolik', 'Pęksa', 'Mularz', 'Kosman',
        'Kolonko', 'Januszewicz', 'Gramza', 'Foremniak', 'Fijałek', 'Cierpka', 'Polnik', 'Drwięga',
        'Semenowicz', 'Pieszak', 'Narożna', 'Ładniak', 'Kontny', 'Klemens', 'Jancewicz', 'Fąferek',
        'Bisaga', 'Złotnik', 'Wosiek', 'Supernak', 'Kala', 'Giża', 'Bielat', 'Żyto', 'Rompa',
        'Kurpanik', 'Kołpak', 'Gołas', 'Długozima', 'Bacia', 'Wincenciak', 'Styn', 'Moczko',
        'Langier', 'Szrama', 'Szok', 'Suchenek', 'Pieczarka', 'Parus', 'Machul', 'Latko',
        'Krzyśków', 'Galos', 'Ekert', 'Dawidek', 'Czerkies', 'Bujas', 'Andryszczyk', 'Zuziak',
        'Węgrzyk', 'Stąpor', 'Pinda', 'Muzyk', 'Maligłówka', 'Łukasiuk', 'Kinal', 'Dobosiewicz',
        'Waraksa', 'Szywała', 'Nastały', 'Mordak', 'Ligenza', 'Leszczak', 'Krauz', 'Kopała',
        'Byzdra', 'Bartman', 'Wojtach', 'Wałaszek', 'Szara', 'Hapka', 'Wielgat', 'Węgier', 'Pokusa',
        'Małż', 'Kononowicz', 'Hawrylak', 'Grund', 'Druszcz', 'Dacko', 'Sprycha', 'Pryszcz',
        'Łachut', 'Dobrosz', 'Brygoła', 'Ryguła', 'Posłuszna', 'Mydlak', 'Bernard', 'Woroch',
        'Uliczka', 'Tomaszuk', 'Pastuła', 'Pachnik', 'Kudra', 'Kretek', 'Keler', 'Heczko', 'Beck',
        'Tekiela', 'Plizga', 'Piekacz', 'Ochab', 'Maziarczyk', 'Krzosek', 'Gabryelczyk', 'Stępka',
        'Rajch', 'Owsiany', 'Kossak', 'Kocaj', 'Gierach', 'Buza', 'Berendt', 'Tabak', 'Przewłoka',
        'Nytko', 'Kuban', 'Gebauer', 'Gajcy', 'Franaszek', 'Chwedczuk', 'Bochnak', 'Stachewicz',
        'Sosnówka', 'Słowiak', 'Mądro', 'Malcharek', 'Łukasz', 'Kornek', 'Hanusiak',
        'Furmankiewicz', 'Dzikiewicz', 'Duży', 'Delikat', 'Chojak', 'Zyga', 'Pyrz', 'Pietrusiewicz',
        'Olszyna', 'Olszowa', 'Ograbek', 'Molga', 'Maron', 'Jasica', 'Frymus', 'Buszta', 'Woszczak',
        'Woronko', 'Trawka', 'Rychcik', 'Przystupa', 'Oczko', 'Migda', 'Klebba', 'Jaje', 'Grabas',
        'Bugno', 'Bortkiewicz', 'Wesoła', 'Sudak', 'Puc', 'Przeklasa', 'Kocoł', 'Goik',
        'Błażejewicz', 'Tuzimek', 'Petrus', 'Pawlaczek', 'Pacholczak', 'Maciejewicz', 'Jakóbik',
        'Frania', 'Duszczak', 'Domurad', 'Bednarowicz', 'Thomas', 'Rakus', 'Przybyś', 'Pasiut',
        'Małyszka', 'Kurz', 'Kuczaj', 'Doktor', 'Tadla', 'Praczyk', 'Milka', 'Leszcz', 'Kryza',
        'Kryszczuk', 'Juraszczyk', 'Durczok', 'Boduch', 'Szeja', 'Pryk', 'Pitala', 'Molek',
        'Duchnik', 'Brachaczek', 'Wieja', 'Waloszek', 'Nawrotek', 'Nawój', 'Mironiuk', 'Matyjasek',
        'Łachacz', 'Kubów', 'Kidawa', 'Jaremek', 'Hasiak', 'Gierat', 'Gawłowicz', 'Wichary',
        'Sornat', 'Solich', 'Kurczab', 'Jasnoch', 'Famuła', 'Budrewicz', 'Pawliszyn', 'Kułach',
        'Kuffel', 'Konieczek', 'Koćwin', 'Imiołczyk', 'Dyda', 'Zander', 'Stochel', 'Osojca',
        'Mysior', 'Kuciak', 'Kłósek', 'Buchholz', 'Zegadło', 'Wiewiórka', 'Stochaj', 'Smolka',
        'Piotrak', 'Misior', 'Leoniak', 'Karwala', 'Jasina', 'Cięciwa', 'Ciastek', 'Chadaj',
        'Białach', 'Tabisz', 'Such', 'Sromek', 'Rysz', 'Puch', 'Plak', 'Palej', 'Och', 'Niedbał',
        'Mytnik', 'Morgała', 'Lukas', 'Lisoń', 'Królikiewicz', 'Kamieniak', 'Jachimczyk',
        'Grzywnowicz', 'Frukacz', 'Feliniak', 'Dzienisz', 'Drążyk', 'Żelasko', 'Waloszczyk',
        'Strójwąs', 'Smoczyk', 'Klorek', 'Kajdan', 'Kajak', 'Gral', 'Zawodnik', 'Ulfik',
        'Sobieszczyk', 'Skrobot', 'Ochał', 'Leżoń', 'Krywult', 'Iciek', 'Gasek', 'Czenczek',
        'Budzeń', 'Botor', 'Wikło', 'Tymczyszyn', 'Szpyra', 'Słonka', 'Prasek', 'Majczyna', 'Lula',
        'Jakubiuk', 'Hanzel', 'Głowiak', 'Calik', 'Zagrajek', 'Stefankiewicz', 'Serzysko',
        'Piechna', 'Myga', 'Maślankiewicz', 'Kuziora', 'Korniak', 'Indyka', 'Gałach', 'Gadzina',
        'Cyba', 'Bystrek', 'Bazela', 'Wabik', 'Ragus', 'Pitek', 'Mizia', 'Łaskawiec', 'Holeksa',
        'Hajdasz', 'Fugiel', 'Białasik', 'Woźniczko', 'Wilma', 'Rode', 'Preś', 'Komander', 'Klus',
        'Sarosiek', 'Sadoch', 'Osipowicz', 'Lelonek', 'Korbut', 'Jarmużek', 'Włodyka', 'Józefczak',
        'Jędra', 'Hamerla', 'Gęgotek', 'Domińczak', 'Wypiór', 'Sudnik', 'Słoboda', 'Pela', 'Kupś',
        'Kostorz', 'Kosak', 'Kopyść', 'Jarmuła', 'Daniec', 'Blank', 'Balcewicz', 'Starostka',
        'Siemieńczuk', 'Reiter', 'Mycek', 'Miętka', 'Łupina', 'Lipok', 'Knych', 'Drobisz', 'Cuch',
        'Wojtarowicz', 'Wojniak', 'Piechura', 'Meissner', 'Lemiesz', 'Klęk', 'Jargieło', 'Jamroz',
        'Huczko', 'Ceynowa', 'Trochim', 'Kremer', 'Janic', 'Gal', 'Cyrulik', 'Bejger', 'Bawoł',
        'Szczepan', 'Plewnia', 'Pędrak', 'Niedośpiał', 'Maras', 'Klepka', 'Kawulok', 'Katana',
        'Bronka', 'Bender', 'Bałdys', 'Wawrzonek', 'Taranek', 'Tadych', 'Szymała', 'Stebel', 'Skup',
        'Skubała', 'Pasieczna', 'Karkocha', 'Hak', 'Gąszczak', 'Pyś', 'Prażuch', 'Politowicz',
        'Piestrzeniewicz', 'Pajek', 'Nitek', 'Kozok', 'Kowala', 'Kalinka', 'Galuba', 'Buk', 'Breś',
        'Bodych', 'Bittner', 'Bakiera', 'Rembacz', 'Podgórna', 'Myrcik', 'Mojsa', 'Karpiak',
        'Kajdas', 'Gregorczuk', 'Dziurla', 'Dzienniak', 'Dyrek', 'Żołądkiewicz', 'Szumacher',
        'Sado', 'Pyszny', 'Narożny', 'Kuszyk', 'Jakimiak', 'Dynak', 'Dejneka', 'Wiekiera',
        'Tatarczuk', 'Rudyk', 'Nieścioruk', 'Laszkiewicz', 'Gołota', 'Golisz', 'Bąbel', 'Taczała',
        'Świć', 'Siciarz', 'Ropiak', 'Pacura', 'Makulec', 'Krauza', 'Grzesiek', 'Gemza', 'Dering',
        'Banek', 'Andziak', 'Wiza', 'Trojanowicz', 'Parkitna', 'Pacholik', 'Majtczak', 'Krenc',
        'Koniec', 'Wawrzeńczyk', 'Stupak', 'Roda', 'Maciejczuk', 'Irla', 'Husak', 'Fuławka',
        'Fabiańczyk', 'Bryda', 'Zackiewicz', 'Szoka', 'Melcer', 'Kempny', 'Dulemba', 'Duc',
        'Ziniewicz', 'Truchel', 'Szajner', 'Petryk', 'Peda', 'Obarzanek', 'Maszkiewicz', 'Łabaj',
        'Cymbała', 'Biesaga', 'Zdobylak', 'Wojtiuk', 'Ulrych', 'Szymków', 'Sporysz', 'Smardz',
        'Mandrysz', 'Kulus', 'Duras', 'Dumin', 'Borejko', 'Wyłupek', 'Ufniarz', 'Stypka',
        'Młyńczyk', 'Miros', 'Maciuk', 'Hrabia', 'Burzec', 'Buksa', 'Wygoda', 'Tomzik', 'Pindral',
        'Nijak', 'Mszyca', 'Maciejuk', 'Kudłacz', 'Dziwak', 'Chaba', 'Borkowicz', 'Berek',
        'Żakiewicz', 'Wykręt', 'Sztuba', 'Smykała', 'Pyc', 'Pęciak', 'Parzonka', 'Kyc', 'Klemczak',
        'Gąsienica', 'Gabryszak', 'Częścik', 'Cisoń', 'Zmyślony', 'Komisarek', 'Ficoń', 'Citko',
        'Bidas', 'Bas', 'Żabierek', 'Wyciszkiewicz', 'Tarach', 'Staniewicz', 'Reichel',
        'Panasewicz', 'Kucewicz', 'Kilar', 'Hein', 'Fronia', 'Derek', 'Bruś', 'Antoń', 'Pawlos',
        'Ochwat', 'Kurbiel', 'Gosik', 'Gierasimiuk', 'Doroba', 'Chłąd', 'Wrochna', 'Protasiuk',
        'Opalach', 'Mućko', 'Martyn', 'Drgas', 'Ceran', 'Bryczek', 'Ziarno', 'Wołodźko', 'Wac',
        'Szpala', 'Szlachcic', 'Rurka', 'Oczkowicz', 'Mik', 'Małysiak', 'Kubek', 'Imiela', 'Graboń',
        'Garbacik', 'Dolega', 'Broncel', 'Baum', 'Bancerz', 'Siedlik', 'Miąsko', 'Lenc', 'Konat',
        'Kaletka', 'Jenek', 'Honkisz', 'Droś', 'Suchojad', 'Ratka', 'Raba', 'Lulek', 'Komperda',
        'Kołodziejak', 'Koloch', 'Kolka', 'Joniak', 'Jezior', 'Faltyn', 'Dyjach', 'Czulak', 'Cop',
        'Wyroślak', 'Woda', 'Stranc', 'Solis', 'Skomra', 'Sierpień', 'Rzeźniczek', 'Pajdak',
        'Mostek', 'Machowiak', 'Janduła', 'Fitrzyk', 'Welenc', 'Tyczka', 'Skiepko', 'Potok',
        'Olewniczak', 'Nitkiewicz', 'Myrcha', 'Krata', 'Kara', 'Hołysz', 'Hałka', 'Florian',
        'Dziurdzia', 'Dryka', 'Sysło', 'Rolek', 'Młocek', 'Idzi', 'Haponiuk', 'Grębowiec', 'Gęca',
        'Bochnia', 'Ślipek', 'Sieczko', 'Pierz', 'Nyc', 'Łacina', 'Ludwisiak', 'Kujda', 'Hutyra',
        'Dziugieł', 'Białka', 'Zemanek', 'Zawartka', 'Smyl', 'Smolec', 'Słoka', 'Putek',
        'Pietrewicz', 'Lepka', 'Krzeszowiec', 'Kowalówka', 'Jośko', 'Hamrol', 'Gapys', 'Antoszczyk',
        'Turoń', 'Teter', 'Surdel', 'Pieczyrak', 'Mudlaff', 'Manista', 'Kolek', 'Kadela', 'Jeka',
        'Jamrożek', 'Goliasz', 'Dywan', 'Drewnik', 'Dąbroś', 'Ciaś', 'Obiała', 'Nocek', 'Marko',
        'Ładziak', 'Hadaś', 'Dulik', 'Dorynek', 'Wolańczyk', 'Stoltmann', 'Rozumek', 'Łudzik',
        'Łaś', 'Leoniuk', 'Krzyk', 'Karol', 'Kamyszek', 'Filusz', 'Czermak', 'Budych', 'Żółkiewicz',
        'Tatarczyk', 'Pietrus', 'Pachowicz', 'Niesporek', 'Kultys', 'Kornet', 'Kajstura',
        'Grześków', 'Dub', 'Drobot', 'Urynowicz', 'Swacha', 'Prokopczuk', 'Michnowicz', 'Malka',
        'Labocha', 'Capiga', 'Zawalich', 'Wizner', 'Startek', 'Smolorz', 'Rozynek', 'Pal',
        'Madajczyk', 'Ławniczek', 'Haremza', 'Bejnarowicz', 'Żuberek', 'Windak', 'Sobolak',
        'Sibiga', 'Rajczak', 'Pudełek', 'Michalkiewicz', 'Fularczyk', 'Broniarek', 'Żabka',
        'Towarek', 'Sugier', 'Pikula', 'Pawlonka', 'Marosz', 'Kut', 'Grymuza', 'Dąbkiewicz',
        'Ciechowicz', 'Brodawka', 'Borzych', 'Bela', 'Zaguła', 'Tyniec', 'Trepczyk', 'Stwora',
        'Paczos', 'Olbrych', 'Ogrodowicz', 'Michel', 'Mazepa', 'Lazarek', 'Krzystek', 'Jażdżyk',
        'Goska', 'Fraszczyk', 'Drożdżal', 'Cofała', 'Chołody', 'Wawrzyk', 'Prokurat', 'Policht',
        'Płodzień', 'Pasztaleniec', 'Osipiuk', 'Mateńko', 'Kiciak', 'Grotek', 'Członka', 'Żal',
        'Zimmer', 'Wosiak', 'Srokosz', 'Paździora', 'Patoła', 'Pałęga', 'Orawiec', 'Nastaj',
        'Mirgos', 'Merda', 'Machniak', 'Łokietek', 'Fogiel', 'Elias', 'Świergiel', 'Stempel',
        'Skocz', 'Potoczek', 'Penar', 'Miecznik', 'Kwapis', 'Jakóbiak', 'Gietka', 'Flisek',
        'Dudzicz', 'Cich', 'Broniek', 'Wiercigroch', 'Usarek', 'Tryc', 'Szylar', 'Szczot', 'Ptok',
        'Prystupa', 'Preuss', 'Piekara', 'Łaszczyk', 'Kurzaj', 'Kopiczko', 'Jachimczak', 'Hirsch',
        'Dytrych', 'Dorna', 'Bystroń', 'Worach', 'Tokaj', 'Szmagaj', 'Solnica', 'Rejmak', 'Reimann',
        'Pazoła', 'Nieradzik', 'Miechowicz', 'Langiewicz', 'Kruś', 'Kozień', 'Kielczyk', 'Jargiło',
        'Dąbal', 'Cichos', 'Sorbian', 'Ruman', 'Piotrkowicz', 'Oziębło', 'Henke', 'Czosnyka',
        'Choina', 'Chabior', 'Warzybok', 'Seweryniak', 'Pyzel', 'Niewola', 'Nesterowicz', 'Liss',
        'Kiepas', 'Kalista', 'Demiańczuk', 'Cłapa', 'Błasik', 'Berdzik', 'Bełza', 'Złotek',
        'Tonder', 'Szwaj', 'Szarzec', 'Suchora', 'Sarota', 'Palica', 'Matula', 'Malecha', 'Magryta',
        'Łuckiewicz', 'Kuster', 'Stoltman', 'Siewert', 'Serwach', 'Schwarz', 'Kuźnia', 'Kuśmider',
        'Kurzac', 'Klisz', 'Gwardiak', 'Gotfryd', 'Deneka', 'Ciuruś', 'Żmija', 'Tałaj', 'Sobuś',
        'Rajman', 'Perlik', 'Kurda', 'Kosznik', 'Kaluga', 'Jaracz', 'Hanas', 'Dzwonnik', 'Ziegert',
        'Szyma', 'Różewicz', 'Paszkowiak', 'Maślach', 'Lewicz', 'Heba', 'Godzwon', 'Drej', 'Borak',
        'Adamów', 'Tywoniuk', 'Ścieszka', 'Smal', 'Łabuś', 'Kominiak', 'Dietrich', 'Cąkała',
        'Budzich', 'Bąbol', 'Zgoła', 'Sładek', 'Sierżant', 'Misiurek', 'Miąsik', 'Mądrzyk',
        'Kretowicz', 'Kasznia', 'Jeżyna', 'Humeniuk', 'Fiutak', 'Czerniakiewicz', 'Bork', 'Żymełka',
        'Tomalik', 'Szarpak', 'Sołtan', 'Maciuszek', 'Krysta', 'Grzeszkowiak', 'Brachman', 'Zys',
        'Westfal', 'Waluk', 'Wacławiak', 'Sałuda', 'Sabak', 'Niedojadło', 'Nazarko', 'Murat',
        'Majzner', 'Ludwin', 'Kubaczyk', 'Kielich', 'Doliwa', 'Dej', 'Chuchla', 'Boguś', 'Bobik',
        'Zadworny', 'Wójs', 'Tyma', 'Sztuczka', 'Strządała', 'Sowała', 'Omiotek', 'Oleśkiewicz',
        'Morawiak', 'Kwapisiewicz', 'Krokosz', 'Hajder', 'Garczyk', 'Burdach', 'Związek', 'Wojczuk',
        'Stanclik', 'Piekart', 'Mielke', 'Machowicz', 'Kozieja', 'Kaziród', 'Gaś', 'Garbaciak',
        'Chatys', 'Bzdęga', 'Bartoszczyk', 'Zdonek', 'Więcławek', 'Wielgo', 'Steuer', 'Staręga',
        'Sakwa', 'Orpel', 'Kobel', 'Golonko', 'Stark', 'Soczówka', 'Nickel', 'Kupaj', 'Kolman',
        'Kieca', 'Kamyk', 'Jeżyk', 'Glica', 'Gasz', 'Gamrat', 'Franiak', 'Bacik', 'Andrukiewicz',
        'Troka', 'Siwka', 'Odrzywołek', 'Nurkiewicz', 'Kozubal', 'Kott', 'Głowienka', 'Doroszuk',
        'Cogiel', 'Cheba', 'Baś', 'Andreasik', 'Wenzel', 'Szumna', 'Rosłoń', 'Ogłaza',
        'Mikłaszewicz', 'Kubieniec', 'Jędral', 'Bieniak', 'Wons', 'Władyka', 'Rolak', 'Prejs',
        'Płocharczyk', 'Ostręga', 'Łęgowik', 'Ludwik', 'Kopik', 'Kleinschmidt', 'Karczmarek',
        'Gładka', 'Czylok', 'Wawrzynkiewicz',
    )
    male_last_names = (
        'Kowalski', 'Wiśniewski', 'Dąbrowski', 'Lewandowski', 'Wójcik', 'Kamiński', 'Kowalczyk',
        'Zieliński', 'Szymański', 'Woźniak', 'Kozłowski', 'Jankowski', 'Wojciechowski',
        'Kwiatkowski', 'Kaczmarek', 'Mazur', 'Krawczyk', 'Piotrowski', 'Grabowski', 'Nowakowski',
        'Pawłowski', 'Michalski', 'Nowicki', 'Adamczyk', 'Dudek', 'Zając', 'Wieczorek', 'Jabłoński',
        'Król', 'Majewski', 'Olszewski', 'Jaworski', 'Wróbel', 'Malinowski', 'Pawlak', 'Witkowski',
        'Walczak', 'Stępień', 'Górski', 'Rutkowski', 'Michalak', 'Sikora', 'Ostrowski', 'Baran',
        'Duda', 'Szewczyk', 'Tomaszewski', 'Pietrzak', 'Marciniak', 'Wróblewski', 'Zalewski',
        'Jakubowski', 'Jasiński', 'Zawadzki', 'Sadowski', 'Bąk', 'Chmielewski', 'Włodarczyk',
        'Borkowski', 'Czarnecki', 'Sawicki', 'Sokołowski', 'Urbański', 'Kubiak', 'Maciejewski',
        'Szczepański', 'Kucharski', 'Wilk', 'Kalinowski', 'Lis', 'Mazurek', 'Wysocki', 'Adamski',
        'Kaźmierczak', 'Wasilewski', 'Sobczak', 'Czerwiński', 'Andrzejewski', 'Cieślak', 'Głowacki',
        'Zakrzewski', 'Kołodziej', 'Sikorski', 'Krajewski', 'Gajewski', 'Szymczak', 'Szulc',
        'Baranowski', 'Laskowski', 'Brzeziński', 'Makowski', 'Ziółkowski', 'Przybylski', 'Domański',
        'Nowacki', 'Borowski', 'Błaszczyk', 'Chojnacki', 'Ciesielski', 'Mróz', 'Szczepaniak',
        'Wesołowski', 'Górecki', 'Krupa', 'Kaczmarczyk', 'Leszczyński', 'Lipiński', 'Kowalewski',
        'Urbaniak', 'Kozak', 'Kania', 'Mikołajczyk', 'Czajkowski', 'Mucha', 'Tomczak', 'Kozioł',
        'Markowski', 'Kowalik', 'Nawrocki', 'Brzozowski', 'Janik', 'Musiał', 'Wawrzyniak',
        'Markiewicz', 'Orłowski', 'Tomczyk', 'Jarosz', 'Kołodziejczyk', 'Kurek', 'Kopeć', 'Żak',
        'Wolski', 'Łuczak', 'Dziedzic', 'Kot', 'Stasiak', 'Stankiewicz', 'Piątek', 'Jóźwiak',
        'Urban', 'Dobrowolski', 'Pawlik', 'Kruk', 'Domagała', 'Piasecki', 'Wierzbicki', 'Karpiński',
        'Jastrzębski', 'Polak', 'Zięba', 'Janicki', 'Wójtowicz', 'Stefański', 'Sosnowski',
        'Bednarek', 'Majchrzak', 'Bielecki', 'Małecki', 'Maj', 'Sowa', 'Milewski', 'Gajda',
        'Klimek', 'Olejniczak', 'Ratajczak', 'Romanowski', 'Matuszewski', 'Śliwiński', 'Madej',
        'Kasprzak', 'Wilczyński', 'Grzelak', 'Socha', 'Czajka', 'Marek', 'Kowal', 'Bednarczyk',
        'Skiba', 'Wrona', 'Owczarek', 'Marcinkowski', 'Matusiak', 'Orzechowski', 'Sobolewski',
        'Kędzierski', 'Kurowski', 'Rogowski', 'Olejnik', 'Dębski', 'Barański', 'Skowroński',
        'Mazurkiewicz', 'Pająk', 'Czech', 'Janiszewski', 'Bednarski', 'Łukasik', 'Chrzanowski',
        'Bukowski', 'Leśniak',
    )

    prefixes_male = ('pan',)
    prefixes_female = ('pani',)

    first_names = first_names_male + first_names_female

    def last_name(self):
        return self.random_element(self.unisex_last_names)

    def identity_card_number(self):
        """
        Returns 9 character Polish Identity Card Number,
        Polish: Numer Dowodu Osobistego.

        The card number consists of 3 letters followed by 6 digits (for example, ABA300000),
        of which the first digit (at position 3) is the check digit.

        https://en.wikipedia.org/wiki/Polish_identity_card
        """
        identity = []

        for _ in range(3):
            identity.append(self.random_letter().upper())

        # it will be overwritten by a checksum
        identity.append(0)

        for _ in range(5):
            identity.append(self.random_digit())

        identity[3] = checksum_identity_card_number(identity)

        return ''.join(str(character) for character in identity)

    @staticmethod
    def pesel_compute_check_digit(pesel):
        checksum_values = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
        return sum(int(a) * b for a, b in zip(pesel, checksum_values)) % 10

    def pesel(self, date_of_birth=None, sex=None):
        """
        Returns 11 characters of Universal Electronic System for Registration of the Population.
        Polish: Powszechny Elektroniczny System Ewidencji Ludności.

        PESEL has 11 digits which identifies just one person.
        pesel_date: if person was born in 1900-2000, december is 12. If person was born > 2000, we have to add 20 to
        month, so december is 32.
        pesel_sex: last digit identifies person's sex. Even for females, odd for males.

        https://en.wikipedia.org/wiki/PESEL
        """
        if date_of_birth is None:
            date_of_birth = self.generator.date_of_birth()

        pesel_date = '{year}{month:02d}{day:02d}'.format(
            year=date_of_birth.year, day=date_of_birth.day,
            month=date_of_birth.month if date_of_birth.year < 2000 else date_of_birth.month + 20)
        pesel_date = pesel_date[2:]

        pesel_core = ''.join(map(str, (self.random_digit() for _ in range(3))))
        pesel_sex = self.random_digit()

        if (sex == 'M' and pesel_sex % 2 == 0) or (sex == 'F' and pesel_sex % 2 == 1):
            pesel_sex = (pesel_sex + 1) % 10

        pesel = '{date}{core}{sex}'.format(date=pesel_date, core=pesel_core, sex=pesel_sex)
        pesel += str(self.pesel_compute_check_digit(pesel))

        return pesel

    @staticmethod
    def pwz_doctor_compute_check_digit(x):
        return sum((i + 1) * d for i, d in enumerate(x)) % 11

    def pwz_doctor(self):
        """
        Function generates an identification number for medical doctors
        Polish: Prawo Wykonywania Zawodu (PWZ)

        https://www.nil.org.pl/rejestry/centralny-rejestr-lekarzy/zasady-weryfikowania-nr-prawa-wykonywania-zawodu
        """
        core = [self.random_digit() for _ in range(6)]
        check_digit = self.pwz_doctor_compute_check_digit(core)

        if check_digit == 0:
            core[-1] = (core[-1] + 1) % 10
            check_digit = self.pwz_doctor_compute_check_digit(core)

        return '{}{}'.format(check_digit, ''.join(map(str, core)))

    def pwz_nurse(self, kind='nurse'):
        """
        Function generates an identification number for nurses and midwives
        Polish: Prawo Wykonywania Zawodu (PWZ)

        http://arch.nipip.pl/index.php/prawo/uchwaly/naczelnych-rad/w-roku-2015/posiedzenie-15-17-grudnia/3664-uchwala-
        nr-381-vi-2015-w-sprawie-trybu-postepowania-dotyczacego-stwierdzania-i-przyznawania-prawa-wykonywania-zawodu-pi
        elegniarki-i-zawodu-poloznej-oraz-sposobu-prowadzenia-rejestru-pielegniarek-i-rejestru-poloznych-przez-okregowe
        -rady-pielegniarek-i-polo
        """
        region = self.random_int(1, 45)
        core = [self.random_digit() for _ in range(5)]
        kind_char = 'A' if kind == 'midwife' else 'P'

        return '{:02d}{}{}'.format(region, ''.join(map(str, core)), kind_char)

    tax_office_codes = (
        '101',  # Dolnośląski Urząd Skarbowy we Wrocławiu
        '102',  # Kujawsko-Pomorski Urząd Skarbowy w Bydgoszczy
        '103',  # Lubelski Urząd Skarbowy w Lublinie
        '104',  # Lubuski Urząd Skarbowy w Zielonej Górze
        '105',  # Łódzki Urząd Skarbowy w Łodzi
        '106',  # Małopolski Urząd Skarbowy w Krakowie
        '107',  # Pierwszy Mazowiecki Urząd Skarbowy w Warszawie
        '108',  # Drugi Mazowiecki Urząd Skarbowy w Warszawie
        '109',  # Trzeci Mazowiecki Urząd Skarbowy w Radomiu
        '111',  # Urząd Skarbowy Warszawa-Mokotów
        '112',  # Urząd Skarbowy Warszawa-Bemowo
        '113',  # Urząd Skarbowy Warszawa-Praga
        '114',  # Urząd Skarbowy Warszawa-Targówek
        '115',  # Pierwszy Urząd Skarbowy Warszawa-Śródmieście
        '116',  # Drugi Urząd Skarbowy Warszawa-Śródmieście
        '117',  # Urząd Skarbowy Warszawa-Wola
        '118',  # Urząd Skarbowy Warszawa-Bielany
        '119',  # Urząd Skarbowy w Grodzisku Mazowieckim
        '121',  # Urząd Skarbowy w Nowym Dworze Mazowieckim
        '122',  # Urząd Skarbowy w Otwocku
        '123',  # Urząd Skarbowy w Piasecznie
        '124',  # Urząd Skarbowy w Pruszkowie
        '125',  # Urząd Skarbowy w Wołominie
        '126',  # Urząd Skarbowy w Białej Podlaskiej
        '127',  # Urząd Skarbowy w Parczewie
        '128',  # Urząd Skarbowy w Radzyniu Podlaskim
        '129',  # Pierwszy Urząd Skarbowy w Białymstoku
        '131',  # Urząd Skarbowy w Bielsku Podlaskim
        '132',  # Urząd Skarbowy w Mońkach
        '133',  # Urząd Skarbowy w Siemiatyczach
        '134',  # Urząd Skarbowy w Sokółce
        '135',  # Pierwszy Urząd Skarbowy w Bielsku-Białej
        '136',  # Urząd Skarbowy w Cieszynie
        '137',  # Urząd Skarbowy w Oświęcimiu
        '138',  # Urząd Skarbowy w Suchej Beskidzkiej
        '139',  # Urząd Skarbowy w Wadowicach
        '141',  # Urząd Skarbowy w Żywcu
        '142',  # Pierwszy Urząd Skarbowy w Bydgoszczy
        '143',  # Urząd Skarbowy w Chojnicach
        '144',  # Urząd Skarbowy w Inowrocławiu
        '145',  # Urząd Skarbowy w Mogilnie
        '146',  # Urząd Skarbowy w Nakle nad Notecią
        '147',  # Urząd Skarbowy w Świeciu
        '148',  # Urząd Skarbowy w Tucholi
        '149',  # Urząd Skarbowy w Żninie
        '151',  # Urząd Skarbowy w Chełmie
        '152',  # Urząd Skarbowy w Krasnymstawie
        '153',  # Urząd Skarbowy we Włodawie
        '154',  # Urząd Skarbowy w Ciechanowie
        '155',  # Urząd Skarbowy w Działdowie
        '156',  # Urząd Skarbowy w Mławie
        '157',  # Urząd Skarbowy w Płońsku
        '158',  # Urząd Skarbowy w Pułtusku
        '159',  # Pierwszy Urząd Skarbowy w Częstochowie
        '161',  # Urząd Skarbowy w Kłobucku
        '162',  # Urząd Skarbowy w Lublińcu
        '163',  # Urząd Skarbowy w Myszkowie
        '164',  # Urząd Skarbowy w Oleśnie
        '165',  # Urząd Skarbowy w Braniewie
        '166',  # Urząd Skarbowy w Elblągu
        '167',  # Urząd Skarbowy w Kwidzynie
        '168',  # Urząd Skarbowy w Malborku
        '169',  # Pierwszy Urząd Skarbowy w Gdańsku
        '171',  # Drugi Urząd Skarbowy w Gdańsku
        '172',  # Pierwszy Urząd Skarbowy w Gdyni
        '173',  # Urząd Skarbowy w Kartuzach
        '174',  # Urząd Skarbowy w Kościerzynie
        '175',  # Urząd Skarbowy w Pucku
        '176',  # Urząd Skarbowy w Sopocie
        '177',  # Urząd Skarbowy w Starogardzie Gdańskim
        '178',  # Urząd Skarbowy w Tczewie
        '179',  # Urząd Skarbowy w Wejherowie
        '181',  # Urząd Skarbowy w Choszcznie
        '182',  # Urząd Skarbowy w Gorzowie Wielkopolskim
        '183',  # Urząd Skarbowy w Myśliborzu
        '184',  # Urząd Skarbowy w Międzychodzie
        '185',  # Urząd Skarbowy w Międzyrzeczu
        '186',  # Urząd Skarbowy w Słubicach
        '187',  # Urząd Skarbowy w Bolesławcu
        '188',  # Urząd Skarbowy w Jeleniej Górze
        '189',  # Urząd Skarbowy w Kamiennej Górze
        '191',  # Urząd Skarbowy w Lubaniu
        '192',  # Urząd Skarbowy w Lwówku Śląskim
        '193',  # Urząd Skarbowy w Zgorzelcu
        '194',  # Urząd Skarbowy w Jarocinie
        '195',  # Pierwszy Urząd Skarbowy w Kaliszu
        '196',  # Urząd Skarbowy w Kępnie
        '197',  # Urząd Skarbowy w Krotoszynie
        '198',  # Urząd Skarbowy w Ostrowie Wielkopolskim
        '199',  # Urząd Skarbowy w Będzinie
        '201',  # Opolski Urząd Skarbowy w Opolu
        '202',  # Podkarpacki Urząd Skarbowy w Rzeszowie
        '203',  # Podlaski Urząd Skarbowy w Białymstoku
        '204',  # Pomorski Urząd Skarbowy w Gdańsku
        '205',  # Pierwszy Śląski Urząd Skarbowy w Sosnowcu
        '206',  # Drugi Śląski Urząd Skarbowy w Bielsku-Białej
        '207',  # Świętokrzyski Urząd Skarbowy w Kielcach
        '208',  # Warmińsko-Mazurski Urząd Skarbowy w Olsztynie
        '209',  # Pierwszy Wielkopolski Urząd Skarbowy w Poznaniu
        '211',  # Urząd Skarbowy w Bytomiu
        '212',  # Urząd Skarbowy w Chorzowie
        '213',  # Urząd Skarbowy w Chrzanowie
        '214',  # Urząd Skarbowy w Czechowicach-Dziedzicach
        '215',  # Urząd Skarbowy w Dąbrowie Górniczej
        '216',  # Pierwszy Urząd Skarbowy w Gliwicach
        '217',  # Urząd Skarbowy w Jastrzębiu-Zdroju
        '218',  # Urząd Skarbowy w Jaworznie
        '219',  # Pierwszy Urząd Skarbowy w Katowicach
        '221',  # Urząd Skarbowy w Mikołowie
        '222',  # Urząd Skarbowy w Mysłowicach
        '223',  # Urząd Skarbowy w Olkuszu
        '224',  # Urząd Skarbowy w Pszczynie
        '225',  # Urząd Skarbowy w Raciborzu
        '226',  # Urząd Skarbowy w Rudzie Śląskiej
        '227',  # Urząd Skarbowy w Rybniku
        '228',  # Urząd Skarbowy w Siemianowicach Śląskich
        '229',  # Urząd Skarbowy w Sosnowcu
        '231',  # Urząd Skarbowy w Tarnowskich Górach
        '232',  # Urząd Skarbowy w Tychach
        '233',  # Urząd Skarbowy w Wodzisławiu Śląskim
        '234',  # Urząd Skarbowy w Zabrzu
        '235',  # Urząd Skarbowy w Zawierciu
        '236',  # Urząd Skarbowy w Żorach
        '237',  # Urząd Skarbowy w Busku-Zdroju
        '238',  # Urząd Skarbowy w Jędrzejowie
        '239',  # Pierwszy Urząd Skarbowy w Kielcach
        '241',  # Urząd Skarbowy w Końskich
        '242',  # Urząd Skarbowy w Miechowie
        '243',  # Urząd Skarbowy w Ostrowcu Świętokrzyskim
        '244',  # Urząd Skarbowy w Pińczowie
        '245',  # Urząd Skarbowy w Starachowicach
        '246',  # Urząd Skarbowy w Skarżysku-Kamiennej
        '247',  # Urząd Skarbowy w Kole
        '248',  # Urząd Skarbowy w Koninie
        '249',  # Urząd Skarbowy w Słupcy
        '251',  # Urząd Skarbowy w Turku
        '252',  # Urząd Skarbowy w Białogardzie
        '253',  # Urząd Skarbowy w Drawsku Pomorskim
        '254',  # Urząd Skarbowy w Kołobrzegu
        '255',  # Pierwszy Urząd Skarbowy w Koszalinie
        '256',  # Urząd Skarbowy w Szczecinku
        '257',  # Urząd Skarbowy Kraków-Krowodrza
        '258',  # Urząd Skarbowy Kraków-Nowa Huta
        '259',  # Urząd Skarbowy Kraków-Podgórze
        '261',  # Urząd Skarbowy w Kraków-Śródmieście
        '262',  # Urząd Skarbowy w Kraków-Stare Miasto
        '263',  # Urząd Skarbowy w Myślenicach
        '264',  # Urząd Skarbowy w Proszowicach
        '265',  # Urząd Skarbowy w Wieliczce
        '266',  # Urząd Skarbowy w Brzozowie
        '267',  # Urząd Skarbowy w Jaśle
        '268',  # Urząd Skarbowy w Krośnie
        '269',  # Urząd Skarbowy w Lesku
        '271',  # Urząd Skarbowy w Sanoku
        '272',  # Urząd Skarbowy w Ustrzykach Dolnych
        '273',  # Urząd Skarbowy w Głogowie
        '274',  # Urząd Skarbowy w Jaworze
        '275',  # Urząd Skarbowy w Legnicy
        '276',  # Urząd Skarbowy w Lubinie
        '277',  # Urząd Skarbowy w Złotoryi
        '278',  # Urząd Skarbowy w Gostyniu
        '279',  # Urząd Skarbowy w Kościanie
        '281',  # Urząd Skarbowy w Lesznie
        '282',  # Urząd Skarbowy w Rawiczu
        '283',  # Urząd Skarbowy w Kraśniku
        '284',  # Urząd Skarbowy w Lubartowie
        '285',  # Pierwszy Urząd Skarbowy w Lublinie
        '286',  # Drugi Urząd Skarbowy w Lublinie
        '287',  # Urząd Skarbowy w Opolu Lubelskim
        '288',  # Urząd Skarbowy w Puławach
        '289',  # Urząd Skarbowy w Grajewie
        '291',  # Urząd Skarbowy w Kolnie
        '292',  # Urząd Skarbowy w Łomży
        '293',  # Urząd Skarbowy w Wysokiem Mazowieckim
        '294',  # Urząd Skarbowy w Zambrowie
        '295',  # Urząd Skarbowy w Głownie
        '296',  # Pierwszy Urząd Skarbowy Łódź-Bałuty
        '297',  # Pierwszy Urząd Skarbowy Łódź-Górna
        '298',  # Urząd Skarbowy Łódź-Polesie
        '301',  # Drugi Wielkopolski Urząd Skarbowy w Kaliszu
        '302',  # Zachodniopomorski Urząd Skarbowy w Szczecinie
        '311',  # Urząd Skarbowy Łódź-Śródmieście
        '312',  # Urząd Skarbowy Łódź-Widzew
        '313',  # Urząd Skarbowy w Pabianicach
        '314',  # Urząd Skarbowy w Zgierzu
        '315',  # Urząd Skarbowy w Gorlicach
        '316',  # Urząd Skarbowy w Limanowej
        '317',  # Urząd Skarbowy w Nowym Sączu
        '318',  # Urząd Skarbowy w Nowym Targu
        '319',  # Urząd Skarbowy w Zakopanem
        '321',  # Urząd Skarbowy w Bartoszycach
        '322',  # Urząd Skarbowy w Iławie
        '323',  # Urząd Skarbowy w Kętrzynie
        '324',  # Urząd Skarbowy w Olsztynie
        '325',  # Urząd Skarbowy w Ostródzie
        '326',  # Urząd Skarbowy w Szczytnie
        '327',  # Urząd Skarbowy w Brzegu
        '328',  # Urząd Skarbowy w Głubczycach
        '329',  # Urząd Skarbowy w Kędzierzynie-Koźlu
        '331',  # Urząd Skarbowy w Kluczborku
        '332',  # Urząd Skarbowy w Namysłowie
        '333',  # Urząd Skarbowy w Nysie
        '334',  # Pierwszy Urząd Skarbowy w Opolu
        '335',  # Urząd Skarbowy w Prudniku
        '336',  # Urząd Skarbowy w Strzelcach Opolskich
        '337',  # Urząd Skarbowy w Makowie Mazowieckim
        '338',  # Urząd Skarbowy w Ostrołęce
        '339',  # Urząd Skarbowy w Ostrowi Mazowieckiej
        '341',  # Urząd Skarbowy w Przasnyszu
        '342',  # Urząd Skarbowy w Wyszkowie
        '343',  # Urząd Skarbowy w Czarnkowie
        '344',  # Urząd Skarbowy w Pile
        '345',  # Urząd Skarbowy w Wałczu
        '346',  # Urząd Skarbowy w Wągrowcu
        '347',  # Urząd Skarbowy w Złotowie
        '348',  # Urząd Skarbowy w Bełchatowie
        '349',  # Urząd Skarbowy w Opocznie
        '351',  # Urząd Skarbowy w Piotrkowie Trybunalskim
        '352',  # Urząd Skarbowy w Radomsku
        '353',  # Urząd Skarbowy w Tomaszowie Mazowieckim
        '354',  # Urząd Skarbowy w Kutnie
        '355',  # Urząd Skarbowy w Płocku
        '356',  # Urząd Skarbowy w Sierpcu
        '357',  # Urząd Skarbowy w Gnieźnie
        '358',  # Urząd Skarbowy w Nowym Tomyślu
        '359',  # Urząd Skarbowy Poznań-Grunwald
        '361',  # Urząd Skarbowy Poznań-Jeżyce
        '362',  # Urząd Skarbowy Poznań-Nowe Miasto
        '363',  # Pierwszy Urząd Skarbowy Poznań
        '364',  # Urząd Skarbowy Poznań-Śródmieście
        '365',  # Urząd Skarbowy Poznań-Wilda
        '366',  # Urząd Skarbowy w Szamotułach
        '367',  # Urząd Skarbowy w Śremie
        '368',  # Urząd Skarbowy w Środzie Wielkopolskiej
        '369',  # Urząd Skarbowy we Wrześni
        '371',  # Urząd Skarbowy w Jarosławiu
        '372',  # Urząd Skarbowy w Lubaczowie
        '373',  # Urząd Skarbowy w Przemyślu
        '374',  # Urząd Skarbowy w Przeworsku
        '375',  # Urząd Skarbowy w Białobrzegach
        '376',  # Urząd Skarbowy w Grójcu
        '377',  # Urząd Skarbowy w Kozienicach
        '378',  # Pierwszy Urząd Skarbowy w Radomiu
        '379',  # Urząd Skarbowy w Szydłowcu
        '381',  # Urząd Skarbowy w Zwoleniu
        '382',  # Urząd Skarbowy w Kolbuszowej
        '383',  # Urząd Skarbowy w Leżajsku
        '384',  # Urząd Skarbowy w Łańcucie
        '385',  # Urząd Skarbowy w Mielcu
        '386',  # Urząd Skarbowy w Ropczycach
        '387',  # Urząd Skarbowy w Rzeszowie
        '388',  # Urząd Skarbowy w Strzyżowie
        '389',  # Urząd Skarbowy w Garwolinie
        '391',  # Urząd Skarbowy w Łukowie
        '392',  # Urząd Skarbowy w Mińsku Mazowieckim
        '393',  # Urząd Skarbowy w Siedlcach
        '394',  # Urząd Skarbowy w Sokołowie Podlaskim
        '395',  # Urząd Skarbowy w Węgrowie
        '396',  # Urząd Skarbowy w Łasku
        '397',  # Urząd Skarbowy w Poddębicach
        '398',  # Urząd Skarbowy w Sieradzu
        '399',  # Urząd Skarbowy w Wieluniu
        '411',  # Urząd Skarbowy w Zduńskiej Woli
        '412',  # Urząd Skarbowy w Brzezinach
        '413',  # Urząd Skarbowy w Łowiczu
        '414',  # Urząd Skarbowy w Rawie Mazowieckiej
        '415',  # Urząd Skarbowy w Skierniewicach
        '416',  # Urząd Skarbowy w Sochaczewie
        '417',  # Urząd Skarbowy w Żyrardowie
        '418',  # Urząd Skarbowy w Bytowie
        '419',  # Urząd Skarbowy w Człuchowie
        '421',  # Urząd Skarbowy w Lęborku
        '422',  # Urząd Skarbowy w Słupsku
        '423',  # Urząd Skarbowy w Augustowie
        '424',  # Urząd Skarbowy w Ełku
        '425',  # Urząd Skarbowy w Giżycku
        '426',  # Urząd Skarbowy w Olecku
        '427',  # Urząd Skarbowy w Piszu
        '428',  # Urząd Skarbowy w Suwałkach
        '429',  # Urząd Skarbowy w Goleniowie
        '431',  # Urząd Skarbowy w Gryficach
        '432',  # Urząd Skarbowy w Gryfinie
        '433',  # Urząd Skarbowy w Pyrzycach
        '434',  # Urząd Skarbowy w Stargardzie Szczecińskim
        '435',  # Pierwszy Urząd Skarbowy w Szczecinie
        '436',  # Drugi Urząd Skarbowy w Szczecinie
        '437',  # Urząd Skarbowy w Świnoujściu
        '438',  # Urząd Skarbowy w Janowie Lubelskim
        '439',  # Urząd Skarbowy w Opatowie
        '441',  # Urząd Skarbowy w Sandomierzu
        '442',  # Urząd Skarbowy w Stalowej Woli
        '443',  # Urząd Skarbowy w Staszowie
        '444',  # Urząd Skarbowy w Tarnobrzegu
        '445',  # Urząd Skarbowy w Bochni
        '446',  # Urząd Skarbowy w Brzesku
        '447',  # Urząd Skarbowy w Dąbrowie Tarnowskiej
        '448',  # Urząd Skarbowy w Dębicy
        '449',  # Pierwszy Urząd Skarbowy w Tarnowie
        '451',  # Urząd Skarbowy w Brodnicy
        '452',  # Urząd Skarbowy w Chełmnie
        '453',  # Urząd Skarbowy w Grudziądzu
        '454',  # Urząd Skarbowy w Nowym Mieście Lubawskim
        '455',  # Drugi Urząd Skarbowy w Toruniu
        '456',  # Urząd Skarbowy w Wąbrzeźnie
        '457',  # Urząd Skarbowy w Bystrzycy Kłodzkiej
        '458',  # Urząd Skarbowy w Dzierżoniowie
        '459',  # Urząd Skarbowy w Kłodzku
        '461',  # Urząd Skarbowy w Nowej Rudzie
        '462',  # Urząd Skarbowy w Świdnicy
        '463',  # Urząd Skarbowy w Wałbrzychu
        '464',  # Urząd Skarbowy w Ząbkowicach Śląskich
        '465',  # Urząd Skarbowy w Aleksandrowie Kujawskim
        '466',  # Urząd Skarbowy w Lipnie
        '467',  # Urząd Skarbowy w Radziejowie
        '468',  # Urząd Skarbowy w Rypinie
        '469',  # Urząd Skarbowy we Włocławku
        '471',  # Urząd Skarbowy Wrocław-Fabryczna
        '472',  # Urząd Skarbowy Wrocław-Krzyki
        '473',  # Urząd Skarbowy Wrocław-Psie Pole
        '474',  # Urząd Skarbowy Wrocław-Stare Miasto
        '475',  # Pierwszy Urząd Skarbowy we Wrocławiu
        '476',  # Drugi Urząd Skarbowy Wrocław-Śródmieście
        '477',  # Urząd Skarbowy w Miliczu
        '478',  # Urząd Skarbowy w Oleśnicy
        '479',  # Urząd Skarbowy w Oławie
        '481',  # Urząd Skarbowy w Strzelnie
        '482',  # Urząd Skarbowy w Środzie Śląskiej
        '483',  # Urząd Skarbowy w Trzebnicy
        '484',  # Urząd Skarbowy w Biłgoraju
        '485',  # Urząd Skarbowy w Hrubieszowie
        '486',  # Urząd Skarbowy w Tomaszowie Lubelskim
        '487',  # Urząd Skarbowy w Zamościu
        '488',  # Urząd Skarbowy w Krośnie Odrzańskim
        '489',  # Urząd Skarbowy w Nowej Soli
        '491',  # Urząd Skarbowy w Świebodzinie
        '492',  # Urząd Skarbowy w Wolsztynie
        '493',  # Pierwszy Urząd Skarbowy w Zielonej Górze
        '494',  # Urząd Skarbowy w Żaganiu
        '495',  # Urząd Skarbowy w Żarach
        '496',  # Urząd Skarbowy w Łosicach
        '497',  # Urząd Skarbowy w Łosicach
        '498',  # Urząd Skarbowy w Piekarach Śląskich
        '499',  # Drugi Urząd Skarbowy w Koszalinie
        '501',  # Urząd Skarbowy W Górze
        '502',  # Urząd Skarbowy W Polkowicach
        '503',  # Urząd Skarbowy W Golubiu-Dobrzyniu
        '504',  # Urząd Skarbowy W Sepólnie Krajeńskim
        '505',  # Urząd Skarbowy W Łęcznej
        '506',  # Urząd Skarbowy W Rykach
        '507',  # Urząd Skarbowy W Łęczycy
        '508',  # Urząd Skarbowy W Pajęcznie
        '509',  # Urząd Skarbowy W Lipsku
        '511',  # Urząd Skarbowy w Żurominie
        '512',  # Urząd Skarbowy w Żurominie
        '513',  # Urząd Skarbowy w Lesznie
        '514',  # Urząd Skarbowy w Ostrzeszowie
        '516',  # Urząd Skarbowy w Ostrzeszowie
        '519',  # Urząd Skarbowy w Legionowie
        '521',  # Urząd Skarbowy Warszawa-Mokotów
        '522',  # Urząd Skarbowy Warszawa-Bemowo
        '523',  # Urząd Skarbowy Warszawa-Praga
        '524',  # Urząd Skarbowy Warszawa-Targówek
        '525',  # Pierwszy Urząd Skarbowy Warszawa-Śródmieście
        '526',  # Drugi Urząd Skarbowy Warszawa-Śródmieście
        '527',  # Urząd Skarbowy Warszawa-Wola
        '528',  # Urząd Skarbowy Warszawa-Bielany
        '529',  # Urząd Skarbowy w Grodzisku Mazowieckim
        '531',  # Urząd Skarbowy w Nowym Dworze Mazowieckim
        '532',  # Urząd Skarbowy w Otwocku
        '533',  # Urząd Skarbowy w Piasecznie
        '534',  # Urząd Skarbowy w Pruszkowie
        '535',  # Urząd Skarbowy w Wołominie
        '536',  # Urząd Skarbowy w Legionowie
        '537',  # Urząd Skarbowy w Białej Podlaskiej
        '538',  # Urząd Skarbowy w Radzyniu Podlaskim
        '539',  # Urząd Skarbowy w Parczewie
        '541',  # Filia US w Białej Podlaskiej/Łosice
        '542',  # Pierwszy Urząd Skarbowy w Białymstoku
        '543',  # Urząd Skarbowy w Bielsku Podlaskim
        '544',  # Urząd Skarbowy w Siemiatyczach
        '545',  # Urząd Skarbowy w Sokółce
        '546',  # Urząd Skarbowy w Mońkach
        '547',  # Pierwszy Urząd Skarbowy w Bielsku-Białej
        '548',  # Urząd Skarbowy w Cieszynie
        '549',  # Urząd Skarbowy w Oświęcimiu
        '551',  # Urząd Skarbowy w Wadowicach
        '552',  # Urząd Skarbowy w Suchej Beskidzkiej
        '553',  # Urząd Skarbowy w Żywcu
        '554',  # Pierwszy Urząd Skarbowy w Bydgoszczy
        '555',  # Urząd Skarbowy w Chojnicach
        '556',  # Urząd Skarbowy w Inowrocławiu
        '557',  # Urząd Skarbowy w Mogilnie
        '558',  # Urząd Skarbowy w Nakle nad Notecią
        '559',  # Urząd Skarbowy w Świeciu
        '561',  # Urząd Skarbowy w Tucholi
        '562',  # Urząd Skarbowy w Żninie
        '563',  # Urząd Skarbowy w Chełmie
        '564',  # Urząd Skarbowy w Krasnymstawie
        '565',  # Urząd Skarbowy we Włodawie
        '566',  # Urząd Skarbowy w Ciechanowie
        '567',  # Urząd Skarbowy w Płońsku
        '568',  # Urząd Skarbowy w Pułtusku
        '569',  # Urząd Skarbowy w Mławie
        '571',  # Urząd Skarbowy w Działdowie
        '572',  # Filia US w Mławie/Żuromin
        '573',  # Pierwszy Urząd Skarbowy w Częstochowie
        '574',  # Urząd Skarbowy w Kłobucku
        '575',  # Urząd Skarbowy w Lublińcu
        '576',  # Urząd Skarbowy w Oleśnie
        '577',  # Urząd Skarbowy w Myszkowie
        '578',  # Urząd Skarbowy w Elblągu
        '579',  # Urząd Skarbowy w Malborku
        '581',  # Urząd Skarbowy w Kwidzynie
        '582',  # Urząd Skarbowy w Braniewie
        '583',  # Pierwszy Urząd Skarbowy w Gdańsku
        '584',  # Drugi Urząd Skarbowy w Gdańsku
        '585',  # Urząd Skarbowy w Sopocie
        '586',  # Pierwszy Urząd Skarbowy w Gdyni
        '587',  # Urząd Skarbowy w Pucku
        '588',  # Urząd Skarbowy w Wejherowie
        '589',  # Urząd Skarbowy w Kartuzach
        '591',  # Urząd Skarbowy w Kościerzynie
        '592',  # Urząd Skarbowy w Starogardzie Gdańskim
        '593',  # Urząd Skarbowy w Tczewie
        '594',  # Urząd Skarbowy w Choszcznie
        '595',  # Urząd Skarbowy w Międzychodzie
        '596',  # Urząd Skarbowy w Międzyrzeczu
        '597',  # Urząd Skarbowy w Myśliborzu
        '598',  # Urząd Skarbowy w Słubicach
        '599',  # Urząd Skarbowy w Gorzowie Wielkopolskim
        '601',  # Urząd Skarbowy w Przysusze
        '602',  # Urząd Skarbowy w Nisku
        '603',  # Urząd Skarbowy w Hajnówce
        '604',  # Urząd Skarbowy w Pruszczu Gdańskim
        '605',  # Urząd Skarbowy w Kazimierzy Wielkiej
        '606',  # Urząd Skarbowy w Obornikach
        '607',  # Urząd Skarbowy w Chodzieży
        '608',  # Urząd Skarbowy w Pleszewie
        '609',  # Urząd Skarbowy we Włoszczowie
        '611',  # Urząd Skarbowy w Jeleniej-Górze
        '612',  # Urząd Skarbowy w Bolesławcu
        '613',  # Urząd Skarbowy w Lubaniu
        '614',  # Urząd Skarbowy w Kamiennej-Górze
        '615',  # Urząd Skarbowy w Zgorzelcu
        '616',  # Urząd Skarbowy w Lwówku ŚLąskim
        '617',  # Urząd Skarbowy w Jarocinie
        '618',  # Pierwszy Urząd Skarbowy w Kaliszu
        '619',  # Urząd Skarbowy w Kępnie
        '621',  # Urząd Skarbowy w Krotoszynie
        '622',  # Urząd Skarbowy w Ostrowie Wielkopolskim
        '623',  # Urząd Skarbowy w Piekarach Śląskich
        '624',  # Drugi Urząd Skarbowy w Koszalinie
        '625',  # Urząd Skarbowy w Będzinie
        '626',  # Urząd Skarbowy w Bytomiu
        '627',  # Urząd Skarbowy w Chorzowie
        '628',  # Urząd Skarbowy w Chrzanowie
        '629',  # Urząd Skarbowy w Dąbrowie Górniczej
        '631',  # Pierwszy Urząd Skarbowy w Gliwicach
        '632',  # Urząd Skarbowy w Jaworznie
        '633',  # Urząd Skarbowy w Jastrzębiu-Zdroju
        '634',  # Pierwszy Urząd Skarbowy w Katowicach
        '635',  # Urząd Skarbowy w Mikołowie
        '636',  # Urząd Skarbowy w Mysłowicach
        '637',  # Urząd Skarbowy w Olkuszu
        '638',  # Urząd Skarbowy w Pszczynie
        '639',  # Urząd Skarbowy w Raciborzu
        '641',  # Urząd Skarbowy w Rudzie Śląskiej
        '642',  # Urząd Skarbowy w Rybniku
        '643',  # Urząd Skarbowy w Siemianowicach Śląskich
        '644',  # Urząd Skarbowy w Sosnowcu
        '645',  # Urząd Skarbowy w Tarnowskich Górach
        '646',  # Urząd Skarbowy w Tychach
        '647',  # Urząd Skarbowy w Wodzisławiu Śląskim
        '648',  # Urząd Skarbowy w Zabrzu
        '649',  # Urząd Skarbowy w Zawierciu
        '651',  # Urząd Skarbowy w Żorach
        '652',  # Urząd Skarbowy w Czechowicach Dziedzicach
        '653',  # Urząd Skarbowy Tarnowskie Góry filia Piekary Śląskie
        '654',  # Filia US w Będzinie/Czeladź
        '655',  # Urząd Skarbowy w Busku-Zdroju
        '656',  # Urząd Skarbowy w Jędrzejowie
        '657',  # Pierwszy Urząd Skarbowy w Kielcach
        '658',  # Urząd Skarbowy w Końskich
        '659',  # Urząd Skarbowy w Miechowie
        '661',  # Urząd Skarbowy w Ostrowcu Świętokrzyskim
        '662',  # Urząd Skarbowy w Pińczowie
        '663',  # Urząd Skarbowy w Skarżysku Kamiennej
        '664',  # Urząd Skarbowy w Starachowicach
        '665',  # Urząd Skarbowy w Koninie
        '666',  # Urząd Skarbowy w Kole
        '667',  # Urząd Skarbowy w Słupcy
        '668',  # Urząd Skarbowy w Turku
        '669',  # Pierwszy Urząd Skarbowy w Koszalinie
        '671',  # Urząd Skarbowy w Kołobrzegu
        '672',  # Urząd Skarbowy w Białogardzie
        '673',  # Urząd Skarbowy w Szczecinku
        '674',  # Urząd Skarbowy w Drawsku Pomorskim
        '675',  # Urząd Skarbowy Kraków-Śródmieście
        '676',  # Urząd Skarbowy Kraków-Stare Miasto
        '677',  # Urząd Skarbowy Kraków-Krowodrza
        '678',  # Urząd Skarbowy Kraków-Nowa Huta
        '679',  # Urząd Skarbowy Kraków-Podgórze
        '681',  # Urząd Skarbowy w Myślenicach
        '682',  # Urząd Skarbowy w Proszowicach
        '683',  # Urząd Skarbowy w Wieliczce
        '684',  # Urząd Skarbowy w Krośnie
        '685',  # Urząd Skarbowy w Jaśle
        '686',  # Urząd Skarbowy w Brzozowie
        '687',  # Urząd Skarbowy w Sanoku
        '688',  # Urząd Skarbowy w Lesku
        '689',  # Urząd Skarbowy w Ustrzykach Dolnych
        '691',  # Urząd Skarbowy w Legnicy
        '692',  # Urząd Skarbowy w Lubinie
        '693',  # Urząd Skarbowy w Głogowie
        '694',  # Urząd Skarbowy w Złotoryi
        '695',  # Urząd Skarbowy w Jaworze
        '696',  # Urząd Skarbowy w Gostyniu
        '697',  # Urząd Skarbowy w Lesznie
        '698',  # Urząd Skarbowy w Kościanie
        '699',  # Urząd Skarbowy w Rawiczu
        '701',  # Trzeci Urząd Skarbowy Warszawa-Śródmieście
        '711',  # Urząd Skarbowy w Lesznie
        '712',  # Pierwszy Urząd Skarbowy w Lublinie
        '713',  # Drugi Urząd Skarbowy w Lublinie
        '714',  # Urząd Skarbowy w Lubartowie
        '715',  # Urząd Skarbowy w Kraśniku
        '716',  # Urząd Skarbowy w Puławach
        '717',  # Urząd Skarbowy w Opolu Lubelskim
        '718',  # Urząd Skarbowy w Łomży
        '719',  # Urząd Skarbowy w Grajewie
        '721',  # Urząd Skarbowy w Kolnie
        '722',  # Urząd Skarbowy w Wysokiem Mazowieckiem
        '723',  # Urząd Skarbowy w Zambrowie
        '724',  # Pierwszy Urząd Skarbowy Łódź-Śródmieście
        '725',  # Urząd Skarbowy Łódź-Śródmieście
        '726',  # Pierwszy Urząd Skarbowy Łódź-Bałuty
        '727',  # Urząd Skarbowy Łódź-Polesie
        '728',  # Urząd Skarbowy Łódź-Widzew
        '729',  # Pierwszy Urząd Skarbowy Łódź-Górna
        '731',  # Urząd Skarbowy w Pabianicach
        '732',  # Urząd Skarbowy w Zgierzu
        '733',  # Urząd Skarbowy w Głownie
        '734',  # Urząd Skarbowy w Nowym Sączu
        '735',  # Urząd Skarbowy w Nowym Targu
        '736',  # Urząd Skarbowy w Zakopanem
        '737',  # Urząd Skarbowy w Limanowej
        '738',  # Urząd Skarbowy w Gorlicach
        '739',  # Urząd Skarbowy w Olsztynie
        '741',  # Urząd Skarbowy w Ostródzie
        '742',  # Urząd Skarbowy w Kętrzynie
        '743',  # Urząd Skarbowy w Bartoszycach
        '744',  # Urząd Skarbowy w Iławie
        '745',  # Urząd Skarbowy w Szczytnie
        '746',  # Filia US w Szczytnie/Nidzica
        '747',  # Urząd Skarbowy w Brzegu
        '748',  # Urząd Skarbowy w Głubczycach
        '749',  # Urząd Skarbowy w Kędzierzynie-Koźlu
        '751',  # Urząd Skarbowy w Kluczborku
        '752',  # Urząd Skarbowy w Namysłowie
        '753',  # Urząd Skarbowy w Nysie
        '754',  # Pierwszy Urząd Skarbowy w Opolu
        '755',  # Urząd Skarbowy w Prudniku
        '756',  # Urząd Skarbowy w Strzelcach Opolskich
        '757',  # Urząd Skarbowy w Makowie Mazowieckim
        '758',  # Urząd Skarbowy w Ostrołęce
        '759',  # Urząd Skarbowy w Ostrowi Mazowieckiej
        '761',  # Urząd Skarbowy w Przasnyszu
        '762',  # Urząd Skarbowy w Wyszkowie
        '763',  # Urząd Skarbowy w Czarnkowie
        '764',  # Urząd Skarbowy w Pile
        '765',  # Urząd Skarbowy w Wałczu
        '766',  # Urząd Skarbowy w Wągrowcu
        '767',  # Urząd Skarbowy w Złotowie
        '768',  # Urząd Skarbowy w Opocznie
        '769',  # Urząd Skarbowy w Bełchatowie
        '771',  # Urząd Skarbowy w Piotrkowie Trybunalskim
        '772',  # Urząd Skarbowy w Radomsku
        '773',  # Urząd Skarbowy w Tomaszowie Mazowieckim
        '774',  # Urząd Skarbowy w Płocku
        '775',  # Urząd Skarbowy w Kutnie
        '776',  # Urząd Skarbowy w Sierpcu
        '777',  # Pierwszy Urząd Skarbowy Poznań
        '778',  # Urząd Skarbowy Poznań-Śródmieście
        '779',  # Urząd Skarbowy Poznań-Grunwald
        '781',  # Urząd Skarbowy Poznań-Jeżyce
        '782',  # Urząd Skarbowy Poznań-Nowe Miasto
        '783',  # Urząd Skarbowy Poznań-Wilda
        '784',  # Urząd Skarbowy w Gnieźnie
        '785',  # Urząd Skarbowy w Śremie
        '786',  # Urząd Skarbowy w Środzie Wielkopolskiej
        '787',  # Urząd Skarbowy w Szamotułach
        '788',  # Urząd Skarbowy w Nowym Tomyślu
        '789',  # Urząd Skarbowy we Wrześni
        '791',  # Filia US w Nowym Tomyślu/Grodzisk Wlkp.
        '792',  # Urząd Skarbowy w Jarosławiu
        '793',  # Urząd Skarbowy w Lubaczowie
        '794',  # Urząd Skarbowy w Przeworsku
        '795',  # Urząd Skarbowy w Przemyślu
        '796',  # Pierwszy Urząd Skarbowy w Radomiu
        '797',  # Urząd Skarbowy w Grójcu
        '798',  # Urząd Skarbowy w Białobrzegach
        '799',  # Urząd Skarbowy w Szydłowcu
        '811',  # Urząd Skarbowy w Zwoleniu
        '812',  # Urząd Skarbowy w Kozienicach
        '813',  # Urząd Skarbowy w Rzeszowie
        '814',  # Urząd Skarbowy w Kolbuszowej
        '815',  # Urząd Skarbowy w Łańcucie
        '816',  # Urząd Skarbowy w Leżajsku
        '817',  # Urząd Skarbowy w Mielcu
        '818',  # Urząd Skarbowy w Ropczycach
        '819',  # Urząd Skarbowy w Strzyżowie
        '821',  # Urząd Skarbowy w Siedlcach
        '822',  # Urząd Skarbowy w Mińsku Mazowieckim
        '823',  # Urząd Skarbowy w Sokołowie Podlaskim
        '824',  # Urząd Skarbowy w Węgrowie
        '825',  # Urząd Skarbowy w Łukowie
        '826',  # Urząd Skarbowy w Garwolinie
        '827',  # Urząd Skarbowy w Sieradzu
        '828',  # Urząd Skarbowy w Poddębicach
        '829',  # Urząd Skarbowy w Zduńskiej Woli
        '831',  # Urząd Skarbowy w Łasku
        '832',  # Urząd Skarbowy w Wieluniu
        '833',  # Urząd Skarbowy w Brzezinach
        '834',  # Urząd Skarbowy w Łowiczu
        '835',  # Urząd Skarbowy w Rawie Mazowieckiej
        '836',  # Urząd Skarbowy w Skierniewicach
        '837',  # Urząd Skarbowy w Sochaczewie
        '838',  # Urząd Skarbowy w Żyrardowie
        '839',  # Urząd Skarbowy w Słupsku
        '841',  # Urząd Skarbowy w Lęborku
        '842',  # Urząd Skarbowy w Bytowie
        '843',  # Urząd Skarbowy w Człuchowie
        '844',  # Urząd Skarbowy w Suwałkach
        '845',  # Urząd Skarbowy w Giżycku
        '846',  # Urząd Skarbowy w Augustowie
        '847',  # Urząd Skarbowy w Olecku
        '848',  # Urząd Skarbowy w Ełku
        '849',  # Urząd Skarbowy w Piszu
        '851',  # Pierwszy Urząd Skarbowy w Szczecinie
        '852',  # Drugi Urząd Skarbowy w Szczecinie
        '853',  # Urząd Skarbowy w Pyrzycach
        '854',  # Urząd Skarbowy w Starogardzie Szczecińskim
        '855',  # Urząd Skarbowy w Świnoujściu
        '856',  # Urząd Skarbowy w Goleniowie
        '857',  # Urząd Skarbowy w Gryficach
        '858',  # Urząd Skarbowy w Gryfinie
        '859',  # Filia US w Goleniowie/Nowogard
        '861',  # Filia US w Gryficach/Kamień Pom.
        '862',  # Urząd Skarbowy w Janowie Lubelskim
        '863',  # Urząd Skarbowy w Opatowie
        '864',  # Urząd Skarbowy w Sandomierzu
        '865',  # Urząd Skarbowy w Stalowej Woli
        '866',  # Urząd Skarbowy w Staszowie
        '867',  # Urząd Skarbowy w Tarnobrzegu
        '868',  # Urząd Skarbowy w Bochni
        '869',  # Urząd Skarbowy w Brzesku
        '871',  # Urząd Skarbowy w Dąbrowie Tarnowskiej
        '872',  # Urząd Skarbowy w Dębicy
        '873',  # Pierwszy Urząd Skarbowy w Tarnowie
        '874',  # Urząd Skarbowy w Brodnicy
        '875',  # Urząd Skarbowy w Chełmnie
        '876',  # Urząd Skarbowy w Grudziądzu
        '877',  # Urząd Skarbowy w Nowym Mieście Lubawskim
        '878',  # Urząd Skarbowy w Wąbrzeźnie
        '879',  # Drugi Urząd Skarbowy w Toruniu
        '881',  # Urząd Skarbowy w Bystrzycy Kłodzkiej
        '882',  # Urząd Skarbowy w Dzierżoniowie
        '883',  # Urząd Skarbowy w Kłodzku
        '884',  # Urząd Skarbowy w Świdnicy
        '885',  # Urząd Skarbowy w Nowej Rudzie
        '886',  # Urząd Skarbowy w Wałbrzychu
        '887',  # Urząd Skarbowy w Ząbkowicach Śląskich
        '888',  # Urząd Skarbowy w Włocławku
        '889',  # Urząd Skarbowy w Radziejowie
        '891',  # Urząd Skarbowy w Aleksandrowie Kujawskim
        '892',  # Urząd Skarbowy w Rypinie
        '893',  # Urząd Skarbowy w Lipnie
        '894',  # Urząd Skarbowy Wrocław-Fabryczna
        '895',  # Urząd Skarbowy Wrocław-Psie Pole
        '896',  # Pierwszy Urząd Skarbowy we Wrocławiu
        '897',  # Urząd Skarbowy Wrocław-Stare Miasto
        '898',  # Drugi Urząd Skarbowy Wrocław-Śródmieście
        '899',  # Urząd Skarbowy Wrocław-Krzyki
        '911',  # Urząd Skarbowy w Oleśnicy
        '912',  # Urząd Skarbowy w Oławie
        '913',  # Urząd Skarbowy w Środzie Wielkopolskiej
        '914',  # Urząd Skarbowy w Strzelnie
        '915',  # Urząd Skarbowy w Trzebnicy
        '916',  # Urząd Skarbowy w Miliczu
        '917',  # Filia US w Trzebnicy/Wołów
        '918',  # Urząd Skarbowy w Biłgoraju
        '919',  # Urząd Skarbowy w Hrubieszowie
        '921',  # Urząd Skarbowy w Tomaszowie Lubelskim
        '922',  # Urząd Skarbowy w Zamościu
        '923',  # Urząd Skarbowy w Wolsztynie
        '924',  # Urząd Skarbowy w Żaganiu
        '925',  # Urząd Skarbowy w Nowej Soli
        '926',  # Urząd Skarbowy w Krośnie Odrzańskim
        '927',  # Urząd Skarbowy w Świebodzinie
        '928',  # Urząd Skarbowy w Żarach
        '929',  # Pierwszy Urząd Skarbowy w Zielonej Górze
        '931',  # Urząd Skarbowy Warszawa-Ursynów
        '932',  # Urząd Skarbowy Warszawa-Wawer
        '933',  # Drugi Urząd Skarbowy w Bydgoszczy
        '934',  # Drugi Urząd Skarbowy w Katowicach
        '935',  # Trzeci Urząd Skarbowy w Szczecinie
        '936',  # Pierwszy Urząd Skarbowy w Toruniu
        '937',  # Drugi Urząd Skarbowy w Bielsku-Białej
        '938',  # Drugi Urząd Skarbowy w Bielsku-Białej
        '939',  # Drugi Urząd Skarbowy w Częstochowie
        '941',  # Trzeci Urząd Skarbowy w Gdańsku
        '942',  # Drugi Urząd Skarbowy w Gdyni
        '943',  # Drugi Urząd Skarbowy w Kielcach
        '944',  # Urząd Skarbowy Kraków-Dębniki
        '945',  # Urząd Skarbowy Kraków-Prądnik
        '946',  # Trzeci Urząd Skarbowy w Lublinie
        '947',  # Drugi Urząd Skarbowy Łódź-Bałuty
        '948',  # Drugi Urząd Skarbowy w Radomiu
        '949',  # Drugi Urząd Skarbowy w Częstochowie
        '951',  # Urząd Skarbowy Warszawa-Ursynów
        '952',  # Urząd Skarbowy Warszawa-Wawer
        '953',  # Drugi Urząd Skarbowy w Bydgoszczy
        '954',  # Drugi Urząd Skarbowy w Katowicach
        '955',  # Trzeci Urząd Skarbowy w Szczecinie
        '956',  # Pierwszy Urząd Skarbowy w Toruniu
        '957',  # Trzeci Urząd Skarbowy w Gdańsku
        '958',  # Drugi Urząd Skarbowy w Gdyni
        '959',  # Drugi Urząd Skarbowy w Kielcach
        '961',  # Urząd Skarbowy Kraków-Dębniki
        '962',  # Urząd Skarbowy Kraków-Prądnik
        '963',  # Trzeci Urząd Skarbowy w Lublinie
        '964',  # Drugi Urząd Skarbowy Łódź-Bałuty
        '965',  # Drugi Urząd Skarbowy w Radomiu
        '966',  # Drugi Urząd Skarbowy w Białymstoku
        '967',  # Trzeci Urząd Skarbowy w Bydgoszczy
        '968',  # Drugi Urząd Skarbowy w Kaliszu
        '969',  # Drugi Urząd Skarbowy w Gliwicach
        '971',  # Urząd Skarbowy w Gostyninie
        '972',  # Urząd Skarbowy Poznań-Winogrady
        '973',  # Drugi Urząd Skarbowy w Zielonej-Górze
        '974',  # Drugi Urząd Skarbowy w Białymstoku
        '975',  # Trzeci Urząd Skarbowy w Bydgoszczy
        '976',  # Drugi Urząd Skarbowy w Bydgoszczy
        '977',  # Drugi Urząd Skarbowy w Gliwicach
        '978',  # Urząd Skarbowy w Gostyninie
        '979',  # Urząd Skarbowy Poznań-Winogrady
        '981',  # Drugi Urząd Skarbowy w Zielonej Górze
        '982',  # Drugi Urząd Skarbowy Łódź-Górna
        '983',  # Drugi Urząd Skarbowy Łódź-Górna
        '984',  # Urząd Skarbowy w Nidzicy
        '985',  # Urząd Skarbowy w Nidzicy
        '986',  # Urząd Skarbowy w Kamieniu Pomorskim
        '987',  # Urząd Skarbowy w Kamieniu Pomorskim
        '988',  # Urząd Skarbowy w Wołowie
        '989',  # Urząd Skarbowy w Wołowie
        '991',  # Drugi Urząd Skarbowy w Opolu
        '992',  # Drugi Urząd Skarbowy w Opolu
        '993',  # Drugi Urząd Skarbowy w Tarnowie
        '994',  # Drugi Urząd Skarbowy w Tarnowie
        '995',  # Urząd Skarbowy w Grodzisku Wielkopolskim
        '996',  # Urząd Skarbowy w Grodzisku Wielkopolskim
        '997',  # Urząd Skarbowy Wieluń lokalizacja w Wieruszowie
        '998',  # Urząd Skarbowy Wieluń lokalizacja w Wieruszowie
    )

    def nip(self):
        """
        Returns 10 digit of Number of tax identification.
        Polish: Numer identyfikacji podatkowej (NIP).

        https://pl.wikipedia.org/wiki/NIP
        """

        nip = [int(i) for i in self.random_choices(self.tax_office_codes, 1)[0]]
        for _ in range(6):
            nip.append(self.random_digit())

        weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(nip, weights)) % 11

        if check_sum % 11 == 10:
            position = self.random_int(3, 8)
            if nip[position] < 9:
                nip[position] = (nip[position] + 1) % 10
                nip.append((check_sum + weights[position]) % 11)
            else:
                nip[position] = (nip[position] - 1) % 10
                nip.append((check_sum - weights[position]) % 11)

        else:
            nip.append(check_sum % 11)

        return ''.join(str(character) for character in nip)
