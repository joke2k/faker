# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    """
    The names used here are the top 100 names released by the Federal statistics institute
    in Bosnia and Herzegovina, available from demography section at  
    http://fzs.ba/index.php/statisticke-oblasti/stanovnistvo-i-drustvene-statistike/stanovnistvo-i-registar/
    male: http://fzs.ba/wp-content/uploads/2018/05/100-najčešćih-muških-imena-dodjeljivanih-djeci-rođenoj-u-2017.pdf
    female: http://fzs.ba/wp-content/uploads/2018/05/100-najčešćih-ženskih-imena-dodjeljivanih-djeci-rođenoj-u-2017.pdf
    """

    formats = ['{{first_name}} {{last_name}}', ]

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
        "Omer", "Petar", "Rejjan", "Rijad", "Tarik", "Vedad", "Zejd"
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
        "Zana", "Zara", "Zejneb", "Zerina"
    ]

    first_names = first_names_female + first_names_male
    """
    Last names were taken from Wikipedia
    """
    last_names = [
        "Abadžić", "Adilović", "Alečković", "Alomerović", "Arnautović",
        "Babić", "Bajraktarević", "Bajramović", "Balašević", "Baljić",
        "Bašić", "Bećirović", "Beganović", "Begović", "Berović", "Bešić",
        "Bešlagić", "Bičakčić", "Bolić", "Bosnić", "Brunčević", "Burić",
        "Čaušević", "Čejvan", "Čengić", "Čorbadžić", "Ćosić", "Delić",
        "Demirović", "Divjak", "Dizdarević", "Dodik", "Dugalić", "Džeko",
        "Edhemović", "Ferhatović", "Galijašević", "Gudelj", "Hadžić",
        "Hadžihalilović", "Handanović", "Hodžić", "Izetbegović",
        "Jašić", "Kapić", "Kolašinac", "Kopanja", "Koroman", "Kovač",
        "Kurjak", "Kurtćehajić", "Kusturica", "Mahmuljin",
        "Majstorović", "Mandić", "Marjanović", "Matković",
        "Mehmedbašić", "Mehmedović", "Mešić", "Muratović",
        "Mutapčić", "Muftić", "Nadarević", "Nikić", "Nišić",
        "Novalić", "Pačariz", "Predojević", "Preldžić", "Rakić",
        "Salatić", "Salihović", "Sarajlić", "Šarić", "Sidran",
        "Sijerčić", "Sokolović", "Sušić", "Tahirović", "Terzić",
        "Topalović", "Topčagić", "Toskić", "Turković", "Zahirović"
    ]
