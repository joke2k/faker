Changelog
=========

0.5 - 16-Feb-2015
-----------------

* Localized providers
* Updated ko_KR provider. Thanks Lee Yeonjae.
* Added pt_PT provider. Thanks JoÃ£o Delgado.
* Fixed mispellings for en_US company provider. Thanks Greg Meece.
* Added currency provider. Thanks Wiktor ÅšlÄ™czka
* Ensure choice_distribution always uses floats. Thanks Katy Lavallee.
* Added uk_UA provider. Thanks Cyril Tarasenko.
* Fixed encoding issues with README, CHANGELOG and setup.py. Thanks Sven-Hendrik Haase.
* Added Turkish person names and phone number patterns. Thanks Murat Ã‡orlu.
* Added ne_NP provider. Thanks Sudip Kafle.
* Added provider for Austria de_AT. Thanks Bernhard Essl.

0.4.2 - 20-Aug-2014
-------------------

* Fixed setup

0.4.1 - 20-Aug-2014
-------------------

* Added MAC address provider. Thanks Sébastien Béal.
* Added lt_LT and lv_LV localized providers. Thanks Edgar Gavrik.
* Added nl_NL localized providers. Thanks @LolkeAB, @mdxs.
* Added bg_BG localized providers. Thanks Bret B.
* Added sl_SI. Thanks to @janezkranjc
* Added distribution feature. Thanks to @fcurella
* Relative date time. Thanks to @soobrosa
* Fixed `date_time_ad` on 32bit Linux. Thanks @mdxs.
* Fixed `domain_word` to output slugified strings.

0.4 - 30-Mar-2014
-----------------

* Modified en_US ``person.py`` to ouput female and male names. Thanks Adrian Klaver.
* Added SSN provider for ``en_US`` and ``en_CA``. Thanks Scott (@milliquet).
* Added ``hi_IN`` localized provider. Thanks Pratik Kabra.
* Refactoring of command line

0.3.2 - 11-Nov-2013
-------------------

* New provider: Credit card generator
* Improved Documentor


0.3.1
-----

* FIX setup.py


0.3 - 18-Oct-2013
-----------------

* PEP8 style conversion (old camelCased methods are deprecated!)
* New language: ``pt_BR`` (thanks to @rvnovaes)
* all localized provider now uses ``from __future__ import unicode_literals``
* documentor prints localized provider after all defaults
* FIX tests for python 2.6


0.2 - 01-Dec-2012
-----------------

* New providers: ``Python``, ``File``
* Providers imported with ``__import__``
* Module is runnable with ``python -m faker [name] [*args]``
* Rewrite fake generator system (allow autocompletation)
* New language: French
* Rewrite module ``__main__`` and new Documentor class

0.1 - 13-Nov-2012
-----------------

* First release

