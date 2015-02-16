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

Making Changes
--------------

-  Create a topic branch from where you want to base your work.
-  This is usually the master branch.
-  Only target release branches if you are certain your fix must be on
   that branch.
-  To quickly create a topic branch based on master;
   ``git branch fix/master/my_contribution master`` then checkout
   the new branch with ``git checkout fix/master/my_contribution``.
   Please avoid working directly on the ``master`` branch.
-  Make commits of logical units.
-  Check for unnecessary whitespace with ``git diff --check`` before
   committing.
-  Make sure your commit messages are in the proper format.

::

        Make the example in CONTRIBUTING imperative and concrete

        Without this patch applied the example commit message in the CONTRIBUTING
        document is not a concrete example.  This is a problem because the
        contributor is left to imagine what the commit message should look like
        based on a description rather than an example.  This patch fixes the
        problem by making the example concrete and imperative.

        The first line is a real life imperative statement with a ticket number
        from our issue tracker.  The body describes the behavior without the patch,
        why this is a problem, and how the patch fixes the problem when applied.

-  Make sure you have added the necessary tests for your changes.
-  Run *all* the tests to assure nothing else was accidentally broken.

Submitting Changes
------------------

-  Push your changes to a topic branch in your fork of the repository.
-  Submit a pull request to the repository.

Additional Resources
====================

-  `General GitHub documentation <http://help.github.com/>`__
-  `GitHub pull request
   documentation <http://help.github.com/send-pull-requests/>`__

