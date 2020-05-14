Pytest Fixtures
===============

``Faker`` includes a ``faker`` fixture for ``pytest``.

.. code:: python

   def test_faker(faker):
       assert isinstance(faker.name(), str)

Out of the box, the ``faker`` fixture returns a session-scoped ``Faker`` instance to be used across
all tests in your test suite. This instance defaults to the ``en-US`` locale, and it is reseeded
using a seed value of ``0`` prior to each test.

To change the default locale, you can define a session-scoped autouse ``faker_session_locale``
fixture in your top level ``conftest.py``. To change the default seed value, you define a
session-scoped autouse ``faker_seed`` fixture. For example, if you want to use the ``it_IT``
locale and a seed value of ``12345``, then all you need to do is to include the following in
your top level ``conftest.py`` like so:

.. code:: python

   import pytest

   @pytest.fixture(scope='session', autouse=True)
   def faker_session_locale():
       return ['it_IT']

   @pytest.fixture(scope='session', autouse=True)
   def faker_seed():
       return 12345

If you need an instance with multiple locale support, then just return a list with multiple, unique,
and valid locales:

.. code:: python

   import pytest

   @pytest.fixture(scope='session', autouse=True)
   def faker_session_locale():
       return ['it_IT', 'ja_JP', 'en_US']

Configuration options
---------------------

As mentioned above, out of the box, a session-scoped ``Faker`` instance is returned for your use.
This is done so by design in order to prevent unnecessary ``Faker`` instantiations for most use
cases. Of course, there are some uncommon use cases where this approach is insufficient, which is
why the ``faker`` fixture is actually a function-scoped fixture that can be configured to behave
differently on demand.

.. important::

   Configuring the ``faker`` fixture requires some basic understanding of how ``pytest`` handles
   fixtures (more specifically scoping, sharing, injection). If you are not familiar with the topic,
   it is highly recommended to read up on `pytest fixtures`_ before proceeding.

Locale configuration
~~~~~~~~~~~~~~~~~~~~

If a ``faker_locale`` fixture is active for a test, the ``faker`` fixture will fallback to returning
a new ``Faker`` instance for that test (function-scoped), so if you do not like to use the session-scoped
``Faker`` instance, just define and activate a ``faker_locale`` fixture in the appropriate place in
accordance to how ``pytest`` handles fixtures.

For example, if you need to switch to a different locale only for certain tests, you may define an
autouse ``faker_locale`` fixture with a non-session scope in a submodule's ``conftest.py`` or in
the test files themselves like so:

.. code:: python

   import pytest

   @pytest.fixture(scope=any_non_session_scope, autouse=True)
   def faker_locale():
       return ['it_IT']

When the ``faker`` fixture is used in the relevant tests, the fixture will automatically use new
``Faker`` instances:

.. code:: python

   def test_something(faker):
       # The faker fixture here will return a new instance, not the session-scoped instance
       pass

If you want to be more explicit or if you need finer control over which tests should use a new
instance, you may drop ``autouse=True`` and use manual injection:

.. code:: python

   import pytest

   @pytest.fixture()
   def faker_locale():
       return ['it_IT']

   def test_something(faker):
       # The faker fixture will return the session-scoped instance
       pass

   def test_something_else(faker, faker_locale):
       # The faker fixture will return a new instance, not the session-scoped instance
       pass

Seeding configuration
~~~~~~~~~~~~~~~~~~~~~

On top of ``faker_locale``, the ``faker`` fixture also checks if a ``faker_seed`` fixture is active
for a test. If there is none, a seed value of ``0`` will be used, and if there is one, then the
return value will be used as the seed. The important thing to remember here is this: any test that
uses the ``faker`` fixture, whether it returns a session-scoped or a function-scoped ``Faker``
instance, is guaranteed a seeded instance. Seeding is performed independently of the instance
selection logic.

Like briefly mentioned above, defining an autouse session-scoped ``faker_seed`` fixture will affect
all relevant tests in the session, but if you want to use a certain seed for a specific set of tests
and just like ``faker_locale``, you will just need to define and activate a ``faker_locale`` fixture
in the appropriate place in accordance to how ``pytest`` handles fixtures. For example, if you declare
this in a submodule's ``conftest.py``, the ``faker`` fixture will return an instance seeded using
``12345`` for all relevant tests under that submodule.

.. code:: python

   import pytest

   @pytest.fixture(scope=any_non_session_scope,  autouse=True)
   def faker_seed():
       return 12345

If you want to be more explicit or if you need finer control over which tests should use a different
seed, you may drop ``autouse=True`` and use manual injection just as you would for ``faker_locale``:

.. code:: python

   import pytest

   @pytest.fixture(scope=any_non_session_scope)
   def faker_seed():
       return 12345

   def test_something(faker):
       # The faker fixture will use the session seed value
       pass

   def test_something_else(faker, faker_seed):
       # The faker fixture will use the seed value 12345
       pass

If you need multiple different seeds for each test, or if you need to reseed halfway inside a test,
you may still explicitly call ``seed_instance`` as you normally would with any ``Faker`` instance.
Doing so will not affect other tests because of the ``faker`` fixture's seeding guarantee.

.. code:: python

   # Assume the active seed value is 54321 for these tests

   def test_something_first(faker):
       # The faker fixture, at first, uses seed value 54321
       do_thing_a()

       # Explicit call to seed_instance
       faker.seed_instance(12345)

       # The faker fixture now uses seed value 12345
       do_thing_b()

   def test_something_second(faker):
       # The faker fixture's seed value is still 54321, not 12345
       pass

.. _pytest fixtures: https://docs.pytest.org/en/latest/fixture.html
