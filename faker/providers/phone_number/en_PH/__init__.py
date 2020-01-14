from ... import BaseProvider


class Provider(BaseProvider):
    """
    Provider for Philippine mobile and landline telephone numbers

    This provider has methods that generate phone numbers specific to service providers whenever applicable, because the
    kinds of services, the quality of said services, and even the fees may vary depending on the service provider and
    the service location. This in turn, affects subscriber behavior, e.g. someone with a SIM from company X may be very
    unlikely to respond to calls and texts sent from a company Y SIM as the service charge might be more expensive. The
    provider methods are there to enable the creation of more "realistic" fake data for such cases.

    Additional Notes:
    - The Philippine telecommunication industry is dominated by the Globe-PLDT duopoly. Globe offers landline services
      under the Globe brand and mobile services under the Globe and TM brands. PLDT offers landline services under the
      PLDT brand, and its subsidiaries offer mobile services under the Smart, TNT, and SUN brands. The rest of the
      industry is shared by smaller players, and Bayantel is one of the more well-known players that provide landline
      services.
    - Globe mobile prefixes include both Globe and TM brands, and the Smart mobile prefixes include both Smart and TNT
      brands but not the SUN brand. Available sources only split the prefixes this way.
    - In October 2019, Area 2 landline numbers were migrated to an 8 digit scheme, while the rest of the country still
      uses the original 7 digit scheme. Area 2 is comprised of the whole National Capital Region (aka Metro Manila) and
      parts of surrounding provinces, and within this area, the service provider's identifier is included in every 8
      digit landline number.

    Sources:
    - https://en.wikipedia.org/wiki/Telephone_numbers_in_the_Philippines
    - https://www.prefix.ph/prefixes/2019-updated-complete-list-of-philippine-mobile-network-prefixes/
    - https://powerpinoys.com/network-prefixes-philippines/
    """

    globe_mobile_number_prefixes = (
        '817', '904', '905', '906', '915', '916', '917',
        '926', '927', '935', '936', '937', '945', '955',
        '956', '965', '966', '967', '973', '975', '976',
        '977', '978', '979', '994', '995', '996', '997',
    )
    smart_mobile_number_prefixes = (
        '813', '907', '908', '909', '910', '911', '912', '913',
        '914', '918', '919', '920', '921', '928', '929', '930',
        '938', '939', '940', '946', '947', '948', '949', '950',
        '951', '961', '970', '981', '989', '992', '998', '999',
    )
    sun_mobile_number_prefixes = (
        '922', '923', '924', '925',
        '931', '932', '933', '934',
        '941', '942', '943', '944',
    )
    globe_mobile_number_formats = (
        '0{{globe_mobile_number_prefix}}-###-####',
        '+63{{globe_mobile_number_prefix}}-###-####',
    )
    smart_mobile_number_formats = (
        '0{{smart_mobile_number_prefix}}-###-####',
        '+63{{smart_mobile_number_prefix}}-###-####',
    )
    sun_mobile_number_formats = (
        '0{{sun_mobile_number_prefix}}-###-####',
        '+63{{sun_mobile_number_prefix}}-###-####',
    )
    mobile_number_formats = globe_mobile_number_formats + smart_mobile_number_formats + sun_mobile_number_formats

    bayantel_landline_identifiers = tuple(str(x) for x in range(3000, 3500))
    misc_landline_identifiers = tuple(str(x) for x in range(5300, 5800)) + tuple(str(x) for x in range(6000, 6700))
    non_area2_landline_area_codes = (
        '32', '33', '34', '35', '36', '38', '42', '43', '44',
        '45', '46', '47', '48', '49', '52', '53', '54', '55',
        '56', '62', '63', '64', '65', '68', '72', '74', '75',
        '77', '78', '82', '83', '84', '85', '86', '87', '88',
    )
    globe_area2_landline_number_formats = (
        '02-7###-####',
        '+632-7###-####',
    )
    pldt_area2_landline_number_formats = (
        '02-8###-####',
        '+632-8###-####',
    )
    bayantel_area2_landline_number_formats = (
        '02-{{bayantel_landline_identifier}}-####',
        '+632-{{bayantel_landline_identifier}}-####',
    )
    misc_area2_landline_number_formats = (
        '02-{{misc_landline_identifier}}-####',
        '+632-{{misc_landline_identifier}}-####',
    )
    area2_landline_number_formats = (
            globe_area2_landline_number_formats
            + pldt_area2_landline_number_formats
            + bayantel_area2_landline_number_formats
            + misc_area2_landline_number_formats
    )
    non_area2_landline_number_formats = (
        '0{{non_area2_landline_area_code}}-###-####',
        '+63{{non_area2_landline_area_code}}-###-####',
    )
    landline_number_formats = area2_landline_number_formats + non_area2_landline_number_formats

    def _create_phone_number(self, formats):
        pattern = self.random_element(formats)
        return self.numerify(self.generator.parse(pattern))

    def globe_mobile_number_prefix(self):
        return self.random_element(self.globe_mobile_number_prefixes)

    def smart_mobile_number_prefix(self):
        return self.random_element(self.smart_mobile_number_prefixes)

    def sun_mobile_number_prefix(self):
        return self.random_element(self.sun_mobile_number_prefixes)

    def bayantel_landline_identifier(self):
        return self.random_element(self.bayantel_landline_identifiers)

    def misc_landline_identifier(self):
        return self.random_element(self.misc_landline_identifiers)

    def non_area2_landline_area_code(self):
        return self.random_element(self.non_area2_landline_area_codes)

    def globe_mobile_number(self):
        return self._create_phone_number(self.globe_mobile_number_formats)

    def smart_mobile_number(self):
        return self._create_phone_number(self.smart_mobile_number_formats)

    def sun_mobile_number(self):
        return self._create_phone_number(self.sun_mobile_number_formats)

    def mobile_number(self):
        return self._create_phone_number(self.mobile_number_formats)

    def globe_area2_landline_number(self):
        return self._create_phone_number(self.globe_area2_landline_number_formats)

    def pldt_area2_landline_number(self):
        return self._create_phone_number(self.pldt_area2_landline_number_formats)

    def bayantel_area2_landline_number(self):
        return self._create_phone_number(self.bayantel_area2_landline_number_formats)

    def misc_area2_landline_number(self):
        return self._create_phone_number(self.misc_area2_landline_number_formats)

    def area2_landline_number(self):
        return self._create_phone_number(self.area2_landline_number_formats)

    def non_area2_landline_number(self):
        return self._create_phone_number(self.non_area2_landline_number_formats)

    def landline_number(self):
        return self._create_phone_number(self.landline_number_formats)
