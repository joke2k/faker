## Changelog

### [v5.7.0 - 2021-01-25](https://github.com/joke2k/faker/compare/v5.6.5...v5.7.0)

* Add new currency provider ``pricetag()``. Thanks @eumiro.

### [v5.6.5 - 2021-01-20](https://github.com/joke2k/faker/compare/v5.6.4...v5.6.5)

* Update ``th_TH`` Lorem text provider's punctuations, reduce size of word list (#1376). Thanks @bact.

### [v5.6.4 - 2021-01-20](https://github.com/joke2k/faker/compare/v5.6.3...v5.6.4)

* Synchronize ``cs_CZ`` and ``sk_SK`` address provider and split postcodes (#1174). Thanks @eumiro.

### [v5.6.3 - 2021-01-19](https://github.com/joke2k/faker/compare/v5.6.2...v5.6.3)

* Enable parallel coveralls builds (#1382). Thanks @fcurella.

### [v5.6.2 - 2021-01-19](https://github.com/joke2k/faker/compare/v5.6.1...v5.6.2)

* Fix coveralls (#1374). Thanks @joke2k.

### [5.6.1 - 2021-01-15](https://github.com/joke2k/faker/compare/v5.6.0...v5.6.1)

* Fix transliteration for ``ru_RU`` ``person`` provider. Thanks @valestel.

### [5.6.0 - 2021-01-13](https://github.com/joke2k/faker/compare/v5.5.1...v5.6.0)

* Add ``address``, ``bank``, ``geo`` and ``person`` provider for ``en_IE``. Thanks @NiL.
* Add ``person`` provider for ``ga_IE``. Thanks @NiL.

### [5.5.1 - 2021-01-12](https://github.com/joke2k/faker/compare/v5.5.0...v5.5.1)

* Fix lorem provider ``sentence`` method.

### [5.5.0 - 2021-01-11](https://github.com/joke2k/faker/compare/v5.4.1...v5.5.0)

* Add elements caching and other optimizations. Thanks @prescod.
* Add ``use_weighting`` parameter for improved performance. Thanks @prescod.
 
### [5.4.1 - 2021-01-11](https://github.com/joke2k/faker/compare/v5.4.0...v5.4.1)

* Remove empty string from  ``ar_AA`` Person Provider.

### [5.4.0 - 2021-01-07](https://github.com/joke2k/faker/compare/v5.3.0...v5.4.0)

* Add ``da_DK`` address provider. Thanks @JoseNavy.

### [5.3.0 - 2020-12-30](https://github.com/joke2k/faker/compare/v5.2.0...v5.3.0)

* ``json`` and ``fixed_width`` now allow for strings to be fixed or pinned to a static value by prepending ``@``. Thanks @johnbrandborg.

### [5.2.0 - 2020-12-30](https://github.com/joke2k/faker/compare/v5.1.0...v5.2.0)

* Add ``en_IN`` address + phone number provider. Thanks @pulkitgupta2k.

### [5.1.0 - 2020-12-28](https://github.com/joke2k/faker/compare/v5.0.1...v5.1.0)

* Add ``en_IN`` person provider. Thanks @pulkitgupta2k.

### [5.0.2 - 2020-12-15](https://github.com/joke2k/faker/compare/v5.0.1...v5.0.2)

* Remove invalid surname in `nl_NL`. Thanks @TheoSinnige.

### [5.0.1 - 2020-12-07](https://github.com/joke2k/faker/compare/v5.0.0...v5.0.1)

* ``th_TH`` ``strftime``: normalize output for unsupported directive on ``musl``-based Linux. Thanks @bact.

### [5.0.0 - 2020-12-03](https://github.com/joke2k/faker/compare/v4.18.0...v5.0.0)

* Drop support for Python 3.5. Thanks @cclaus.
* Add support for Python 3.9. Thanks @cclaus.

### [4.18.0 - 2020-11-30](https://github.com/joke2k/faker/compare/v4.17.1...v4.18.0)

* Add ``date_time`` and ``bank`` providers for ``th_TH``. Thanks @bact.

### [4.17.1 - 2020-11-19](https://github.com/joke2k/faker/compare/v4.17.0...v4.17.1)

* Correct spelling errors in city names for ``de_DE``. Thanks @AnjaGer.
### [4.17.0 - 2020-11-19](https://github.com/joke2k/faker/compare/v4.16.0...v4.17.0)

* Add name pairs to get matched representation in ``ja_JP`` person provider. Thanks @yu-ichiro.

### [4.16.0 - 2020-11-17](https://github.com/joke2k/faker/compare/v4.15.0...v4.16.0)

* Add SSN, company name, address, and license plate providers for ``th_TH``. Thanks @bact.

### [4.15.0 - 2020-11-16](https://github.com/joke2k/faker/compare/v4.14.2...v4.15.0)

* Add postcode format, country names, person prefix weights, and update phone number format for ``th_TH``. Thanks @bact.

### [4.14.2 - 2020-11-04](https://github.com/joke2k/faker/compare/v4.14.1...v4.14.2)

* Fix generation of names ending with spaces. Thanks @edomora97.

### [4.14.1 - 2020-11-04](https://github.com/joke2k/faker/compare/v4.14.0...v4.14.1)

* Add relative frequencies for japanese last names. Thanks @TianyiShi2001.

### [4.14.0 - 2020-10-13](https://github.com/joke2k/faker/compare/v4.13.0...v4.14.0)

* Add Swiss bank provider locales. Thanks @mondeja.

### [4.13.0 - 2020-10-13](https://github.com/joke2k/faker/compare/v4.12.0...v4.13.0)

* Split first names into male and female on ``pt_PT`` provider. Thanks @gplgps.

### [4.12.0 - 2020-10-13](https://github.com/joke2k/faker/compare/v4.11.0...v4.12.0)

* Geo provider added for ``tr_TR`` locale. Thanks @iamnotagentleman.

### [4.11.0 - 2020-10-13](https://github.com/joke2k/faker/compare/v4.10.0...v4.11.0)

* Add ``sk_SK`` Job provider. Thanks @pipozzz.

### [4.10.0 - 2020-10-13](https://github.com/joke2k/faker/compare/v4.9.0...v4.10.0)

* Add ``date_time`` provider for ``pt_PT``. Thanks @gplgps.

### [4.9.0 - 2020-10-08](https://github.com/joke2k/faker/compare/v4.8.0...v4.9.0)

* Add ``.unique()`` for unique values. Thanks @coiax.

### [4.8.0 - 2020-10-08](https://github.com/joke2k/faker/compare/v4.7.0...v4.8.0)

* Add automotive provider for ``tr_TR``. Thanks @molcay.

### [4.7.0 - 2020-10-08](https://github.com/joke2k/faker/compare/v4.6.0...v4.7.0)

* Add province list and add 2 new district to ``ne_NP``. Thanks @iamsauravsharma.


### [4.6.0 - 2020-10-08](https://github.com/joke2k/faker/compare/v4.5.0...v4.6.0)

* Add Currency provider for ``sv_SE``. Thanks @frangiz.

### [4.5.0 - 2020-10-06](https://github.com/joke2k/faker/compare/v4.4.0...v4.5.0)

* Add ``pt_PT`` credit card provider. Thanks @rubenandre.

### [4.4.0 - 2020-10-02](https://github.com/joke2k/faker/compare/v4.3.0...v4.4.0)

* Added Company Provider for ``tr_TR`` locale. Thanks @iamnotagentleman.

### [4.3.0 - 2020-10-02](https://github.com/joke2k/faker/compare/v4.2.0...v4.3.0)

* Add job providers for ``tr_TR``. Thanks @molcay.

### [4.2.0 - 2020-10-02](https://github.com/joke2k/faker/compare/v4.1.8...v4.2.0)

* Implement color provider for ``sk_SK`` locale. Thanks @pipozzz.

### [4.1.8 - 2020-10-02](https://github.com/joke2k/faker/compare/v4.1.7...v4.1.8)

* Fix ``hu_HU`` color provider inheritance. Thanks @n1ngu.

### [4.1.7 - 2020-10-02](https://github.com/joke2k/faker/compare/v4.1.6...v4.1.7)
* Bigger zipcode ranges for VA, TX and MD in ``en_US``. Thanks @Antetokounpo.

### [4.1.6 - 2020-10-01](https://github.com/joke2k/faker/compare/v4.1.5...v4.1.6)
* Add new style ``pt_PT`` automotive plates. Thanks @gplgps.

### [4.1.5 - 2020-10-01](https://github.com/joke2k/faker/compare/v4.1.4...v4.1.5)
* Remove duplicate jobs from the ``pt_PT`` provider (#1282). Thanks @gplgps.

### [4.1.4 - 2020-09-30](https://github.com/joke2k/faker/compare/v4.1.3...v4.1.4)

* Use "Belarus" instead of "Vitryssland" for ``sv_SE``. Thanks @Majsvaffla.
* Added bank provider for ``tr_TR`` locale. Thanks @iamnotagentleman.
* Improve VAT generation for IT provider. Thanks @LordGordonQ.
* Use non-zero number for first digit of Swedish postal codes. Thanks @Majsvaffla.

### [4.1.3 - 2020-09-14](https://github.com/joke2k/faker/compare/v4.1.2...v4.1.3)

* Add ``es_ES`` autonomous communities (Spanish regions). Thanks @mondeja.
* Add JSON and Fixed Width argument group and parser support. Thanks @johnbrandborg.
* Update ``zh_CN`` ssn provider to support gender. Thanks @mapoor.
* Fix typo in ``de_DE`` job provider. Thanks @datadominik.
* ``or_IN`` Odia person's name added. Thanks @soumendrak.
* Remove ``datetime_safe`` shim subclass in favor of native Python ``datetime.datetime``. Thanks @samcrang.

### [4.1.2 - 2020-08-17](https://github.com/joke2k/faker/compare/v4.1.1...v4.1.2)

* Extend Person Provider to support non-binary suffixes and prefixes. Thank you @crd.
* Add ``safe_domain_name`` generator. Thanks @crd.
* Fix max_value/positive ``pyfloat`` interaction. Thanks @coiax.
* Update ``bban_format`` for ``fi_FI`` locale. Thanks @ALMP-SallaH.
* Fix ``person.ja_JP`` kana and roman characters. Thanks @yameholo.
* Add ``json`` and ``fixed_width`` generators. Thank you @johnbrandborg.
* Add SWIFT code provider methods: ``swift``, ``swift8`` and ``swift11``. Thanks @malefice.
* Add ``es_ES`` internet provider. Thanks @mondeja.
* Update ``bban_format`` for ``fr_FR`` locale. Thanks @r3gis3r.
* Update ``fr_FR`` ``job`` provider. Thanks @mondeja.
* Add ``es_ES`` ``barcode`` provider. Thanks @mondeja.
* Add parser argument support. Thanks @johnbrandborg.

### [4.1.1 - 2020-06-15](https://github.com/joke2k/faker/compare/v4.1.0...v4.1.1)

* Add ``date_time`` providers for ``cs_CZ``, ``de_AT``, ``es_ES``, ``it_IT``, ``sk_SK``,
  ``tr_TR``. Thanks @eumiro.
* Add prefix support to BarcodeProvider. Thanks @yu-ichiro.
* Fix company format for ``hy_AM`` provider. Thanks @mdantonio.
* Add .uk email providers and TLDs for ``en_GB``. Thanks @craiga.
* Add ``language_name`` generator. Thanks @ikhomutov and @mondeja.
* Add ``pytimezone`` generator returning ``tzinfo`` objects. Thanks @OJFord.
* Add ``es_ES`` currency provider. Thanks @mondeja.

### [4.1.0 - 2020-05-12](https://github.com/joke2k/faker/compare/v4.0.3...v4.1.0)

* Add ``pytest`` plugin. Thanks @malefice.
* Fix phone numbers for ``es_ES``. Thanks @pablofm.
* Fix ``uuid`` provider to return a ``uuid4`` object when ``cast_to`` is set to ``None``. Thanks @rodrigondec.
* Update names for ``es_ES`` person provider. Thanks @mondeja.
* Add provider for ``sk_SK`` ``birth_number``. Thanks @eumiro.
* Add ``day_of_week`` and ``month_name`` for ``de_DE`` provider. Thanks @eumiro.

### [4.0.3 - 2020-04-13](https://github.com/joke2k/faker/compare/v4.0.2...v4.0.3)

* Fixed ``MSISDN`` for ``pt_BR``  to return only mobile numbers. Thanks @rodrigondec.
* Added Domain Generator Algorithm by date. Thanks @pishchalnikov.
* Fixed issue where ``pydict`` provider was not returning the correct number of elements. Thanks @mstellon.
* Added support for Indian Aadhaar numbers. Thanks @curiousElf.
* Added ``company_vat`` for ``it_IT``. Thanks @alitaker.
* Improved autodocumentation of providers. Thanks @malefice.
* Added provider for ``es_ES`` license plates. Thanks @mondeja.
* Implemented ``__dir__`` method to Faker proxy for better autocompletion. Thanks @douglasfarinelli.
* Uppercased HEX colors for all localized color providers. Thanks @mondeja.
* Added bank provider for ``es_ES`` locale. Thanks @mondeja.
* Added support for UK counties. Thanks @neilav.
* Added color provider for ``no_NO`` license plates. Thanks @bjorskog.
* Made ``value_types`` a keyword argument in ``python`` provider. Thanks @slafs.

### [4.0.2 - 2020-03-11](https://github.com/joke2k/faker/compare/v4.0.1...v4.0.2)

* Add more data for ``ko_KR`` address provider. Thanks @alstn2468.
* Improved ``pt_PT`` locale for address and bank. Thanks @mustakarhu.
* Add ``port_number`` method to internet provider. Thanks @pishchalnikov.
* Add color provider for ``fa_IR`` locale. Thanks @abtinmo.
* Add formatting options for ``pt_BR`` postcodes. Thanks @perssonsimon1 and @klaraesr.
* Add ``country_calling_code`` to ``phone_number`` provider. Thanks @perssonsimon1.
* Fix leap year issue. Thanks @mmcmahon.
* Add ``AutomotiveProvider`` for ``fr_FR`` locale. Thanks @clarissedescamps and @perssonsimon1.
* Fix ``cellphone_formats`` in ``pt_BR`` ``PhoneNumberProvider``. Thanks @rodrigondec.

### [4.0.1 - 2020-02-17](https://github.com/joke2k/faker/compare/v4.0.0...v4.0.1)

* Provider improvements for Russian locale:
    * added city suffixes, regions and country list
    * regions converted into states for now
    * street address formats and states expanded
    * lists for street titles changed
    * Fixed errors in Automotive Provider
    * Fixed errors in Address Provider
    * Bank Provider expanded:
        * BIC added)
        * Added list of banks
    * Improved Company Provider
    * Credit Card and Person Provider improvements
    * Currency Provider improvements
    * Date-Time Provider improvements
    * translit fix

  Thanks @valestel.
* Add Birth Number to czech locale. Thanks @Jengah.
* Add persons provider for ``fr_QC``. Thanks @Lionesk.

### [4.0.0 - 2020-01-14](https://github.com/joke2k/faker/compare/v3.0.1...v4.0.0)

* Breaking change: Remove support for end-of-life Python 2.7.

### [3.0.1 - 2020-01-14](https://github.com/joke2k/faker/compare/v3.0.0...v3.0.1)

**NOTE**: This is the last release to support Python 2.7.x.

* Add provider methods ``zip`` and ``tar`` for generating zip and tar files.
  Thanks @malefice.
* Add ``en-CA`` ``postcode_in_province()`` method. Thanks @oeuftete.
* Update Address and Automotive provider for Russian locale. Thanks @valestel.
* Add provider methods for dsv files: ``csv``, ``tsv``, ``psv`` and generic
  ``dsv``. Thanks @malefice.
* Remove parenthesis from city name in ``de_DE`` ``address`` provider. Thanks
  @jerr0328.
* Add ``NIP`` generator in ``pl_PL``. Thanks @IlfirinPL.
* Fix ``Faker.random_number`` intermittent exceptions. Thanks @Jengah.


### [3.0.0 - 2019-12-04](https://github.com/joke2k/faker/compare/v2.0.5...v3.0.0)

* Breaking change: Add support for multiple locale data generation.
  Thanks @malefice.

### [2.0.5 - 2019-12-03](https://github.com/joke2k/faker/compare/v2.0.4...v2.0.5)

* Add Iranian credit card. Thanks @abtinmo.
* Improve color provider. Thanks @malefice.
* Add counties (concelhos) for locale ``pt_PT``. Thanks @tng10.
* Change NY zipcode range. Thanks @arielkaluzhny.
* Fix pyfloat out of min/max range. Thanks @bryan-brancotte.

### [2.0.4 - 2019-11-12](https://github.com/joke2k/faker/compare/v2.0.3...v2.0.4)

* Drop python 3.4.
* Fix master card number generator. Thanks @nkthanh98.
* Add provider for Finnish IBAN numbers. Thanks @sitomani.
* Add color in Thai language. Thanks @mesodiar.
* Split first names into male/female for ``person/de_AT``. Thanks @Jayday.
* Extend data for ``de_AT`` and ``it_IT`` person providers. Thanks @Jayday.
* Add ``ta_IN`` support. Thanks @jcopps.
* Add ``*_PH`` locales. Thanks @malefice.
* Add Thai lorem. Thanks @mesodiar.
* Add job in ``ja_JP``. Thanks @shmokmt.
* Optimize IPv4 address generation. Thanks @malefice.
* Increase bban_format length for ``en_GB``. Thanks @Necrathex.
* Fix occasional errors in ISBN provider. Thanks @malefice.
* Add more phone numbers to ``fa_IR`` locale. Thanks @abtinmo.
* Add support for token-based string generation. Thanks @malefice.
* Improve barcode provider. Thanks @malefice.
* Fix for pyfloat empty randrange. Thanks @jcardali.

### [2.0.3 - 2019-10-14](https://github.com/joke2k/faker/compare/v2.0.2...v2.0.3)

* Use the provider's RNG instead of the random module in ``invalid_ssn``. Thanks @luser.
* Fix ``randomize_nb_elements`` ``max`` argument. Thanks @jorrit-wehelp.
* Add ``de_DE`` jobs. Thanks @CodeAndChoke.
* Add ``pt_PT`` automotive plates. Thanks @rubenandre.
* Add ``el_GR`` jobs. Thanks @athaks.
* Add police id for ``el_GR``. Thanks @athaks.
* Add jobs for for ``pt_PT``. Thanks @rubenandre.

### [2.0.2 - 2019-09-17](https://github.com/joke2k/faker/compare/v2.0.1...v2.0.2)

* Fix typos, misspellings. Add locations, names, dates in ``hi_IN`` providers. Thanks @kathawala.
* Bump required version ``text-unidecode`` to 1.3. Thanks @moggers87.
* Bug fix for ``pyfloat`` going over ``max_value``. Thanks @fgs-dbudwin.

### [2.0.1 - 2019-08-20](https://github.com/joke2k/faker/compare/v2.0.0...v2.0.1)

* Add nationalities for locale ``pt_PT``. Thanks @tng10.
* Add ``ios()`` and ``android()`` to ``user_agent`` provider. Thanks @gsilvan.
* Update ``zh_CN`` provinces. Thanks @casen27.

### [2.0.0 - 2019-07-15](https://github.com/joke2k/faker/compare/v1.0.8...v2.0.0)
* Breaking change: Only allow providers to use ``OrderedDict`` s, to avoid any more ``PYTHONHASHSEED`` problems. Thanks @adamchainz.

### [1.0.8 - 2019-06-15](https://github.com/joke2k/faker/compare/v1.0.7...v1.0.8)

* Rename ``pyint`` ``min`` and ``max`` to ``min_value`` and ``max_value``.
  Thanks @francoisfreitag.
* Remove some validations from Faker and delegate it to an external library,
  ``validators``. Thanks @kingbuzzman.
* Add an "Invalid SSN" generator to the ``en_US`` SSN Provider.
  Thanks @darrylwhiting.
* Include "Praia" as street_prefix in ``pr_BR`` address Provider.
  Thanks @G5Olivieri.
* Loosen version restrictions on ``freezegun`` and ``random2``.
  Thanks @timokau.
* Add SSN provider for ``es_MX``. Thanks @mrfunnyshoes.
* Add ``pwz`` generator for ``pl_PL``. Thanks @torm89.
* Add ``date_of_birth`` and ``sex`` argument to ``pesel`` Provider (`pl_PL`).
  Thanks @torm89.
* Fix datetime parsing on environments with negative offsets.
  Thanks @bluesheeptoken.

### [1.0.7 - 2019-05-14](https://github.com/joke2k/faker/compare/v1.0.6...v1.0.7)

* Remove dead url from ``image_placeholder_services``. Thanks @Monstrofil.
* Fix missing ``first_names`` in Romanian person provider. Thanks @xlotlu.
* Add Catalan, adds doi/nie/nif/cif to Spain ssn. Thanks @kingbuzzman.
* Add ``texts`` to generate list of texts. Thanks @pishchalnikov.
* Add provider for ``pl_PL`` automotive and Polish pesel number.
  Thanks @adwojak.
* Corrected behavior for ``pyfloat``. Thanks @ariksu.

### [1.0.6 - 2019-04-26](https://github.com/joke2k/faker/compare/v1.0.5...v1.0.6)

* Add missing commas to company/nl_NL provider. Thanks @francoisfreitag.
* Add bounds to ``pyint``. Thanks @francoisfreitag.
* Accept step argument in ``random_int()``. Thanks @francoisfreitag.

### [1.0.5 - 2019-04-12](https://github.com/joke2k/faker/compare/v1.0.4...v1.0.5)

* Add min and max values for ``pyfloat`` and ``pydecimal``. Thanks @Lrcezimbra.
* Add ``months`` and ``M`` to the syntax for ``start_date`` and ``end_date``.
  Thanks @anneclairebrld.
* Add support for ``PyInstaller``. Thanks @arossert.
* Add Dutch company names. Thanks @MathynS.
* Fix some invalid French phone numbers starting with ``+33 8x``.
  Thanks @stephane.
* Add Armenian locale ``hy_AM``. Thanks @hovikman.

`1.0.4 - 12-March-2019 <https://github.com/joke2k/faker/compare/v1.0.3...v1.0.4>`_

* Fix erratic test.

### [1.0.3 - 2019-03-12](https://github.com/joke2k/faker/compare/v1.0.2...v1.0.3)

* Fix ``AttributeError`` in ``user_Agent`` provider. Thanks @Mattwmaster58 for
  the report.
* Update ``zh_TW`` ``person`` provider. Thanks @TimeFinger.
* Add street data & remove ``street_prefixes`` from ``id_ID`` address provider.
  Thanks @codenoid.
* Fix parsing of timedeltas in ``date_time`` provider. Thanks @riconnon for
  the report.
* Split name formats into ``formats_male`` and ``formats_female`` for ``de_DE``
  provider. Thanks @petro-zdebskyi.
* Pin ``more-itertools`` to a version compatible with Python 2.7.
  Thanks @canarduck.
* Fix ``fr_FR`` ``postcodes_format``. Thanks @canarduck.
* Fix hex code for ``yellowgreen`` color. Thanks @hovikman.
* Add Brazilian RG (identity card). Thanks @davizucon.
* Allow overriding of random generator class.

### [1.0.2 - 2019-01-22](https://github.com/joke2k/faker/compare/v1.0.1...v1.0.2)

* Fix state abbreviations for ``id_ID`` to be 2-letters. Thanks @dt-ap.
* Fix format for ``city_with_postcode`` on ``de_DE`` locale. Thanks @TZanke.
* Update ``person`` providers for ``zh_CN``. Thanks @TimeFinger.
* Implement ``zipcode_in_state`` and aliases in ``en_US`` locale for generating
  a zipcode for a specified state. Thanks @mattyg.
* Group first names by gender on ``zh_CN`` provider. Thanks @TimeFinger.

### [1.0.1 - 2018-12-12](https://github.com/joke2k/faker/compare/v1.0.0...v1.0.1)

* Fix number of digits in ``phone_number`` provider for ``no_NO``.
  Thanks @aleksanb.
* Add categories to ``jp_JP`` company provider. Thanks @shirakia.
* Add trunk prefix for ``ru_RU`` phone numbers. thanks @pishchalnikov.

### [1.0.0 - 2018-11-13](https://github.com/joke2k/faker/compare/v0.9.3...v1.0.0)

* Breaking change: ``latlng``, ``latitude`` and ``longitude`` no longer return
  coordinates that are close the locale's country. Use the ``local_latlng``,
  ``local_latitude`` and ``local_longitude`` instead.
* Add ``location_on_land`` provider. Thanks @shacker.

### [0.9.3 - 2018-11-13](https://github.com/joke2k/faker/compare/v0.9.2...v0.9.3)

* Add ``cellphone_number`` method for ``pt_BR``. Thanks @Newman101.
* Fix urls generated by from `image_url`. Thanks @tsiaGeorge.
* Add job provider for ``th_TH``. Thanks @mesodiar.
* Add phone number provider for ``th_TH``. Thanks @zkan.
* Add bank provider for ``pl_PL`` locale. Thanks @andrzej3393.
* Add lorem provider for ``pl_PL`` locale. Thanks @andrzej3393.
* Add Postcode and City format for ``de_DE`` provider. Thanks @Newman101.
* Add ``vat_id`` to ``ssn`` providers for ``bg_BG``, ``cs_CZ``, ``de_AT``,
  ``de_CH``, ``de_de``, ``dk_DK``, ``el_CY``, ``el_GR``, ``en_GB``, ``en_IE``,
  ``es_ES``, ``et_EE``, ``fi_FI``, ``fr_CH``, ``fr_FR``, ``hr_HR``, ``hu_HU``,
  ``it_IT``, ``lb_LU``, ``lt_LT``, ``lv_LV``, ``mt_MT``, ``nl_BE``, ``nl_NL``,
  ``no_NO``, ``pl_PL``, ``pt_PT``, ``ro_RO``, ``sk_SK``, ``sl_SI`` and
  ``sv_SE``. Thanks @mastacheata.
* Add ``postcode`` and ``city_with_postcode`` for ``cs_CZ``. Thanks @Newman101.
* Add ``postcode`` and ``city_with_postcode`` for ``de_AT``. Thanks @Newman101.
* Add ``license_plate`` for ``ru_RU``. Thanks @codaver.
* Remove incorrect phone number formats from ``en_US``. Thanks @stephenross.
* Add job provider for ``bs_BA``. Thanks @elahmo.
* Add ``hostname`` provider. Thanks @ediblesushi.
* Add license plates for ``sv_SE``. Thanks @vilhelmmelkstam.
* Allow ``uuid4`` to return a ``UUID`` object. Thanks @ediblesushi.

### [0.9.2 - 2018-10-12](https://github.com/joke2k/faker/compare/v0.9.1...v0.9.2)

* Add company names to ``pl_PL`` provider. Thanks @@twkrol.
* Add replacements for non-ascii characters in ``pt_BR``. Thanks @clarmso.
* Add some more placeholder image services. Thanks @clarmso.
* Separate male name and female name formats in ``cs_CZ`` provider.
  Thanks @clarmso.
* Add second level domains (mostly provinces) for ``cn`` top level domain.
  Thanks @clarmso.
* Add ``fr_FR`` localization to ``lorem`` provider. Thanks @tristandeborde.
* Lots of work on internal cleanup and optimizing the CI. Thanks @jdufresne.
* Add ``flake8`` to the CI. Thanks @andrzej3393.

### [0.9.1 - 2018-09-13](https://github.com/joke2k/faker/compare/v0.9.0...v0.9.1)

* Fix missing and misplaced comma's in many providers. Thanks @153957.
* Refactor IPv4 address generation to leverage ``ipaddress`` module.
  Thanks @maticomp.
* An ``en_NZ`` provider for addresses, phone numbers and email addresses.
  Thanks @doctorlard.
* Add ``unique`` argument to ``words()`` for returning unique words.
  Thanks @micahstrube.
* Allow US territories to be excluded from ``state_abbr()`` for ``en_US``
  provider. Thanks @micahstrube.
* Add support for Python 3.7. Thanks @michael-k.

### [0.9.0 - 2018-08-13](https://github.com/joke2k/faker/compare/v0.8.18...v0.9.0)
-
* ``.random_sample()`` now returns a list of unique elements instead of a set.
* ``.random_sample_unique()`` is removed in favor of ``.random_sample()``.
* Added ``random_choices()``, ``random_elements()`` and ``random_letters()``.
* Added ``faker.utils.distribution.choices_distribution_unique()``.
* ``words()``, ``password()``, ``uri_path`` and ``pystr()`` now use the new the
  ``random_choices()`` method.

### [0.8.18 - 2018-08-13](https://github.com/joke2k/faker/compare/v0.8.17...v0.8.18)

* Change blood group from ``0`` (zero) to ``O`` (capital letter O). Some
  locales do use 'zero', but ``O`` is more common and it is the medical
  standard. Thanks @mohi7solanki.
* Fix alpha-2 country code for Haiti. Thanks @sevens-ef for the report.
* Fix abbreviation for Nunavut. Thanks @straz for the report.
* Standardized ``postcode`` in address providers. Now all locales are
  guaranteed to have a ``postcode`` method and may have a localized alias for
  it (eg: ``zipcode``). Thanks @straz for the report.
* Fix typo in ``pt_BR`` Person perovider. Thanks @Nichlas.
* Fix timezone handling. Thanks @Fraterius.
* Use tzinfo when provided in ``date_of_birth``. Thanks @Kelledin.


### [0.8.17 - 2018-07-12](https://github.com/joke2k/faker/compare/v0.8.16...v0.8.17)

* Add ``ein``, ``itin`` and refactored ``ssn`` Provider for ``en_US``.
  Thanks @crd.
* Add ``job`` provider for ``zh_CN``. Thanks @ramwin.
* Add ``date_of_birth`` provider. Thanks @cdr.
* Add alpha-3 representation option for ``country-code`` provider. Thanks @cdr.

### [0.8.16 - 2018-06-15](https://github.com/joke2k/faker/compare/v0.8.15...v0.8.16)

* Fix test for CPF (Brazilian SSN). Thanks Rubens Takiguti Ribeiro.
* Fix Canadian SIN generation. Thanks @crd.
* Fix Norwegian SSN date portion. Thanks @frangiz.
* Add ``start_datetime`` argument for ``unix_time()``. Thanks @crd.

### [0.8.15 - 2018-05-14](https://github.com/joke2k/faker/compare/v0.8.14...v0.8.15)

* Change logging level to ``DEBUG``.

### [0.8.14 - 2018-05-11](https://github.com/joke2k/faker/compare/v0.8.13...v0.8.14)

* Add possibility to make artificial ssn numbers for ``FI_fi``. Thanks @kivipe.
* Update ``ko_KR`` person data based on statistics. Thanks @unace.
* Improved logging. Thanks @confirmationbias616.


### [0.8.13 - 2018-04-12](https://github.com/joke2k/faker/compare/v0.8.12...v0.8.13)

* Add ``no_NO`` bank provider. Thanks @cloveras.
* Add ``ipv4_network_class``, ``ipv4_private``, ``ipv4_public`` providers.
  Thanks @ZuluPro.
* Add ``address_class`` and ``private`` arguments to ``ipv4`` provider.
  Thanks @ZuluPro.
* Add ``currency``, ``currency_name``, ``cryptocurrency``,
  ``cryptocurrency_code`` and ``cryptocurrency_name`` to currency provider.
  Thanks @ZuluPro.
* Add automotive provider for ``de_DE``. Thanks @gsilvan.
* Fix edgecases for Finnish ``ssn`` provider. Thanks @sanga.
* Add job provider for ``pt_BR``. Thanks @paladini.
* Add ``unix_device`` and ``unix_partition`` to ``file`` provider.
  Thanks @ZuluPro.
* Add ``random_lowercase_letter`` and ``random_uppercase_letter`` to the base
  provider. Thanks @ZuluPro.
* Clarify CLI help. Thanks @confirmationbias616.


### [0.8.12 - 2018-03-12](https://github.com/joke2k/faker/compare/v0.8.11...v0.8.12)

* Fix issue with ``cx_Freeze``. Thanks @sedominik.
* Add dutch ``nl_NL`` bank provider. Thanks @PatSousa.
* Add ``distrito`` and ``freguesia`` to ``pt_PT`` ``address`` provider.
  Thanks @ZuluPro.
* Fix  unicode issues with the ``person`` provider. Thanks @karthikarul20.
* Add ``en_SG`` ``person`` provider. Thanks @karthikarul20.
* Add street names to the Ukrainian address provider. Thanks @cadmi.
* Add ``de_AT`` address provider. Thanks @bessl.
* Fix credit card prefixes. Thanks @jphalip.
* Fix capitalization in ``no_NO`` address provider. Thanks @cloveras.
* Fix deprecated syntax for raw strings. Thanks @dchudz.
* Add ``latitude`` and ``longitude`` to ``de_AT`` ``address`` provider.
  Thanks @bessl.
* Fix incorrect value in list of middle name for locale ``ru_RU``.
  Thanks @damirazo.

### [0.8.11 - 2018-02-12](https://github.com/joke2k/faker/compare/v0.8.10...v0.8.11)

* Add scheme selection for internet ``url`` provider. Thanks @ProvoK.
* Increase lower bound on AD date generation. Thanks @prophile.
* Add the ability to specify the min and max age for some ssn locales.
  Thanks @frangiz.

### [0.8.10 - 2018-01-16](https://github.com/joke2k/faker/compare/v0.8.9...v0.8.10)
--
* Pass ``python_requires`` argument to ``setuptools``. Thanks @jdufresne.
* Remove some words from ``en_US`` lorem ipsum provider. Thanks @Pomax.

### [0.8.9 - 2018-01-12](https://github.com/joke2k/faker/compare/v0.8.8...v0.8.9)

* Remove support for Python 3.3. Thanks @jdufresne.
* Allow past dates within a second. Thanks @DanEEstar.
* Added phone number formatting to ``en_GB`` localisation to ensure no genuine
  phone numbers are generated. Thanks @TheSapper.
* Added ``en_GB`` localisation for SSN (UK National Insurance Number).
  Thanks @TheSapper.
* Added ``ro_RO`` person Provider. Thanks @vasilesmartup.
* Added ``domain`` argument to ``email`` provider. Thanks @lcd1232.


### [0.8.8 - 2017-12-19](https://github.com/joke2k/faker/compare/v0.8.7...v0.8.8)

* made ``seed_instance`` return ``self`` for chainability.
* Add ``en_US`` locale for ``lorem``. Thanks @shacker.
* ``fi_FI`` gender specific data added. Thanks @mikkhola.
* ``fi_FI`` address and job lists updated. Thanks @mikkhola.
* Add ``iban`` provider. Thanks @cdaller.

### [0.8.7 - 2017-11-14](https://github.com/joke2k/faker/compare/v0.8.6...v0.8.7)

* Corrected some issues with the Hungarian (``hu_HU``) providers, such as
  incorrectly capitalized company suffixes, street/road type names and place
  names. Thanks @chrisvoncsefalvay.
* The Hungarian locale's ``providers.job.job`` provider now returns Hungarian
  job names, taken from the Hungarian National Statistical Office (KSH)'s 2008
  survey nomenclature of employment (FEOR '08). Thanks @chrisvoncsefalvay.
* Added ``he_IL`` locale. Thanks @bjesus.
* Fix possible infinite loop in ``random_sample_unique``. Thanks @153957.
* Add aliases to make ``pt_BR`` address provider compatible ``with en_US``.
  Thanks @diegoholiveira.
* Fix ResourceWarning in ``setup.py``. Thanks @jdufresne.
* Update test requirements.

### [0.8.6 - 2017-10-16](https://github.com/joke2k/faker/compare/v0.8.5...v0.8.6)

* Replace ``unidecode`` dependency in favor of ``text-unidecode``. Faker now
  requires [text-unidecode](https://pypi.org/project/text-unidecode/).

### [0.8.5 - 2017-10-13](https://github.com/joke2k/faker/compare/v0.8.4...v0.8.5)

* Add ASCII emails. Thanks @barseghyanartur.
* Add ``id_ID`` Providers. Thanks Sidi Ahmad.
* Fix ``date_time.time_series()`` to ensure start and end bounds are inclusive.
  Thanks @bijanvakili.
* Create a provider to Brazilian license plates. Thanks @diegoholiveira.
* Use a proper international format for Ukrainian phone numbers.
  Thanks @illia-v.
* Faker now requires [Unidecode](https://pypi.org/project/Unidecode/).

### [0.8.4 - 2017-09-22](https://github.com/joke2k/faker/compare/v0.8.3...v0.8.4)

* Move ``email_validator`` to ``test_requires`` and unpinned the
  version number.
* Date feature parity with datetime. Thanks @noirbizarre.
* Add ``MSISDN`` in the ``phone_number`` provider. Thanks @patrickporto.
* Add Arabic locales. Thanks @ahmedaljazzar.
* Fix datetime issue on Windows. Thanks @kungfu71186.

### [0.8.3 - 2017-09-05](https://github.com/joke2k/faker/compare/v0.8.2...v0.8.3)

* Fix release build.

### [0.8.2 - 2017-09-05](https://github.com/joke2k/faker/compare/v0.8.1...v0.8.2)

* Revert name change of ``faker.generator.random``. Thanks @adamchainz.
* Document the global shared ``random.Random`` and ``seed_instance()``.
  Thanks @adamchainz.

### [0.8.1 - 2017-08-28](https://github.com/joke2k/faker/compare/v0.8.0...v0.8.1)

* Rolled back breaking change in ``randomize_nb_elements``.

### [0.8.0 - 2017-08-28](https://github.com/joke2k/faker/compare/v0.7.18...v0.8.0)

* Add ``identity_card_number`` for ``pl_PL`` ``person`` provider. Thanks @pdaw.
* More descriptive error message when a formatter is not found.
  Thanks @fcurella.
* Add ``time_series`` provider. Thanks @fcurella.
* Add per-instance seeding via ``.seed_instance`` method. Thanks @reverbc.
* Fix ``tz_TW`` ``address`` provider. Thanks @clarmso.

### [0.7.18 - 2017-07-19](https://github.com/joke2k/faker/compare/v0.7.17...v0.7.18)

* Generate proper dates before 1970. Thanks @kungfu71186.
* Made it possible to seed ``.binary()``. Thanks @kungfu71186.
* Add color names for ``hr_HR``. Thanks @mislavcimpersak.
* Add implementation of ``ssn`` provider for the ``pl_PL`` locale.
  Thanks @pdaw.
* Add ``pt_BR`` colors localization. Thanks @ppcmiranda.
* Create a method for codes of cryptocurrencies in the currency provider.
  Thanks @illia-v.
* Fix female name format typo in ``hu_HU`` person provider. Thanks @swilcox.
* Fix deprecated usage of ``print`` statement in README. Thanks @cclauss.
* Add gender-specific names for ``sv_SE`` person provider. Thanks @swilcox.
* Add an implementation of `regon` for ``pl_PL`` company provider.
  Thanks @pdaw.
* Addi an implementation of ``local_regon`` for ``pl_PL`` company provider.
  Thanks @pdaw.
* Replace deprecated ``getargspec`` on py3. Thanks @fcurella.
* Add new ``automotive`` provider. Thanks @zafarali.
* Add an implementation of ``company_vat`` for ``pl_PL`` company provider.
  Thanks @pdaw.
* Add Taiwan/Traditional character support for internet and lorem providers.
  Thanks @bearnun.
* Use ``random.choices`` when available for better performance.
  Thanks @catleeball.
* Refactor RGB color methods. Thanks @catleeball.

### [0.7.17 - 2017-06-12](https://github.com/joke2k/faker/compare/v0.7.16...v0.7.17)

* Fix a timezone issue with the ``date_time_between_dates`` provider.

### [0.7.16 - 2017-06-09](https://github.com/joke2k/faker/compare/v0.7.15...v0.7.16)

* fix timezone issues with ``date_time_between`` provider.
* Add ``ext_word_list`` parameter to methods in the ``Lorem`` generator.
  Thanks @guinslym.

### [0.7.15 - 2017-06-02](https://github.com/joke2k/faker/compare/v0.7.14...v0.7.15)

* fix start and end date for datetime provider methods.

### [0.7.14 - 2017-06-02](https://github.com/joke2k/faker/compare/v0.7.13...v0.7.14)

* fix ``future_date``, `and ``past_date`` bounds.

### [0.7.13 - 2017-06-02](https://github.com/joke2k/faker/compare/v0.7.12...v0.7.13)

* Remove capitalisation from ``hu_HU`` addresses. Thanks @Newman101.
* Add ``et_EE`` (Estonian) provider: names and ssn. Thanks @trtd.
* Proper prefix for gender in ``pl_PL`` names. Thanks @zgoda.
* Add DateTime provider for ``pl_PL``. Thanks @zgoda.
* Add ``pl_PL`` internet data provider. Thanks @zgoda.
* Fix diacritics in ``pl_PL`` street names. Thanks @zgoda.
* Add ``future_date``, ``future_datetime``, ``past_date`` and ``past_datetime``
  to DateTime Provider


### [0.7.12 - 2017-05-10](https://github.com/joke2k/faker/compare/v0.7.11...v0.7.12)

* Add Japanese lorem provider. Thanks @richmondwang.
* Add ``hr_HR`` names of month and names of days. Thanks @mislavcimpersak.
* Add ``sl_SI`` names of month and names of days. Thanks @mislavcimpersak.
* Update the provider ``user_agent``. Thanks @illia-v.
* Add russian words for date_time. Thanks @iskhomutov.
* Add Georgian (``ka_GE``) person and address providers.
  Thanks @GeorgeLubaretsi.
* Add company provider to hu_HU locale. Thanks @Newman101.
* Allow subdomains for ``domain_name`` provider. Thanks @hiagofigueiro.
* Implement hu_HU months + days. Thanks @Newman101.
* Replacement rules for emails à->a, è->e in ``de_DE`` internet provider.
  Thanks @Bergil32.


### [0.7.11 - 2017-04-09](https://github.com/joke2k/faker/compare/v0.7.10...v0.7.11)
-
* Added french words for days and months. Thanks @sblondon.
* Reorganized tests. Thanks @grantbachman.
* Added file path provider. Thanks @diegommarino.
* Fixed packaging issue with tests module. Thanks @eukreign for the report.

### [0.7.10 - 2017-03-13](https://github.com/joke2k/faker/compare/v0.7.9...v0.7.10)
--
* Add ISBN-10 and ISBN-13. Thanks @grantbachman.
* Add colors for ``fr_FR``. Thanks @sblondon.

### [0.7.9 - 2017-02-24](https://github.com/joke2k/faker/compare/v0.7.8...v0.7.9)

* Fix packaging issue. Thanks @jorti.

### [0.7.8 - 2017-02-24](https://github.com/joke2k/faker/compare/v0.7.7...v0.7.8)

* Add a Russian language to color provider. Thanks @kotyara1005.
* Correct UnboundLocalError in Finnish SSN generator. Thanks @lamby.
* Create internet IT provider. Thanks @GlassGruber.
* Add ``fix_len`` parameter to ``random_number``. Thanks @vlad-ki.
* Support zh_CN lorem. Thanks @yihuang.
* Customize chinese word connector. Thanks @yihuang.
* Add more company data to ``fa_IR``. Thanks @aminalaee.
* Python 3.6 support. Thanks @stephane.
* Add ``hu_HU`` providers. Thanks @chrisvoncsefalvay.
* Fix tests failures.

### [0.7.7 - 2016-12-20](https://github.com/joke2k/faker/compare/v0.7.6...v0.7.7)

* Fix ``no_NO`` postcodes. Thanks @kdeldycke.
* Fix ``fa_IR`` city generator. Thanks @kdeldycke.

### [0.7.6 - 2016-12-19](https://github.com/joke2k/faker/compare/v0.7.5...v0.7.6)
-
* Fix packaging issue with ``docs`` directory. Thanks @wyattanderson.

### [0.7.5 - 2016-12-16](https://github.com/joke2k/faker/compare/v0.7.4...v0.7.5)

* Deprecate ``fake-factory`` package on PyPI.

### [0.7.4 - 2016-12-16](https://github.com/joke2k/faker/compare/v0.7.3...v0.7.4)
-
* Add Ukrainian ``address`` provider. Thanks @illia-v.
* Add Ukrainian ``internet`` provider. Thanks @illia-v.
* Middle name support for ``person.ru_RU`` provider. Thanks @zeal18.
* Add ``address``, ``company``, ``internet`` ans ``SSN`` provider for
  ``ru_RU``. Thanks @zeal18.
* Improved ``address.pl_PL`` provider. Thanks @pkisztelinski.
* Add date and time object providers. Thanks @jtojnar.
* Refactor Korean address methods. Thanks @item4.
* Add provider for locale `nl_BE` (address, phone, ssn). Thanks @vema.
* Add additional job titles. Thanks @wontonst.
* Add Ukrainian color provider. Thanks @illia-v.
* Add support to brazilian company IDs (CNPJ). Thanks @lamenezes.
* Improve the Internet provider. Thanks@illia-v.
* Improve the Ukrainian person provider. Thanks @illia-v.
* Improve some SSN providers. Thanks @illia-v.
* Improve code samples in `README.rst` and `docs/index.rst`. Thanks @illia-v.
* Improve the method `locale`. Thanks @illia-v.
* Fix `pyfloat`. Thanks @illia-v.
* Allow left/right_digits=0 for pyfloat. Thanks @mnalt.
* update fa_IR person names and phone numbers. Thanks @aminalaee.

### [0.7.3 - 2016-09-16](https://github.com/joke2k/faker/compare/v0.6.0...v0.7.3)

* ``date_time_this_century`` now returns ``datetime`` s outside the current
  decade. Thanks @JarUrb.
* Add support for localized jobs for ``hr_HR``. Thanks @mislavcimpersak.
* Adding support for Croatian ``hr_HR`` ssn (oib). Thanks @mislavcimpersak.
* Rename PyPI package to ``Faker``.

### [0.6.0 - 2016-08-09](https://github.com/joke2k/faker/compare/v0.5.11...v0.6.0)
-
* Dropped Python 2.6 support


### [0.5.11 - 2016-08-09](https://github.com/joke2k/faker/compare/v0.5.10...v0.5.11)

* Add optional parameter `sex` to `profile` and `simple_profile`.
  Thanks @navyad.
* Fix whitespace in dk_DK provider last_names/last_name. Thanks @iAndriy.
* Fix utf8 coding issue with ``address/fi_FI`` provider. Thanks @delneg.
* ! Latest version to support Python 2.6

### [0.5.10 - 2016-08-01](https://github.com/joke2k/faker/compare/v0.5.9...v0.5.10)

* Fix random_sample_unique. Thanks @cecedille1.

### [0.5.9 - 2016-06-08](https://github.com/joke2k/faker/compare/v0.5.8...v0.5.9)

* Add more ``pt_BR`` names. Thanks @cuducos.
* Added ``en_GB`` names. Thanks @jonny5532.
* Add romanized internet provider for ``zh_CN``.
* Add ``fr_CH`` providers. Thanks @gfavre.

### [0.5.8 - 2016-06-28](https://github.com/joke2k/faker/compare/v0.5.7...v0.5.8)

* Improve CLI output and help. Thanks @cbaines.
* Update ``en_US`` anmes to be more realistic. Thanks @dethpickle.
* Modify pystr provider to accept a minimum number of characters.
  Thanks @tamarbuta.
* Add `job` Provider for ``zh_TW``. Thanks @weihanglo.
* Modify ``zh_TW`` phone number for a more valid format. Thanks @weihanglo.
* Reduce the maximum value of start timestamps. Thanks @cbaines.
* Add `random_sample` and `random_sample_unique`. Thanks @bengolder.

### [0.5.7 - 2016-03-07](https://github.com/joke2k/faker/compare/v0.5.6...v0.5.7)

* Repackage to resolve PyPI issue.

### [0.5.6 - 2016-03-07](https://github.com/joke2k/faker/compare/v0.5.5...v0.5.6)

* Add date handling for datetime functions. Thanks @rpkilby.
* Discern male and female first names in pt_BR. Thanks @gabrielusvicente.

### [0.5.5 - 2016-02-29](https://github.com/joke2k/faker/compare/v0.5.4...v0.5.5)

* Specify help text for command line. Thanks @cbaines.

### [0.5.4 - 2016-02-29](https://github.com/joke2k/faker/compare/v0.5.3...v0.5.4)

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
* Differentiate male and female first names in ``fr_FR`` locale.
  Thanks @GregoryVds
* Add Maestro credit card. Thanks @anthonylauzon.
* Add ``hr_HR`` localization. Thanks @mislavcimpersak.
* Update ``de_DE`` first names. Thanks @WarrenFaith and @mschoebel.
* Allow generation of IPv4 and IPv6 network address with valid CIDR.
  Thanks @kdeldycke.
* Unittest IPv4 and IPv6 address and network generation. Thanks @kdeldycke.
* Add a new provider to generate random binary blob. Thanks @kdeldycke.
* Check that randomly produced language codes are parseable as locale by the
  factory constructor. Thanks @kdeldycke.
* Fix chinese random language code. Thanks @kdeldycke.
* Remove duplicate words from Lorem provider. Thanks @jeffwidman.

### [0.5.3 - 2015-09-21](https://github.com/joke2k/faker/compare/v0.5.2...v0.5.3)

* Added ``company_vat`` to company ``fi_FI`` provider. Thanks @kivipe.
* Seed a Random instance instead of the module. Thanks Amy Hanlon.
* Fixed en_GB postcodes to be more realistic. Thanks @mapleoin for the report.
* Fixed support for Python 3 in the python provider. Thanks @derekjamescurtis.
* Fixed U.S. SSN generation. Thanks @jschaf.
* Use environment markers for wheels. Thanks @RonnyPfannschmidt
* Fixed Python3 issue in ``pyiterable`` and ``pystruct`` providers.
  Thanks @derekjamescurtis.
* Fixed ``en_GB`` postcodes to be more realistic. Thanks @mapleoin.
* Fixed and improved performance of credit card number provider. Thanks @0x000.
* Added Brazilian SSN, aka CPF. Thanks @ericchaves.
* Added female and male names for ``fa_IR``. Thanks @afshinrodgar.
* Fixed issues with Decimal objects as input to geo_coordinate. Thanks @davy.
* Fixed bug for ``center`` set to ``None`` in geo_coordinate. Thanks @davy.
* Fixed deprecated image URL placeholder services.
* Fixed provider's example formatting in documentation.
* Added en_AU provider. Thanks @xfxf.

### [0.5.2 - 2015-06-11](https://github.com/joke2k/faker/compare/v0.5.1...v0.5.2)
-
* Added ``uuid4`` to ``misc`` provider. Thanks Jared Culp.
* Fixed ``jcb15`` and ``jcb16`` in ``credit_card`` provider.
  Thanks Rodrigo Braz.
* Fixed CVV and CID code generation in `credit_card` provider.
  Thanks Kevin Stone.
* Added ``--include`` flag to command line tool. Thanks Flavio Curella.
* Added ``country_code`` to `address`` provider. Thanks @elad101 and Tobin Brown.


### [0.5.1 - 2015-05-21](https://github.com/joke2k/faker/compare/v0.5...v0.5.1)
-----------------------------------------------------------------------------

* Fixed egg installation. Thanks David R. MacIver, @kecaps
* Updated person names for ``ru_RU``. Thanks @mousebaiker.
* Updated ko_KR locale. Thanks Lee Yeonjae.
* Fixed installation to install importlib on Python 2.6.
  Thanks Guillaume Thomas.
* Improved tests. Thanks Aarni Koskela, @kecaps, @kaushal.
* Made Person ``prefixes``/``suffixes`` always return strings.
  Thanks Aarni Koskela.
* ``pl_PL`` jobs added. Thanks Dariusz Choruży.
* Added ``ja_JP`` provider. Thanks Tatsuji Tsuchiya, Masato Ohba.
* Localized remaining providers for consistency. Thanks Flavio Curella.
* List of providers in compiled on runtime and is not hardcoded anymore.
  Thanks Flavio Curella.
* Fixed State names in ``en_US``. Thanks Greg Meece.
* Added ``time_delta`` method to ``date_time`` provider. Thanks Tobin Brown.
* Added filename and file extension methods to ``file`` provider.
  Thanks Tobin Brown.
* Added Finnish ssn (HETU) provider. Thanks @kivipe.
* Fixed person names for ``pl_PL``. Thanks Marek Bleschke.
* Added ``sv_SE`` locale providers.
  Thanks Tome Cvitan.
* ``pt_BR`` Provider: Added ``catch_phrase`` to Company provider and fixed
  names in Person Provider. Thanks Marcelo Fonseca Tambalo.
* Added ``sk_SK`` localized providers. Thanks @viktormaruna.
* Removed ``miscelleneous`` provider. It is superceded by the
  ``misc`` provider.

### [0.5.0 - 2015-02-16](https://github.com/joke2k/faker/compare/v0.4.2...v0.5)
------------------------------------------------------------------------------

* Localized providers
* Updated ``ko_KR`` provider. Thanks Lee Yeonjae.
* Added ``pt_PT`` provider. Thanks João Delgado.
* Fixed mispellings for ``en_US`` company provider. Thanks Greg Meece.
* Added currency provider. Thanks Wiktor Ślęczka
* Ensure choice_distribution always uses floats. Thanks Katy Lavallee.
* Added ``uk_UA`` provider. Thanks Cyril Tarasenko.
* Fixed encoding issues with README, CHANGELOG and setup.py.
  Thanks Sven-Hendrik Haase.
* Added Turkish person names and phone number patterns. Thanks Murat Çorlu.
* Added ``ne_NP`` provider. Thanks Sudip Kafle.
* Added provider for Austrian ``de_AT``. Thanks Bernhard Essl.

### [0.4.2 - 2014-08-20](https://github.com/joke2k/faker/compare/v0.4.1...v0.4.2)

* Fixed setup

### [0.4.1 - 2014-08-20](https://github.com/joke2k/faker/compare/v0.4...v0.4.1)

* Added MAC address provider. Thanks Sébastien Béal.
* Added ``lt_LT`` and ``lv_LV`` localized providers. Thanks Edgar Gavrik.
* Added ``nl_NL`` localized providers. Thanks @LolkeAB, @mdxs.
* Added ``bg_BG`` localized providers. Thanks Bret B.
* Added ``sl_SI``. Thanks to @janezkranjc
* Added distribution feature. Thanks to @fcurella
* Relative date time. Thanks to @soobrosa
* Fixed ``date_time_ad`` on 32bit Linux. Thanks @mdxs.
* Fixed ``domain_word`` to output slugified strings.

### [0.4 - 2014-03-30](https://github.com/joke2k/faker/compare/v0.3.2...v0.4)

* Modified en_US ``person.py`` to ouput female and male names.
  Thanks Adrian Klaver.
* Added SSN provider for ``en_US`` and ``en_CA``. Thanks Scott (@milliquet).
* Added ``hi_IN`` localized provider. Thanks Pratik Kabra.
* Refactoring of command line

### 0.3.2 - 2013-11-11

* New provider: Credit card generator
* Improved Documentor

### 0.3.1 - 2013-10-18

* FIX setup.py

### 0.3 - 2013-10-18

* PEP8 style conversion (old camelCased methods are deprecated!)
* New language: ``pt_BR`` (thanks to @rvnovaes)
* all localized provider now uses ``from __future__ import unicode_literals``
* documentor prints localized provider after all defaults
* FIX tests for python 2.6


### 0.2 - 2010-12-01

* New providers: ``Python``, ``File``
* Providers imported with ``__import__``
* Module is runnable with ``python -m faker [name] [*args]``
* Rewrite fake generator system (allow autocompletation)
* New language: French
* Rewrite module ``__main__`` and new Documentor class

### 0.1 - 2012-11-13

* First release
