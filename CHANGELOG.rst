Changelog
=========

`0.5.1 - 21-May-2015 <http://github.com/joke2k/faker/compare/v0.5...v0.5.1>`__
------------------------------------------------------------------------------

* Fixed egg installation. Thanks David R. MacIver, @kecaps
* Updated person names for ru_RU. Thanks @mousebaiker.
* Updated ko_KR locale. Thanks Lee Yeonjae.
* Fixed installation to install importlib on Python 2.6. Thanks Guillaume Thomas.
* Improved tests. Thanks Aarni Koskela, @kecaps, @kaushal.
* Made Person `prefixes`/`suffixes` always return strings. Thanks Aarni Koskela.
* pl_PL jobs added. Thanks Dariusz Choruży.
* Added ja_JP provider. Thanks Tatsuji Tsuchiya, Masato Ohba.
* Localized remaining providers for consistency. Thanks Flavio Curella.
* List of providers in compiled on runtime and is not hardcoded anymore. Thanks Flavio Curella.
* Fixed State names in en_US. Thanks Greg Meece.
* Added `time_delta` method to `date_time` provider. Thanks Tobin Brown.
* Added filename and file extension methods to `file` provider. Thanks Tobin Brown.
* Added Finnish ssn (HETU) provider. Thanks @kivipe.
* Fixed person names for pl_PL. Thanks Marek Bleschke.
* Added sv_SE locale providers. Thanks Tome Cvitan.
* pt_BR Provider: Added `catch_phrase` to Company provider and fixed names in Person Provider. Thanks Marcelo Fonseca Tambalo. 
* Added sk_SK localized providers. Thanks @viktormaruna.
* Removed `miscelleneous` provider. It is superceded by the `misc` provider.

`0.5.0 - 16-Feb-2015 <http://github.com/joke2k/faker/compare/v0.4.2...v0.5>`__
------------------------------------------------------------------------------

* Localized providers
* Updated ko_KR provider. Thanks Lee Yeonjae.
* Added pt_PT provider. Thanks João Delgado.
* Fixed mispellings for en_US company provider. Thanks Greg Meece.
* Added currency provider. Thanks Wiktor Ślęczka
* Ensure choice_distribution always uses floats. Thanks Katy Lavallee.
* Added uk_UA provider. Thanks Cyril Tarasenko.
* Fixed encoding issues with README, CHANGELOG and setup.py. Thanks Sven-Hendrik Haase.
* Added Turkish person names and phone number patterns. Thanks Murat Çorlu.
* Added ne_NP provider. Thanks Sudip Kafle.
* Added provider for Austria de_AT. Thanks Bernhard Essl.

`0.4.2 - 20-Aug-2014 <http://github.com/joke2k/faker/compare/v0.4.1...v0.4.2>`__
--------------------------------------------------------------------------------

* Fixed setup

`0.4.1 - 20-Aug-2014 <http://github.com/joke2k/faker/compare/v0.4...v0.4.1>`__
------------------------------------------------------------------------------

* Added MAC address provider. Thanks Sébastien Béal.
* Added lt_LT and lv_LV localized providers. Thanks Edgar Gavrik.
* Added nl_NL localized providers. Thanks @LolkeAB, @mdxs.
* Added bg_BG localized providers. Thanks Bret B.
* Added sl_SI. Thanks to @janezkranjc
* Added distribution feature. Thanks to @fcurella
* Relative date time. Thanks to @soobrosa
* Fixed `date_time_ad` on 32bit Linux. Thanks @mdxs.
* Fixed `domain_word` to output slugified strings.

`0.4 - 30-Mar-2014 <http://github.com/joke2k/faker/compare/v0.3.2...v0.4>`__
----------------------------------------------------------------------------

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

