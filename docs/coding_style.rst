Coding Style
============

We use the black code style with a line length of 120 characters and trailing commas.

You can format the code with::

    black --line-length 120

Please include `type hints`_ for every provider method you write. An overview of generic types is included below.

You can find our complete flake8 configuration in the tox.ini_ file.


Data Sets
---------

For each data set, please provide a comment with reference to the source
and/or origin of the data.

We only accept new data if it's coming from statistical sources, such as census or government institutions.
This include names and their distribution.


Name Lists
----------

When you have long lists of names, please order them alphabetically. Keep the lines length as close as
possible to 120 characters, without exceeding the limit.

Type Hints
----------
``typing.py`` includes generic types that can be re-used throughout the codebase. Moreover, some type definitions are
included in other parts of the code. If you add a generic type, please specify its usage below:


.. list-table:: Title
   :widths: 15 60
   :header-rows: 1

   * - Type
     - Used for
   * - ``providers.ElementsType``
     - When creating a variable in a ``Provider`` (e.g. for a specific locale), which is not defined in the superclass, ``self.random_element()``, ``self.random_elements()``, ``self.random_choices()`` and ``self.random_sample()`` assume this to be the input format.
   * - ``typing.DateParseType``
     - Input for various ``faker.providers.date_time`` functions that parse (relative) dates/times.
   * - ``typing.HueType``
     - Hue name, float value or integer range.
   * - ``typing.GenderType``
     - String variable that can only have values ``"F"`` (female) and ``"M"`` (male)

.. _`tox.ini`: https://github.com/joke2k/faker/blob/master/tox.ini
.. _`pep 8`: https://python.org/dev/peps/pep-0008
.. _`pep 263`: https://python.org/dev/peps/pep-0263
.. _`type hints`: https://docs.python.org/3/library/typing.html
