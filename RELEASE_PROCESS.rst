Release Process
---------------

This project releases automatically every time a PR is squash-merged.

The changelog is updated with a new entry containing the message commit, and the
library version number is incremented according the the labels on the PR:

* ``bump-version:major``: Increments the MAJOR version
* ``bump-version:minor``: Increments the MINOR version
* None of the above: Increments the PATCH version.

If more than one label is applied to the PR, only the highest part gets incremented.

Bugfixes and Pull requests updating data for existing providers will result in a patch bump.

Pull requests that adds new methods to existing providers, or add new providers will
result in a minor bump.

Breaking changes such as change of functionality, removal of methods, etc will result in
a major bump.
