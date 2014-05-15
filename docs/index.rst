.. Faker documentation master file, created by
   sphinx-quickstart on Tue Mar 11 11:25:48 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Faker's documentation!
=================================

::

    _|_|_|_|          _|
    _|        _|_|_|  _|  _|      _|_|    _|  _|_|
    _|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
    _|      _|    _|  _|  _|    _|        _|
    _|        _|_|_|  _|    _|    _|_|_|  _|


*Faker* is a Python package that generates fake data for you. Whether you need to bootstrap your database,
create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service,
Faker is for you.

Faker is heavily inspired by PHP's `Faker <https://github.com/fzaninotto/Faker>`_, Perl's `Data::Faker <http://search.cpan.org/~jasonk/Data-Faker-0.07/>`_, and by ruby's `Faker <http://faker.rubyforge.org/>`_.

.. image:: https://travis-ci.org/joke2k/faker.png?branch=master 

.. image:: https://d2weczhvl823v0.cloudfront.net/joke2k/faker/trend.png

.. image:: https://coveralls.io/repos/joke2k/faker/badge.png?branch=master

.. image:: https://badge.fury.io/py/fake-factory.png

.. image:: https://pypip.in/d/fake-factory/badge.png

Basic Usage
------------

Install with pip::

    pip install fake-factory

Use ``faker.Factory.create()`` to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

::

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


Each call to method ``fake.name()`` yields a different (random) result.
This is because faker forwards ``faker.Generator.method_name()`` calls to ``faker.Generator.format(method_name)``.

::

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

Providers
---------

Each of the generator properties (like ``name``, ``address``, and ``lorem``) are called :doc:`providers`.
A faker generator has many of them, packaged in "providers".

Localization
---------------

``faker.Factory`` can take a locale as an argument, to return localized data.
If no localized provider is found, the factory fallbacks to the default locale (en_EN).

See the full list of included :doc:`locales`.

Using from shell
----------------

In a python environment with faker installed you can use it with::

    python -m faker [option] [*args]

[option]:

*  formatter name as `text`, `address`: display result of fake

[*args]: pass value to formatter (actually only strings)

::

    $ python -m faker address
    968 Bahringer Garden Apt. 722
    Kristinaland, NJ 09890


How to create a Provider
------------------------

::

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


How to use with factory-boy
---------------------------

::

    import factory
    from faker import Factory as FakerFactory
    from myapp.models import Book

    faker = FakerFactory.create()


    class Book(factory.Factory):
        FACTORY_FOR = Book

        title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
        author_name = factory.LazyAttribute(lambda x: faker.name())


Seeding the Generator
---------------------

You may want to get always the same generated data - for instance when using Faker for unit testing purposes.
The generator offers a `seed()` method, which seeds the random number generator.
Calling the same script twice with the same seed produces the same results.

::

    from faker import Faker
    fake = Faker()
    fake.seed(4321)

    print fake.name()   # Margaret Boehm



Tests
-----

Run tests::

    $ python setup.py test

or::

    $ python -m unittest -v faker.tests

Write documentation for providers::

    $ python -m faker > docs.txt



License
-------

Faker is released under the MIT Licence. See the bundled LICENSE file for details.


Credits
-------

- `FZaninotto <https://github.com/fzaninotto>`_ / `Faker <https://github.com/fzaninotto/Faker>`_
- `Distribute <http://pypi.python.org/pypi/distribute>`_
- `Buildout <http://www.buildout.org/>`_
- `modern-package-template <http://pypi.python.org/pypi/modern-package-template>`_

Contents
--------

.. toctree::
   :maxdepth: 2

   providers
   locales



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

