	_|_|_|_|          _|
	_|        _|_|_|  _|  _|      _|_|    _|  _|_|
	_|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
	_|      _|    _|  _|  _|    _|        _|
	_|        _|_|_|  _|    _|    _|_|_|  _|


*Faker* is a Python package that generates fake data for you. Whether you need to bootstrap your database,
create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service,
Faker is for you.

Faker is heavily inspired by PHP's [Faker][php-faker], Perl's [Data::Faker][perl-faker], and by ruby's [Faker][ruby-faker].

[![Build Status](https://travis-ci.org/joke2k/faker.png)](https://travis-ci.org/joke2k/faker)
[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/joke2k/faker/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
[![Coverage Status](https://coveralls.io/repos/joke2k/faker/badge.png?branch=master)](https://coveralls.io/r/joke2k/faker?branch=master)
[![PyPI version](https://badge.fury.io/py/fake-factory.png)](http://badge.fury.io/py/fake-factory)
[![Downloads](https://pypip.in/d/fake-factory/badge.png)](https://crate.io/packages/fake-factory)

## Basic Usage

Install with pip:

    pip install fake-factory

Use `faker.Factory.create()` to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

```python

    from faker import Factory
    fake = Factory.create()

    # OR
    from faker import Faker
    fake = Faker()

    fake.name()
    # 'Lucy Cechtelar'

    fake.address()
    # "426 Jordy Lodge
    #  Cartwrightshire, SC 88120-6700"

    fake.text()
    # Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
    # beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
    # amet quidem. Iusto deleniti cum autem ad quia aperiam.
    # A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
    # quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
    # voluptatem sit aliquam. Dolores voluptatum est.
    # Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
    # Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
    # Et sint et. Ut ducimus quod nemo ab voluptatum.
```

Each call to method `fake.name()` yields a different (random) result.
This is because faker forwards `faker.Generator.method_name()` calls to `faker.Generator.format(method_name)`.

```python

for i in range(0,10):
  print fake.name()

	# Adaline Reichel
	# Dr. Santa Prosacco DVM
	# Noemy Vandervort V
	# Lexi O'Conner
	# Gracie Weber
	# Roscoe Johns
	# Emmett Lebsack
	# Keegan Thiel
	# Wellington Koelpin II
	# Ms. Karley Kiehn V
```


## Formatters

Each of the generator properties (like `name`, `address`, and `lorem`) are called "formatters".
A faker generator has many of them, packaged in "providers". Here is a list of the bundled formatters in the default locale.


### faker.providers.base

	fake.random_digit_not_null()                                             # 1
	fake.randomize_nb_elements(number=10, le=False, ge=False)                # 13
	fake.random_letter()                                                     # S
	fake.random_digit()                                                      # 6
	fake.bothify(text="## ??")                                               # 05 Gm
	fake.random_element(array=('a', 'b', 'b'))                               # b
	fake.random_number(digits=None)                                          # 38
	fake.lexify(text="????")                                                 # gJPH
	fake.random_int(min=0, max=9999)                                         # 2355
	fake.numerify(text="###")                                                # 646

### faker.providers.lorem

	fake.text(max_nb_chars=200)                                              # Quam quibusdam iusto commodi velit. Earum voluptatibus officiis suscipit. Sed
	                                                                            ut nesciunt iste.
	fake.sentence(nb_words=6, variable_nb_words=True)                        # Ut beatae distinctio aliquid placeat mollitia.
	fake.word()                                                              # rem
	fake.paragraphs(nb=3)                                                    # [u'Aliquid repellat dolores sed autem et. Voluptatem nisi sint quae aut autem
	                                                                            cupiditate. Delectus ullam nemo tempore et ab aut fuga molestias.', u'Blandi
	                                                                           tiis sint enim id est nostrum aliquid molestiae. Eius sint tempore autem atqu
	                                                                           e consequatur assumenda. Et voluptatem sunt fugiat sunt et.', u'Voluptate lab
	                                                                           orum maiores veniam saepe. Beatae ipsam quam nihil qui qui asperiores. Enim c
	                                                                           ulpa laudantium temporibus quibusdam aliquid. Corporis ut nostrum voluptate e
	                                                                           t sit tempore.']
	fake.words(nb=3)                                                         # [u'consectetur', u'est', u'rerum']
	fake.paragraph(nb_sentences=3, variable_nb_sentences=True)               # Perferendis placeat dolores exercitationem quae ducimus. Magnam debitis eum e
	                                                                           xcepturi at quidem qui. Animi ad cupiditate in.
	fake.sentences(nb=3)                                                     # [u'Accusantium molestiae ut exercitationem voluptatem.', u'Fuga consequatur c
	                                                                           onsequuntur quam molestiae nam.', u'Dolor omnis hic perferendis aut itaque si
	                                                                           t.']

### faker.providers.address

	fake.state_abbr()                                                        # ID
	fake.latitude()                                                          # 76.060836
	fake.street_name()                                                       # Bernadine Vista
	fake.address()                                                           # 59802 Kohler Gateway
	                                                                           Keeblertown, CA 89092
	fake.street_address()                                                    # 39719 Klein Mews
	fake.postcode()                                                          # 97628
	fake.longitude()                                                         # -80.950377
	fake.country()                                                           # Palau
	fake.geo_coordinate()                                                    # 8.572122
	fake.street_suffix()                                                     # Corners
	fake.city_prefix()                                                       # West
	fake.city_suffix()                                                       # burgh
	fake.building_number()                                                   # 26481
	fake.secondary_address()                                                 # Apt. 399
	fake.city()                                                              # East Noemie
	fake.state()                                                             # Kansas

### faker.providers.person

	fake.name()                                                              # Deborah Johnston
	fake.suffix()                                                            # I
	fake.last_name()                                                         # Cummings
	fake.first_name()                                                        # Violet
	fake.prefix()                                                            # Miss

### faker.providers.date_time

	fake.date_time_ad()                                                      # 0335-11-13 23:08:35
	fake.month()                                                             # 11
	fake.am_pm()                                                             # PM
	fake.iso8601()                                                           # 1988-03-30T13:39:34
	fake.date_time_this_century()                                            # 1930-10-08 21:49:52
	fake.date_time()                                                         # 1997-03-13 02:03:24
	fake.month_name()                                                        # June
	fake.date_time_this_month()                                              # 2013-11-04 18:41:20
	fake.date_time_this_decade()                                             # 2010-12-11 02:32:12
	fake.day_of_week()                                                       # Wednesday
	fake.day_of_month()                                                      # 16
	fake.time(pattern="%H:%M:%S")                                            # 11:30:21
	fake.date_time_between(start_date="-30y", end_date="now")                # 2002-10-11 14:57:38
	fake.unix_time()                                                         # 763964108
	fake.date_time_this_year()                                               # 2012-12-11 07:09:57
	fake.timezone()                                                          # Europe/Zurich
	fake.century()                                                           # XVII
	fake.date(pattern="%Y-%m-%d")                                            # 1982-04-26
	fake.year()                                                              # 2000

### faker.providers.company

	fake.company()                                                           # Funk and Sons
	fake.company_suffix()                                                    # and Sons
	fake.catch_phrase()                                                      # Triple-buffered executive focusgroup
	fake.bs()                                                                # brand proactive communities

### faker.providers.internet

	fake.ipv4()                                                              # 131.175.254.102
	fake.url()                                                               # http://www.bernier.com/
	fake.company_email()                                                     # barrows.brandyn@altenwerth.org
	fake.uri()                                                               # http://www.murray.net/about.html
	fake.tld()                                                               # info
	fake.uri_path(deep=None)                                                 # search/main
	fake.free_email()                                                        # gmccullough@gmail.com
	fake.user_name()                                                         # wiza.johnathon
	fake.free_email_domain()                                                 # hotmail.com
	fake.domain_name()                                                       # mertz.com
	fake.uri_extension()                                                     # .jsp
	fake.ipv6()                                                              # 6a67:a71f:ec3c:f641:177f:f33f:fb11:e27b
	fake.safe_email()                                                        # greinger@example.org
	fake.uri_page()                                                          # login
	fake.email()                                                             # dorcas53@hotmail.com
	fake.domain_word()                                                       # bahringer
	fake.slug(value=None)                                                    # maxime-ea-omnis

### faker.providers.misc

	fake.locale()                                                            # cn_TJ
	fake.md5(raw_output=False)                                               # 98063a4419ebc124a94a0fe9411d95ba
	fake.sha1(raw_output=False)                                              # 910aa38699b69228fee09ca0f2fb6e65f987ebd4
	fake.null_boolean()                                                      # False
	fake.sha256(raw_output=False)                                            # 0aed69e82a0abfa4c03dcf17e212c5b0ac08f12751b1acac96553c1abc3352b5
	fake.country_code()                                                      # TG
	fake.language_code()                                                     # pt
	fake.boolean(chance_of_getting_true=50)                                  # True
	fake.password(length=10, special_chars=True, digits=True,\
	              upper_case=True, lower_case=True))                         # bLKB3ehb8@

### faker.providers.phone_number

	fake.phone_number()                                                      # +94(1)6262568403

### faker.providers.user_agent

	fake.mac_processor()                                                     # U; Intel
	fake.firefox()                                                           # Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gecko/2012-01-08 15:31:21 Firefox/
	                                                                           3.8
	fake.linux_platform_token()                                              # X11; Linux x86_64
	fake.opera()                                                             # Opera/8.46.(Windows NT 5.2; it-IT) Presto/2.9.161 Version/11.00
	fake.windows_platform_token()                                            # Windows 95
	fake.internet_explorer()                                                 # Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.1; Trident/3.1)
	fake.user_agent()                                                        # Mozilla/5.0 (X11; Linux i686; rv:1.9.6.20) Gecko/2010-12-19 10:41:34 Firefox/
	                                                                           3.6.17
	fake.chrome()                                                            # Mozilla/5.0 (Windows 98) AppleWebKit/5332 (KHTML, like Gecko) Chrome/15.0.849
	                                                                           .0 Safari/5332
	fake.linux_processor()                                                   # i686
	fake.mac_platform_token()                                                # Macintosh; U; Intel Mac OS X 10_7_4
	fake.safari()                                                            # Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_3 rv:2.0; it-IT) AppleWebKit/532
	                                                                           .47.1 (KHTML, like Gecko) Version/5.0.5 Safari/532.47.1

### faker.providers.file

	fake.mime_type(category=None)                                            # video/mpeg

### faker.providers.ssn
	fake.ssn()                                                               # 856-98-8232

### faker.providers.python

	fake.pyiterable(nb_elements=10, variable_nb_elements=True, *value_types) # set([Decimal('7.2022029784E+11'), Decimal('7.80290776173E+12'), u'Dolor imped
	                                                                           it quia.', 3014507.7827, u'ramiro.carter@schumm.org', 4443, u'Sed iusto magna
	                                                                           m.'])
	fake.pystr(max_chars=20)                                                 # Nulla odit ex fuga.
	fake.pyfloat(left_digits=None, right_digits=None, positive=False)        # 69950445.94
	fake.pystruct(count=10, *value_types)                                    # ([u'Corporis excepturi.', -6.3746979, 8874, 641.670735144, u'Dolores ut aut v
	                                                                           el.', u'Non cumque.', datetime(1988, 1, 10, 18, 20, 26), u'http://cronin.info
	                                                                           /search/category/search.htm', -543720939267106.0, u'Est dignissimos et.'], {u
	                                                                           'neque': datetime(2002, 10, 12, 1, 41, 44), u'sit': u'Et sed ut nisi.', u'arc
	                                                                           hitecto': u'Minus sunt quos.', u'numquam': u'Officiis in.', u'esse': Decimal(
	                                                                           '851592439.65'), u'ex': 55651.0, u'praesentium': u'Beatae excepturi.', u'dolo
	                                                                           rem': Decimal('-3.49169242935E+13'), u'vel': u'Exercitationem.', u'quo': date
	                                                                           time(2003, 2, 7, 2, 16, 28)}, {u'consequuntur': {9: u'Eaque quis autem.', 10:
	                                                                            [-922275532.2, u'Incidunt aut.', u'Et sint excepturi.'], 11: {9: datetime(19
	                                                                           77, 9, 27, 4, 49, 32), 10: u'Est sunt.', 11: [u'victoria.blick@littel.info',
	                                                                           u'Quos aut quo.']}}, u'non': {2: 6716, 3: [29014.550976, u'Praesentium.', 870
	                                                                           4], 4: {2: 3649, 3: datetime(1979, 11, 8, 9, 59, 37), 4: [u'http://langworthr
	                                                                           osenbaum.org/register/', Decimal('62790.0')]}}, u'est': {5: u'Maxime incidunt
	                                                                           .', 6: [-9.5832, u'http://www.nitzsche.biz/search/search/author.htm', u'Cum s
	                                                                           uscipit dolor.'], 7: {5: u'Consequuntur autem.', 6: 1684, 7: [u'http://rath.c
	                                                                           om/posts/homepage/', u'Ea sit error.']}}, u'voluptatum': {4: u'Omnis omnis op
	                                                                           tio.', 5: [u'Voluptatibus.', u'Numquam qui qui.', u'http://bahringer.com/auth
	                                                                           or/'], 6: {4: datetime(1976, 6, 3, 20, 42, 52), 5: Decimal('12939334042.1'),
	                                                                           6: [u'Vel sed similique.', Decimal('-968.39980246')]}}, u'voluptas': {8: {8:
	                                                                           [u'Vel rerum quia.', u'Aperiam officiis in.'], 6: u'Ipsa non beatae.', 7: u'h
	                                                                           ttp://donnelly.com/terms/'}, 6: Decimal('-35.6'), 7: [9534, 1605, Decimal('-4
	                                                                           .21540418737E+12')]}, u'molestiae': {0: -811865398.937, 1: [u'Ipsum quos in o
	                                                                           mnis.', 4467, u'Nobis.'], 2: {0: u'Rerum alias dolorem.', 1: u'http://pfanner
	                                                                           still.com/home.html', 2: [u'Aut et officiis.', u'jackie.gottlieb@hotmail.com'
	                                                                           ]}}, u'enim': {1: u'Beatae nam ut odio.', 2: [u'Et aut aut quasi.', u'Saepe o
	                                                                           fficiis.', u'http://gusikowski.biz/'], 3: {1: 7259, 2: u'alex.farrell@walker.
	                                                                           com', 3: [u'http://www.tromp.com/blog/tags/privacy.php', Decimal('57290273.37
	                                                                           2')]}}, u'molestias': {8: datetime(1978, 1, 10, 19, 59, 3), 9: [52692718.897,
	                                                                            u'http://www.quitzon.com/', 113896345221807.0], 10: {8: u'mariane50@hotmail.
	                                                                           com', 9: u'eric.emmerich@hand.biz', 10: [4015, 1200]}}, u'et': {8: [u'Est dig
	                                                                           nissimos.', -582365.7420196, u'Et odit laborum ut.'], 9: {8: Decimal('-1.9923
	                                                                           2256052E+13'), 9: [u'Enim consequatur.', u'http://www.huels.com/tag/main/tags
	                                                                           /index.asp'], 7: u'Praesentium.'}, 7: 1035}, u'atque': {3: u'Repellendus fugi
	                                                                           t.', 4: [u'kvolkman@bodejast.com', u'Nam saepe nihil et.', u'Officiis quo.'],
	                                                                            5: {3: 7778, 4: 4111, 5: [u'reichel.katharina@schulist.com', datetime(1984,
	                                                                           12, 22, 6, 38, 11)]}}})
	fake.pydecimal(left_digits=None, right_digits=None, positive=False)      # 813138968.731
	fake.pylist(nb_elements=10, variable_nb_elements=True, *value_types)     # [u'Dignissimos.', u'http://www.boganhintz.com/categories/categories/homepage.
	                                                                           php', u'sanford.magnolia@hotmail.com', u'At non aliquid.', 7741, 87500826857.
	                                                                           2962, u'ralph02@aufderharpollich.com', 7686, u'http://koelpindouglas.org/tags
	                                                                           /blog/terms.html', u'Voluptas ea natus.', 7165, u'Doloremque earum.', 1823]
	fake.pytuple(nb_elements=10, variable_nb_elements=True, *value_types)    # (u'tokuneva@kling.org', u'A dolorem.', 6377, u'Ullam corrupti.', u'Eos deseru
	                                                                           nt.', u'Nihil quia.', 5019)
	fake.pybool()                                                            # True
	fake.pyset(nb_elements=10, variable_nb_elements=True, *value_types)      # set([u'osvaldo06@gmail.com', 4298, datetime(1977, 6, 8, 5, 15, 47), u'rempel.
	                                                                           eliezer@rutherford.com', u'Velit quae.', u'Temporibus.', u'Aut accusantium.']
	                                                                           )
	fake.pydict(nb_elements=10, variable_nb_elements=True, *value_types)     # {u'eum': u'Repudiandae.', u'velit': u'Aliquam optio ut.', u'commodi': u'Moles
	                                                                           tiae autem.', u'quis': u'quigley.christian@gmail.com', u'accusamus': Decimal(
	                                                                           '-14.48787'), u'ut': 61715747966374.0, u'error': u'Occaecati explicabo.', u'f
	                                                                           acilis': u'Et vitae totam.', u'enim': u'Quam repellat.', u'explicabo': dateti
	                                                                           me(1985, 2, 23, 1, 28, 19), u'officiis': u'Et id culpa sequi.', u'labore': u'
	                                                                           Aut tempore culpa.'}
	fake.pyint()                                                             # 4166

### faker.providers.credit_card

	fake.credit_card_security_code(card_type=None)                           # 816
	fake.credit_card_full(card_type=None, validate=False, max_check=10)      #
	                                                                           American Express
	                                                                           Ralph Bartoletti
	                                                                           379037504006334  12/18
	                                                                           CVC: 686
	fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")    # 06/15
	fake.credit_card_number(card_type=None, validate=False, max_check=10)    # 201493034311625
	fake.credit_card_provider(card_type=None)                                # VISA 13 digit

## Localization

`faker.Factory` can take a locale as an argument, to return localized data.
If no localized provider is found, the factory fallbacks to the default locale (en_EN).

    from faker import Factory
    fake = Factory.create('it_IT')
    for i in range(0,10):
        print fake.name()

    > Elda Palumbo
    > Pacifico Giordano
    > Sig. Avide Guerra
    > Yago Amato
    > Eustachio Messina
    > Dott. Violante Lombardo
    > Sig. Alighieri Monti
    > Costanzo Costa
    > Nazzareno Barbieri
    > Max Coppola

You can check available Faker locales in the source code, under the providers package.
The localization of Faker is an ongoing process, for which we need your help.
Don't hesitate to create localized providers to your own locale and submit a PR!

Some example of included localized providers:

## LANGUAGE it_IT

### faker.providers.address

	fake.state_abbr()             # RA
	fake.latitude()               # -99.579871
	fake.street_name()            # Canale Conti
	fake.address()                # Borgo Nabil 59 Appartamento 21
	                                Quarto Brigitta ligure, 36534 Pavia (VR)
	fake.street_address()         # Canale Gianriccardo 743
	fake.postcode()               # 61219
	fake.longitude()              # -4.116482
	fake.country()                # Isole Falkland (Malvinas)
	fake.geo_coordinate()         # -46.328470
	fake.street_suffix()          # Borgo
	fake.city_prefix()            # San
	fake.city_suffix()            # sardo
	fake.building_number()        # 06
	fake.secondary_address()      # Piano 7
	fake.city()                   # Borgo Tristano umbro
	fake.state()                  # Terni

### faker.providers.person

	fake.name()                   # Sig. Cesidia De Angelis
	fake.last_name()              # Neri
	fake.first_name()             # Gianmarco
	fake.prefix()                 # Dott.

### faker.providers.company

	fake.company()                # Bianchi SPA
	fake.company_suffix()         # e figli
	fake.catch_phrase()           # Migrazione stand-alone logistica
	fake.bs()                     # webservices evolutive verticalizzate

### faker.providers.phone_number

	fake.phone_number()           # +23 42 2530333

## LANGUAGE fr_FR

### faker.providers.address

	fake.address()                      # 87, boulevard de Nguyen
	                                      18 421 Bernier
	fake.latitude()                     # 18.516947
	fake.department_number()            # 81
	fake.street_name()                  # boulevard de Herve
	fake.department()                   # (u'38', u'Is\xe8re')
	fake.department_name()              # Finistère
	fake.street_address()               # 26, rue René Ribeiro
	fake.postcode()                     # 86 828
	fake.longitude()                    # -98.262211
	fake.country()                      # Guatemala
	fake.geo_coordinate()               # 111.305524
	fake.street_prefix()                # boulevard
	fake.street_suffix()                # Street
	fake.city_suffix()                  # -la-Forêt
	fake.building_number()              # 621
	fake.region()                       # Wallis-et-Futuna
	fake.city()                         # Rodrigues

### faker.providers.person

	fake.name()                         # Léon Thierry
	fake.last_name()                    # Jourdan
	fake.first_name()                   # Isaac
	fake.prefix()                       # de

### faker.providers.company

	fake.company()                      # Colas Grondin et Fils
	fake.company_suffix()               # S.A.
	fake.catch_phrase_verb()            # d'atteindre vos buts
	fake.catch_phrase()                 # L'avantage de rouler autrement
	fake.catch_phrase_noun()            # le droit
	fake.siren()                        # 575 730 129
	fake.siret(max_sequential_digits=2) # 205 560 539 00917
	fake.catch_phrase_attribute()       # plus facilement

### faker.providers.internet

	fake.ipv4()                         # 6.14.119.96
	fake.url()                          # http://www.langlois.com/
	fake.company_email()                # michaud.honore@fontaine.com
	fake.uri()                          # http://www.navarro.com/index.htm
	fake.tld()                          # com
	fake.uri_path(deep=None)            # blog/wp-content
	fake.free_email()                   # guerin.daniel@ifrance.com
	fake.user_name()                    # vincent53
	fake.free_email_domain()            # live.com
	fake.domain_name()                  # monnier.com
	fake.uri_extension()                # .htm
	fake.ipv6()                         # c578:0382:cf59:46e8:98e3:7c13:c5b6:91a6
	fake.safe_email()                   # josephine.guilbert@example.net
	fake.uri_page()                     # register
	fake.email()                        # martine74@caron.fr
	fake.domain_word()                  # bodin
	fake.slug(value=None)               # voluptas-ut-autem

### faker.providers.phone_number

	fake.phone_number()                 # +33 4 38 41 91 92

## LANGUAGE pt_BR

### faker.providers.address

	fake.estado_nome()            # Rio de Janeiro
	fake.latitude()               # -106.011949
	fake.street_name()            # Vereda Ribeiro
	fake.street_prefix()          # Rodovia
	fake.address()                # Conjunto Pereira, 775
	                                Acaiaca
	                                08618559 Barbosa de Cunha / RS
	fake.street_address()         # Praça Martins, 48
	fake.bairro()                 # São João Batista
	fake.longitude()              # -160.626433
	fake.country()                # Sudão
	fake.geo_coordinate()         # 21.660349
	fake.estado_sigla()           # PI
	fake.street_suffix()          # Street
	fake.city_suffix()            # de Minas
	fake.building_number()        # 94
	fake.estado()                 # (u'MA', u'Maranh\xe3o')
	fake.city()                   # Cunha
	fake.postcode()               # 92673-460

### faker.providers.person

	fake.name()                   # Sabrina Martins
	fake.last_name()              # Rocha
	fake.first_name()             # Maitê
	fake.prefix()                 # do

### faker.providers.company

	fake.company()                # Lima Azevedo e Filhos
	fake.company_suffix()         # - EI

### faker.providers.internet

	fake.ipv4()                   # 221.193.94.76
	fake.url()                    # http://www.carvalho.com/
	fake.company_email()          # thiago.gomes@costela.br
	fake.uri()                    # http://www.souza.com/search/author/
	fake.tld()                    # br
	fake.uri_path(deep=None)      # explore/tags/category
	fake.free_email()             # rafaela04@gmail.com
	fake.user_name()              # alexia.pinto
	fake.free_email_domain()      # uol.com.br
	fake.domain_name()            # ferreira.com
	fake.uri_extension()          # .jsp
	fake.ipv6()                   # 5f15:bd2b:fa0f:0d20:4e4d:3ab6:7eb7:0904
	fake.safe_email()             # vitor38@example.br
	fake.uri_page()               # author
	fake.email()                  # bianca.dias@dias.com
	fake.domain_word()            # castro
	fake.slug(value=None)         # magnam-consequatur

### faker.providers.phone_number

	fake.phone_number()           # +55 71 8130 0097

## LANGUAGE de_DE

### faker.providers.address

	fake.address()              # Rosenowring 437
	                              43872 Regen
	fake.latitude()             # 42.7075055
	fake.street_name()          # Hanne-Faust-Straße
	fake.street_address()       # Sonya-Ullmann-Weg 8/3
	fake.postcode()             # 40685
	fake.longitude()            # 70.895020
	fake.country()              # Guinea
	fake.geo_coordinate()       # 75.306346
	fake.building_number()      # 5
	fake.state()                # Saarland
	fake.city()                 # Wolgast

### faker.providers.person

	fake.name()                 # Herr Falk Blümel
	fake.last_name()            # Rose
	fake.first_name()           # Erika
	fake.prefix()               # Ing.
	fake.prefix_male()          # Prof.
	fake.prefix_female()        # Univ.Prof.
	fake.suffix()               # B.Sc.

### faker.providers.company

	fake.company()              # Barth Ruppersberger GmbH
	fake.company_suffix()       # AG & Co. OHG

### faker.providers.internet

	fake.ipv4()                 # 84.192.240.173
	fake.url()                  # http://www.loewer.com/
	fake.company_email()        # hornich.berthold@albers.com
	fake.uri()                  # http://www.trubin.org/wp-content/app/home/
	fake.tld()                  # net
	fake.uri_path(deep=None)    # posts/tag
	fake.free_email()           # cweimer@gmx.de
	fake.user_name()            # zsteckel
	fake.free_email_domain()    # gmx.de
	fake.domain_name()          # lehmann.com
	fake.uri_extension()        # .jsp
	fake.ipv6()                 # ad0b:fa6d:d23f:af56:48a8:68d4:97f0:7cb8
	fake.safe_email()           # tfreudenberger@example.com
	fake.uri_page()             # register
	fake.email()                # zaenker.gisbert@kensy.org
	fake.domain_word()          # salz
	fake.slug(value=None)       # cupiditate-officia

### faker.providers.phone_number

	fake.phone_number()         # +49 (0) 8561 046769

## LANGUAGE fi_FI

### faker.providers.address

	fake.address()             # Kirsikkatie 388
	                           # 40559 Kiuruvesi     
	fake.street_name()         # Banaanikuja
	fake.country()             # Norsunluurannikko
	fake.city()                # Kuusamo
	fake.state()               # Savonlinnan ja Kymenkartanon lääni
	fake.postcode()            # 29335

### faker.providers.person

	fake.name()                # Pirjo Vuoristo
	fake.last_name()           # Nousiainen
	fake.first_name()          # Anna-Leena
	fake.prefix()              # arkkit.
	fake.suffix()              # DI

### faker.providers.company

	fake.company()             # Hintikka Oy
	fake.company_suffix()      # As Oy

### faker.providers.internet
	
	fake.email()               # venalainen.kaija@nikkola.com
	fake.safe_email()          # eveliina.tikkanen@example.net
	fake.free_email()          # jalonen.jussi@kolumbus.fi
	fake.company_email()       # uleino@tiilikainen.com
	fake.url()                 # http://www.vaatainen.com/
	fake.uri()                 # http://www.mikkola.com/author/
	fake.domain_name()         # isomaki.fi
	fake.user_name()           # hsaarinen
	fake.uri_extension()       # .html
	fake.tld()                 # fi

### faker.providers.phone_number

	fake.phone_number()        # +358415027958

## LANGUAGE ru_RU

### faker.providers.person
	fake.name()                   # тов. Агафон Корнилов
	fake.last_name()              # Белов
	fake.first_name()             # Богдан
	fake.prefix()                 # г-н.

### faker.providers.phone_number

	fake.phone_number()           # +7 948 512 7518 

### faker.providers.job
	fake.job()                    # Булочник

## LANGUAGE el_GR

### faker.providers.person

	fake.name():                # Θεοδώρα Αλεξανδράκη
	fake.name_male():           # Σόλων-Αγγελής Πετράκης
	fake.name_female():         # Μαρία Ξυγκάκου
	fake.first_name():          # Μάριος
	fake.first_name_male():     # Επαμεινώνδας
	fake.first_name_female():   # Ρεβέκα
	fake.last_name():           # Φραγκόπουλος
	fake.last_name_male():      # Αποστολάκης
	fake.last_name_female():    # Χαλκίδου

### faker.providers.address

	fake.address():             # Μαστρογιαννίδου 7,
	                              ΤΚ 36777 Αλεξανδρούπολη
	fake.line_address():        # Αργυροπούλου 3, 34924 Δράμα
	fake.street_name():         # Αρδείας
	fake.street_address():      # Λεωφ. Ευόσμου 44
	fake.building_number():     # 131
	fake.postcode():            # ΤΚ 991 51
	fake.city():                # Καστοριά
	fake.region():              # Πέλλα
	fake.country():             # Μπρουνέι
	fake.latitude():            # 38.818785
	fake.longitude():           # 27.367441
	fake.latlng():              # (36.706833, 28.523434)

### faker.providers.lorem

	fake.text():                # Πιο προγραμματιστής παραδώσεις γραμμή στη νιρβάνα
	                              κι. Πολύ έγραψες ημέρα τι συνεντεύξεις. Γραμμής
	                              βρίσκονται αποθηκευτικού από συνάδελφος μέχρι τα.

### faker.providers.phone_number

	fake.phone_number():        # 210 761 8331

### faker.providers.internet

	fake.email():               # aimilia.lioliopoulou@doukatziskapetanios.gr
	fake.free_email():          # yzygouris@gmail.com
	fake.company_email():       # eutychia.tsachaki@ioakeim.gr
	fake.user_name():           # konstantina.maniotis
	fake.url():                 # http://www.anastasiou.org/

## LANGUAGE dk_DK

### faker.provider.person
	fake.name()                 # Hr Lucas Østergaard
	fake.last_name()            # Overgaard
	fake.first_name()           # Julius
	fake.prefix()               # Dr.
	fake.prefix_male()          # Prof.
	fake.prefix_female()        # Univ.Prof.

## LANGUAGE es_ES

### faker.providers.person
	fake.name()                   # Jorge Gil-Arellano
	fake.last_name()              # Palmer
	fake.first_name()             # Juliana
	fake.prefix()                 # de

### faker.providers.address
    fake.street_name()            # Via de Arturo Cuadrado Pasaje de Samuel Mármol 88
    fake.address()                # Girona, 13415
    fake.street_address()         # Alameda Victoria Izquierdo 86 Apt. 17
    fake.postcode()               # 41456
    fake.country()                # Andorra
    fake.street_prefix()          # Camino
    fake.building_number()        # 6
    fake.secondary_address()      # Puerta 4
    fake.city()                   # Tarragona
    fake.state()                  # Sevilla

### faker.providers.phone_number

	fake.phone_number()           # +34 971 78 60 60


## LANGUAGE cs_CZ

### faker.providers.address

    fake.latitude()               # 31.819644
    fake.street_name()            # Šůrova
    fake.address()                # K Vodě 2
                                    223 99 Králův Dvůr
    fake.street_address()         # Pod Kostelem 5
    fake.postcode()               # 585 77
    fake.longitude()              # -123.137230
    fake.country()                # Čad
    fake.city_name()              # Bohušovice nad Ohří
    fake.geo_coordinate()         # -76.679571
    fake.building_number()        # 95
    fake.street_suffix_long()     # náměstí
    fake.street_suffix_short()    # nám.
    fake.city()                   # Cvikov
    fake.state()                  # Ústecký kraj

### faker.providers.person

    fake.last_name_male()         # Procházka
    fake.prefix_male()            # JUDr.
    fake.prefix()                 # Mgr.
    fake.name()                   # Renáta Blažková
    fake.first_name()             # Iveta
    fake.suffix()                 # Ph.D.
    fake.first_name_male()        # Alexandr
    fake.first_name_female()      # Ludmila
    fake.last_name_female()       # Křížová
    fake.last_name()              # Dvořák
    fake.prefix_female()          # JUDr.

### faker.providers.company

    fake.company()                # Čermák
    fake.company_suffix()         # o.s.

### faker.providers.internet

    fake.ipv4()                   # 157.11.60.71
    fake.url()                    # http://www.hajkova.cz/
    fake.company_email()          # robert78@riha.cz
    fake.uri()                    # http://benesova.cz/blog/login.html
    fake.tld()                    # com
    fake.uri_path(deep=None)      # app
    fake.free_email()             # rostislav86@volny.cz
    fake.user_name()              # maly.ivan
    fake.free_email_domain()      # chello.cz
    fake.domain_name()            # kral.cz
    fake.uri_extension()          # .php
    fake.ipv6()                   # 0d83:a564:52c3:3d28:606b:060e:7da4:b6ba
    fake.safe_email()             # duskova.olga@example.org
    fake.uri_page()               # privacy
    fake.email()                  # kkrejci@email.cz
    fake.domain_word()            # maskova
    fake.slug(value=None)         # modi-porro-minima

### faker.providers.phone_number

    fake.phone_number()           # 738 361 445

##

# Using from shell

In a python environment with faker installed you can use it with:

    python -m faker [option] [*args]

[option]:

*  formatter name as `text`, `address`: display result of fake

[*args]: pass value to formatter (actually only strings)

    $ python -m faker address
    968 Bahringer Garden Apt. 722
    Kristinaland, NJ 09890


# How to create a Provider

    from faker import Faker
    fake = Faker()

    # first, import a similar Provider or use the default one
    from faker.providers import BaseProvider

    # create new provider class
    class MyProvider(BaseProvider):
        def foo(self):
            return 'bar'

    # then add new provider to faker instance
    fake.add_provider(MyProvider)

    # now you can use:
    fake.foo()
    > 'bar'


# Seeding the Generator

You may want to get always the same generated data - for instance when using Faker for unit testing purposes.
The generator offers a `seed()` method, which seeds the random number generator.
Calling the same script twice with the same seed produces the same results.

    from faker import Faker
    fake = Faker()
    fake.seed(4321)

    print fake.name()   # Margaret Boehm



# Tests

Run tests:

    $ python setup.py test

or

    $ python -m unittest -v faker.tests

Write documentation for providers:

    $ python -m faker > docs.txt



## License

Faker is released under the MIT Licence. See the bundled LICENSE file for details.


Credits
-------
- [FZaninotto][fzaninotto] / [Faker][php-faker]
- [Distribute][distribute]
- [Buildout][buildout]
- [modern-package-template][modern-package-template]

[fzaninotto]: https://github.com/fzaninotto  "F.Zaninotto"
[php-faker]: https://github.com/fzaninotto/Faker "Php faker"
[perl-faker]: http://search.cpan.org/~jasonk/Data-Faker-0.07/ "Perl faker"
[ruby-faker]: http://faker.rubyforge.org/ "Ruby faker"
[buildout]: http://www.buildout.org/
[distribute]:  http://pypi.python.org/pypi/distribute
[modern-package-template]: http://pypi.python.org/pypi/modern-package-template


