Writing Documentation
=====================

Everything under :doc:`Standard Providers <providers>` and :doc:`Localized Providers <locales>`
is automatically generated using ``sphinx.ext.autodoc`` which pulls docstrings from provider
methods during the ``sphinx-build`` process. This also means that the docstrings must be written
in valid ``reStructuredText``.

Furthermore, because of the nature of this library, it is imperative to include sample usage to
best demonstrate the capabilities and the possibilities. Since there are so many provider methods
and localized versions, keeping the docs updated would have been a nightmare if the sample usage
section (with reproducible output) of each provider method were to be written by hand.

Automating sample usage sections
--------------------------------

To ease the burden of docs maintenance, the project takes advantage of docstring preprocessing offered
by ``sphinx.ext.autodoc`` to automatically generate sample usage section, complete with reproducible
output, all from a couple of lines of text using a ``:sample:`` "pseudo-role" like so:

.. code-block::

   :sample[ size=SIZE][ seed=SEED]:[ KWARGS]

What this will do is generate a sample usage section by calling the provider method ``SIZE`` times using
an initial seed value of ``SEED`` with optional keyword arguments ``KWARGS``. If no ``SIZE`` is specified
or if ``SIZE`` is less than ``5``, it defaults to ``5``. If no ``SEED`` is specified, it defaults to ``0``.

For example, let us assume that the line ``:sample:`` is present in the docstring of a provider method
named ``method1``. That short line of text will automatically generate a sample usage section like this:

.. code-block:: python

   >>> Faker.seed(0)
   >>> for _ in range(5):
   ...     fake.method1()
   ...
   # Output 1
   # Output 2
   # Output 3
   # Output 4
   # Output 5


Depending on the nature of the provider method, the default of 5 samples may not be enough, so it is
possible to increase that by using ``size=SIZE``. You may also want to supply arguments to change the
behavior of the method, so that can be done using ``KWARGS``. Putting it all together, if we use
``:sample size=10: a=1, b=2, c=3``, the sample usage section generated will look like this:

.. code-block:: python

   >>> Faker.seed(0)
   >>> for _ in range(10):
   ...     fake.method1(a=1, b=2, c=3)
   ...
   # Output 1
   # Output 2
   # Output 3
   # Output 4
   # Output 5
   # Output 6
   # Output 7
   # Output 8
   # Output 9
   # Output 10


There may also be times when it is desirable to show a particular output, but the pseudo-RNG gets in
the way, e.g. very low chance of said output being generated. To work around this, you may use
``seed=SEED`` to specify an initial seed value that is known to generate the desired output. If we
specify ``:sample seed=12345: a=2``, the sample usage section generated will look like this:

.. code-block:: python

   >>> Faker.seed(12345)
   >>> for _ in range(5):
   ...     fake.method1(a=2)
   ...
   # Output 1
   # Output 2
   # Output 3
   # Output 4
   # Output 5


You can mix and match ``SIZE``, ``SEED``, and ``KWARGS``, and if ``KWARGS`` is becoming too long to
fit a single line, you can break ``KWARGS`` into multiple lines in the same way you can break keyword
arguments across multiples lines in actual Python code. For example, let us say the docstring contains
this:

.. code-block:: text

   :sample size=25 seed=12345: arg1='very long value, unfortunately',
                               arg2='yet another long value'

The sample section usage generated will look something like this:

.. code-block:: python

   >>> Faker.seed(12345)
   >>> for _ in range(25):
   ...     fake.method1(arg1='very long value, unfortunately', arg2='yet another long value')
   ...
   # Output 1
   # Output 2
   # ...
   # Output 24
   # Output 25

Docstring preprocessing behavior
--------------------------------

If a provider method does not have a docstring or if the docstring does not contain properly
formatted ``:sample:`` lines, a default sample usage section will automatically be generated
for the benefit of insufficiently documented provider methods.

A docstring may contain multiple ``:sample:`` lines, and all prospective ``:sample:`` lines are
first checked to see if they are properly formatted. Malformed instances will be discarded, and
details will be logged to the console as a warning. All properly formatted ``:sample:`` lines will
then be removed from the docstring and will undergo sample validation and generation, and the
resulting docstring will have an ``:examples:`` section appended to the end. In code form:

.. code-block:: python

   # Source code docstring
   def foo():
       """Summary line

       Lorem ipsum dolor sit amet, consectetur adipiscing elit.
       Fusce auctor faucibus condimentum.

       :sample:

       Duis posuere lacinia porta.
       Quisque mauris nisl, mattis sed ornare eget, accumsan sit amet mauris.

       :sample size=10 seed=1000:
       """
       return 1


.. code-block:: python

   # Resulting docstring (more or less) after preprocessing
   def foo():
       """Summary line

       Lorem ipsum dolor sit amet, consectetur adipiscing elit.
       Fusce auctor faucibus condimentum.


       Duis posuere lacinia porta.
       Quisque mauris nisl, mattis sed ornare eget, accumsan sit amet mauris.

       :examples:

       >>> Faker.seed(0)
       >>> for _ in range(5):
       ...     fake.foo()
       ...
       1
       1
       1
       1
       1

       >>> Faker.seed(1000)
       >>> for _ in range(10):
       ...     fake.foo()
       ...
       1
       1
       1
       1
       1
       1
       1
       1
       1
       1
       """
       pass


Notice how it did not remember where the ``:sample:`` lines are. Regardless of the original positions
of the ``:sample:`` lines, the resulting output of all those lines will be collected and appended
towards the end of the docstring. Please keep this in mind when structuring the flow of docstrings.

There are definitely benefits in allowing sample sections to be generated in place as it make the
creation of richer documentation possible, but unfortunately it is not yet possible due to time
constraints. Until that feature is available, please keep all ``:sample:`` lines towards the end
of the docstring to help out the code reviewers.

Sample validation and security segue
------------------------------------

Under the hood, the sample sections are generated by feeding the parsed docstring sample lines
into the standard library's ``eval()``. This setup most definitely have some security implications
out of the box, and this is why ``:sample:`` lines undergo validation prior to generation.

There are many details behind the validation process, but the long and short of it is that ``SIZE``
and ``SEED`` can only be integers, and ``KWARGS`` can only be keyword arguments with literal values
or ``OrderedDict`` objects. Attempting to do anything else like calling other builtins or even just
performing basic arithmetic will fail the validation. Details of failed validation will be logged
to the console as a warning.

To further improve security, all of the potentially dangerous code used for this purpose have been
isolated into the ``faker.sphinx`` module, and this module will be excluded from release distributions
that are hosted in PyPI.

If you are interested in learning more or in performing a security audit on how sample validation is
implemented, please refer to the source code and docstrings of ``faker.sphinx.validator.SampleCodeValidator``
and ``faker.sphinx.docstring.ProviderMethodDocstring``.

Sample generation
-----------------

Once a ``:sample:`` line has been validated, the ``sphinx-build`` process will attempt to generate
results based on the information provided. A sample run can still fail if ``KWARGS`` contains keyword
arguments that the provider method is not expecting or if executing the provider method results in
an exception. Details of such instances will also be logged to the console as a warning.
