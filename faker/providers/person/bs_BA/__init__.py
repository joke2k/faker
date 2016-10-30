# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    """
    The names used here are the top 100 names released by the Federal statistics 
    institute in Bosnia and Herzegovina, available from demography section at  
    http://fzs.ba/index.php/statisticke-oblasti/stanovnistvo-i-drustvene-statistike/stanovnistvo-i-registar/
    male: http://fzs.ba/wp-content/uploads/2018/05/100-najčešćih-muških-imena-dodjeljivanih-djeci-rođenoj-u-2017.pdf
    female: http://fzs.ba/wp-content/uploads/2018/05/100-najčešćih-ženskih-imena-dodjeljivanih-djeci-rođenoj-u-2017.pdf
    """

    formats = ["{{first_name}} {{last_name}}"]

    first_names_male = [
        "Abdulah", "Adem", "Adi", "Adian", "Adijan", "Adin", "Adnan", "Afan",
        "Ahmed", "Ajdin", "Ajlan", "Ajnur", "Aldin", "Alem", "Ali", "Almin",
        "Amar", "Amel", "Amer", "Ammar", "Andrej", "Anes", "Ante", "Anur",
        "Arian", "Arman", "Armin", "Arslan", "Azur", "Benjamin", "Bilal",
        "Damir", "Dani", "Danin", "Danis", "Daris", "David", "Davud", "Demir",
        "Din", "Dino", "Džan", "Džanan", "Dženan", "Edin", "Eldar", "Eldin",
        "Elmin", "Eman", "Emil", "Emin", "Emir", "Emrah", "Ensar", "Ermin",
        "Faris", "Faruk", "Fatih", "Filip", "Hamza", "Haris", "Harun",
        "Ibrahim", "Ilhan", "Imran", "Isak", "Ishak", "Ismail", "Ismar",
        "Ivan", "Jakov", "Josip", "Jusuf", "Kan", "Kenan", "Kerim", "Leon",
        "Luka", "Mahir", "Maid", "Mak", "Malik", "Marko", "Matej", "Mateo",
        "Mihael", "Mirza", "Muhamed", "Mustafa", "Nedim", "Nikola", "Omar",
        "Omer", "Petar", "Rejjan", "Rijad", "Tarik", "Vedad", "Zejd",
    ]

    first_names_female = [
        "Adna", "Aida", "Aiša", "Ajla", "Ajlin", "Ajna", "Ajša", "Alejna",
        "Alina", "Amila", "Amina", "Amna", "Amra", "Ana", "Anđela", "Anesa",
        "Anida", "Asija", "Asja", "Aylin", "Azra", "Belma", "Berina", "Dalal",
        "Dalia", "Dalija", "Dalila", "Dunja", "Džana", "Džejla", "Džejna",
        "Ejna", "Ela", "Elena", "Ella", "Elma", "Ema", "Emina", "Emma", "Ena",
        "Erna", "Esma", "Eva", "Farah", "Fatima", "Hana", "Hanna", "Ilhana",
        "Ilma", "Iman", "Iva", "Jasmina", "Klara", "Lajla", "Lamija", "Lana",
        "Lara", "Laura", "Lea", "Lejla", "Lejna", "Lena", "Lucija", "Majra",
        "Marija", "Marta", "Matea", "Medina", "Melina", "Merjem", "Merjema",
        "Mia", "Nađa", "Nadija", "Nadja", "Nahla", "Naida", "Najla", "Nedžla",
        "Nejla", "Nejra", "Nika", "Nora", "Nur", "Petra", "Rita", "Sajra",
        "Sara", "Sarah", "Šejla", "Selma", "Sumeja", "Tajra", "Uma", "Una",
        "Zana", "Zara", "Zejneb", "Zerina",
    ]

    first_names = first_names_female + first_names_male
    """
    Last names were taken from Wikipedia Category listing about bosnian surnames
    https://en.wikipedia.org/wiki/Category:Bosnian-language_surnames
    """
    last_names = ["Abadžić", "Ademović", "Adilović", "Aganović", "Ahmetović",
        "Ahmić", "Alečković", "Alibegović", "Alić", "Alihodžić", "Alikadić",
        "Alispahić", "Alomerović", "Amidžić", "Arnautović", "Avdić", "Babić",
        "Bajraktarević", "Bajramović", "Balašević", "Baljić", "Bašić",
        "Bećirović", "Bećirspahić", "Beganović", "Begić", "Begović", "Bekić",
        "Bekrić", "Berović", "Bešić", "Bešlagić", "Bičakčić", "Bilbi", "Bolić",
        "Bosnić", "Bradarić", "Brkić", "Brković", "Brunčević", "Bukvić",
        "Buljubašić", "Burić", "Ćatić", "Čaušević", "Čejv", "Čelebić", "Čengić",
        "Cerić", "Čorbadžić", "Ćosić", "Delić", "Demirović", "Divj",
        "Dizdarević", "Đumić", "Đurasović", "Dod", "Dragović", "Dugalić",
        "Džaferović", "Džeko", "Džumh", "Ekmečić", "Fatić", "Fazlić",
        "Ferhatović", "Galijašević", "Gatarić", "Gorčić", "Graov", "Gude",
        "Hadžiabdić", "Hadžibegić", "Hadžić", "Hadžihalilović",
        "Hadžiosmanović", "Hajradinović", "Hajrović", "Halilhodžić",
        "Halilović", "Handanović", "Haračić", "Hasagić", "Hasanagić",
        "Hasanbegović", "Hasanović", "Hodžić", "Hukić", "Ibišević",
        "Ibrahimović", "Ignjatić", "Imamović", "Isaković", "Izetbegović",
        "Jahić", "Jakupović", "Jašić", "Jugić", "Junuzović", "Kalajdžić",
        "Kapetanović", "Kapić", "Kariš", "Kecmanović", "Kod", "Kolašin",
        "Koljić", "Komšić", "Kopan", "Korom", "Košar", "Kovač", "Krunić",
        "Kulenović", "Kurj", "Kurtćehajić", "Kusturi", "Lulić", "Mahmulj",
        "Majstorović", "Mandić", "Marjanović", "Mećava", "Medunjan",
        "Mehmedbašić", "Mehmedović", "Memić", "Mena", "Mešanović", "Mešić",
        "Mišić", "Muhić", "Mujić", "Mulić", "Muratović", "Musemić", "Mušović",
        "Mustafić", "Mutapčić", "Muzaferi", "Muzurović", "Nadarević", "Nikić",
        "Nišić", "Pačar", "Pašalić", "Pjanić", "Plakalović", "Predojević",
        "Preldžić", "Rahimić", "Rakić", "Rastod", "Sadiković", "Salatić",
        "Salihović", "Salkić", "Saračević", "Sarajlić", "Šarić", "Šećerović",
        "Seferović", "Šehić", "Selimović", "Šetkić", "Sidr", "Sijerčić",
        "Šimunović", "Šišić", "Skenderović", "Smajić", "Smajlović", "Sokolović",
        "Suljić", "Sušić", "Tahirović", "Tanković", "Terzić", "Tinjić",
        "Topalović", "Topčagić", "Toskić", "Turković", "Varešanović", "Velagić",
        "Vidić", "Vučkić", "Vugdalić", "Vuković", "Zahirović", "Zakarić",
        "Zukanović", 
    ]
