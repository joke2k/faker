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
[![Build status](https://ci.appveyor.com/api/projects/status/b8qg53rqmuag9o49/branch/master)](https://ci.appveyor.com/project/joke2k/faker/branch/master)
[![Coverage Status](https://coveralls.io/repos/joke2k/faker/badge.png?branch=master)](https://coveralls.io/r/joke2k/faker?branch=master)
[![PyPI version](https://badge.fury.io/py/fake-factory.png)](http://badge.fury.io/py/fake-factory)
[![Downloads](https://pypip.in/d/fake-factory/badge.png)](https://crate.io/packages/fake-factory)

For more details, see the [extended docs](http://fake-factory.readthedocs.org/en/latest/).

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

## Providers

Each of the generator properties (like `name`, `address`, and `lorem`) are called "fake".
A faker generator has many of them, packaged in "providers". Here is a list of the bundled formatters in the default locale.

## Localization

`faker.Factory` can take a locale as an argument, to return localized data.
If no localized provider is found, the factory falls back to the default en_US locale.

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
Please don't hesitate to create a localized provider for your own locale and submit
a Pull Request (PR).

Included localized providers:

* [bg_BG](http://fake-factory.readthedocs.org/en/master/locales/bg_BG.html)
* [cs_CZ](http://fake-factory.readthedocs.org/en/master/locales/cs_CZ.html)
* [de_DE](http://fake-factory.readthedocs.org/en/master/locales/de_DE.html)
* [dk_DK](http://fake-factory.readthedocs.org/en/master/locales/dk_DK.html)
* [el_GR](http://fake-factory.readthedocs.org/en/master/locales/el_GR.html)
* [en_CA](http://fake-factory.readthedocs.org/en/master/locales/en_CA.html)
* [en_GB](http://fake-factory.readthedocs.org/en/master/locales/en_GB.html)
* [en_US](http://fake-factory.readthedocs.org/en/master/locales/en_US.html)
* [es_ES](http://fake-factory.readthedocs.org/en/master/locales/es_ES.html)
* [es_MX](http://fake-factory.readthedocs.org/en/master/locales/es_MX.html)
* [fa_IR](http://fake-factory.readthedocs.org/en/master/locales/fa_IR.html)
* [fi_FI](http://fake-factory.readthedocs.org/en/master/locales/fi_FI.html)
* [fr_FR](http://fake-factory.readthedocs.org/en/master/locales/fr_FR.html)
* [hi_IN](http://fake-factory.readthedocs.org/en/master/locales/hi_IN.html)
* [it_IT](http://fake-factory.readthedocs.org/en/master/locales/it_IT.html)
* [ko_KR](http://fake-factory.readthedocs.org/en/master/locales/ko_KR.html)
* [lt_LT](http://fake-factory.readthedocs.org/en/master/locales/lt_LT.html)
* [lv_LV](http://fake-factory.readthedocs.org/en/master/locales/lv_LV.html)
* [nl_NL](http://fake-factory.readthedocs.org/en/master/locales/nl_NL.html)
* [pl_PL](http://fake-factory.readthedocs.org/en/master/locales/pl_PL.html)
* [pt_BR](http://fake-factory.readthedocs.org/en/master/locales/pt_BR.html)
* [ru_RU](http://fake-factory.readthedocs.org/en/master/locales/ru_RU.html)
* [sl_SI](http://fake-factory.readthedocs.org/en/master/locales/sl_SI.html)
* [zh_CN](http://fake-factory.readthedocs.org/en/master/locales/zh_CN.html)
* [zh_TW](http://fake-factory.readthedocs.org/en/master/locales/zh_TW.html)


# Command line usage

When installed, you can invoke faker from the command-line:

    faker [-h] [--version] [-o output]
          [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
          [-r REPEAT] [-s SEP]
          [fake [fake ...]]

Where:

* `faker`: is the script when installed in your environment,
   in development you could use `python -m faker` instead

* `-h`, `--help`: shows a help message

* `--version`: shows the program's version number

* `-o FILENAME`: redirects the output to the specified filename

* `-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}`: allows use of a localized provider

* `-r REPEAT`: will generate a specified number of outputs

* `-s SEP`: will generate the specified separator after each generated output

* `fake`: is the name of the fake to generate an output for, 
  such as `name`, `address`, or `text`

* `[fake ...]`: is an optional comma-separated list of field names to pass to the fake,
  such as `ssn,birthday` when the `profile` fake is used

Examples:

    $ faker address
    968 Bahringer Garden Apt. 722
    Kristinaland, NJ 09890
    
    $ faker -l de_DE address
    Samira-Niemeier-Allee 56
    94812 Biedenkopf
    
    $ faker profile ssn,birthdate
    {'ssn': u'628-10-1085', 'birthdate': '2008-03-29'}

    $ faker -r=3 -s=";" name
    Willam Kertzmann
    ;
    Josiah Maggio
    ;
    Gayla Schmitt
    ;


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


# How to use with factory-boy

    import factory
    from faker import Factory as FakerFactory
    from myapp.models import Book

    faker = FakerFactory.create()


    class Book(factory.Factory):
        FACTORY_FOR = Book

        title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
        author_name = factory.LazyAttribute(lambda x: faker.name())


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


