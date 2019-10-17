# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
    )

    # Names from
    # https://andela-celisha-wigwe.github.io/names.html

    first_names_male = (
        'Abimbola', 'Abisola', 'Abisoye', 'Adeboye', 'Adedayo', 'Adegoke', 'Akande', 'Akanni', 'Alade', 'Ayinde',
        'Azubuike',
        'Banji', 'Bankole', 'Buchi', 'Bukola',
        'Chinedu', 'Chisom', 'Chukwu',
        'Damilare', 'Damilola', 'Danjuma',
        'Ebiowei', 'Emeka', 'Emmanuel', 'Esse',
        'Funmilade', 'Funmilayo',
        'Gbeminiyi', 'Gbemisola',
        'Habiba', 'Ifeanyichukwu',
        'Ikenna', 'Ikhidie', 'Ireti',
        'Jadesola', 'Johnson',
        'Kayode', 'Kemi', 'Kubra', 'Kubura',
        'Lolade',
        'Makinwa', 'Mohammed', 'Musa', 'Muyiwa',
        'Nnamdi',
        'Olaide', 'Olufunmi', 'Olumide', 'Oluwunmi', 'Onoriode',
        'Remilekun', 'Rotimi',
        'Shade', 'Shalewa', 'Sname',
        'Tari', 'Temitope', 'Titilope', 'Tobiloba', 'Toke', 'Tomiloba', 'Tope',
        'Uzodimma',
        'Wale',
        'Yakubu', 'Yusuf', 'Yusuf',
    )

    first_names_female = (
        'Adaugo', 'Akunna', 'Aminat', 'Aminu', 'Augustina', 'Ayebatari',
        'Cherechi', 'Chiamaka', 'Chimamanda', 'Chinyere', 'Chizoba',
        'Ebiere', 'Efe',
        'Fatima', 'Ifeoma',
        'Ifunanya', 'Isioma',
        'Jolayemi',
        'Lola',
        'Obioma', 'Omawunmi', 'Omolara', 'Onome',
        'Rasheedah',
        'Sekinat', 'Simisola', 'Sumayyah',
        'Titi', 'Titilayo', 'Toluwani',
        'Zainab',
    )

    first_names = first_names_male + first_names_female

    last_names = OrderedDict((
        ('Abiodun', 0.9),
        ('Abiola', 0.33),
        ('Abodunrin', 0.11),
        ('Abosede', 0.48),
        ('Adaobi', 0.92),
        ('Adebayo', 0.92),
        ('Adegboye', 0.48),
        ('Adegoke', 0.95),
        ('Ademayowa', 0.83),
        ('Ademola', 0.35),
        ('Adeniyan', 0.47),
        ('Adeoluwa', 0.46),
        ('Aderinsola', 0.64),
        ('Aderonke', 0.33),
        ('Adesina', 0.08),
        ('Adewale', 0.91),
        ('Adewale', 0.99),
        ('Adewale', 0.27),
        ('Adewunmi', 0.07),
        ('Adewura', 0.7),
        ('Adeyemo', 0.48),
        ('Afolabi', 0.69),
        ('Afunku', 0.9),
        ('Agboola', 0.1),
        ('Agboola', 0.19),
        ('Agnes', 0.95),
        ('Aigbiniode', 0.51),
        ('Ajakaiye', 0.72),
        ('Ajose-adeogun', 0.78),
        ('Akeem-omosanya', 0.16),
        ('Akerele', 0.53),
        ('Akintade', 0.75),
        ('Aligbe', 0.14),
        ('Amaechi', 0.63),
        ('Aminat', 0.8),
        ('Aremu', 0.84),
        ('Atanda', 0.02),
        ('Ayisat', 0.12),
        ('Ayobami', 0.55),
        ('Ayomide', 0.59),
        ('Ayomide', 0.64),
        ('Babalola', 0.82),
        ('Babatunde', 0.21),
        ('Balogun', 0.46),
        ('Bamisebi', 0.6),
        ('Bello', 0.87),
        ('Busari', 0.43),
        ('Chibike', 0.12),
        ('Chibuike', 0.87),
        ('Chidinma', 0.7),
        ('Chidozie', 0.62),
        ('Christian', 0.46),
        ('Clare', 0.23),
        ('David', 0.86),
        ('David', 0.8),
        ('Ebubechukwu', 0.29),
        ('Egbochukwu', 0.76),
        ('Ehigiator', 0.78),
        ('Ekwueme', 0.83),
        ('Elebiyo', 0.38),
        ('Elizabeth', 0.45),
        ('Elizabeth', 0.49),
        ('Elizabeth', 0.94),
        ('Emmanuel', 0.58),
        ('Emmanuel', 0.84),
        ('Esther', 0.95),
        ('Funmilayo', 0.27),
        ('Gbadamosi', 0.84),
        ('Gbogboade', 0.05),
        ('Grace', 0.96),
        ('Habeeb', 0.59),
        ('Hanifat', 0.68),
        ('Isaac', 0.61),
        ('Ismail', 0.04),
        ('Isokun', 0.82),
        ('Israel', 0.94),
        ('Iyalla', 0.16),
        ('Jamiu', 0.19),
        ('Jimoh', 0.27),
        ('Joshua', 0.7),
        ('Justina', 0.01),
        ('Katherine', 0.93),
        ('Kayode', 0.41),
        ('Kayode', 0.9),
        ('Kimberly', 0.38),
        ('Ladega', 0.45),
        ('Latifat', 0.11),
        ('Lawal', 0.24),
        ('Leonard', 0.31),
        ('Makuachukwu', 0.03),
        ('Maryam', 0.86),
        ('Maryjane', 0.29),
        ('Mayowa', 0.19),
        ('Miracle', 0.94),
        ('Mobolaji', 0.44),
        ('Mogbadunade', 0.89),
        ('Motalo', 0.43),
        ('Muinat', 0.07),
        ('Mukaram', 0.44),
        ('Mustapha', 0.22),
        ('Mutiat', 0.81),
        ('Ndukwu', 0.07),
        ('Ngozi', 0.7),
        ('Nojeem', 0.48),
        ('Nwachukwu', 0.66),
        ('Nwogu', 0.73),
        ('Nwuzor', 0.55),
        ('Obiageli', 0.35),
        ('Obianuju', 0.39),
        ('Odunayo', 0.43),
        ('Odunayo', 0.13),
        ('Ogunbanwo', 0.77),
        ('Ogunwande', 0.79),
        ('Okonkwo', 0.94),
        ('Okunola', 0.69),
        ('Oladeji', 0.23),
        ('Oladimeji', 0.59),
        ('Olaoluwa', 0.71),
        ('Olasunkanmi', 0.34),
        ('Olasunkanmi-fasayo', 0.49),
        ('Olawale', 0.65),
        ('Olubukola', 0.97),
        ('Olubunmi', 0.35),
        ('Olufeyikemi', 0.21),
        ('Olumide', 0.4),
        ('Olutola', 0.86),
        ('Oluwakemi', 0.21),
        ('Oluwanisola', 0.02),
        ('Oluwaseun', 0.45),
        ('Oluwaseyi', 0.31),
        ('Oluwashina', 0.91),
        ('Oluwatosin', 0.0),
        ('Omobolaji', 0.86),
        ('Omobolanle', 0.87),
        ('Omolara', 0.52),
        ('Omowale', 0.49),
        ('Onohinosen', 0.85),
        ('Onose', 0.59),
        ('Onyinyechukwu', 0.37),
        ('Opeyemi', 0.33),
        ('Osuagwu', 0.67),
        ('Oyebola', 0.1),
        ('Oyelude', 0.49),
        ('Oyinkansola', 0.48),
        ('Peter', 0.64),
        ('Sabdat', 0.61),
        ('Saheed', 0.06),
        ('Salami', 0.25),
        ('Samuel', 0.57),
        ('Sanusi', 0.68),
        ('Sarah', 0.51),
        ('Segunmaru', 0.59),
        ('Sekinat', 0.7),
        ('Sulaimon', 0.5),
        ('Sylvester', 0.67),
        ('Taiwo', 0.81),
        ('Tamunoemi', 0.69),
        ('Tella', 0.82),
        ('Temitope', 0.69),
        ('Tolulope', 0.6),
        ('Uchechi', 0.83),
        ('Wasiu', 0.15),
        ('Wilcox', 0.65),
        ('Wuraola', 0.48),
        ('Yaqub', 0.99),
        ('Yussuf', 0.77),
    ))

    prefixes_female = ('Mrs.', 'Ms.', 'Miss', 'Dr.')
    prefixes_male = ('Mr.', 'Dr.')
