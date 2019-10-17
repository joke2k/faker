# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        # National & Mobile dialing
        '0{{area_code}}#######',
        '0{{area_code}} ### ####',
        '0{{area_code}}-###-####',
        # International parenthesis
        '234{{area_code}}#######',
        '234 {{area_code}} ### ####',
        '234-{{area_code}}-###-####',
        '+234{{area_code}}#######',
        '+234 {{area_code}} ### ####',
        '+234-{{area_code}}-###-####',
    )

    mobile_codes = [
        # MTN
        '803',
        '703',
        '903',
        '806',
        '706',
        '813',
        '814',
        '816',
        '810',
        '906',
        '704',
        # Airtel
        '802', '902', '701', '808', '708', '812', '901', '907',
        # Glo
        '805', '705', '905', '807', '815', '905', '811',
        # 9Mobile
        '809', '909', '817', '818', '908',
        # Ntel
        '804',
        # Smile
        '702',
        # Multilinks
        '709',
        # Starcomms
        '819',
        # Zoom
        '707',
    ]

    def area_code(self):
        return self.numerify(self.random_element(self.mobile_codes))

    def phone_number(self):
        pattern = self.random_element(self.formats)
        return self.numerify(self.generator.parse(pattern))
