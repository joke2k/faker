Coding Style
============

Lines length should not exceed 120 characters. Please use trailing commas.

You can find our complete flake8 configuration in the tox.ini_ file.


Encoding
--------

Every Python source file should be encoded as UTF-8.
As per `PEP 263`_, the first or the second line must be::

    # coding=utf-8


Data Sets
---------

For each data set, please provide a comment with reference to the source
and/or origin of the data.

We only accept new data if it's coming from statistical sources, such as census or government institutions. This include names and their distribution.


Name Lists
----------

When you have long lists of names, please order them alphabetically. Keep the lines length as close as possible to 120 characters, without exceeding the limit.

.. _`tox.ini`: https://github.com/joke2k/faker/blob/master/tox.ini
.. _`pep 8`: https://python.org/dev/peps/pep-0008
.. _`pep 263`: https://python.org/dev/peps/pep-0263

Tests
-----

Use `factory.seed` to check for specific cases, and avoid using loops in order to get values you are looking for. Seeding with specific values will  make the test deterministic, faster and will help you target each condition of your code, increasing coverage.

For example::

    # Bad
    def test_ssn(self):
        for _ in range(100):
            assert re.search(r'^\d{11}$', self.factory.ssn())
    
    # Good
    def test_ssn(self):
        self.factory.seed(0)
        value = self.factory.ssn()
        assert re.search(r'^\d{11}$', value)
        assert not value.endswith('0')

        self.factory.seed(18)
        value = self.factory.ssn()
        assert re.search(r'^\d{11}$', value)
        assert value.endswith('0')
