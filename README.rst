::

    _|_|_|_|          _|
    _|        _|_|_|  _|  _|      _|_|    _|  _|_|
    _|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
    _|      _|    _|  _|  _|    _|        _|
    _|        _|_|_|  _|    _|    _|_|_|  _|

*Faker* is a Python package that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

Faker is heavily inspired by `PHP Faker`_, `Perl Faker`_, and by `Ruby Faker`_.

----

|pypi| |unix_build| |windows_build| |coverage| |license|

----

For more details, see the `extended docs`_.

Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install Faker

*Note: this package was previously called* ``fake-factory``.

Use ``faker.Factory.create()`` to create and initialize a faker
generator, which can generate data by accessing properties named after
the type of data you want.

.. code:: python

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
This is because faker forwards ``faker.Generator.method_name()`` calls
to ``faker.Generator.format(method_name)``.

.. code:: python

    for _ in range(0, 10):
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

Each of the generator properties (like ``name``, ``address``, and
``lorem``) are called "fake". A faker generator has many of them,
packaged in "providers".

Check the `extended docs`_ for a list of `bundled providers`_ and a list of
`community providers`_.

Localization
------------

``faker.Factory`` can take a locale as an argument, to return localized
data. If no localized provider is found, the factory falls back to the
default en\_US locale.

.. code:: python

    from faker import Factory
    fake = Factory.create('it_IT')
    for _ in range(0, 10):
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

You can check available Faker locales in the source code, under the
providers package. The localization of Faker is an ongoing process, for
which we need your help. Please don't hesitate to create a localized
provider for your own locale and submit a Pull Request (PR).

Included localized providers:

-  `bg\_BG <https://faker.readthedocs.io/en/master/locales/bg_BG.html>`__ - Bulgarian
-  `cs\_CZ <https://faker.readthedocs.io/en/master/locales/cs_CZ.html>`__ - Czech
-  `de\_DE <https://faker.readthedocs.io/en/master/locales/de_DE.html>`__ - German
-  `dk\_DK <https://faker.readthedocs.io/en/master/locales/dk_DK.html>`__ - Danish
-  `el\_GR <https://faker.readthedocs.io/en/master/locales/el_GR.html>`__ - Greek
-  `en\_AU <https://faker.readthedocs.io/en/master/locales/en_AU.html>`__ - English (Australia)
-  `en\_CA <https://faker.readthedocs.io/en/master/locales/en_CA.html>`__ - English (Canada)
-  `en\_GB <https://faker.readthedocs.io/en/master/locales/en_GB.html>`__ - English (Great Britain)
-  `en\_US <https://faker.readthedocs.io/en/master/locales/en_US.html>`__ - English (United States)
-  `es\_ES <https://faker.readthedocs.io/en/master/locales/es_ES.html>`__ - Spanish (Spain)
-  `es\_MX <https://faker.readthedocs.io/en/master/locales/es_MX.html>`__ - Spanish (Mexico)
-  `fa\_IR <https://faker.readthedocs.io/en/master/locales/fa_IR.html>`__ - Persian (Iran)
-  `fi\_FI <https://faker.readthedocs.io/en/master/locales/fi_FI.html>`__ - Finnish
-  `fr\_FR <https://faker.readthedocs.io/en/master/locales/fr_FR.html>`__ - French
-  `hi\_IN <https://faker.readthedocs.io/en/master/locales/hi_IN.html>`__ - Hindi
-  `hr\_HR <https://faker.readthedocs.io/en/master/locales/hr_HR.html>`__ - Croatian
-  `hu\_HU <https://faker.readthedocs.io/en/master/locales/hu_HU.html>`__ - Hungarian
-  `it\_IT <https://faker.readthedocs.io/en/master/locales/it_IT.html>`__ - Italian
-  `ja\_JP <https://faker.readthedocs.io/en/master/locales/ja_JP.html>`__ - Japanese
-  `ko\_KR <https://faker.readthedocs.io/en/master/locales/ko_KR.html>`__ - Korean
-  `lt\_LT <https://faker.readthedocs.io/en/master/locales/lt_LT.html>`__ - Lithuanian
-  `lv\_LV <https://faker.readthedocs.io/en/master/locales/lv_LV.html>`__ - Latvian
-  `ne\_NP <https://faker.readthedocs.io/en/master/locales/ne_NP.html>`__ - Nepali
-  `nl\_NL <https://faker.readthedocs.io/en/master/locales/nl_NL.html>`__ - Dutch (Netherlands)
-  `no\_NO <https://faker.readthedocs.io/en/master/locales/no_NO.html>`__ - Norwegian
-  `pl\_PL <https://faker.readthedocs.io/en/master/locales/pl_PL.html>`__ - Polish
-  `pt\_BR <https://faker.readthedocs.io/en/master/locales/pt_BR.html>`__ - Portuguese (Brazil)
-  `pt\_PT <https://faker.readthedocs.io/en/master/locales/pt_PT.html>`__ - Portuguese (Portugal)
-  `ru\_RU <https://faker.readthedocs.io/en/master/locales/ru_RU.html>`__ - Russian
-  `sl\_SI <https://faker.readthedocs.io/en/master/locales/sl_SI.html>`__ - Slovene
-  `sv\_SE <https://faker.readthedocs.io/en/master/locales/sv_SE.html>`__ - Swedish
-  `tr\_TR <https://faker.readthedocs.io/en/master/locales/tr_TR.html>`__ - Turkish
-  `uk\_UA <https://faker.readthedocs.io/en/master/locales/uk_UA.html>`__ - Ukrainian
-  `zh\_CN <https://faker.readthedocs.io/en/master/locales/zh_CN.html>`__ - Chinese (China)
-  `zh\_TW <https://faker.readthedocs.io/en/master/locales/zh_TW.html>`__ - Chinese (Taiwan)

Command line usage
------------------

When installed, you can invoke faker from the command-line:

.. code:: bash

    faker [-h] [--version] [-o output]
          [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
          [-r REPEAT] [-s SEP]
          [-i {module.containing.custom_provider othermodule.containing.custom_provider}]
          [fake] [fake argument [fake argument ...]]

Where:

-  ``faker``: is the script when installed in your environment, in
   development you could use ``python -m faker`` instead

-  ``-h``, ``--help``: shows a help message

-  ``--version``: shows the program's version number

-  ``-o FILENAME``: redirects the output to the specified filename

-  ``-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}``: allows use of a localized
   provider

-  ``-r REPEAT``: will generate a specified number of outputs

-  ``-s SEP``: will generate the specified separator after each
   generated output

-  ``-i {my.custom_provider other.custom_provider}`` list of additional custom providers to use.
   Note that is the import path of the module containing your Provider class, not the custom Provider class itself.

-  ``fake``: is the name of the fake to generate an output for, such as
   ``name``, ``address``, or ``text``

-  ``[fake argument ...]``: optional arguments to pass to the fake (e.g. the profile fake takes an optional list of comma separated field names as the first argument)

Examples:

.. code:: bash

    $ faker address
    968 Bahringer Garden Apt. 722
    Kristinaland, NJ 09890

    $ faker -l de_DE address
    Samira-Niemeier-Allee 56
    94812 Biedenkopf

    $ faker profile ssn,birthdate
    {'ssn': u'628-10-1085', 'birthdate': '2008-03-29'}

    $ faker -r=3 -s=";" name
    Willam Kertzmann;
    Josiah Maggio;
    Gayla Schmitt;

How to create a Provider
------------------------

.. code:: python

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

How to use with Factory Boy
---------------------------

`Factory Boy` already ships with integration with ``Faker``. Simply use the
``factory.Faker`` method of ``factory_boy``:

.. code:: python

    import factory
    from myapp.models import Book

    class BookFactory(factory.Factory):
        class Meta:
            model = Book

        title = factory.Faker('sentence', nb_words=4)
        author_name = factory.Faker('name')

Accessing the `random` instance
-------------------------------

The ``.random`` property on the generator returns the instance of ``random.Random``
used to generate the values:

.. code:: python

    from faker import Faker
    fake = Faker()
    fake.random
    fake.random.getstate()

Seeding the Generator
---------------------

When using Faker for unit testing, you will often want to generate the same
data set. For convenience, the generator also provide a ``seed()`` method, which
seeds the random number generator. Calling the same script twice with the same
seed produces the same results.

.. code:: python

    from faker import Faker
    fake = Faker()
    fake.seed(4321)

    print fake.name()
    > Margaret Boehm

The code above is equivalent to the following:

.. code:: python

    from faker import Faker
    fake = Faker()
    fake.random.seed(4321)

    print fake.name()
    > Margaret Boehm

Tests
-----

Installing dependencies:

.. code:: bash

    $ pip install -r tests/requirements.txt

Run tests:

.. code:: bash

    $ python setup.py test

or

.. code:: bash

    $ python -m unittest -v tests

Write documentation for providers:

.. code:: bash

    $ python -m faker > docs.txt


Contribute
----------

Please see `CONTRIBUTING`_.

License
-------

Faker is released under the MIT License. See the bundled `LICENSE`_ file for details.

Credits
-------

-  `FZaninotto`_ / `PHP Faker`_
-  `Distribute`_
-  `Buildout`_
-  `modern-package-template`_


.. _FZaninotto: https://github.com/fzaninotto
.. _PHP Faker: https://github.com/fzaninotto/Faker
.. _Perl Faker: http://search.cpan.org/~jasonk/Data-Faker-0.07/
.. _Ruby Faker: http://faker.rubyforge.org/
.. _Distribute: https://pypi.python.org/pypi/distribute
.. _Buildout: http://www.buildout.org/
.. _modern-package-template: https://pypi.python.org/pypi/modern-package-template
.. _extended docs: https://faker.readthedocs.io/en/latest/
.. _bundled providers: https://faker.readthedocs.io/en/latest/providers.html
.. _community providers: https://faker.readthedocs.io/en/latest/communityproviders.html
.. _LICENSE: https://github.com/joke2k/faker/blob/master/LICENSE.txt
.. _CONTRIBUTING: https://github.com/joke2k/faker/blob/master/CONTRIBUTING.rst
.. _Factory Boy: https://github.com/FactoryBoy/factory_boy

.. |pypi| image:: https://img.shields.io/pypi/v/Faker.svg?style=flat-square&label=version
    :target: https://pypi.python.org/pypi/Faker
    :alt: Latest version released on PyPi

.. |coverage| image:: https://img.shields.io/coveralls/joke2k/faker/master.svg?style=flat-square
    :target: https://coveralls.io/r/joke2k/faker?branch=master
    :alt: Test coverage

.. |unix_build| image:: https://img.shields.io/travis/joke2k/faker/master.svg?style=flat-square&label=unix%20build
    :target: http://travis-ci.org/joke2k/faker
    :alt: Build status of the master branch on Mac/Linux

.. |windows_build|  image:: https://img.shields.io/appveyor/ci/joke2k/faker/master.svg?style=flat-square&label=windows%20build
    :target: https://ci.appveyor.com/project/joke2k/faker
    :alt: Build status of the master branch on Windows

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://raw.githubusercontent.com/joke2k/faker/master/LICENSE.txt
    :alt: Package license
