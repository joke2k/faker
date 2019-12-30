Using the Faker Class
=====================

In version ``2.0.4`` and below, the ``Faker`` object is just a shortcut for the class method
``Factory.create``, and that method creates a ``Generator`` object with access to the wide
selection of provider methods. Because of how everything was set up, it was difficult to do
certain things without going through the ``Factory`` and ``Generator`` internals and without
potentially breaking a lot of things that will be difficult for users to fix when they upgrade.

The solution was to introduce a new ``Faker`` proxy class that will, for the most part, behave
just like the old ``Faker`` shortcut but with support for multiple locales while providing the
option to subclass and a very simple upgrade path should old code be affected. For the purposes
of this document, the terms new ``Faker`` and old ``Faker`` will be used where the former refers
to the new proxy class, and the latter refers to the ``Factory.create`` shortcut.

Breaking Change
---------------

Any codebase that uses the ``Faker.seed()`` method will be affected, because while both old and
new ``Faker.seed()`` points to ``Generator.seed()``, in new ``Faker``, invocation of the method
from a ``Faker`` object instance has been disabled, and attempting to do so will raise a
``TypeError`` as shown below.

.. code:: python

    TypeError: Calling `.seed()` on instances is deprecated. Use the class method `Faker.seed()` instead.

The rationale can be found in `the relevant PR`_, but the goal is to deal with a non-explicit
legacy behavior involving a shared ``random.Random`` instance that we believe can only become
more confusing once new ``Faker`` is added.

Upgrade Guide
-------------

Suppose that the affected code looks something like this:

.. code:: python

    from faker import Faker
    fake = Faker()
    fake.seed(0)  # This will raise a TypeError

Just replace all `seed()` method calls from instances with ``Faker.seed()`` as shown below. This
is all that is needed to start using the new ``Faker`` class and its features, even if additional
arguments are passed to ``Faker``, because the arguments expected by new ``Faker`` and old
``Faker`` are the same.

.. code:: python

    from faker import Faker
    fake = Faker()
    Faker.seed(0)

A conservative approach is to redefine ``Faker`` as the old shortcut shown below. This will skip
using the new proxy class, but the code will still be able to use any new provider methods moving
forward while being unaffected by new bugs. Of course, that also means there will be no multiple
locale support and no option to subclass.

.. code:: python

    from faker.factory import Factory
    Faker = Factory.create
    fake = Faker()
    fake.seed(0)

Proxy Class Implementation Details
----------------------------------

A new ``Faker`` instance is just a proxy object that has references to ``Generator`` objects,
one for each unique locale specified at instantiation. Those ``Generator`` objects are just
"instances" of old ``Faker``. If there is only one internal ``Generator`` object, the new
``Faker`` instance is running in single locale mode. If there is more than one, then it is
running in multiple locale mode.

In single locale mode, a new ``Faker`` instance can easily be forced to behave like an instance
created using old ``Faker``, because a similar interface can be exposed on the new ``Faker``
instance, and then proxy calls to methods, properties, and attributes to the sole ``Generator``
object in a 1:1 fashion. In fact, that is how it is implemented and how backwards compatibility
was preserved (save for ``Faker.seed``).

In multiple locale mode, however, that 1:1 mapping is no longer present, and how calls are proxied
depends on whether the attribute is a provider method or some attribute present in ``Generator``
objects. It is possible to provide sane default implementations that will map neatly like what
we did for ``seed_instance``, but the rest like `add_provider` and the `random` getter and setter
are more dependent on specific use cases or are potentially dangerous.

In those cases, it is better for users to create their own subclass with their implementation or to
directly call those methods from the internal ``Generator`` objects themselves. Multiple locale mode
will be discussed in more detail in its `dedicated section`_.

Proxy Class Attribute Name Resolution
-------------------------------------

The proxy class has a fairly involved attribute name resolution behavior that runs in this order:

1. If the attribute name is ``seed``, raise a TypeError. This prevents the class method ``seed``
   from being called from an instance.
2. If #1 does not apply, check if the attribute name matches an attribute present in the proxy
   class instance. If there is one, return the matching attribute.
3. If #2 failed, check if the instance is in single locale mode. If yes, proxy the call to the
   sole internal ``Generator`` object, and attempt to return a matching attribute.
4. If #3 does not apply, the instance is henceforth known to be in multiple locale mode. Proceed
   by checking if the attribute name matches a ``Generator`` attribute. If it does, raise a
   NotImplementedError.
5. If #4 does not apply, check if the attribute name matches a cache pattern regex. If it does not,
   raise an AttributeError, since it should already have been handled by #2 if one does exist.
6. If everything else has failed or does not apply, assume that the attribute name might be
   referring to a provider method and perform factory/generator selection, and proxy the call
   to the selected ``Generator`` object.

Factory/generator selection will be discussed in more detail under multiple locale mode's
`dedicated section`_.

Locale Normalization
--------------------

Depending on the ``locale`` value passed, a new ``Faker`` instance will either operate in single
locale mode or multiple locale mode. The value of ``locale`` can be one of the following:

1. Any empty value like ``None`` (automatically defaults to ``en_US``)
2. A valid locale string, underscored or hyphenated
3. A list, tuple, or set with valid locale strings, underscored or hyphenated
4. An OrderedDict with key-value pairs of valid locale strings (underscored or
   hyphenated) and weights

The first two are options already expected by old ``Faker``, so it is pretty much the same for new
``Faker``. Using any of those two options will always result in a new ``Faker`` instance that is
in single locale mode. In that mode, there is really no need to retrieve a reference to the
internal ``Generator`` object because of the 1:1 proxying behavior discussed earlier.

The potential pitfalls lie in multiple locale mode and when there is a need to access the internal
``Generator`` objects individually. Since locale strings can be written underscored (``en_US``) or
hyphenated (``en-US``), this can lead to confusion and errors, so locale strings have to be normalized
to provide consistent results without duplicates.

During instantiation, new ``Faker`` will normalize locale strings to the underscore format, and it
will also store them as such. In other words, the locale string ``en_US`` will be treated the same
as ``en-US``, and when both are specified, the last to be processed will be treated as a duplicate
and will be discarded. The same normalization is also performed when accessing the internal
``Generator`` object via key index.

For example, the code below will create a new ``Faker`` instance that is in single locale mode
even if four locales were specified.

.. code:: python

    from faker import Faker
    fake = Faker(['en-US', 'en_US', 'en_US', 'en-US'])

    # Will return ['en_US']
    fake.locales

    # Get reference to en_US generator
    us1 = fake['en_US']

    # Get reference to en-US generator
    us2 = fake['en-US']

    # Will return True
    us1 == us2

.. _dedicated section:

Multiple Locale Mode
--------------------

To enable multiple locale mode, the value of ``locale`` argument must be a list, tuple, set, or
OrderedDict with more than one valid locale, post-normalization. For example:

.. code:: python

    from collections import OrderedDict
    from faker import Faker

    locale_list = ['en-US', 'ja-JP', 'en_US']
    fake1 = Faker(locale_list)

    # Will return ['en_US', 'ja_JP']
    fake1.locales

    locale_odict = OrderedDict([
        ('en-US', 1),
        ('ja-JP', 2),
        ('en_US', 2),
    ])
    fake2 = Faker(odict)

    # Will return ['en_US', 'ja_JP']
    fake1.locales

In this mode, calling a prospective provider method from the new ``Faker`` instance will run
factory/selection logic in this order:

1. Check if a cached mapping already exists for the provider method. If yes, use that mapping,
   and skip to #3.
2. If #1 does not apply, check which ``Generator`` objects support the provider method. Cache
   the results of the mapping, along with corresponding weights if they were provided during
   instantiation.
3. If no generator supports the provider method, an AttributeError will be raised just as it
   would have been raised using old ``Faker``.
4. If there is only one generator that supports the provider method, return the only generator.
5. If there is more than one applicable generator, and no weights were provided, randomly select
   a generator using a uniform distribution, i.e. ``random.choice``.
6. If there is more than one applicable generator, and weights were provided, randomly select
   a generator using a distribution defined by the provided weights.

Other than being able to customize probabilities based on locales and minimizing performance
penalties, the factory selection logic guarantees that invoking a provider method will not fail,
for as long as at least there is at least one internal ``Generator`` object supports it.

Examples
--------

There are times when it is much easier to show than it is to explain in words, so here is
a cheatsheet for new ``Faker`` in multiple locale mode.

.. code:: python

    from collections import OrderedDict
    from faker import Faker
    locales = OrderedDict([
        ('en-US', 1),
        ('en-PH', 2),
        ('ja_JP', 3),
    ])
    fake = Faker(locales)

    # Get the list of locales specified during instantiation
    fake.locales

    # Get the list of internal generators of this `Faker` instance
    fake.factories

    # Get the internal generator for 'en_US' locale
    fake['en_US']

    # Get the internal generator for 'en_PH' locale
    fake['en_PH']

    # Get the internal generator for 'ja_JP' locale
    fake['ja_JP']

    # Will raise a KeyError as 'en_GB' was not included
    fake['en_GB']

    # Set the seed value of the shared `random.Random` object
    # across all internal generators that will ever be created
    Faker.seed(0)

    # Creates and seeds a unique `random.Random` object for
    # each internal generator of this `Faker` instance
    fake.seed_instance(0)

    # Creates and seeds a unique `random.Random` object for
    # the en_US internal generator of this `Faker` instance
    fake.seed_locale('en_US', 0)

    # Generate a name based on the provided weights
    # en_US - 16.67% of the time (1 / (1 + 2 + 3))
    # en_PH - 33.33% of the time (2 / (1 + 2 + 3))
    # ja_JP - 50.00% of the time (3 / (1 + 2 + 3))
    fake.name()

    # Generate a name under the en_US locale
    fake['en-US'].name()

    # Generate a zipcode based on the provided weights
    # Note: en_PH does not support the zipcode provider method
    # en_US - 25% of the time (1 / (1 + 3))
    # ja_JP - 75% of the time (3 / (1 + 3))
    fake.zipcode()

    # Generate a zipcode under the ja_JP locale
    fake['ja_JP'].zipcode()

    # Will raise an AttributeError
    fake['en_PH'].zipcode()

    # Generate a Luzon province name
    # Note: only en_PH out of the three supports this provider method
    fake.luzon_province()

    # Generate a Luzon province name
    fake['en_PH'].luzon_province()

    # Will raise an AttributeError
    fake['ja_JP'].luzon_province()

.. _the relevant PR: https://github.com/joke2k/faker/pull/1052#issuecomment-557170225
