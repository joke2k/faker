# coding=utf8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):

    building_number_formats = ('###', '##', '#')

    postcode_formats = ('#####', )

    city_formats = ('{{city_name}}', )
    
    street_name_formats = ('{{fruit}}{{street_suffix}}', )
    
    street_address_formats = ('{{street_name}} {{building_number}}',)
    
    address_formats = ("{{street_address}}\n{{postcode}} {{city}}", )

    cities = (
        'Akaa', 'Alajärvi', 'Alavus', 'Espoo', 'Forssa', 'Haapajärvi', 
        'Haapavesi', 'Hämeenlinna', 'Hamina', 'Hanko', 'Harjavalta', 
        'Haukipudas', 'Heinola', 'Helsinki', 'Huittinen', 'Hyvinkää', 
        'Iisalmi', 'Ikaalinen', 'Imatra', 'Jakobstad', 'Joensuu', 'Juankoski', 
        'Jyväskylä', 'Jämsä', 'Järvenpää', 'Kaarina', 'Kajaani', 'Kalajoki', 
        'Kankaanpää', 'Kannus', 'Karkkila', 'Kaskinen', 'Kauhajoki', 'Kauhava', 
        'Kauniainen', 'Kemi', 'Kemijärvi', 'Kerava', 'Keuruu', 'Kitee', 
        'Kiuruvesi', 'Kokemäki', 'Kokkola', 'Kotka', 'Kouvola', 'Kristinestad', 
        'Kuhmo', 'Kuopio', 'Kurikka', 'Kuusamo', 'Lahti', 'Laitila', 
        'Lappeenranta', 'Lapua', 'Lieksa', 'Lohja', 'Loimaa', 'Loviisa', 
        'Mänttä-Vilppula', 'Mariehamn', 'Mikkeli', 'Naantali', 'Närpes', 
        'Nilsiä', 'Nivala', 'Nokia', 'Nurmes', 'Nykarleby', 'Orimattila', 
        'Orivesi', 'Oulainen', 'Oulu', 'Outokumpu', 'Paimio', 'Pargas', 
        'Parkano', 'Pieksämäki', 'Pori', 'Porvoo', 'Pudasjärvi', 'Pyhäjärvi', 
        'Raahe', 'Raseborg', 'Rauma', 'Raisio', 'Riihimäki', 'Rovaniemi', 
        'Saarijärvi', 'Salo', 'Sastamala', 'Savonlinna', 'Seinäjoki', 'Siuntio', 
        'Somero', 'Suonenjoki', 'Tampere', 'Tornio', 'Turku', 'Ulvila', 
        'Uusikaupunki', 'Vaasa', 'Valkeakoski', 'Vantaa', 'Varkaus', 
        'Viitasaari', 'Virrat', 'Ylivieska', 'Ylöjärvi', 'Äänekoski', 'Ähtäri'
    )

    countries = (
        'Afganistan', 'Alankomaat', 'Albania', 'Algeria', 'Andorra', 'Angola', 
        'Antigua ja Barbuda', 'Argentiina', 'Armenia', 'Australia', 
        'Azerbaidžan', 'Bahama', 'Bahrain', 'Bangladesh', 'Barbados', 'Belgia', 
        'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia ja Hertsegovina', 
        'Botswana', 'Brasilia', 'Brunei', 'Bulgaria', 'Burkina', 'Faso', 
        'Burundi', 'Chile', 'Costa', 'Rica', 'Djibouti', 'Dominica', 
        'Dominikaaninen tasavalta', 'Ecuador', 'Egypti', 'El', 'Salvador', 
        'Eritrea', 'Espanja', 'Etelä-Afrikka', 'Korean tasavalta', 
        'Etelä-Sudan', 'Etiopia', 'Fidži', 'Filippiinit', 'Gabon', 'Gambia', 
        'Georgia', 'Ghana', 'Grenada', 'Guatemala', 'Guinea-Bissau', 'Guinea', 
        'Guyana', 'Haiti', 'Honduras', 'Indonesia', 'Intia', 'Irak', 'Iran', 
        'Irlanti', 'Islanti', 'Israel', 'Italia', 'Itä-Timor', 'Itävalta', 
        'Jamaika', 'Japani', 'Jemen', 'Jordania', 'Kambodža', 'Kamerun', 
        'Kanada', 'Kap', 'Verde', 'Kazakstan', 'Kenia', 
        'Keski-Afrikan tasavalta', 'Kiina', 'Kirgisia', 'Kiribati', 
        'Kolumbia', 'Komorit', 'Kongon demokraattinen tasavalta', 
        'Kongon tasavalta', 'Kosovo', 'Kreikka', 'Kroatia', 'Kuuba', 'Kuwait', 
        'Kypros', 'Laos', 'Latvia', 'Lesotho', 'Libanon', 'Liberia', 'Libya', 
        'Liechtenstein', 'Liettua', 'Luxemburg', 'Madagaskar', 'Makedonia', 
        'Malawi', 'Malediivit', 'Malesia', 'Mali', 'Malta', 'Marokko', 
        'Marshallinsaaret', 'Mauritania', 'Mauritius', 'Meksiko', 'Mikronesia', 
        'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Mosambik', 'Myanmar', 
        'Namibia', 'Nauru', 'Nepal', 'Nicaragua', 'Nigeria', 'Niger', 'Norja', 
        'Norsunluurannikko', 'Oman', 'Pakistan', 'Palau', 'Panama', 
        'Papua-Uusi-Guinea', 'Paraguay', 'Peru', 
        'Korean demokraattinen kansantasavalta', 'Portugali', 'Puola', 
        'Päiväntasaajan Guinea', 'Qatar', 'Ranska', 'Romania', 'Ruanda', 
        'Ruotsi', 'Saint Kitts ja Nevis', 'Saint Lucia', 
        'Saint Vincent ja Grenadiinit', 'Saksa', 'Salomonsaaret', 'Sambia', 
        'Samoa', 'San Marino', 'São Tomé ja Príncipe', 
        'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychellit', 'Sierra', 'Leone', 
        'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'Sri', 'Lanka', 'Sudan', 
        'Suomi', 'Suriname', 'Swazimaa', 'Sveitsi', 'Syyria', 'Tadžikistan', 
        'Tansania', 'Tanska', 'Thaimaa', 'Togo', 'Tonga', 'Trinidad ja Tobago', 
        'Tšad', 'Tšekki', 'Tunisia', 'Turkki', 'Turkmenistan', 'Tuvalu', 
        'Uganda', 'Ukraina', 'Unkari', 'Uruguay', 'Uusi-Seelanti', 'Uzbekistan', 
        'Valko-Venäjä', 'Vanuatu', 'Vatikaanivaltio', 'Venezuela', 'Venäjä', 
        'Vietnam', 'Viro', 'Yhdistyneet arabiemiirikunnat', 
        'Yhdistynyt kuningaskunta', 'Yhdysvallat', 'Zimbabwe'
    )

    states = (
        'Turun ja Porin lääni', 'Uudenmaan ja Hämeen lääni', 'Pohjanmaan lääni', 
        'Viipurin ja Savonlinnan lääni', 'Käkisalmen lääni', 
        'Savonlinnan ja Kymenkartanon lääni', 'Kymenkartanon ja Savon lääni', 
        'Vaasan lääni', 'Oulun lääni', 'Kymenkartanon lääni', 
        'Savon ja Karjalan lääni', 'Viipurin lääni', 'Uudenmaan lääni', 
        'Hämeen lääni', 'Mikkelin lääni', 'Kuopion lääni', 'Ahvenanmaan lääni', 
        'Petsamon lääni', 'Lapin lääni', 'Kymen lääni', 'Keski-Suomen lääni', 
        'Pohjois-Karjalan lääni', 'Etelä-Suomen lääni', 'Länsi-Suomen lääni', 
        'Itä-Suomen lääni', '', 'Turun ja Porin lääni', 
        'Uudenmaan ja Hämeen lääni', 'Pohjanmaan lääni', 
        'Viipurin ja Savonlinnan lääni', 'Käkisalmen lääni', 
        'Savonlinnan ja Kymenkartanon lääni', 'Kymenkartanon ja Savon lääni', 
        'Vaasan lääni', 'Oulun lääni', 'Kymenkartanon lääni', 
        'Savon ja Karjalan lääni', 'Viipurin lääni', 'Uudenmaan lääni', 
        'Hämeen lääni', 'Mikkelin lääni', 'Kuopion lääni', 'Ahvenanmaan lääni', 
        'Petsamon lääni', 'Lapin lääni', 'Kymen lääni', 'Keski-Suomen lääni', 
        'Pohjois-Karjalan lääni', 'Etelä-Suomen lääni', 'Länsi-Suomen lääni', 
        'Itä-Suomen lääni'
    )

    street_suffixes = ('tie', 'katu', 'polku', 'kuja', 'bulevardi')

    # Using fruits to generate street names, since it doesn't make 
    # much grammatical sense to use first names

    fruits = (
        'Ananas', 'Ananaskirsikka', 'Annoona', 'Appelsiini', 'Aprikoosi', 
        'Avokado', 'Banaani', 'Cantaloupemeloni', 'Durio', 'Feijoa', 
        'Galiameloni', 'Granaattiomena', 'Granadilla', 'Greippi', 'Guava', 
        'Hunajameloni', 'Jakkihedelmä', 'Kaki', 'Kaktusviikuna', 'Karambola', 
        'Kastanja', 'Keittobanaani', 'Keltainen', 'kiivi', 'Keltapassio', 
        'Kiivi', 'Kirsikka', 'Kirsikkaluumu', 'Kiwai', 'Kiwano','Kookospähkinä', 
        'Kumkvatti', 'Limetti', 'Limkvatti', 'Litsi', 'Longaani', 'Luumu', 
        'Mandariini', 'Mango', 'Mangostaani', 'Maracuya', 'Meloni', 'Nashi', 
        'Nektariini', 'Omena', 'Papaija', 'Passionhedelmä', 'Persikka','Pepino', 
        'Pikkusitrukset', 'Pitahaya', 'Pomelo', 'Pähkinä', 'Päärynä', 
        'Rambutani', 'Rumeliini', 'Sapodilla', 'Salaki', 'Sitruuna', 
        'Sokerimeloni', 'Sweetie', 'Taateli', 'Tamarillo', 'Tomaatti', 
        'Verkkomeloni', 'Vesimeloni', 'Viikuna', 'Viinirypäle', 'Ananas', 
        'Annoona', 'Appelsiini', 'Aprikoosi', 'Avokado', 'Banaani', 
        'Cantaloupemeloni', 'Durio', 'Feijoa', 'Galiameloni', 'Granaattiomena', 
        'Granadilla', 'Greippi', 'Guava', 'Hunajameloni', 'Jakkihedelmä','Kaki', 
        'Kaktusviikuna', 'Karambola', 'Kastanja', 'Keittobanaani','Keltapassio', 
        'Kiivi', 'Kirsikka', 'Kirsikkaluumu', 'Kiwai', 'Kiwano','Kookospähkinä', 
        'Kumkvatti', 'Limetti', 'Limkvatti', 'Litsi', 'Longaani', 'Luumu', 
        'Mandariini', 'Mango', 'Mangostaani', 'Maracuya', 'Meloni', 'Nashi', 
        'Nektariini', 'Omena', 'Papaija', 'Passionhedelmä', 'Persikka','Pepino', 
        'Pikkusitrukset', 'Pitahaya', 'Pomelo', 'Pähkinä', 'Päärynä',
        'Rambutani', 'Rumeliini', 'Sapodilla', 'Salaki', 'Sitruuna', 
        'Sokerimeloni', 'Sweetie', 'Taateli', 'Tamarillo', 'Tomaatti', 
        'Verkkomeloni', 'Vesimeloni', 'Viikuna', 'Viinirypäle'
    )

    @classmethod
    def fruit(cls):
        return cls.random_element(cls.fruits)

    @classmethod
    def city_name(cls):
        return cls.random_element(cls.cities)

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
