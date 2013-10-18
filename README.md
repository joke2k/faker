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
[![Coverage Status](https://coveralls.io/repos/joke2k/faker/badge.png?branch=wip0.3)](https://coveralls.io/r/joke2k/faker?branch=wip0.3)
[![PyPI version](https://badge.fury.io/py/fake-factory.png)](http://badge.fury.io/py/fake-factory)
[![Downloads](https://pypip.in/d/fake-factory/badge.png)](https://crate.io/packages/fake-factory)

## Basic Usage

Install with pip:

    pip install fake-factory

Use `fake.Factory.create()` to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

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

Each call to method `fake.name()` yealds a different (random) result.
This is because faker forwards `faker.Genarator.method_name()' calls to `faker.Generator.format(method_name)`.

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

    fake.random_digit_not_null()               # 8
    fake.random_int(min=9999)                  # 5447
    fake.random_letter()                       # W
    fake.random_digit()                        # 6
    fake.bothify(text="## ??")                 # 10 lz
    fake.random_element(array=('a', 'b', 'b')) # b
    fake.random_number(digits=None)            # 38541
    fake.lexify(text="????")                   # MYQL
    fake.randomize_nb_elements(number=False)   # 12
    fake.numerify(text="###")                  # 323

### faker.providers.lorem

    fake.sentence(nbWords=True)                # Totam non non consequuntur reprehenderit quia expedita.
    fake.word()                                # aut
    fake.paragraph(nbSentences=True)           # Dolore necessitatibus aut temporibus et dolorum corporis.
                                                 Ullam et sit provident rem. Culpa aut modi ut in asperiores.
                                                 Iste quis quam rem non facere.
    fake.paragraphs(nb=3)                      # ['Est nemo culpa velit aspernatur. Voluptatibus et velit consectetur
                                                      cum molestias assumenda molestiae. Pariatur voluptatum dignissimos
                                                      accusantium doloremque.',
                                                  'Iusto amet qui iusto minima dolor sint ipsum. Et ipsum qui aut at
                                                      dolor id et. Earum fugit deleniti eos distinctio eos libero vitae.
                                                      Atque animi commodi architecto. Aut rerum possimus nemo est ullam
                                                      tempora distinctio.',
                                                  'Dicta voluptatibus est voluptas doloribus. Reiciendis sed possimus
                                                      qui rerum et. Nisi ut optio nemo reprehenderit. Labore sed quia
                                                      reprehenderit ex incidunt soluta praesentium.']
    fake.words(nb=3)                           # ['voluptas', 'et', 'aut']
    fake.text(maxNbChars=200)                  # Sed et recusandae id enim sed soluta fugit. Optio minus qui dolore
                                                 eligendi veniam porro iste. Enim natus adipisci sit accusantium.
                                                 Vitae rerum nesciunt et et odit dolorum.
    fake.sentences(nb=3)                       # ['Cupiditate et et qui dolorem ea ut.',
                                                 'Esse itaque quos excepturi quis temporibus iusto ducimus.',
                                                 'Quae id quaerat deleniti quaerat.']

### faker.providers.address

    fake.state_abbr()                          # PW
    fake.latitude()                            # -171.819862
    fake.street_name()                         # Weimann Oval
    fake.address()                             # 979 Luettgen Highway
                                               # East Miltonmouth, ID 41175-2736
    fake.street_address()                      # 25627 Stephen Trafficway Suite 021
    fake.postcode()                            # 37602
    fake.longitude()                           # 46.335322
    fake.country()                             # Belarus
    fake.geo_coordinate()                      # 85.943588
    fake.street_suffix()                       # Summit
    fake.city_prefix()                         # East
    fake.city_suffix()                         # berg
    fake.building_number()                     # 89215
    fake.secondary_address()                   # Suite 810
    fake.city()                                # Sauertown
    fake.state()                               # SouthDakota

### faker.providers.person

    fake.name()                                # Dorian Berge
    fake.suffix()                              # V
    fake.last_name()                           # Parisian
    fake.first_name()                          # Margot
    fake.prefix()                              # Mr.

### faker.providers.date_time

    fake.date_time_ad()                        # 1628-01-22 16:14:56
    fake.month()                               # 02
    fake.am_pm()                               # PM
    fake.date_time_this_century()              # 1920-05-02 08:11:48
    fake.date_time()                           # 1987-05-05 19:59:49
    fake.date_time_between(startDate="now")    # 2010-09-18 21:26:53
    fake.date_time_this_month()                # 2013-09-25 19:50:12
    fake.date_time_this_decade()               # 2009-09-27 21:29:58
    fake.day_of_week()                         # Friday
    fake.day_of_month()                        # 17
    fake.time(pattern="%H:%M:%S")              # 19:51:16
    fake.iso8601()                             # 2002-04-11T09:11:42
    fake.month_name()                          # December
    fake.unix_time()                           # 768637430
    fake.date_time_this_year()                 # 2012-12-18 06:20:08
    fake.timezone()                            # Africa/Cairo
    fake.century()                             # XVIII
    fake.date(pattern="%Y-%m-%d")              # 1972-04-10
    fake.year()                                # 1972

### faker.providers.company

    fake.company()                             # Mills Ltd
    fake.company_suffix()                      # Inc
    fake.catch_phrase()                        # Front-line bifurcated definition
    fake.bs()                                  # visualize ubiquitous ROI

### faker.providers.internet

    fake.ipv4()                                # 43.46.102.99
    fake.url()                                 # http://www.cronin.com/
    fake.company_email()                       # batz.shad@windlerbrakus.biz
    fake.uri()                                 # http://greenfelder.net/explore/category/faq/
    fake.tld()                                 # biz
    fake.uri_path(deep=None)                   # blog
    fake.free_email()                          # schamberger.asia@hotmail.com
    fake.user_name()                           # leopold.feest
    fake.free_email_domain()                   # gmail.com
    fake.domain_name()                         # schmittbeahan.com
    fake.uri_extension()                       # .html
    fake.ipv6()                                # 6829:509b:713a:977f:1f7c:9d4b:a4e3:fa86
    fake.safe_email()                          # beatty.frida@example.net
    fake.uri_page()                            # search
    fake.email()                               # dgorczany@yahoo.com
    fake.domain_word()                         # jenkins
    fake.slug(value=None)                      # non-dolor

### faker.providers.miscelleneous

    fake.locale()                              # en_BZ
    fake.md5(raw_output=False)                 # 2fcd9e5a6a44b0a83da7894e64371ca3
    fake.sha1(raw_output=False)                # a80d378c0d790786d4691cf4fda96435d7ac8254
    fake.null_boolean()                        # None
    fake.sha256(raw_output=False)              # f16e5780cc183f8db22b650efe63798d3a2a293b4f6cbf91cc18294f0e03b2d9
    fake.country_code()                        # SR
    fake.boolean(chanceOfGettingTrue=50)       # True
    fake.language_code()                       # de

### faker.providers.phone_number

    fake.phone_number()                        # +61(4)9107201136

### faker.providers.user_agent

    fake.mac_processor()                       # U; Intel
    fake.firefox()                             # Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2011-10-31 06:51:36 Firefox/3.8
    fake.linux_platform_token()                # X11; Linux i686
    fake.opera()                               # Opera/8.71 (X11; Linux i686; it-IT) Presto/2.9.175 Version/10.00
    fake.windows_platform_token()              # Windows NT 5.01
    fake.internet_explorer()                   # Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.1)
    fake.user_agent()                          # Opera/9.60 (Windows NT 6.2; it-IT) Presto/2.9.172 Version/11.00
    fake.chrome()                              # Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_7) AppleWebKit/5331 (KHTML, like Gecko) Chrome/14.0.897.0 Safari/5331
    fake.linux_processor()                     # i686
    fake.mac_platform_token()                  # Macintosh; U; Intel Mac OS X 10_5_7
    fake.safari()                              # Mozilla/5.0 (iPod; U; CPU iPhone OS 4_2 like Mac OS X; sl-SI) AppleWebKit/531.13.1 (KHTML, like Gecko) Version/3.0.5 Mobile/8B113 Safari/6531.13.1

### faker.providers.file

    fake.mime_type(category=None)              # application/xhtml+xml

### faker.providers.python

    fake.pyunicode(maxChars=20)                # Reprehenderit.
    fake.pystr(maxChars=20)                    # Ullam quia ut.
    fake.pytuple(nbElements=True)              # ('Delectus iure et.', u'xbogan@hotmail.com', 4996, 'Impedit ducimus.',
                                                    datetime(2001, 11, 17, 7, 12, 24), 'Id adipisci veniam.', 4858)
    fake.pydecimal(leftDigits=False)           # -43.5720326077
    fake.pystruct(count=10)                    # (['Accusantium est.', Decimal('3.08377127009E+12'),
                                                    datetime(1988, 10, 16, 17, 54, 4), 6350, -33.46725636,
                                                    'Dolores ut et.', 3748, 7235, datetime(1986, 10, 19, 11, 25, 40),
                                                    'Voluptatum.'], {'eum': 'Animi et et.', 'est': u'albert22@yost.com',
                                                    'quis': datetime(1973, 1, 16, 15, 39, 36),
                                                    'sit': u'pansy11@torphyoconnell.biz', 'voluptas': 8007,
                                                    'eveniet': 'Optio enim autem.', 'aliquid': 'Quo accusamus est.',
                                                    'voluptatem': 2923, 'aspernatur': u'wiley.morar@hotmail.com',
                                                    'cupiditate': 'Consequatur.'}, {'dolorum': {9: Decimal('-44997.5'),
                                                    10: [6251, 'Quia dolor.', u'http://pacocha.info/index/'],
                                                    11: {9: -4721.3736, 10: 220821631732559.0, 11: [
                                                    u'http://turcotte.info/home/', 3345]}}, 'ad': {2: 6306,
                                                    3: ['Sint unde ducimus.', datetime(1974, 3, 12, 7, 21), .... removed for brevity
    fake.pyfloat(leftDigits=False)             # -83.39386328
    fake.pyset(nbElements=True)                # set(['Voluptate nostrum.', u'http://jenkins.com/', u'lmckenzie@gmail.com',
                                                    'Delectus magnam.', 'Earum ut deleniti.', datetime(1976, 1, 10, 6, 9, 44),
                                                    u'hudson.deshaun@gmail.com', Decimal('1.7686'), 6836,
                                                    u'http://schuster.com/wp-content/posts/posts/register/',
                                                    datetime(1983, 6, 4, 15, 35, 41)])
    fake.pydict(nbElements=True)               # {'quo': datetime(2005, 6, 10, 18, 56, 16),
                                                    'adipisci': datetime(1970, 5, 17, 3, 12, 38), 'ut': 1485,
                                                    'dignissimos': 'Asperiores.', 'facilis': 'Qui perferendis.',
                                                    'distinctio': u'http://www.moenblock.biz/categories/wp-content/',
                                                    'et': Decimal('-66087.540101'), 'cupiditate': datetime(1978, 7, 14, 17, 20, 5)}
    fake.pybool()                              # False
    fake.pyiterable(nbElements=True)           # (u'http://www.corwinswaniawski.com/app/blog/post/', 9.69637877268032,
                                                    'Ut sed et est.', 5352, u'http://www.konopelski.com/list/search.php',
                                                    'Excepturi itaque.', 8663, 'Itaque voluptatem.', 'Voluptatem omnis.',
                                                    u'http://www.borer.com/tag/app/about/', 'Veritatis et.', 'Aut deleniti.')
    fake.pylist(nbElements=True)               # [1396, u'luis68@streich.com', u'http://www.strosin.com/', 'Atque accusamus.',
                                                    'Exercitationem sint.', 3545, u'http://www.okunevamurazik.com/', u'mraz.ernestina@rowe.info',
                                                    Decimal('-1131032.90283'), Decimal('89.2089'), 'Est alias error.']
    fake.pyint()                               # 7920



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

	fake.street_name()            # Contrada Genziana
	fake.address()                # Stretto Noemi 006 Piano 3
									Flavio laziale, 27476 Mantova (LU)
	fake.street_address()         # Stretto Lombardo 8 Piano 6
	fake.postcode()               # 94032
	fake.longitude()              # 92.051838
	fake.country()                # Germania
	fake.street_suffix()          # Rotonda
	fake.city_prefix()            # Quarto
	fake.city_suffix()            # calabro
	fake.building_number()        # 81
	fake.secondary_address()      # Appartamento 65
	fake.city()                   # Sesto Filomena
	fake.state()                  # Carbonia-Iglesias

### faker.providers.person

	fake.name()                   # Gaetano Silvestri
	fake.last_name()              # Gentile
	fake.first_name()             # Costanzo
	fake.prefix()                 # Dott.

### faker.providers.company
	
	fake.company()                # D'angelo-Vitali s.r.l.
	fake.company_suffix()         # Group
	fake.catch_phrase()           # Utilizzazione polarizzata stabile
	fake.bs()                     # tecnologie utilizzo B2B

### faker.providers.phone_number

	fake.phone_number()           # +16 2658 2544588

## LANGUAGE fr_FR

### faker.providers.address

	fake.address()                      # 14, rue Grégoire Hebert
					      				  27681 Lejeune
	fake.department_number()            # 57
	fake.street_name()                  # chemin de Grenier
	fake.department()                   # (u'80', u'Somme')
	fake.department_name()              # Aude
	fake.street_address()               # rue de Besnard
	fake.postcode()                     # 23 699
	fake.longitude()                    # 61.773719
	fake.country()                      # Macau
	fake.street_prefix()                # rue
	fake.street_suffix()                # Street
	fake.city_suffix()                  # -les-Bains
	fake.building_number()              # 81
	fake.region()                       # Alsace
	fake.city()                         # DenisBourg

### faker.providers.person

	fake.name()                         # Julie Bailly
	fake.last_name()                    # Bertrand
	fake.first_name()                   # Marguerite
	fake.prefix()                       # Le

### faker.providers.company

	fake.company()                      # Gautier
	fake.company_suffix()               # SARL
	fake.catch_phrase_verb()            # d'atteindre vos buts
	fake.catch_phrase()                 # La liberté de rouler naturellement
	fake.catch_phrase_noun()            # le confort
	fake.siren()                        # 596 679 375
	fake.siret(max_sequential_digits=2) # 291 991 838 00804
	fake.catch_phrase_attribute()       # de manière sûre

### faker.providers.internet

	fake.url()                          # http://delorme.com/
	fake.company_email()                # olivier.besnard@andre.fr
	fake.uri()                          # http://www.lebrun.fr/faq.html
	fake.tld()                          # fr
	fake.free_email()                   # elodie.gillet@live.com
	fake.user_name()                    # jean.rossi
	fake.free_email_domain()            # orange.fr
	fake.domain_name()                  # dumont.net
	fake.safe_email()                   # lmarchand@example.com
	fake.uri_page()                     # register
	fake.email()                        # ncamus@noos.fr
	fake.domain_word()                  # gallet
	fake.slug(value=None)               # voluptas

### faker.providers.phone_number

	fake.phone_number()                 # +33 4 80 14 46 78

## LANGUAGE pt_BR

### faker.providers.address

	fake.estado_nome()            # Ceará
	fake.latitude()               # -42.176024
	fake.street_name()            # Colônia Emanuel Pereira
	fake.street_prefix()          # Aeroporto
	fake.address()                # Ladeira Nicole Silva, 40
									Flamengo
									51586-187 Santos / CE
	fake.street_address()         # Recanto Correia, 34
	fake.bairro()                 # Dom Joaquim
	fake.longitude()              # 92.773043
	fake.country()                # Geórgia
	fake.estado_sigla()           # PA
	fake.street_suffix()          # Street
	fake.city_suffix()            # da Serra
	fake.building_number()        # 907
	fake.estado()                 # (u'PB', u'Para\xedba')
	fake.city()                   # Barbosa das Pedras
	fake.postcode()               # 45376684

### faker.providers.person

	fake.name()                   # Igor-Gustavo Ferreira
	fake.last_name()              # Santos
	fake.first_name()             # Maria
	fake.prefix()                 # de

### faker.providers.company

	fake.company()                # Gomes e Filhos
	fake.company_suffix()         # - ME

### faker.providers.internet

	fake.url()                    # http://www.almeida.com/
	fake.company_email()          # bruna.souza@alves.br
	fake.uri()                    # http://carvalho.com/main/tags/category/category/
	fake.free_email()             # melo.bárbara@uol.com.br
	fake.user_name()              # heloísa17
	fake.free_email_domain()      # ig.com.br
	fake.domain_name()            # martins.br
	fake.safe_email()             # rodrigues.antonio@example.com
	fake.email()                  # andre.dias@silva.br
	fake.domain_word()            # ribeiro
	fake.slug(value=None)         # debitis-quo-sit

### faker.providers.phone_number

	fake.phone_number()           # +55 (081) 9413-8074


# Using from shell

In a python environment with faker installed you can use it with:

    python -m faker [option] [*args]

[option]:

*  formatter name as `text`, `address`: display result of fake
*  Provider name as `lorem`: display all Provider's fakes

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


