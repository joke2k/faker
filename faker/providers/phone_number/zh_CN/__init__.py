from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    phonenumber_prefixes = [
        134,
        135,
        136,
        137,
        138,
        139,
        147,
        150,
        151,
        152,
        157,
        158,
        159,
        182,
        187,
        188,
        130,
        131,
        132,
        145,
        155,
        156,
        185,
        186,
        133,
        153,
        180,
        181,
        189,
        # Public mobile network prefixes assigned by the Ministry of Industry and
        # Information Technology (MIIT) since 2011. 149 is a data card prefix, like
        # 145 and 147 above. 174 is left out because only parts of it are public
        # mobile numbers, and IoT prefixes are left out because they have 13 digits.
        # Sources (checked 2026-11-01):
        # - MIIT updates to the national numbering plan, published by the ITU:
        #   https://www.itu.int/dms_pub/itu-t/oth/02/02/T020200002B0006PDFE.pdf
        # - MIIT assigned 190, 192, 196 and 197 in December 2019:
        #   https://m.thepaper.cn/newsDetail_forward_5327717
        # China Mobile
        172,
        178,
        183,
        184,
        195,
        197,
        198,
        # China Unicom
        166,
        175,
        176,
        196,
        # China Telecom
        149,
        173,
        177,
        190,
        191,
        193,
        199,
        # China Broadnet
        192,
        # Mobile virtual network operators
        162,
        165,
        167,
        170,
        171,
    ]
    formats = [str(i) + "########" for i in phonenumber_prefixes]

    def phonenumber_prefix(self) -> int:
        return self.random_element(self.phonenumber_prefixes)
