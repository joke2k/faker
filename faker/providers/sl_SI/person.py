# coding=utf-8
from __future__ import unicode_literals
from ..person import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ['{{first_name}} {{last_name}}', ]

    first_names_male = [
        "Franc", "Janez", "Anton", 
        "Ivan", "Jožef", "Andrej", "Marko", "Jože", "Marjan", 
        "Peter", "Milan", "Stanislav", "Matej", "Tomaž", "Branko", 
        "Aleš", "Bojan", "Robert", "Boštjan", "Matjaž", "Gregor", 
        "Luka", "Martin", "Alojz", "Rok", "Boris", "Dušan", "Igor", 
        "Miha", "Dejan", "David", "Uroš", "Mitja", "Simon", "Jure", 
        "Blaž", "Štefan", "Jan", "Drago", "Darko", "Klemen", "Primož", 
        "Nejc", "Žiga", "Jernej", "Miran", "Aleksander", "Roman", 
        "Vladimir", "Denis", "Matic", "Tadej", "Srečko", "Slavko", 
        "Mirko", "Janko", "Žan", "Gašper", "Miroslav", "Borut", "Alojzij", 
        "Damjan", "Stanko", "Aljaž", "Anže", "Zoran", "Danijel", "Mihael", 
        "Matija", "Jaka", "Marijan", "Rudolf", "Alen", "Vinko", "Jakob", 
        "Viktor", "Domen", "Sašo", "Iztok", "Goran", "Tilen", "Jurij", 
        "Pavel", "Zvonko", "Edvard", "Zdravko", "Danilo", "Matevž", "Rajko", 
        "Andraž", "Ludvik", "Zlatko", "Frančišek", "Bogdan", "Gorazd", "Samo", 
        "Leon", "Urban", "Dragan", "Emil", "Josip", "Nik", "Ciril", "Sandi", 
        "Benjamin", "Vid", "Vojko", "Albin", "Franci", "Sebastjan", "Silvo", 
        "Leopold", "Kristjan", "Tim", "Božidar", "Filip", "Damijan", "Erik", 
        "Viljem", "Vincenc", "Željko", "Damir", "Silvester", "Aljoša", "Karel", 
        "Daniel", "Dominik", "Miloš", "Stojan", "Tomislav", "Franjo", "Valentin", 
        "Davorin", "Maks", "Timotej", "Ladislav", "Niko", "Mario", "Mark", "Nikola", 
        "Bogomir", "Saša", "Vlado", "Karl", "Zdenko", "Mladen", "Grega", "Stjepan", 
        "Davor", "Kristijan", "Ernest", "Maksimiljan", "Patrik", "Avgust", "Sebastijan",
        "Aleksandar", "Lovro", "Ivo", "Rado", "Tine", "Ignac", "Adolf", 
        "Gal", "Valter", "Elvis", "Jasmin", "Ervin", "Jani", "Izidor", 
        "Ferdinand", "Nenad", "Anej", "Petar", "Maj", "Metod", "Albert", 
        "Bruno", "Radovan", "Renato", "Nikolaj", "Feliks", "Karol", 
        "Bernard", "Joško", "Rafael", "Edin", "Marcel", "Aleks", "Cvetko", 
        "Rudi", "Miro", "Hasan", "Slobodan", "Mirsad", "Senad", "Dragutin", 
        "Nino", "Sergej", "Božo", "Milorad"]

    first_names_female = [
        "Marija", "Ana", "Irena", "Maja", "Mojca", "Jožefa", 
        "Mateja", "Frančiška", "Nataša", "Jožica", "Barbara", 
        "Ivana", "Andreja", "Nina", "Petra", "Terezija", "Katja", 
        "Sonja", "Milena", "Katarina", "Tatjana", "Anja", "Alenka",
        "Majda", "Tanja", "Martina", "Vesna", "Tina", "Angela", 
        "Urška", "Antonija", "Helena", "Anica", "Kristina", 
        "Dragica", "Nada", "Olga", "Špela", "Darja", "Danica", 
        "Marjeta", "Tjaša", "Eva", "Ljudmila", "Simona", "Vida", 
        "Sara", "Ivanka", "Zdenka", "Alojzija", "Lidija", "Suzana", 
        "Marta", "Nika", "Sabina", "Janja", "Silva", "Veronika", 
        "Štefanija", "Stanislava", "Darinka", "Karmen", "Elizabeta", 
        "Neža", "Brigita", "Anita", "Aleksandra", "Pavla", "Cvetka", 
        "Metka", "Jana", "Nevenka", "Monika", "Rozalija", "Natalija", 
        "Slavica", "Marjana", "Renata", "Branka", "Jasmina", "Vera", 
        "Ema", "Saša", "Maša", "Lara", "Lucija", "Lea", "Tamara", "Bernarda", 
        "Danijela", "Klavdija", "Erika", "Romana", "Bojana", "Mira", "Jasna", 
        "Klara", "Kaja", "Jelka", "Polona", "Julijana", "Mirjana", 
        "Valerija", "Sandra", "Matilda", "Tadeja", "Valentina", 
        "Mihaela", "Ida", "Amalija", "Albina", "Breda", "Karolina", 
        "Sanja", "Teja", "Ines", "Gabrijela", "Zofija", "Ksenija", 
        "Laura", "Cecilija", "Patricija", "Magdalena", "Zala", "Manca", 
        "Viktorija", "Maruša", "Vanja", "Vlasta", "Justina", "Nuša", 
        "Marjetka", "Emilija", "Melita", "Ljubica", "Lana", "Marica", 
        "Gordana", "Marinka", "Marina", "Polonca", "Nadja", "Milka", 
        "Živa", "Urša", "Damjana", "Hana", "Doroteja", "Tea", "Marijana", 
        "Julija", "Ajda", "Nastja", "Milica", "Alja", "Karin", "Štefka", 
        "Slavka", "Jerneja", "Nives", "Dušanka", "Andrejka", "Ana Marija", 
        "Irma", "Pia", "Jelena", "Marjanca", "Miroslava", "Lilijana", 
        "Stanka", "Zlatka", "Mirjam", "Neja", "Jolanda", "Zora", 
        "Zvonka", "Hermina", "Rebeka", "Ivica", "Hedvika", "Blanka", 
        "Larisa", "Erna", "Anka", "Roza", "Liljana", "Vilma", "Magda", 
        "Daniela", "Jerica", "Taja", "Iris", "Adrijana", "Jadranka", 
        "Silvestra", "Alma", "Anamarija", "Snežana", "Verica", "Daša",
    ]

    last_names = [
        "Novak", "Horvat", "Krajnc", "Kovačič", "Zupančič", 
        "Kovač", "kovač", "Potočnik", "Mlakar", "Vidmar", "Kos", 
        "Golob", "Turk", "Božič", "Kralj", "Zupan", "Korošec", 
        "Bizjak", "Hribar", "Kotnik", "Rozman", 
        "Kavčič", "Petek", "petek", "Kastelic", "Kolar", 
        "Hočevar", "Žagar", "žagar", "Oblak", "Košir", "Koren", 
        "Klemenčič", "Zajc", "Medved", "Knez", "Zupanc", "Petrič", 
        "Pirc", "Hrovat", "Pavlič", "Kuhar", "kuhar", "Lah", 
        "Zorko", "Uršič", "Sever", "Majcen", "Jerman", "Babič", 
        "Tomažič", "Erjavec", "Jereb", "Pušnik", "Kranjc", "Rupnik", 
        "Perko", "Lesjak", "Breznik", "Pečnik", "Pavlin", "Močnik", 
        "Dolenc", "Vidic", "Furlan", "Logar", "Tomšič", "Jenko", 
        "Janežič", "Ribič", "ribič", "Žnidaršič", "Černe", "Maček", 
        "Lešnik", "Fras", "Zadravec", "Marolt", "Jelen", "Gregorič", 
        "Blatnik", "Pintar", "Mihelič", "Hren", "Kokalj", "Bezjak", 
        "Leban", "Cerar", "Čeh", "čeh", "Jug", "Kovačević", "Vidovič", 
        "Rus", "Kobal", "Primožič", "Kocjančič", "Dolinar", "Petrović", 
        "Lazar", "Kolenc", "Nemec", "Kolarič", "Lavrič", "Kodrič", "Kosi", 
        "Bogataj", "Mrak", "Debeljak", "Tavčar", "Žižek", "Krivec", "Zver", 
        "Ivančič", "Likar", "Žibert", "Jarc", "Vodopivec", "Kramberger", 
        "Miklavčič", "Vovk", "Skok", "Toplak", "Petrovič", "Hribernik", 
        "Leskovar", "Stopar", "Jazbec", "Simonič", "Blažič", "Eržen", 
        "Sitar", "Gorenc", "Železnik", "Meglič", "Šinkovec", "Jamnik", 
        "Javornik", "Bukovec", "Hozjan", "Ramšak", "Marković", "Filipič", 
        "Kočevar", "Demšar", "Volk", "volk", "Gomboc", "Podgoršek", 
        "Čuk", "Ilić", "Kokol", "Bregar", "Sušnik", "Pintarič", 
        "Gorjup", "Nikolić", "Jovanović", "Mavrič", "Kramar", "Lebar", 
        "Rutar", "Koželj", "Mohorič", "Popović", "Rajh", "Hodžić", 
        "Rožman", "Resnik", "Šmid", "Kumer", "Gajšek", "Godec", 
        "Bergant", "Pogačnik", "Zemljič", "Hafner", "Tratnik", "Povše", 
        "Rožič", "Cvetko", "Ambrožič", "Bevc", "Mlinarič", "Mlinar", 
        "Kristan", "Jerič", "Kalan", "Markovič", "Šuštar", "Bajc", "Kaučič", 
        "Humar", "Dolinšek", "Zalokar", "Pirnat", "Zorman", "Zakrajšek", 
        "Štrukelj", "Pogačar", "Škof", "Zalar", "Gorišek", "Gruden", 
        "Kranjec", "Trček", "Fekonja" 
    ]

    @classmethod
    def first_name(cls):
        return cls.random_element((cls.first_name_male(), cls.first_name_female()))

    @classmethod
    def first_name_male(cls):
        return cls.random_element(cls.first_names_male)

    @classmethod
    def first_name_female(cls):
        return cls.random_element(cls.first_names_female)

