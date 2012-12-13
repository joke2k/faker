    _|_|_|_|          _|
    _|        _|_|_|  _|  _|      _|_|    _|  _|_|
    _|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
    _|      _|    _|  _|  _|    _|        _|
    _|        _|_|_|  _|    _|    _|_|_|  _|

# Faker #

Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database,
create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service,
Faker is for you.

Faker is heavily inspired by PHP's [Faker][php-faker], Perl's [Data::Faker][perl-faker], and by ruby's [Faker][ruby-faker].

## Basic Usage

Install with pip:

    pip install fake-factory

Use `faker.Factory.create()` to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

```python

    from faker import Factory

    faker = Factory.create()

    faker.name()
    # 'Lucy Cechtelar'

    faker.address()
    # "426 Jordy Lodge
    #  Cartwrightshire, SC 88120-6700"

    faker.text()
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

Each call to method `faker.name()` yealds a different (random) result. This is because faker uses `__getattr__` magic, and forwards `faker.Genarator.method_name()' calls to `faker.Generator.format(method_name)`.

```python

for i in range(0,10):
  print faker.name()

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


### faker.providers.File:

    fake.mimeType()                    # video/webm

### faker.providers.UserAgent:

    fake.chrome()                      # Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_4) AppleWebKit/5341 (KHTML, like Gecko) Chrome/13.0.803.0 Safari/5341
    fake.firefox()                     # Mozilla/5.0 (Windows 95; sl-SI; rv:1.9.1.20) Gecko/2012-01-06 22:35:05 Firefox/3.8
    fake.internetExplorer()            # Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.1)
    fake.linuxPlatformToken()          # X11; Linux x86_64
    fake.linuxProcessor()              # x86_64
    fake.macPlatformToken()            # Macintosh; U; PPC Mac OS X 10_7_6
    fake.macProcessor()                # U; PPC
    fake.opera()                       # Opera/9.41 (Windows CE; it-IT) Presto/2.9.168 Version/12.00
    fake.safari()                      # Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.34.4 (KHTML, like Gecko) Version/5.0 Safari/534.34.4
    fake.userAgent()                   # Mozilla/5.0 (iPod; U; CPU iPhone OS 3_2 like Mac OS X; en-US) AppleWebKit/531.15.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B119 Safari/6531.15.3
    fake.windowsPlatformToken()        # Windows 98; Win 9x 4.90

### faker.providers.PhoneNumber:

    fake.phoneNumber()                 # (593)652-1880

### faker.providers.Miscelleneous:

    fake.boolean()                     # True
    fake.countryCode()                 # BB
    fake.languageCode()                # fr
    fake.locale()                      # pt_GN
    fake.md5()                         # ab9d3552b5c6e68714c04c35725ba73c
    fake.nullBoolean()                 # True
    fake.sha1()                        # 3fc2ede28f2596050f9a94c15c59b800175409d0
    fake.sha256()                      # f06561a971d6b1306ecef60be336556d6de2540c2d0d2158f4d0ea3f212cd740

### faker.providers.Internet:

    fake.companyEmail()                # ggreenfelder@ortizmedhurst.com
    fake.domainName()                  # mayer.com
    fake.domainWord()                  # gusikowski
    fake.email()                       # gbrakus@johns.net
    fake.freeEmail()                   # abbey60@yahoo.com
    fake.freeEmailDomain()             # hotmail.com
    fake.ipv4()                        # 81.132.249.71
    fake.ipv6()                        # 4c55:8c8b:54b5:746d:44ed:c7ab:486a:a50e
    fake.safeEmail()                   # amalia49@example.com
    fake.slug()                        # TypeError
    fake.tld()                         # net
    fake.uri()                         # http://www.parker.com/
    fake.uriExtension()                # .asp
    fake.uriPage()                     # terms
    fake.uriPath()                     # explore/list/app
    fake.url()                         # http://dubuque.info/
    fake.userName()                    # goodwin.edwin

### faker.providers.Company:

    fake.bs()                          # maximize end-to-end infrastructures
    fake.catchPhrase()                 # Multi-tiered analyzing instructionset
    fake.company()                     # Stanton-Luettgen
    fake.companySuffix()               # Group

### faker.providers.DateTime:

    fake.amPm()                        # AM
    fake.century()                     # IX
    fake.date()                        # 1985-02-17
    fake.dateTime()                    # 1995-06-08 14:46:50
    fake.dateTimeAD()                  # 1927-12-17 23:08:46
    fake.dateTimeBetween()             # 1999-08-22 22:49:52
    fake.dateTimeThisCentury()         # 1999-07-24 23:35:49
    fake.dateTimeThisDecade()          # 2008-01-27 01:08:37
    fake.dateTimeThisMonth()           # 2012-11-12 14:13:04
    fake.dateTimeThisYear()            # 2012-05-19 00:40:00
    fake.dayOfMonth()                  # 23
    fake.dayOfWeek()                   # Friday
    fake.iso8601()                     # 2009-04-09T21:30:02
    fake.month()                       # 03
    fake.monthName()                   # April
    fake.time()                        # 06:16:50
    fake.timezone()                    # America/Noronha
    fake.unixTime()                    # 275630166
    fake.year()                        # 2002

### faker.providers.Person:

    fake.firstName()                   # Elton
    fake.lastName()                    # Schowalter
    fake.name()                        # Susan Pagac III
    fake.prefix()                      # Ms.
    fake.suffix()                      # V

### faker.providers.Address:

    fake.address()                     # 044 Watsica Brooks
                                         West Cedrickfort, SC 35023-5157
    fake.buildingNumber()              # 319
    fake.city()                        # Kovacekfort
    fake.cityPrefix()                  # New
    fake.citySuffix()                  # ville
    fake.country()                     # Monaco
    fake.geo_coordinate()              # 148.031951
    fake.latitude()                    # 154.248666
    fake.longitude()                   # 109.920335
    fake.postcode()                    # 82402-3206
    fake.secondaryAddress()            # Apt. 230
    fake.state()                       # Nevada
    fake.stateAbbr()                   # NC
    fake.streetAddress()               # 793 Haskell Stravenue
    fake.streetName()                  # Arvilla Valley
    fake.streetSuffix()                # Crescent

### faker.providers.Lorem:

    fake.paragraph()                   # Itaque quia harum est autem inventore quisquam eaque. Facere mollitia repudiandae
                                         qui et voluptas. Consequatur sunt ullam blanditiis aliquam veniam illum voluptatem.
    fake.paragraphs()                  # ['Alias porro soluta eum voluptate. Iste consequatur qui non nam.',
                                            'Id eum sint eius earum veniam fugiat ipsum et. Et et occaecati at labore
                                            amet et. Rem velit inventore consequatur facilis. Eum consequatur consequatur
                                            quis nobis.', 'Harum autem autem totam ex rerum adipisci magnam adipisci.
                                            Qui modi eos eum vel quisquam. Tempora quas eos dolorum sint voluptatem
                                            tenetur cum. Recusandae ducimus deleniti magnam ullam adipisci ipsa.']
    fake.sentence()                    # Eum magni soluta unde minus nobis.
    fake.sentences()                   # ['Ipsam eius aut veritatis iusto.',
                                            'Occaecati libero a aut debitis sunt quas deserunt aut.',
                                            'Culpa dolor voluptatum laborum at et enim.']
    fake.text()                        # Dicta quo eius possimus quae eveniet cum nihil. Saepe sint non nostrum.
                                         Sequi est sit voluptate et eos eum et. Pariatur non sunt distinctio magnam.
    fake.word()                        # voluptas
    fake.words()                       # ['optio', 'et', 'voluptatem']



## Localization

`faker.Factory` can take a locale as an argument, to return localized data.
If no localized provider is found, the factory fallbacks to the default locale (en_EN).

    from faker import Factory
    fake = Factory.create('it_IT')
    for i in range(0,10):
        print fake.name()

    # Elda Palumbo
    # Pacifico Giordano
    # Sig. Avide Guerra
    # Yago Amato
    # Eustachio Messina
    # Dott. Violante Lombardo
    # Sig. Alighieri Monti
    # Costanzo Costa
    # Nazzareno Barbieri
    # Max Coppola

You can check available Faker locales in the source code, under the providers package.
The localization of Faker is an ongoing process, for which we need your help.
Don't hesitate to create localized providers to your own locale and submit a PR!


# Using from shell

In a python environment with faker installed you can use it with:

    python -m faker [option] [*args]

[option]:

*  formatter name as `text`, `address`: display result of fake
*  Provider name as `Lorem`: display all Provider's fakes

[*args]: pass value to formatter (actually only strings)

    $ python -m faker address
    968 Bahringer Garden Apt. 722
    Kristinaland, NJ 09890


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
