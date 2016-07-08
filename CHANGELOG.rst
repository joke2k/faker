
Changelog
=========

`0.5.9 - 08-July-2016 <http://github.com/joke2k/faker/compare/v0.5.8...v0.5.9>`__
---------------------------------------------------------------------------------

* Add more ``pt_BR`` names. Thanks @cuducos.
* Added ``en_GB`` names. Thanks @jonny5532.
* Add romanized internet provider for ``zh_CN``.
* Add ``fr_CH`` providers. Thanks @gfavre.

`0.5.8 - 28-June-2016 <http://github.com/joke2k/faker/compare/v0.5.7...v0.5.8>`__
---------------------------------------------------------------------------------

* Improve CLI output and help. Thanks @cbaines.
* Update ``en_US`` anmes to be more realistic. Thanks @dethpickle.
* Modify pystr provider to accept a minimum number of characters. Thanks @tamarbuta.
* Add `job` Provider for ``zh_TW``. Thanks @weihanglo.
* Modify ``zh_TW`` phone number for a more valid format. Thanks @weihanglo.
* Reduce the maximum value of start timestamps. Thanks @cbaines.
* Add `random_sample` and `random_sample_unique`. Thanks @bengolder.

`0.5.7 - 07-March-2016 <http://github.com/joke2k/faker/compare/v0.5.6...v0.5.7>`__
----------------------------------------------------------------------------------

* Repackage to resolve PyPI issue.

`0.5.6 - 07-March-2016 <http://github.com/joke2k/faker/compare/v0.5.5...v0.5.6>`__
----------------------------------------------------------------------------------

* Add date handling for datetime functions. Thanks @rpkilby.
* Discern male and female first names in pt_BR. Thanks @gabrielusvicente.

`0.5.5 - 29-February-2016 <http://github.com/joke2k/faker/compare/v0.5.4...v0.5.5>`__
--------------------------------------------------------------------------------------

* Specify help text for command line. Thanks @cbaines.

`0.5.4 - 29-February-2016 <http://github.com/joke2k/faker/compare/v0.5.3...v0.5.4>`__
--------------------------------------------------------------------------------------

* Expose Provider's random instance. Thank @gsingers for the suggestion.
* Make sure required characters are in the password. Thanks @craig552uk.
* Add ``internet`` and ``job`` Providers for ``fa_IR``. Thanks @hamidfzm.
* Correct Poland phone numbers. Thanks @fizista.
* Fix brittly tests due to seconds elapsed in-between comparison
* Allow unicode in emails and domains. Thanks @zdelagrange for the report.
* Use ``dateutil`` for computing next_month. Thanks @mark-love, @rshk.
* Fix tests module import. Thanks @jorti for the report.
* Handle unexpected length in ``ean()``. Thanks @michaelcho.
* Add internet provider for ``ja_JP``. Thanks @massa142.
* Add Romanized Japanese person name. Thanks @massa142.
* Add tzinfo support to datetime methods. Thanks @j0hnsmith.
* Add an 'office' file extensions category. Thanks @j0hnsmith.
* Generate name according to profile's sex. Thanks @Dutcho for the report.
* Add ``bs_BA`` phone number and internet provider. Thanks @elahmo.
* Add a SSN provider for ``zh_CN``. Thanks @felixonmars.
* Differentiate male and female first names in ``fr_FR`` locale. Thanks @GregoryVds
* Add Maestro credit card. Thanks @anthonylauzon.
* Add ``hr_HR`` localization. Thanks @mislavcimpersak.
* Update ``de_DE`` first names. Thanks @WarrenFaith and @mschoebel.
* Allow generation of IPv4 and IPv6 network address with valid CIDR. Thanks @kdeldycke.
* Unittest IPv4 and IPv6 address and network generation. Thanks @kdeldycke.
* Add a new provider to generate random binary blob. Thanks @kdeldycke.
* Check that randomly produced language codes are parseable as locale by the
  factory constructor. Thanks @kdeldycke.
* Fix chinese random language code. Thanks @kdeldycke.
* Remove duplicate words from Lorem provider. Thanks @jeffwidman. 

`0.5.3 - 21-September-2015 <http://github.com/joke2k/faker/compare/v0.5.2...v0.5.3>`__
--------------------------------------------------------------------------------------

* Added ``company_vat`` to company ``fi_FI`` provider. Thanks @kivipe.
* Seed a Random instance instead of the module. Thanks Amy Hanlon.
* Fixed en_GB postcodes to be more realistic. Thanks @mapleoin for the report.
* Fixed support for Python 3 in the python provider. Thanks @derekjamescurtis.
* Fixed U.S. SSN generation. Thanks @jschaf.
* Use environment markers for wheels. Thanks @RonnyPfannschmidt
* Fixed Python3 issue in ``pyiterable`` and ``pystruct`` providers. Thanks @derekjamescurtis.
* Fixed ``en_GB`` postcodes to be more realistic. Thanks @mapleoin.
* Fixed and improved performance of credit card number provider. Thanks @0x000.
* Added Brazilian SSN, aka CPF. Thanks @ericchaves.
* Added female and male names for ``fa_IR``. Thanks @afshinrodgar.
* Fixed issues with Decimal objects as input to geo_coordinate. Thanks @davy.
* Fixed bug for ``center`` set to ``None`` in geo_coordinate. Thanks @davy.
* Fixed deprecated image URL placeholder services.
* Fixed provider's example formatting in documentation.
* Added en_AU provider. Thanks @xfxf.

`0.5.2 - 11-June-2015 <http://github.com/joke2k/faker/compare/v0.5.1...v0.5.2>`__
---------------------------------------------------------------------------------

* Added ``uuid4`` to ``misc`` provider. Thanks Jared Culp.
* Fixed ``jcb15`` and ``jcb16`` in ``credit_card`` provider. Thanks Rodrigo Braz.
* Fixed CVV and CID code generation in `credit_card` provider. Thanks Kevin Stone.
* Added ``--include`` flag to command line tool. Thanks Flavio Curella.
* Added ``country_code`` to `address`` provider. Thanks @elad101 and Tobin Brown.


`0.5.1 - 21-May-2015 <http://github.com/joke2k/faker/compare/v0.5...v0.5.1>`__
------------------------------------------------------------------------------

* Fixed egg installation. Thanks David R. MacIver, @kecaps
* Updated person names for ``ru_RU``. Thanks @mousebaiker.
* Updated ko_KR locale. Thanks Lee Yeonjae.
* Fixed installation to install importlib on Python 2.6. Thanks Guillaume Thomas.
* Improved tests. Thanks Aarni Koskela, @kecaps, @kaushal.
* Made Person ``prefixes``/``suffixes`` always return strings. Thanks Aarni Koskela.
* ``pl_PL`` jobs added. Thanks Dariusz Choruży.
* Added ``ja_JP`` provider. Thanks Tatsuji Tsuchiya, Masato Ohba.
* Localized remaining providers for consistency. Thanks Flavio Curella.
* List of providers in compiled on runtime and is not hardcoded anymore. Thanks Flavio Curella.
* Fixed State names in ``en_US``. Thanks Greg Meece.
* Added ``time_delta`` method to ``date_time`` provider. Thanks Tobin Brown.
* Added filename and file extension methods to ``file`` provider. Thanks Tobin Brown.
* Added Finnish ssn (HETU) provider. Thanks @kivipe.
* Fixed person names for ``pl_PL``. Thanks Marek Bleschke.
* Added ``sv_SE`` locale providers. Thanks Tome Cvitan.
* ``pt_BR`` Provider: Added ``catch_phrase`` to Company provider and fixed names in Person Provider. Thanks Marcelo Fonseca Tambalo.
* Added ``sk_SK`` localized providers. Thanks @viktormaruna.
* Removed ``miscelleneous`` provider. It is superceded by the ``misc`` provider.

`0.5.0 - 16-Feb-2015 <http://github.com/joke2k/faker/compare/v0.4.2...v0.5>`__
------------------------------------------------------------------------------

* Localized providers
* Updated ``ko_KR`` provider. Thanks Lee Yeonjae.
* Added ``pt_PT`` provider. Thanks João Delgado.
* Fixed mispellings for ``en_US`` company provider. Thanks Greg Meece.
* Added currency provider. Thanks Wiktor Ślęczka
* Ensure choice_distribution always uses floats. Thanks Katy Lavallee.
* Added ``uk_UA`` provider. Thanks Cyril Tarasenko.
* Fixed encoding issues with README, CHANGELOG and setup.py. Thanks Sven-Hendrik Haase.
* Added Turkish person names and phone number patterns. Thanks Murat Çorlu.
* Added ``ne_NP`` provider. Thanks Sudip Kafle.
* Added provider for Austrian ``de_AT``. Thanks Bernhard Essl.

`0.4.2 - 20-Aug-2014 <http://github.com/joke2k/faker/compare/v0.4.1...v0.4.2>`__
--------------------------------------------------------------------------------

* Fixed setup

`0.4.1 - 20-Aug-2014 <http://github.com/joke2k/faker/compare/v0.4...v0.4.1>`__
------------------------------------------------------------------------------

* Added MAC address provider. Thanks Sébastien Béal.
* Added ``lt_LT`` and ``lv_LV`` localized providers. Thanks Edgar Gavrik.
* Added ``nl_NL`` localized providers. Thanks @LolkeAB, @mdxs.
* Added ``bg_BG`` localized providers. Thanks Bret B.
* Added ``sl_SI``. Thanks to @janezkranjc
* Added distribution feature. Thanks to @fcurella
* Relative date time. Thanks to @soobrosa
* Fixed ``date_time_ad`` on 32bit Linux. Thanks @mdxs.
* Fixed ``domain_word`` to output slugified strings.

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

