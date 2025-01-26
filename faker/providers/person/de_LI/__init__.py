from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):

    # Top 50 surnames in Liechtenstein
    # Weighted by number of occurrences
    # Source: https://de.wikipedia.org/wiki/Familiennamen_in_Liechtenstein#Die_h%C3%A4ufigsten_50_Familiennamen on 2024-10-31
    last_names = OrderedDict(
        (
            ("Banzer", 0.011916111),
            ("Bargetze", 0.007864633),
            ("Batliner", 0.011201144),
            ("Beck", 0.05926279),
            ("Biedermann", 0.016682555),
            ("Büchel", 0.063711471),
            ("Bühler", 0.01509374),
            ("Eberle", 0.023196695),
            ("Foser", 0.008420718),
            ("Frick", 0.053781379),
            ("Frommelt", 0.021607881),
            ("Gassner", 0.028519225),
            ("Gstöhl", 0.020734032),
            ("Hasler", 0.035668891),
            ("Heeb", 0.011201144),
            ("Hilti", 0.014458214),
            ("Hoop", 0.012789959),
            ("Jehle", 0.010486177),
            ("Kaiser", 0.018509692),
            ("Kaufmann", 0.014855418),
            ("Kieber", 0.010009533),
            ("Kind", 0.010486177),
            ("Kindle", 0.025977121),
            ("Konrad", 0.007626311),
            ("Kranz", 0.015967588),
            ("Lampert", 0.017318081),
            ("Marxer", 0.05608516),
            ("Matt", 0.017635844),
            ("Meier", 0.031776295),
            ("Negele", 0.01080394),
            ("Nigg", 0.015570384),
            ("Nipp", 0.009453448),
            ("Nägele", 0.008102955),
            ("Näscher", 0.011042262),
            ("Oehri", 0.014617096),
            ("Ospelt", 0.026612647),
            ("Risch", 0.016603114),
            ("Ritter", 0.023911662),
            ("Schädler", 0.04313632),
            ("Sele", 0.016920877),
            ("Sprenger", 0.010962822),
            ("Thöny", 0.007626311),
            ("Vogt", 0.047982205),
            ("Wachter", 0.010406737),
            ("Walser", 0.016682555),
            ("Wanger", 0.008976803),
            ("Wille", 0.008182396),
            ("Wohlwend", 0.022402288),
            ("Wolfinger", 0.010247855),
            ("Öhri", 0.01406101),
        )
    )

    # Source: https://www.baby-vornamen.de/Namensthemen/Charts/Beliebteste-Vornamen-Liechtenstein-182.php#Jahrescharts-Liechtenstein
    # Took the 30 most common baby names per year (1996 to 2022) and weighted them by number of occurences (how often the name appeared in one of the year lists)
    first_names_male = OrderedDict(
        (
            ("Aaron", 0.00817),
            ("Adrian", 0.00817),
            ("Ajan", 0.00117),
            ("Alessandro", 0.00233),
            ("Alessio", 0.00467),
            ("Alexander", 0.01517),
            ("Amar", 0.00233),
            ("Andreas", 0.0035),
            ("Andrin", 0.00583),
            ("Aras", 0.00117),
            ("Bastian", 0.00117),
            ("Ben", 0.00933),
            ("Benedikt", 0.00117),
            ("Benjamin", 0.01167),
            ("Brian", 0.00117),
            ("Christoph", 0.00233),
            ("Colin", 0.00117),
            ("Conradin", 0.00117),
            ("Constantin", 0.0035),
            ("Cristiano", 0.00117),
            ("Damian", 0.00233),
            ("Daniel", 0.00817),
            ("Dario", 0.007),
            ("Daris", 0.00117),
            ("David", 0.014),
            ("Davide", 0.00117),
            ("Diego", 0.00233),
            ("Diogo", 0.00117),
            ("Dominic", 0.00117),
            ("Dominik", 0.007),
            ("Dylan", 0.0035),
            ("Eldon", 0.00117),
            ("Elia", 0.00583),
            ("Elias", 0.01984),
            ("Elijah", 0.00117),
            ("Elio", 0.00117),
            ("Eloi", 0.00117),
            ("Emanuel", 0.00467),
            ("Emil", 0.0035),
            ("Emilian", 0.00233),
            ("Emmanuel", 0.00117),
            ("Enea", 0.00233),
            ("Eren", 0.00117),
            ("Eric", 0.00117),
            ("Fabian", 0.014),
            ("Fabio", 0.01517),
            ("Fabrizio", 0.00117),
            ("Felix", 0.00817),
            ("Finn", 0.00583),
            ("Florian", 0.00583),
            ("Florin", 0.00117),
            ("Gabriel", 0.01284),
            ("Gian", 0.0035),
            ("Gian-Luca", 0.00117),
            ("Gion", 0.00117),
            ("Goncalo", 0.00117),
            ("Gustav", 0.00117),
            ("Hans", 0.00117),
            ("Henri", 0.00117),
            ("Henry", 0.00233),
            ("Ian", 0.00117),
            ("Jakob", 0.00233),
            ("James", 0.00117),
            ("Jan", 0.007),
            ("Janick", 0.00117),
            ("Janik", 0.00117),
            ("Janis", 0.00117),
            ("Jano", 0.00117),
            ("Joel", 0.01167),
            ("Johannes", 0.00933),
            ("Jonas", 0.021),
            ("Jonathan", 0.00233),
            ("Josef", 0.00233),
            ("Joshua", 0.00117),
            ("Julian", 0.0245),
            ("Julius", 0.00233),
            ("Justin", 0.00467),
            ("Kevin", 0.00583),
            ("Kian", 0.00117),
            ("Kiano", 0.00117),
            ("Kilian", 0.00233),
            ("Konstantin", 0.00233),
            ("Lars", 0.00233),
            ("Laurenz", 0.00117),
            ("Laurin", 0.00933),
            ("Lean", 0.00117),
            ("Leandro", 0.00817),
            ("Leano", 0.0035),
            ("Lenny", 0.00233),
            ("Leo", 0.0105),
            ("Leon", 0.01634),
            ("Leonardo", 0.00117),
            ("Leonhard", 0.00117),
            ("Leopold", 0.00233),
            ("Levi", 0.00117),
            ("Levin", 0.0035),
            ("Liam", 0.00467),
            ("Lian", 0.00467),
            ("Linus", 0.00233),
            ("Lio", 0.00233),
            ("Lionel", 0.00583),
            ("Lirjan", 0.00117),
            ("Livio", 0.0035),
            ("Lorenz", 0.00117),
            ("Loris", 0.00233),
            ("Louie", 0.00233),
            ("Louis", 0.0105),
            ("Luan", 0.00233),
            ("Luca", 0.0175),
            ("Lucas", 0.00467),
            ("Luej", 0.00117),
            ("Luigi", 0.00117),
            ("Luis", 0.01517),
            ("Lukas", 0.0175),
            ("Mael", 0.00117),
            ("Malik", 0.0035),
            ("Malio", 0.00117),
            ("Mantas", 0.00117),
            ("Manuel", 0.014),
            ("Marc", 0.007),
            ("Marcel", 0.00233),
            ("Marco", 0.0105),
            ("Marino", 0.00117),
            ("Mario", 0.00117),
            ("Marlon", 0.0035),
            ("Martim", 0.00117),
            ("Martin", 0.0035),
            ("Marvin", 0.00117),
            ("Mathias", 0.00117),
            ("Mats", 0.00117),
            ("Matteo", 0.01167),
            ("Matthias", 0.007),
            ("Matti", 0.00117),
            ("Mattia", 0.00233),
            ("Maurice", 0.00117),
            ("Mauro", 0.0035),
            ("Max", 0.00817),
            ("Maxim", 0.00117),
            ("Maximilian", 0.01634),
            ("Metehan", 0.00117),
            ("Michael", 0.01167),
            ("Michele", 0.00233),
            ("Mike", 0.00117),
            ("Mikyas", 0.00117),
            ("Milan", 0.00117),
            ("Milo", 0.00117),
            ("Moritz", 0.00233),
            ("Muhamed", 0.00233),
            ("Muhammed", 0.00467),
            ("Nael", 0.00233),
            ("Nando", 0.00117),
            ("Natanael", 0.00117),
            ("Nelio", 0.00117),
            ("Nevio", 0.00233),
            ("Niclas", 0.00233),
            ("Nico", 0.01284),
            ("Nicola", 0.00117),
            ("Nicolas", 0.00933),
            ("Niels", 0.00117),
            ("Niklas", 0.007),
            ("Nils", 0.00233),
            ("Nino", 0.00467),
            ("Noah", 0.0245),
            ("Noam", 0.00117),
            ("Noe", 0.00117),
            ("Noel", 0.007),
            ("Oliver", 0.00233),
            ("Orlando", 0.00117),
            ("Oscar", 0.00117),
            ("Oskar", 0.00233),
            ("Pascal", 0.01167),
            ("Patrick", 0.007),
            ("Patrik", 0.00117),
            ("Paul", 0.00933),
            ("Philipp", 0.007),
            ("Rafael", 0.00583),
            ("Raffael", 0.00233),
            ("Ramon", 0.0035),
            ("Raphael", 0.01984),
            ("Rino", 0.00117),
            ("Robin", 0.0105),
            ("Rodrigo", 0.00233),
            ("Romeo", 0.00117),
            ("Ruben", 0.00583),
            ("Ryan", 0.00233),
            ("Samir", 0.00117),
            ("Samuel", 0.01867),
            ("Sandro", 0.007),
            ("Santiago", 0.00233),
            ("Sebastian", 0.0105),
            ("Severin", 0.00117),
            ("Silas", 0.00117),
            ("Silvio", 0.00117),
            ("Simon", 0.0175),
            ("Stefan", 0.00117),
            ("Tenzin", 0.00233),
            ("Theo", 0.00233),
            ("Theodor", 0.00233),
            ("Thiago", 0.00117),
            ("Thomas", 0.00117),
            ("Tiago", 0.00233),
            ("Till", 0.00117),
            ("Tim", 0.00467),
            ("Timo", 0.00233),
            ("Timon", 0.00117),
            ("Timur", 0.00117),
            ("Tiziano", 0.00117),
            ("Tobias", 0.01167),
            ("Valentin", 0.00933),
            ("Vince", 0.00117),
            ("Vincent", 0.00233),
            ("Wenzel", 0.00117),
            ("Yanis", 0.00117),
            ("Yannick", 0.0035),
            ("Yassin", 0.00117),
            ("Yoan", 0.00117),
            ("Ömer", 0.00117),
        )
    )

    first_names_female = OrderedDict(
        (
            ("Adriana", 0.00361),
            ("Afra", 0.0012),
            ("Alea", 0.0012),
            ("Alessia", 0.01566),
            ("Alexandra", 0.0012),
            ("Alicia", 0.0012),
            ("Alina", 0.01205),
            ("Alisa", 0.0012),
            ("Alya", 0.0012),
            ("Amaya", 0.0012),
            ("Amelia", 0.0012),
            ("Amelie", 0.01446),
            ("Amy", 0.00361),
            ("Anastasia", 0.0012),
            ("Angelina", 0.00241),
            ("Anika", 0.00241),
            ("Anisa", 0.0012),
            ("Anja", 0.0012),
            ("Anna", 0.02651),
            ("Anna-Lena", 0.0012),
            ("Annalena", 0.0012),
            ("Annika", 0.00241),
            ("Annina", 0.0012),
            ("Anouk", 0.0012),
            ("Aria", 0.0012),
            ("Ariana", 0.00241),
            ("Aurora", 0.00361),
            ("Ayse", 0.0012),
            ("Bianca", 0.0012),
            ("Carla", 0.00361),
            ("Carmen", 0.0012),
            ("Carolina", 0.0012),
            ("Caroline", 0.0012),
            ("Cataleya", 0.0012),
            ("Celina", 0.0012),
            ("Celine", 0.00482),
            ("Chiara", 0.01928),
            ("Christina", 0.0012),
            ("Claudia", 0.0012),
            ("Cosima", 0.0012),
            ("Daria", 0.0012),
            ("Deborah", 0.0012),
            ("Deniis", 0.0012),
            ("Diana", 0.00361),
            ("Dilara", 0.0012),
            ("Eileen", 0.0012),
            ("Ela", 0.00361),
            ("Elea", 0.00241),
            ("Elena", 0.01687),
            ("Elfida", 0.0012),
            ("Eliana", 0.00241),
            ("Eliane", 0.0012),
            ("Elif", 0.00241),
            ("Elin", 0.00482),
            ("Elina", 0.00361),
            ("Eliona", 0.0012),
            ("Elisa", 0.00361),
            ("Elisabeth", 0.0012),
            ("Ella", 0.00482),
            ("Elvana", 0.0012),
            ("Emelina", 0.0012),
            ("Emilia", 0.01566),
            ("Emilie", 0.0012),
            ("Emily", 0.00482),
            ("Emine", 0.0012),
            ("Emma", 0.01928),
            ("Enna", 0.0012),
            ("Enya", 0.0012),
            ("Eowyn", 0.0012),
            ("Erva", 0.0012),
            ("Eslemnur", 0.0012),
            ("Estella", 0.0012),
            ("Eva", 0.00482),
            ("Eva-Maria", 0.0012),
            ("Evita", 0.0012),
            ("Fabienne", 0.00602),
            ("Felicia", 0.0012),
            ("Filippa", 0.00241),
            ("Fiona", 0.00843),
            ("Fjolla", 0.0012),
            ("Florina", 0.0012),
            ("Franziska", 0.00241),
            ("Frida", 0.0012),
            ("Frieda", 0.0012),
            ("Gaia", 0.0012),
            ("Geraldine", 0.0012),
            ("Gina", 0.00241),
            ("Gioia", 0.0012),
            ("Giulia", 0.00482),
            ("Gizem", 0.0012),
            ("Grace", 0.0012),
            ("Gwenda", 0.0012),
            ("Hana", 0.0012),
            ("Hanna", 0.00241),
            ("Hannah", 0.00964),
            ("Helena", 0.00482),
            ("Ilenia", 0.0012),
            ("Irina", 0.0012),
            ("Isabel", 0.00241),
            ("Isabella", 0.00241),
            ("Jacqueline", 0.00241),
            ("Jana", 0.00964),
            ("Janina", 0.00241),
            ("Janine", 0.00361),
            ("Jasmin", 0.0012),
            ("Jennifer", 0.00482),
            ("Jenny", 0.0012),
            ("Jessica", 0.00964),
            ("Joana", 0.00361),
            ("Joanna", 0.0012),
            ("Johanna", 0.00964),
            ("Jolina", 0.0012),
            ("Jule", 0.0012),
            ("Julia", 0.02048),
            ("Katharina", 0.01084),
            ("Kerstin", 0.0012),
            ("Klara", 0.0012),
            ("Klea", 0.0012),
            ("Künkyi", 0.0012),
            ("Ladina", 0.01084),
            ("Lara", 0.02048),
            ("Larissa", 0.00964),
            ("Laura", 0.02289),
            ("Laurina", 0.0012),
            ("Lavinia", 0.0012),
            ("Lea", 0.01687),
            ("Leana", 0.0012),
            ("Lena", 0.01807),
            ("Leni", 0.00241),
            ("Leonie", 0.02048),
            ("Letizia", 0.00241),
            ("Leyla", 0.0012),
            ("Leyla-Katharina", 0.0012),
            ("Lhanzey", 0.0012),
            ("Lia", 0.00602),
            ("Lilia", 0.0012),
            ("Liliana", 0.0012),
            ("Lillian", 0.0012),
            ("Lilly", 0.0012),
            ("Lily", 0.0012),
            ("Lina", 0.01325),
            ("Linda", 0.00361),
            ("Lisa", 0.01928),
            ("Liv", 0.00241),
            ("Livia", 0.00602),
            ("Liya", 0.0012),
            ("Lola", 0.0012),
            ("Lorena", 0.00843),
            ("Louana", 0.0012),
            ("Louisa", 0.0012),
            ("Louise", 0.0012),
            ("Luana", 0.00241),
            ("Luena", 0.0012),
            ("Luisa", 0.01084),
            ("Luna", 0.0012),
            ("Lydia", 0.00241),
            ("Lynn", 0.00482),
            ("Madeleine", 0.0012),
            ("Madleina", 0.00241),
            ("Magdalena", 0.00361),
            ("Maila", 0.0012),
            ("Maisa", 0.0012),
            ("Maivi", 0.0012),
            ("Maja", 0.0012),
            ("Malea", 0.00482),
            ("Malene", 0.0012),
            ("Malu", 0.0012),
            ("Manila", 0.0012),
            ("Mara", 0.00602),
            ("Mara-Julie", 0.0012),
            ("Maren", 0.0012),
            ("Margarita", 0.0012),
            ("Mari", 0.0012),
            ("Maria", 0.01084),
            ("Marie", 0.00602),
            ("Marie-Cecilie", 0.0012),
            ("Mariella", 0.0012),
            ("Marina", 0.00241),
            ("Martina", 0.0012),
            ("Mathilda", 0.0012),
            ("Matilda", 0.00361),
            ("Mavie", 0.0012),
            ("Maxima", 0.0012),
            ("Maya", 0.0012),
            ("Melanie", 0.00843),
            ("Melanine", 0.0012),
            ("Melina", 0.00482),
            ("Melissa", 0.00723),
            ("Merve", 0.0012),
            ("Mia", 0.01446),
            ("Michele", 0.00241),
            ("Michelle", 0.00482),
            ("Mila", 0.00241),
            ("Milena", 0.00482),
            ("Mina", 0.00361),
            ("Mira", 0.0012),
            ("Muriel", 0.0012),
            ("Nadine", 0.0012),
            ("Nahla", 0.0012),
            ("Naomi", 0.00482),
            ("Natalie", 0.0012),
            ("Nathalie", 0.0012),
            ("Nathasha", 0.0012),
            ("Nelia", 0.0012),
            ("Nelya", 0.0012),
            ("Neslisah", 0.0012),
            ("Nicole", 0.00482),
            ("Nina", 0.01928),
            ("Noelia", 0.00482),
            ("Noemi", 0.00964),
            ("Nora", 0.00482),
            ("Nour", 0.0012),
            ("Olivia", 0.00241),
            ("Patricia", 0.0012),
            ("Paula", 0.00723),
            ("Paulina", 0.0012),
            ("Pia", 0.00241),
            ("Rahel", 0.00241),
            ("Ramona", 0.00361),
            ("Raphaela", 0.0012),
            ("Rebecca", 0.00602),
            ("Robin", 0.0012),
            ("Romy", 0.0012),
            ("Ronja", 0.00241),
            ("Sabrina", 0.00482),
            ("Sally", 0.0012),
            ("Salome", 0.00241),
            ("Samantha", 0.0012),
            ("Saphira", 0.00241),
            ("Sara", 0.00723),
            ("Sarah", 0.01446),
            ("Sarina", 0.00241),
            ("Selina", 0.00843),
            ("Sina", 0.01084),
            ("Sofia", 0.00361),
            ("Sophia", 0.02048),
            ("Sophie", 0.00602),
            ("Soraya", 0.0012),
            ("Stefanie", 0.00241),
            ("Svenja", 0.0012),
            ("Tamara", 0.0012),
            ("Tatjana", 0.0012),
            ("Tenzin", 0.0012),
            ("Teresa", 0.0012),
            ("Thalia", 0.0012),
            ("Tina", 0.0012),
            ("Valentina", 0.01325),
            ("Valeria", 0.00241),
            ("Vanessa", 0.01325),
            ("Victoria", 0.00482),
            ("Viktoria", 0.0012),
            ("Xenia", 0.0012),
            ("Yara", 0.0012),
            ("Ylvi", 0.0012),
            ("Zehra", 0.00241),
            ("Zejna", 0.0012),
            ("Zoe", 0.00361),
        )
    )
