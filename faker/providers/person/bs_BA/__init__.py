# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ['{{first_name}} {{last_name}}', ]
    
     """
    The names used here are the top 100 names released by the Federal statistics institute
    in Bosnia and Herzegovina, available at 
    * http://fzs.ba/index.php/2016/05/29/najcesca-dodjeljivana-imena-novorodene-djece-u-2015-godini/
    """

    first_names_male = [
        "Ahmet", "Amar", "Alen", "Adin", "Vedad", "Ahmed", "Tarik", 
        "Ajdin", "Harun", "Kenan", "Davud", "Hamza", "Emir", "Imran", 
        "Daris", "Ajnur", "Muhamed", "Emin", "Armin", "Ivan", "Luka", 
        "Eman", "Kerim", "Faris", "Benjamin", "Ali", "Demir", "Marko", 
        "Eldar", "Omar", "Petar", "David", "Edin", "Emrah", "Bilal", 
        "Adnan", "Ismail", "Nedim", "Anes", "Ante", "Arman", "Danin", 
        "Adi", "Dženan", "Haris", "Mirza", "Ibrahim", "Aldin", "Filip", 
        "Bakir", "Amer", "Ensar", "Josip", "Afan", "Džan", "Rijad", 
        "Eldin", "Abdulah", "Anel", "Mateo", "Mak", "Alem", "Ivano", 
        "Ammar", "Danis", "Omer", "Amel", "Maid", "Jakov", "Matej", 
        "Karlo", "Mahir", "Dino", "Emil", "Leon", "Nikola", "Mustafa", 
        "Adem", "Elmin", "Alen", "Arslan", "Jasmin", "Mehmed", "Almin", 
        "Ermin", "Mihael", "Din", "Ismar", "Amin", "Adian", "Edvin", 
        "Faruk", "Jusuf", "Ishak", "Adis", "Aid", "Azur", "Fatih", 
        "Anis", "Antonio", "Ilhan"
    ]

    first_names_female = [
        "Nudžejma", "Amina", "Lamija", "Sara", "Asja", "Emina", "Lejla", 
        "Merjem", "Esma", "Ajla", "Nejla", "Adna", "Hana", "Ema", "Ajša", 
        "Ajna", "Amna", "Sajra", "Ilma", "Iman", "Lana", "Marija", "Amila", 
        "Nejra", "Ana", "Petra", "Ena", "Nedžla", "Mia", "Ajlin", "Dalila", 
        "Iva", "Sumeja", "Alina", "Naida", "Medina", "Džana", "Lucija", 
        "Elma", "Sarah", "Zara", "Azra", "Farah", "Anida", "Dalia", "Ejna", 
        "Una", "Amra", "Asija", "Šejla", "Džejla", "Aiša", "Elena", "Uma", 
        "Ilhana", "Jasmina", "Tajra", "Berina", "Matea", "Melisa", "Marta", 
        "Selma", "Klara", "Melina", "Nadja", "Emma", "Alejna", "Majra", 
        "Aida", "Ela", "Irma", "Lea", "Nora", "Ivana", "Minela", "Najla", 
        "Anđela", "Fatima", "Maja", "Nađa", "Nika", "Almina", "Belma", 
        "Erna", "Lorena", "Dalal", "Nadija", "Zana", "Dženita", "Lejna", 
        "Eva", "Magdalena", "Amela", "Kanita", "Lajla", "Lara", "Tea", 
        "Zejneb", "Hena", 
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
