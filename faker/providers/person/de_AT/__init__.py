# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
    )
    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{suffix_male}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}} {{suffix_male}}',
    )

    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}} {{suffix_female}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}} {{suffix_female}}',
    )

    formats = formats_male + formats_female

    first_names_male = (
        'Alexander', 'Andreas', 'Anton',
        'Benjamin', 'Bernhard',
        'Christian', 'Christop',
        'Daniel', 'David', 'Dominik',
        'Elias', 'Emil',
        'Fabian', 'Felix', 'Florian', 'Franz',
        'Gabriel', 'Gernot',
        'Heinrich',
        'Ingo',
        'Jakob', 'Johannes', 'Jonas', 'Julian',
        'Konrad', 'Konstantin',
        'Leo', 'Leon', 'Luca', 'Lukas',
        'Marcel', 'Martin', 'Matthias', 'Max', 'Maximilian', 'Michael', 'Moritz',
        'Nico', 'Niklas', 'Noah',
        'Oliver',
        'Paul', 'Philipp',
        'Raphael', 'Robert',
        'Samuel', 'Sebastian', 'Simon',
        'Thomas', 'Tim',
        'Tobias',
        'Valentin',
    )
    first_names_female = (
        'Alina', 'Anna',
        'Bea',
        'Christin',
        'Daniela',
        'Elena', 'Emil',
        'Fabian', 'Felix', 'Florian', 'Franz',
        'Gabriela',
        'Hanna',
        'Ingrid', 'Isabel',
        'Jana', 'Jasmin', 'Johanna', 'Julia',
        'Katharinna',
        'Lara', 'Laura', 'Lena', 'Linda',
        'Maria', 'Matthias', 'Mia',
        'Nina',
        'Olivia',
        'Paula', 'Pia',
        'Ria',
        'Sarah', 'Sophie',
        'Theresa',
        'Valentina',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Auer', 'Aigner',
        'Bauer', 'Baumgartner', 'Berger', 'Binder', 'Brunner',
        'Cap', 'Capek', 'Cech', 'Chum',
        'Deng', 'Denk', 'Daume', 'Dienstl',
        'Ebner', 'Eder', 'Egger',
        'Fasching', 'Felber', 'Ferstel', 'Fichtner', 'Fischer', 'Fuchs',
        'Gasser', 'Gastegger', 'Geier', 'Geisler', 'Grabner', 'Gruber',
        'Haas', 'Haiden', 'Hofer', 'Holzer', 'Huber',
        'Illes', 'Ircher', 'Itzlinger',
        'Jahn', 'Jobst', 'Jung', 'Jungbauer', 'Just',
        'Kainz', 'Karl', 'Karner', 'Koller',
        'Lang', 'Lechner', 'Lehner', 'Leitner',
        'Maier', 'Mair', 'Maurer', 'Mayer', 'Mayr', 'Moser', 'Müllner',
        'Pichler', 'Pucher',
        'Reiter', 'Riegler',
        'Schmid', 'Schneider', 'Schuster', 'Schwarz', 'Stadler', 'Steiner',
        'Wallner', 'Weber', 'Weiss', 'Wieser', 'Wimmer', 'Winkler', 'Winter', 'Wolf',
    )

    prefixes_male = (
        'Herr', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )
    prefixes_female = (
        'Frau', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )
    
    prefixes = ('Dr.', 'Mag.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.')
