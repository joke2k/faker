# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = (
        '{{first_name}}-{{last_name}}-{{street_suffix_long}}',
        '{{last_name}}{{street_suffix_short}}',
    )
    street_address_formats = ('{{street_name}} {{building_number}}', )
    address_formats = ('{{street_address}}\n{{postcode}} {{city}}', )

    building_number_formats = ('###', '##', '#', '#/#', )

    street_suffixes_long = (
        'Gasse', 'Platz', 'Ring', 'Straße', 'Weg', 'Allee',
    )
    street_suffixes_short = (
        'gasse', 'platz', 'ring', 'straße', 'str.', 'weg', 'allee',
    )

    postcode_formats = ('#####', )

    cities = (
        'Aachen', 'Ahaus', 'Altentreptow', 'Altötting', 'Amberg', 'Angermünde',
        'Anklam', 'Ansbach', 'Apolda', 'Arnstadt', 'Artern', 'Aschaffenburg',
        'Aue', 'Auerbach', 'Augsburg', 'Aurich', 'Backnang', 'Bad Brückenau',
        'Bad Freienwalde', 'Bad Kissingen', 'Bad Kreuznach', 'Bad Langensalza',
        'Bad Liebenwerda', 'Bad Mergentheim', 'Badalzungen', 'Badibling',
        'Badoberan', 'Bamberg', 'Bautzen', 'Bayreuth', 'Beeskow', 'Beilngries',
        'Belzig', 'Berchtesgaden', 'Bergzabern', 'Berlin', 'Bernburg',
        'Bersenbrück', 'Biedenkopf', 'Bischofswerda', 'Bitterfeld', 'Bogen',
        'Borken', 'Borna', 'Brand', 'Brandenburg', 'Bremen', 'Bremervörde',
        'Brilon', 'Bruchsal', 'Burg', 'Burgdorf', 'Burglengenfeld',
        'Böblingen', 'Büsingenm Hochrhein', 'Bützow', 'Calau', 'Calw', 'Celle',
        'Chemnitz', 'Cloppenburg', 'Coburg', 'Cottbus', 'Crailsheim',
        'Cuxhaven', 'Dachau', 'Darmstadt', 'Deggendorf', 'Delitzsch', 'Demmin',
        'Dessau', 'Dieburg', 'Diepholz', 'Dinkelsbühl', 'Dinslaken',
        'Donaueschingen', 'Dresden', 'Duderstadt', 'Döbeln', 'Düren',
        'Ebermannstadt', 'Ebern', 'Ebersberg', 'Eberswalde', 'Eckernförde',
        'Eggenfelden', 'Eichstätt', 'Eichstätt', 'Eilenburg', 'Einbeck',
        'Eisenach', 'Eisenberg', 'Eisenhüttenstadt', 'Eisleben', 'Emmendingen',
        'Erbisdorf', 'Erding', 'Erfurt', 'Erkelenz', 'Euskirchen', 'Eutin',
        'Fallingbostel', 'Feuchtwangen', 'Finsterwalde', 'Flöha', 'Forchheim',
        'Forst', 'Freising', 'Freital', 'Freudenstadt', 'Fulda',
        'Fürstenfeldbruck', 'Fürstenwalde', 'Füssen', 'Gadebusch',
        'Gardelegen', 'Garmisch-Partenkirchen', 'Geithain', 'Geldern',
        'Gelnhausen', 'Genthin', 'Gera', 'Germersheim', 'Gerolzhofen',
        'Gießen', 'Gifhorn', 'Goslar', 'Gotha', 'Grafenau', 'Gransee',
        'Greifswald', 'Greiz', 'Grevenbroich', 'Grevesmühlen',
        'Griesbach Rottal', 'Grimma', 'Grimmen', 'Groß-Gerau', 'Großenhain',
        'Gräfenhainichen', 'Guben', 'Gunzenhausen', 'Göppingen', 'Görlitz',
        'Göttingen', 'Günzburg', 'Güstrow', 'Gütersloh', 'Hagenow',
        'Hainichen', 'Halberstadt', 'Haldensleben', 'Hamburg', 'Hammelburg',
        'Hannover', 'Hannoversch Münden', 'Hansestadttralsund', 'Havelberg',
        'Hechingen', 'Heiligenstadt', 'Heinsberg', 'Helmstedt', 'Herford',
        'Hersbruck', 'Herzberg', 'Hettstedt', 'Hildburghausen', 'Hildesheim',
        'Hofgeismar', 'Hohenmölsen', 'Hohenstein-Ernstthal', 'Holzminden',
        'Hoyerswerda', 'Husum', 'Höxter', 'Hünfeld', 'Illertissen', 'Ilmenau',
        'Ingolstadt', 'Iserlohn', 'Jena', 'Jessen', 'Jülich', 'Jüterbog',
        'Kaiserslautern', 'Kamenz', 'Karlsruhe', 'Kassel', 'Kehl', 'Kelheim',
        'Kemnath', 'Kitzingen', 'Kleve', 'Klötze', 'Koblenz', 'Konstanz',
        'Kronach', 'Kulmbach', 'Kusel', 'Kyritz', 'Königs Wusterhausen',
        'Kötzting', 'Leipziger Land', 'Lemgo', 'Lichtenfels', 'Lippstadt',
        'Lobenstein', 'Luckau', 'Luckenwalde', 'Ludwigsburg', 'Ludwigslust',
        'Lörrach', 'Lübben', 'Lübeck', 'Lübz', 'Lüdenscheid', 'Lüdinghausen',
        'Lüneburg', 'Magdeburg', 'Main-Höchst)', 'Mainburg', 'Malchin',
        'Mallersdorf', 'Marienberg', 'Marktheidenfeld', 'Mayen', 'Meiningen',
        'Meißen', 'Melle', 'Mellrichstadt', 'Melsungen', 'Meppen', 'Merseburg',
        'Mettmann', 'Miesbach', 'Miltenberg', 'Mittweida', 'Moers', 'Monschau',
        'Mühldorfm Inn', 'Mühlhausen', 'München', 'Nabburg', 'Naila', 'Nauen',
        'Neu-Ulm', 'Neubrandenburg', 'Neunburg vorm Wald', 'Neuruppin',
        'Neuss', 'Neustadtm Rübenberge', 'Neustadtner Waldnaab', 'Neustrelitz',
        'Niesky', 'Norden', 'Nordhausen', 'Northeim', 'Nördlingen',
        'Nürtingen', 'Oberviechtach', 'Ochsenfurt', 'Olpe', 'Oranienburg',
        'Oschatz', 'Osterburg', 'Osterodem Harz', 'Paderborn', 'Parchim',
        'Parsberg', 'Pasewalk', 'Passau', 'Pegnitz', 'Peine', 'Perleberg',
        'Pfaffenhofenner Ilm', 'Pinneberg', 'Pirmasens', 'Plauen', 'Potsdam',
        'Prenzlau', 'Pritzwalk', 'Pößneck', 'Quedlinburg', 'Querfurt',
        'Rastatt', 'Rathenow', 'Ravensburg', 'Recklinghausen', 'Regen',
        'Regensburg', 'Rehau', 'Reutlingen', 'Ribnitz-Damgarten', 'Riesa',
        'Rochlitz', 'Rockenhausen', 'Roding', 'Rosenheim', 'Rostock', 'Roth',
        'Rothenburg oberauber', 'Rottweil', 'Rudolstadt', 'Saarbrücken',
        'Saarlouis', 'Sangerhausen', 'Sankt Goar', 'Sankt Goarshausen',
        'Saulgau', 'Scheinfeld', 'Schleiz', 'Schlüchtern', 'Schmölln',
        'Schongau', 'Schrobenhausen', 'Schwabmünchen', 'Schwandorf',
        'Schwarzenberg', 'Schweinfurt', 'Schwerin', 'Schwäbisch Gmünd',
        'Schwäbisch Hall', 'Sebnitz', 'Seelow', 'Senftenberg', 'Siegen',
        'Sigmaringen', 'Soest', 'Soltau', 'Soltau', 'Sondershausen',
        'Sonneberg', 'Spremberg', 'Stade', 'Stade', 'Stadtroda',
        'Stadtsteinach', 'Staffelstein', 'Starnberg', 'Staßfurt', 'Steinfurt',
        'Stendal', 'Sternberg', 'Stollberg', 'Strasburg', 'Strausberg',
        'Stuttgart', 'Suhl', 'Sulzbach-Rosenberg', 'Säckingen', 'Sömmerda',
        'Tecklenburg', 'Teterow', 'Tirschenreuth', 'Torgau', 'Tuttlingen',
        'Tübingen', 'Ueckermünde', 'Uelzen', 'Uffenheim', 'Vechta',
        'Viechtach', 'Viersen', 'Vilsbiburg', 'Vohenstrauß', 'Waldmünchen',
        'Wanzleben', 'Waren', 'Warendorf', 'Weimar', 'Weißenfels',
        'Weißwasser', 'Werdau', 'Wernigerode', 'Wertingen', 'Wesel', 'Wetzlar',
        'Wiedenbrück', 'Wismar', 'Wittenberg', 'Wittmund', 'Wittstock',
        'Witzenhausen', 'Wolfach', 'Wolfenbüttel', 'Wolfratshausen', 'Wolgast',
        'Wolmirstedt', 'Worbis', 'Wunsiedel', 'Wurzen', 'Zerbst', 'Zeulenroda',
        'Zossen', 'Zschopau',
    )

    states = (
        'Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
        'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
        'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
        'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
    )

    countries = (
        'Afghanistan', 'Alandinseln', 'Albanien', 'Algerien',
        'Amerikanisch-Ozeanien', 'Amerikanisch-Samoa',
        'Amerikanische Jungferninseln', 'Andorra', 'Angola', 'Anguilla',
        'Antarktis', 'Antigua und Barbuda', 'Argentinien', 'Armenien', 'Aruba',
        'Aserbaidschan', 'Australien', 'Bahamas', 'Bahrain', 'Bangladesch',
        'Barbados', 'Belarus', 'Belgien', 'Belize', 'Benin', 'Bermuda',
        'Bhutan', 'Bolivien', 'Bosnien und Herzegowina', 'Botsuana',
        'Bouvetinsel', 'Brasilien', 'Britische Jungferninseln',
        'Britisches Territorium im Indischen Ozean', 'Brunei Darussalam',
        'Bulgarien', 'Burkina Faso', 'Burundi', 'Chile', 'China', 'Cookinseln',
        'Costa Rica', 'Côte d’Ivoire', 'Demokratische Republik Kongo',
        'Demokratische Volksrepublik Korea', 'Deutschland', 'Dominica',
        'Dominikanische Republik', 'Dschibuti', 'Dänemark', 'Ecuador',
        'El Salvador', 'Eritrea', 'Estland', 'Falklandinseln', 'Fidschi',
        'Finnland', 'Frankreich', 'Französisch-Guayana',
        'Französisch-Polynesien', 'Färöer', 'Gabun', 'Gambia', 'Georgien',
        'Ghana', 'Gibraltar', 'Grenada', 'Griechenland', 'Grönland',
        'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
        'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard- und McDonald-Inseln',
        'Honduras', 'Indien', 'Indonesien', 'Irak', 'Iran', 'Irland', 'Island',
        'Isle of Man', 'Israel', 'Italien', 'Jamaika', 'Japan', 'Jemen',
        'Jersey', 'Jordanien', 'Kaimaninseln', 'Kambodscha', 'Kamerun',
        'Kanada', 'Kap Verde', 'Kasachstan', 'Katar', 'Kenia', 'Kirgisistan',
        'Kiribati', 'Kokosinseln', 'Kolumbien', 'Komoren', 'Kongo', 'Kroatien',
        'Kuba', 'Kuwait', 'Laos', 'Lesotho', 'Lettland', 'Libanon', 'Liberia',
        'Libyen', 'Liechtenstein', 'Litauen', 'Luxemburg', 'Madagaskar',
        'Malawi', 'Malaysia', 'Malediven', 'Mali', 'Malta', 'Marokko',
        'Marshallinseln', 'Martinique', 'Mauretanien', 'Mauritius', 'Mayotte',
        'Mazedonien', 'Mexiko', 'Mikronesien', 'Monaco', 'Mongolei',
        'Montenegro', 'Montserrat', 'Mosambik', 'Myanmar', 'Namibia', 'Nauru',
        'Nepal', 'Neukaledonien', 'Neuseeland', 'Nicaragua', 'Niederlande',
        'Niederländische Antillen', 'Niger', 'Nigeria', 'Niue', 'Norfolkinsel',
        'Norwegen', 'Nördliche Marianen', 'Oman', 'Osttimor', 'Pakistan',
        'Palau', 'Palästinensische Gebiete', 'Panama', 'Papua-Neuguinea',
        'Paraguay', 'Peru', 'Philippinen', 'Pitcairn', 'Polen', 'Portugal',
        'Puerto Rico', 'Republik Korea', 'Republik Moldau', 'Ruanda',
        'Rumänien', 'Russische Föderation', 'Réunion', 'Salomonen', 'Sambia',
        'Samoa', 'San Marino', 'Saudi-Arabien', 'Schweden', 'Schweiz',
        'Senegal', 'Serbien', 'Serbien und Montenegro', 'Seychellen',
        'Sierra Leone', 'Simbabwe', 'Singapur', 'Slowakei', 'Slowenien',
        'Somalia', 'Sonderverwaltungszone Hongkong',
        'Sonderverwaltungszone Macao', 'Spanien', 'Sri Lanka',
        'St. Barthélemy', 'St. Helena', 'St. Kitts und Nevis', 'St. Lucia',
        'St. Martin', 'St. Pierre und Miquelon',
        'St. Vincent und die Grenadinen', 'Sudan', 'Suriname',
        'Svalbard und Jan Mayen', 'Swasiland', 'Syrien',
        'São Tomé und Príncipe', 'Südafrika',
        'Südgeorgien und die Südlichen Sandwichinseln', 'Tadschikistan',
        'Taiwan', 'Tansania', 'Thailand', 'Togo', 'Tokelau', 'Tonga',
        'Trinidad und Tobago', 'Tschad', 'Tschechische Republik', 'Tunesien',
        'Turkmenistan', 'Turks- und Caicosinseln', 'Tuvalu', 'Türkei',
        'Uganda', 'Ukraine', 'Ungarn', 'Uruguay', 'Usbekistan', 'Vanuatu',
        'Vatikanstadt', 'Venezuela', 'Vereinigte Arabische Emirate',
        'Vereinigte Staaten', 'Vereinigtes Königreich', 'Vietnam',
        'Wallis und Futuna', 'Weihnachtsinsel', 'Westsahara',
        'Zentralafrikanische Republik', 'Zypern', 'Ägypten',
        'Äquatorialguinea', 'Äthiopien', 'Äußeres Ozeanien', 'Österreich',
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
