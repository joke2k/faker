from .. import BaseProvider


class Provider(BaseProvider):
    # Derived from KSH's FEOR'08
    jobs = (
        'Titkár(nő)',
        'Értékbecslő',
        'Közterület-felügyelő',
        'Építőmérnök',
        'Köszörűs',
        'Gépjármű- és motorkarbantartó',
        'Mezőgazdasági mérnök',
        'Számítógéphálózat- és rendszertechnikus',
        'Adósságbehajtó',
        'Fémöntőminta-készítő',
        'Gyümölcs- és zöldségfeldolgozó',
        'Telekommunikációs mérnök',
        'Könyv- és lapkiadó szerkesztője',
        'Geológus',
        'Manikűrös',
        'Energetikus',
        'Kézbesítő',
        'Kontroller',
        'Mentőtiszt',
        'Háztartási takarító és kisegítő',
        'Dekoratőr',
        'Tejfeldolgozó',
        'Gyógytornász',
        'Csomagkihordó',
        'Kádár',
        'Színész',
        'Anyaggazdálkodó',
        'Szoftverfejlesztő',
        'Adó- és illetékhivatali ügyintéző',
        'Utaskísérő',
        'Táj- és kertépítészmérnök',
        'Muzeológus',
        'Koreográfus',
        'Tetőfedő',
        'Telepőr',
        'Pedikűrös',
        'Fémfeldolgozó',
        'Intézményi takarító és kisegítő',
        'Irodai szakmai irányító',
        'Recepciós',
        'Gépíró, szövegszerkesztő',
        'Ifjúságsegítő',
        'Pap',
        'Adatbázis- és hálózati elemző',
        'Szoftver- és alkalmazásfejlesztő',
        'Burkoló',
        'Történész',
        'Intézményi takarító és kisegítő ',
        'Kohó- és anyagtechnikus',
        'Jogi asszisztens',
        'Tőzsde- és pénzügyi ügynök',
        'Varró',
        'Bolti pénztáros',
        'Kémikus',
        'Kőműves',
        'Szakorvos',
        'Elemző közgazdász',
        'Kézi mosó, vasaló',
        'Irattáros',
        'Földmérő és térinformatikus',
        'Vendéglős',
        'Élelmiszer-ipari mérnök',
        'Kisállattartó és -tenyésztő',
        'Szociológus',
        'Lakatos',
        'Pszichológus',
        'Utcaseprő',
        'Adatbázis-tervező és -üzemeltető',
        'Gyermekfelügyelő',
        'Metróvezető',
        'Háztartási alkalmazott',
        'Könyvelő',
        'Általános irodai adminisztrátor',
        'Épületasztalos',
        'Ékszerkészítő',
        'Üvegező',
        'Könyvtári, levéltári nyilvántartó',
        'Általános iskolai tanár, tanító',
        'Szemétgyűjtő',
        'Rendőr',
        'Orvosi laboratóriumi asszisztens',
        'Kubikos',
        'Adatrögzítő',
        'Informatikatanár',
        'Fizikus',
        'Vegyésztechnikus',
        'Hímző',
        'Ügynök',
        'Kalapos',
        'Egyéb művészetek tanára',
        'Zöldségtermesztő',
        'Dísznövény-, virág- és faiskolai kertész, csemetenevelő',
        'Csipkeverő',
        'Postai ügyfélkapcsolati foglalkozású',
        'Tolmács',
        'Kódoló',
        'Fa- és könnyűipari mérnök',
        'Szarvasmarha-, ló-, sertés-, juhtartó és -tenyésztő ',
        'Település- és közlekedéstervező mérnök',
        'Rendszergazda',
        'Állatorvosi asszisztens',
        'Újságíró',
        'Piaci, utcai étel- és italárus',
        'Néprajzkutató',
        'Vám- és pénzügyőr',
        'Hordár',
        'Webrendszer-technikus',
        'Hivatalsegéd',
        'Üzletpolitikai elemző',
        'Fogorvos',
        'Statisztikus',
        'Stukkózó',
        'Utazásszervező',
        'Épületbádogos',
        'Szociális gondozó',
        'Villamosipari technikus (elektronikai technikus)',
        'Iratkezelő',
        'Matróz',
        'Trolibuszvezető',
        'Banki pénztáros',
        'Szikvízkészítő',
        'Kovács',
        'Minőségbiztosítási mérnök',
        'Csillagász',
        'Író',
        'Könyvtáros',
        'Fényképész',
        'Bányászati technikus',
        'Üzletpolitikai elemző, szervező',
        'Jelnyelvi tolmács',
        'Alkalmazásprogramozó',
        'Cipőkészítő',
        'Drágakőcsiszoló',
        'Botanikus',
        'Járműtakarító',
        'Biztosítási ügynök',
        'Gépészmérnök',
        'Légiforgalmi irányító',
        'Üveggyártó',
        'Gumitermékgyártó',
        'Repülőgépmotor-karbantartó',
        'Építészmérnök',
        'Tűzoltó',
        'Könyvkötő',
        'Pultos',
        'Borász',
        'Gyógyszerész',
        'Kozmetikus',
        'Segédápoló',
        'Ápoló',
        'Fordító',
        'Munkavédelmi és üzembiztonsági foglalkozású',
        'Végrehajtó, adósságbehajtó',
        'Gyógyszertári asszisztens',
        'Szőrmefestő',
        'Bőrtermékkészítő',
        'Műsorszóró és audiovizuális technikus',
        'Kártevőirtó',
        'Rakodómunkás',
        'Szabásminta-készítő',
        'Hulladékosztályozó',
        'Erdő- és természetvédelmi mérnök',
        'Készlet- és anyagnyilvántartó',
        'Fogászati asszisztens',
        'Séf',
        'Könyvszakértő',
        'Bróker',
        'Áru- és divatbemutató',
        'Kölcsönző',
        'Épületgondnok',
        'Telekommunikációs technikus',
        'Környezetvédelmi technikus',
        'Házvezető',
        'Famegmunkáló',
        'Szállodai recepciós',
        'Kézi csomagoló',
        'Ötvös',
        'Csecsemő- és kisgyermeknevelő',
        'Kerékpár-karbantartó',
        'Operatőr',
        'Ügyvéd',
        'Szigetelő',
        'Fizioterápiás asszisztens',
        'Kereskedő',
        'Biológus',
        'Ruházati gép kezelője és gyártósor mellett dolgozó',
        'Szűcs',
        'Ügyféltájékoztató',
        'Gyógynövénytermesztő',
        'Lelkész',
        'Énekes',
        'Munka- és termelésszervező ',
        'Légiforgalmi irányítástechnikus',
        'Számítógép-hálózati elemző',
        'Szabó',
        'Szakács',
        'Növényorvos ',
        'Testőr',
        'Erdő- és természetvédelmi technikus',
        'Kőfaragó',
        'Bányászati szakmai irányító',
        'Régész',
        'Lakossági kérdező',
        'Számviteli ügyintéző',
        'Természetvédelmi őr',
        'Egyetemi, főiskolai oktató',
        'Óvodapedagógus',
        'Gyomírtó',
        'Növényvédelmi szakértő',
        'Védőnő',
        'Egészségügyi dokumentátor ',
        'Finommechanikai műszerész',
        'Műszaki rajzoló',
        'Demográfus',
        'Általános orvos',
        'Fedélzeti tiszt',
        'Vagyonőr',
        'Rendszerelemző',
        'Tímár',
        'Hajózómérnök',
        'Hálózat- és multimédia-fejlesztő',
        'Konyhai kisegítő',
        'Mozigépész',
        'Épületvillamossági szerelő',
        'Bionövény-termesztő',
        'Fogtechnikus',
        'Büntetés-végrehajtási őr',
        'Erdész',
        'Vízgazdálkodási gépkezelő',
        'Szerszámkészítő',
        'Vegyészmérnök',
        'Festő',
        'Iratkezelő, irattáros',
        'Légiforgalmi irányítástechnikai berendezések üzemeltetője',
        'Masszőr',
        'Zenetanár',
        'Zálogházi ügyintéző és pénzkölcsönző',
        'Jogtanácsos',
        'Tehergépkocsi-vezető',
        'Bolti eladó',
        'Pénzintézeti ügyintéző',
        'Növényorvosi asszisztens',
        'Fitnesz- és rekreációs program irányítója',
        'Zeneszerző',
        'Építményszerkezet-szerelő',
        'Vegyes profilú gazdálkodó',
        'Pultfeltöltő',
        'Képzőművész',
        'Végrehajtó',
        'Szerencsejáték-szervező',
        'Jegypénztáros',
        'Konyhafőnök',
        'Műtőssegéd',
        'Adótanácsadó',
        'Jogász',
        'Orvosi képalkotó diagnosztikai asszisztens',
        'Zoológus',
        'Látszerész',
        'Szállítási, szállítmányozási nyilvántartó',
        'Kárpitos',
        'Házi gondozó',
        'Táncművész',
        'Cipész',
        'Élelmiszer-ipari technikus',
        'Zenész',
        'Könyvelő (analitikus)',
        'Felvásárló',
        'Személyzeti és pályaválasztási szakértő',
        'Bányamérnök',
        'Pincér',
        'Mosodai gép kezelője',
        'Dietetikus',
        'Rendező',
        'Bognár',
        'Targoncavezető',
        'Hobbiállat-gondozó',
        'Segédrendező',
        'Marketing- és PR-ügyintéző',
        'Bőrdíszműves',
        'Darukezelő',
        'Hallás- és beszédterapeuta',
        'Konduktor',
        'Villamosmérnök (energetikai mérnök)',
        'Meteorológus',
        'Táplálkozási tanácsadó',
        'Cirkuszi előadóművész',
        'Húsfeldolgozó',
        'Vezető eladó',
        'Könyvvizsgáló',
        'Feldolgozóipari szakmai irányító',
        'Pedagógiai szakértő',
        'Telefonos értékesítési ügynök',
        'Villamosvezető',
        'Baromfitartó és -tenyésztő',
        'Politológus',
        'Mérőóra-leolvasó',
        'Egyéb növénytermesztési foglalkozású',
        'Méhész',
        'Felvonószerelő',
        'Személygépkocsi-vezető',
        'Textilműves',
        'Építő- és építésztechnikus',
        'Bőröndös',
        'Gipszkartonozó',
        'Kalauz',
        'Járművezető-oktató',
        'Bérelszámoló',
        'Bútorasztalos',
        'Villanyszerelő',
        'Kesztyűs',
        'Nyomdai előkészítő',
        'Mezőgazdasági technikus',
        'Szőlő-, gyümölcstermesztő',
        'Oktatási asszisztens',
        'Édesiparitermék-gyártó',
        'Fodrász',
        'Nyomdász',
        'Keramikus',
        'Általános egészségügyi asszisztens',
        'Ács',
        'Kereskedelmi ügyintéző',
        'Környezetfelmérő',
        'Kéményseprő',
        'Fotó- és mozgófilmlaboráns',
        'Statisztikai ügyintéző',
        'Szakképzett edző',
        'Fa- és könnyűipari technikus',
        'Múzeumi gyűjteménygondnok',
        'Árufeltöltő',
        'Idegenvezető',
        'Mozdonyvezető',
        'Kohó- és anyagmérnök',
        'Műköves',
        'Állatorvos',
        'Földmérő és térinformatikai technikus ',
        'Nyelvtanár',
        'Ügyész',
        'Sportoló',
        'Címfestő',
        'Nyelvész',
        'Gyógypedagógus',
        'Üzemanyagtöltő állomás kezelője',
        'Fémcsiszoló',
        'Kulturális szervező',
        'Lakberendező',
        'Grafikus és multimédia-tervező ',
        'Középiskolai tanár',
        'Cukrász',
        'Légijármű-vezető',
        'Sportszervező',
        'Parkolóőr',
        'Favágó',
        'Matematikus',
        'Pénzügyi elemző és befektetési tanácsadó',
        'Konferencia- és rendezvényszervező',
        'Faesztergályos',
        'Kályha- és kandallóépítő',
        'Közjegyző',
        'Festékszóró',
        'Statiszta',
        'Minőségbiztosítási technikus',
        'Épületszerkezet-tisztító',
        'Menetjegyellenőr',
        'Kereskedelmi tervező ',
        'Munkaerő-piaci szolgáltatási ügyintéző',
        'Adószakértő',
        'Hegesztő',
        'Gyorséttermi eladó',
        'Iparművész',
        'Díszítő',
        'Szociálpolitikus',
        'Gyártmány- és ruhatervező',
        'Ingatlanforgalmazási ügyintéző',
        'Kormányos',
        'Díszletező',
        'Segédszínész',
        'Levéltáros',
        'Robbantómester',
        'Villamosipari technikus (energetikai technikus)',
        'Ortopédiai eszközkészítő',
        'Gépésztechnikus',
        'Szociális segítő',
        'Pék',
        'Ipari alpinista',
        'Villamosmérnök (elektronikai mérnök)',
        'Személyi asszisztens',
        'Ablaktisztító',
        'Portás',
        'Filozófus',
        'Forgácsoló',
        'Bábművész',
        'Kárszakértő',
        'Humánpolitikai adminisztrátor',
        'Hangszerkészítő',
        'Társadalombiztosítási és segélyezési hatósági ügyintéző',
        'Optometrista',
        'Szántóföldinövény-termesztő',
        'Ingatlanügynök',
        'Nyomozó',
        'Egyéb, máshova nem sorolható technikus',
        'Vezető takarító',
        'Autóbuszvezető',
        'Kárbecslő',
        'Piaci árus',
        'Bíró',
        'Általános iskolai tanár',
        'Szerszámköszörűs',
        'Építőipari szakmai irányító')

    def job(self):
        return self.random_element(self.jobs)
