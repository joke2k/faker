How to contribute
=================

We love pull requests. Here's a quick guide:

Getting Started
---------------

-  Make sure you have a `GitHub account <https://github.com/signup/free>`__
-  Submit a ticket for your issue, assuming one does not already exist.
-  Clearly describe the issue including steps to reproduce when it is a bug.
-  Make sure you fill in the earliest version that you know has the issue.
-  Fork the repository on GitHub
-  Please only make changes or add data to locales you're familiar with.

Adding Providers
----------------

We only accept providers that are useful for general use. If you want to add a
domain-specific provider, you can package it independently, and we'll be happy to
add it to our `community providers`_ page.

Making Changes
--------------

-  Create a topic branch from where you want to base your work.
-  This is usually the master branch.
-  To quickly create a topic branch based on master;
   ``git branch fix/master/my_contribution master`` then checkout
   the new branch with ``git checkout fix/master/my_contribution``.
   Please avoid working directly on the ``master`` branch.
-  Make commits of logical units.
-  Follow our `coding style`_. You can run ``make lint`` to format your code.
-  Check for unnecessary whitespace with ``git diff --check`` before
   committing.
-  Make sure you have added the necessary tests for your changes.
-  Run ``make lint`` in the repository directory and commit any changes it makes.
-  Run *all* the tests to assure nothing else was accidentally broken:

   .. code:: bash

       $ python -m pip install tox
       $ tox

Submitting Changes
------------------

-  Make sure there isn't already a Pull Request opened by somebody else.
-  Push your changes to a topic branch in your fork of the repository.
-  Submit a pull request to the repository.

Additional Resources
====================

-  `General GitHub documentation <https://help.github.com>`__
-  `GitHub pull request
   documentation <https://help.github.com/articles/about-pull-requests>`__


.. _`coding style`: https://github.com/joke2k/faker/blob/master/docs/coding_style.rst
.. _`community providers`: https://github.com/joke2k/faker/blob/master/docs/communityproviders.rst

