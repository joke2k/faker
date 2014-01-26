# coding=utf-8
from __future__ import unicode_literals
from ..address import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = (
        '{{first_name}}-{{last_name}}-{{street_suffix_long}}',
        '{{last_name}}{{street_suffix_short}}'
    )
    street_address_formats = ('{{street_name}} {{building_number}}', )
    address_formats = ('{{street_address}}\n{{postcode}} {{city}}', )

    building_number_formats = ('###', '##', '#', '#/#')

    street_suffixes_long = (
        'Gasse', 'Platz', 'Ring', 'Straße', 'Weg', 'Allee'
    )
    street_suffixes_short = (
        'gasse', 'platz', 'ring', 'straße', 'str.', 'weg', 'allee'
    )

    postcode_formats = ('#####', )

    cities = (
        'Augsburg', 'Aschaffenburg', 'Aachen', 'Auerbach', 'Ahaus',
        'Badibling', 'Amberg', 'Ansbach', 'Angermünde', 'Anklam',
        'Altötting', 'Apolda', 'Arnstadt', 'Artern', 'Altentreptow', 'Aue',
        'Aurich', 'Berlin', 'Bamberg', 'Böblingen', 'Bernburg', 'Brand',
        'Erbisdorf', 'Beilngries', 'Belzig', 'Berchtesgaden', 'Biedenkopf',
        'Bischofswerda', 'Backnang', 'Borna', 'Bogen', 'Borken', 'Bruchsal',
        'Brandenburg', 'Burg', 'Brilon', 'Bad Brückenau', 'Bremervörde',
        'Bersenbrück', 'Beeskow', 'Bayreuth', 'Bitterfeld', 'Burgdorf',
        'Burglengenfeld', 'Büsingenm Hochrhein', 'Bützow', 'Bautzen',
        'Bergzabern', 'Chemnitz', 'Calau', 'Cottbus', 'Celle', 'Cloppenburg',
        'Coburg', 'Crailsheim', 'Cuxhaven', 'Calw', 'Darmstadt', 'Dachau',
        'Badoberan', 'Dresden', 'Dessau', 'Deggendorf', 'Diepholz',
        'Dieburg', 'Dinslaken', 'Dinkelsbühl', 'Döbeln', 'Demmin', 'Düren',
        'Donaueschingen', 'Duderstadt', 'Delitzsch', 'Eilenburg',
        'Ebersberg', 'Ebern', 'Ebermannstadt', 'Eckernförde', 'Erding',
        'Erfurt', 'Eggenfelden', 'Eisenhüttenstadt', 'Eichstätt',
        'Eichstätt', 'Eisleben', 'Einbeck', 'Eisenberg', 'Emmendingen',
        'Erkelenz', 'Eisenach', 'Euskirchen', 'Eutin', 'Eberswalde', 'Soltau',
        'Fallingbostel', 'Fulda', 'Freudenstadt', 'Feuchtwangen',
        'Fürstenfeldbruck', 'Main-Höchst)', 'Finsterwalde', 'Flöha',
        'Forchheim', 'Forst', 'Bad Freienwalde', 'Freising', 'Freital',
        'Füssen', 'Fürstenwalde', 'Gera', 'Gardelegen', 'Garmisch-Partenkirchen',
        'Schwäbisch Gmünd', 'Gadebusch', 'Geldern',
        'Gerolzhofen', 'Germersheim', 'Gifhorn', 'Groß-Gerau', 'Geithain',
        'Gräfenhainichen', 'Gießen', 'Grimmen', 'Gelnhausen', 'Genthin',
        'Sankt Goar', 'Sankt Goarshausen', 'Göttingen', 'Göppingen',
        'Görlitz', 'Grafenau', 'Großenhain', 'Griesbach Rottal', 'Grimma',
        'Gransee', 'Greiz', 'Goslar', 'Gütersloh', 'Gotha', 'Guben',
        'Gunzenhausen', 'Güstrow', 'Grevenbroich', 'Grevesmühlen',
        'Günzburg', 'Hannover', 'Hammelburg', 'Bremen', 'Hildburghausen',
        'Halberstadt', 'Hainichen', 'Hechingen', 'Haldensleben', 'Helmstedt',
        'Hersbruck', 'Hettstedt', 'Herford', 'Hagenow', 'Greifswald',
        'Hamburg', 'Hohenmölsen', 'Hildesheim', 'Heiligenstadt', 'Lübeck',
        'Hannoversch Münden', 'Hofgeismar', 'Holzminden', 'Hohenstein-Ernstthal',
        'Rostock', 'Heinsberg', 'Hansestadttralsund', 'Hünfeld',
        'Husum', 'Havelberg', 'Wismar', 'Höxter', 'Hoyerswerda', 'Herzberg',
        'Ilmenau', 'Illertissen', 'Ingolstadt', 'Iserlohn', 'Jena',
        'Jüterbog', 'Jessen', 'Jülich', 'Karlsruhe', 'Kronach', 'Kelheim',
        'Kehl', 'Kemnath', 'Bad Kissingen', 'Bad Kreuznach',
        'Kaiserslautern', 'Kleve', 'Klötze', 'Kamenz', 'Konstanz', 'Koblenz',
        'Kötzting', 'Kassel', 'Kitzingen', 'Kulmbach', 'Kusel', 'Königs Wusterhausen',
        'Kyritz', 'Leipziger Land', 'Ludwigsburg',
        'Lobenstein', 'Lübz', 'Luckau', 'Lemgo', 'Lüneburg', 'Lüdinghausen',
        'Bad Liebenwerda', 'Lichtenfels', 'Lübben', 'Lörrach', 'Lippstadt',
        'Bad Langensalza', 'Lüdenscheid', 'Luckenwalde', 'Ludwigslust',
        'München', 'Marienberg', 'Mainburg', 'Mallersdorf',
        'Marktheidenfeld', 'Miesbach', 'Malchin', 'Magdeburg', 'Mettmann',
        'Melsungen', 'Meißen', 'Melle', 'Meppen', 'Merseburg',
        'Mellrichstadt', 'Bad Mergentheim', 'Meiningen', 'Mühlhausen',
        'Miltenberg', 'Moers', 'Monschau', 'Mühldorfm Inn', 'Mittweida',
        'Mayen', 'Nabburg', 'Naila', 'Nauen', 'Neubrandenburg', 'Nordhausen',
        'Neuss', 'Neunburg vorm Wald', 'Neustadtner Waldnaab', 'Northeim',
        'Norden', 'Nördlingen', 'Neuruppin', 'Neustadtm Rübenberge',
        'Nürtingen', 'Neu-Ulm', 'Niesky', 'Neustrelitz', 'Osterburg',
        'Ochsenfurt', 'Olpe', 'Osterodem Harz', 'Oranienburg',
        'Oberviechtach', 'Oschatz', 'Potsdam', 'Passau', 'Pfaffenhofenner Ilm',
        'Parsberg', 'Paderborn', 'Parchim', 'Peine', 'Pegnitz',
        'Perleberg', 'Pinneberg', 'Pritzwalk', 'Plauen', 'Pößneck',
        'Pirmasens', 'Pasewalk', 'Prenzlau', 'Querfurt', 'Quedlinburg',
        'Regensburg', 'Rastatt', 'Ribnitz-Damgarten', 'Recklinghausen',
        'Regen', 'Rehau', 'Roth', 'Riesa', 'Rochlitz', 'Rathenow',
        'Rosenheim', 'Roding', 'Rockenhausen', 'Rothenburg oberauber',
        'Reutlingen', 'Rudolstadt', 'Ravensburg', 'Rottweil', 'Stuttgart',
        'Schwandorf', 'Säckingen', 'Stadtsteinach', 'Saarbrücken',
        'Strasburg', 'Schleiz', 'Stade', 'Sondershausen', 'Stendal',
        'Sebnitz', 'Seelow', 'Scheinfeld', 'Senftenberg', 'Staßfurt',
        'Sangerhausen', 'Schwäbisch Hall', 'Suhl', 'Siegen', 'Sigmaringen',
        'Saulgau', 'Schmölln', 'Saarlouis', 'Schlüchtern', 'Badalzungen',
        'Schwabmünchen', 'Schwerin', 'Soest', 'Schrobenhausen', 'Schongau',
        'Soltau', 'Sömmerda', 'Sonneberg', 'Spremberg', 'Strausberg',
        'Stadtroda', 'Steinfurt', 'Starnberg', 'Sternberg', 'Stade',
        'Staffelstein', 'Stollberg', 'Sulzbach-Rosenberg', 'Schweinfurt',
        'Schwarzenberg', 'Tecklenburg', 'Teterow', 'Torgau', 'Tirschenreuth',
        'Tuttlingen', 'Tübingen', 'Uelzen', 'Ueckermünde', 'Uffenheim',
        'Vechta', 'Vilsbiburg', 'Viersen', 'Viechtach', 'Vohenstrauß',
        'Warendorf', 'Wittenberg', 'Worbis', 'Wiedenbrück', 'Werdau',
        'Weimar', 'Wertingen', 'Wesel', 'Wolfenbüttel', 'Witzenhausen',
        'Wittstock', 'Wolgast', 'Wolmirstedt', 'Wolfach', 'Wolfratshausen',
        'Wernigerode', 'Waren', 'Weißenfels', 'Weißwasser', 'Wittmund',
        'Waldmünchen', 'Wunsiedel', 'Wurzen', 'Wetzlar', 'Wanzleben',
        'Zerbst', 'Zschopau', 'Zeulenroda', 'Zossen'
    )

    states = (
        'Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
        'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
        'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
        'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen'
    )

    countries = (
        'Afghanistan', 'Alandinseln', 'Albanien', 'Algerien', 'Amerikanisch-Ozeanien',
        'Amerikanisch-Samoa', 'Amerikanische Jungferninseln',
        'Andorra', 'Angola', 'Anguilla', 'Antarktis', 'Antigua und Barbuda',
        'Argentinien', 'Armenien', 'Aruba', 'Aserbaidschan', 'Australien',
        'Ägypten', 'Äquatorialguinea', 'Äthiopien', 'Äußeres Ozeanien',
        'Bahamas', 'Bahrain', 'Bangladesch', 'Barbados', 'Belarus', 'Belgien',
        'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivien', 'Bosnien und Herzegowina',
        'Botsuana', 'Bouvetinsel', 'Brasilien', 'Britische Jungferninseln',
        'Britisches Territorium im Indischen Ozean', 'Brunei Darussalam',
        'Bulgarien', 'Burkina Faso', 'Burundi', 'Chile', 'China',
        'Cookinseln', 'Costa Rica', 'Côte d’Ivoire', 'Demokratische Republik Kongo',
        'Demokratische Volksrepublik Korea', 'Deutschland',
        'Dominica', 'Dominikanische Republik', 'Dschibuti', 'Dänemark',
        'Ecuador', 'El Salvador', 'Eritrea', 'Estland',
        'Falklandinseln', 'Fidschi', 'Finnland', 'Frankreich', 'Französisch-Guayana',
        'Französisch-Polynesien',
        'Färöer', 'Gabun', 'Gambia', 'Georgien', 'Ghana',
        'Gibraltar', 'Grenada', 'Griechenland', 'Grönland', 'Guadeloupe',
        'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana',
        'Haiti', 'Heard- und McDonald-Inseln', 'Honduras', 'Indien',
        'Indonesien', 'Irak', 'Iran', 'Irland', 'Island', 'Isle of Man',
        'Israel', 'Italien', 'Jamaika', 'Japan', 'Jemen', 'Jersey',
        'Jordanien', 'Kaimaninseln', 'Kambodscha', 'Kamerun', 'Kanada', 'Kap Verde',
        'Kasachstan', 'Katar', 'Kenia', 'Kirgisistan', 'Kiribati',
        'Kokosinseln', 'Kolumbien', 'Komoren', 'Kongo', 'Kroatien', 'Kuba',
        'Kuwait', 'Laos', 'Lesotho', 'Lettland', 'Libanon', 'Liberia',
        'Libyen', 'Liechtenstein', 'Litauen', 'Luxemburg', 'Madagaskar',
        'Malawi', 'Malaysia', 'Malediven', 'Mali', 'Malta', 'Marokko',
        'Marshallinseln', 'Martinique', 'Mauretanien', 'Mauritius',
        'Mayotte', 'Mazedonien', 'Mexiko', 'Mikronesien', 'Monaco',
        'Mongolei', 'Montenegro', 'Montserrat', 'Mosambik', 'Myanmar',
        'Namibia', 'Nauru', 'Nepal', 'Neukaledonien', 'Neuseeland',
        'Nicaragua', 'Niederlande', 'Niederländische Antillen', 'Niger',
        'Nigeria', 'Niue', 'Norfolkinsel', 'Norwegen', 'Nördliche Marianen',
        'Oman', 'Osttimor', 'Österreich', 'Pakistan', 'Palau',
        'Palästinensische Gebiete', 'Panama', 'Papua-Neuguinea', 'Paraguay',
        'Peru', 'Philippinen', 'Pitcairn', 'Polen', 'Portugal', 'Puerto Rico',
        'Republik Korea', 'Republik Moldau', 'Ruanda', 'Rumänien',
        'Russische Föderation', 'Réunion', 'Salomonen', 'Sambia', 'Samoa',
        'San Marino', 'Saudi-Arabien', 'Schweden', 'Schweiz', 'Senegal',
        'Serbien', 'Serbien und Montenegro', 'Seychellen', 'Sierra Leone',
        'Simbabwe', 'Singapur', 'Slowakei', 'Slowenien', 'Somalia',
        'Sonderverwaltungszone Hongkong', 'Sonderverwaltungszone Macao',
        'Spanien', 'Sri Lanka', 'St. Barthélemy', 'St. Helena', 'St. Kitts und Nevis',
        'St. Lucia', 'St. Martin', 'St. Pierre und Miquelon',
        'St. Vincent und die Grenadinen', 'Sudan', 'Suriname', 'Svalbard und Jan Mayen',
        'Swasiland', 'Syrien', 'São Tomé und Príncipe',
        'Südafrika', 'Südgeorgien und die Südlichen Sandwichinseln',
        'Tadschikistan', 'Taiwan', 'Tansania', 'Thailand', 'Togo', 'Tokelau',
        'Tonga', 'Trinidad und Tobago', 'Tschad', 'Tschechische Republik',
        'Tunesien', 'Turkmenistan', 'Turks- und Caicosinseln', 'Tuvalu',
        'Türkei', 'Uganda', 'Ukraine', 'Ungarn', 'Uruguay', 'Usbekistan',
        'Vanuatu', 'Vatikanstadt', 'Venezuela', 'Vereinigte Arabische Emirate',
        'Vereinigte Staaten', 'Vereinigtes Königreich', 'Vietnam', 'Wallis und Futuna',
        'Weihnachtsinsel', 'Westsahara', 'Zentralafrikanische Republik',
        'Zypern'
    )

    @classmethod
    def street_suffix_short(cls):
        return cls.random_element(cls.street_suffixes_short)

    @classmethod
    def street_suffix_long(cls):
        return cls.random_element(cls.street_suffixes_long)

    @classmethod
    def city_name(cls):
        return cls.random_element(cls.cities)

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
