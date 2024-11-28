# from README.rst
"""
*Faker* is a Python package that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

Faker is heavily inspired by `PHP Faker`_, `Perl Faker`_, and by `Ruby Faker`_.

Check the `extended docs`_ for more information.

----

::

    _|_|_|_|          _|
    _|        _|_|_|  _|  _|      _|_|    _|  _|_|
    _|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
    _|      _|    _|  _|  _|    _|        _|
    _|        _|_|_|  _|    _|    _|_|_|  _|

----


Contribute
----------

Please see `CONTRIBUTING`_.

License
-------

Faker is released under the MIT License. See the bundled `LICENSE`_ file
for details.

Credits
-------

-  `FZaninotto`_ / `PHP Faker`_
-  `Distribute`_
-  `Buildout`_
-  `modern-package-template`_


.. _FZaninotto: https://github.com/fzaninotto
.. _PHP Faker: https://github.com/fzaninotto/Faker
.. _Perl Faker: http://search.cpan.org/~jasonk/Data-Faker-0.07/
.. _Ruby Faker: https://github.com/stympy/faker
.. _Distribute: https://pypi.org/project/distribute/
.. _Buildout: http://www.buildout.org/
.. _modern-package-template: https://pypi.org/project/modern-package-template/
.. _extended docs: https://faker.readthedocs.io/en/stable/
.. _bundled providers: https://faker.readthedocs.io/en/stable/providers.html
.. _community providers: https://faker.readthedocs.io/en/stable/communityproviders.html
.. _LICENSE: https://github.com/joke2k/faker/blob/master/LICENSE.txt
.. _CONTRIBUTING: https://github.com/joke2k/faker/blob/master/CONTRIBUTING.rst
"""

from faker.factory import Factory
from faker.generator import Generator
from faker.proxy import Faker

VERSION = "33.1.0"

__all__ = ("Factory", "Generator", "Faker")
