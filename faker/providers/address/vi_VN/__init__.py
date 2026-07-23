"""This module provides address-related functionalities for Vietnamese addresses."""

from typing import Optional, Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """Provider for generating Vietnamese addresses.
    Sources:

    # https://vi.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:K%C3%BD_hi%E1%BB%87u_quy_%C6%B0%E1%BB%9Bc_c%C3%A1c_t%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam
    # administrative units: https://github.com/thanglequoc/vietnamese-provinces-database
    # postcode: https://mst.gov.vn/van-ban-phap-luat/25175.htm
    """

    # Building
    vi_building_number_formats = (
        "%",
        "%#",
        "%##",
        "%/%#",
        "%/%#/%##",
        "%#/%##",
    )
    building_number_formats = (
        "Số {{vi_building_number_format}}",
        "{{vi_building_number_format}}",
    )

    # Sub-street
    sub_street_prefixes = (
        "Ngõ",
        "Hẻm",
        "Khu",
        "Khóm",
    )
    sub_street_formats = ("{{sub_street_prefix}} %#",)

    # Street
    street_prefixes = (
        "Đường",
        "đường",
        "Phố",
        "phố",
    )
    street_suffixes = (
        "Đường",
        "Ngõ",
        "Hẻm",
        "Làng",
        "Khu",
        "Tổ",
        "Số",
        "Dãy",
    )
    streets = (
        "Nguyễn Trãi",
        "Nguyễn Huệ",
        "Nguyễn Du",
        "Nguyễn Đình Chiểu",
        "Nguyễn Thị Minh Khai",
        "Nguyễn Văn Cừ",
        "Nguyễn Chí Thanh",
        "Nguyễn Hữu Cảnh",
        "Nguyễn Tất Thành",
        "Nguyễn Văn Linh",
        "Trần Hưng Đạo",
        "Trần Phú",
        "Trần Quang Khải",
        "Trần Quốc Toản",
        "Trần Bình Trọng",
        "Trần Não",
        "Lê Lợi",
        "Lê Lai",
        "Lê Duẩn",
        "Lê Thánh Tôn",
        "Lê Văn Sỹ",
        "Lê Văn Việt",
        "Lê Đức Thọ",
        "Lê Quang Định",
        "Lý Thường Kiệt",
        "Lý Tự Trọng",
        "Lý Chính Thắng",
        "Hai Bà Trưng",
        "Bà Triệu",
        "Điện Biên Phủ",
        "Cách Mạng Tháng Tám",
        "Nam Kỳ Khởi Nghĩa",
        "Xô Viết Nghệ Tĩnh",
        "Hoàng Văn Thụ",
        "Hoàng Diệu",
        "Hoàng Hoa Thám",
        "Phan Đình Phùng",
        "Phan Chu Trinh",
        "Phan Văn Trị",
        "Phan Xích Long",
        "Võ Văn Tần",
        "Võ Thị Sáu",
        "Võ Văn Kiệt",
        "Đinh Tiên Hoàng",
        "Đinh Bộ Lĩnh",
        "Tôn Đức Thắng",
        "Pasteur",
        "Alexandre de Rhodes",
        "Hùng Vương",
        "Quang Trung",
        "Ngô Quyền",
        "Đồng Khởi",
        "Bạch Đằng",
        "Kinh Dương Vương",
        "Phạm Văn Đồng",
        "Phạm Ngũ Lão",
        "Phạm Hùng",
        "Phạm Thế Hiển",
        "Huỳnh Tấn Phát",
        "Huỳnh Văn Bánh",
        "Cộng Hòa",
        "Trường Chinh",
        "Giải Phóng",
        "Thống Nhất",
        "Độc Lập",
        "Hòa Bình",
        "Dân Chủ",
        "Tự Do",
        "30 Tháng 4",
        "2 Tháng 9",
        "3 Tháng 2",
    )
    numbered_street_formats = (
        "số %",
        "%#",
        "số %#",
    )
    street_formats = (
        "{{street_prefix}} {{numbered_street}}",
        "{{street_prefix}} {{street_name}}",
        "{{street_name}}",
    )
    street_address_formats = (
        "{{building_number}} {{street}}",
        "{{building_number}} {{sub_street}} {{street}}",
    )

    # Commune level: communes, wards
    communes = (
        "Tân An",
        "An Bình",
        "Hòa Bình",
        "Long Bình",
        "An Hải",
        "An Khê",
        "An Nhơn",
        "An Phú",
        "Bình Minh",
        "Bình Thuận",
        "Diên Hồng",
        "Đông Hải",
        "Đông Hòa",
        "Hoàng Mai",
        "Hòa Thành",
        "Tân Phú Đông",
        "Tuy Phước Đông",
        "Dương Minh Châu",
    )
    commune_prefixes = (
        "Phường",
        "phường",
        "Xã",
        "xã",
    )
    commune_formats = ("{{commune_prefix}} {{commune_name}}",)

    # Provincial level: cities, provinces
    cities = (
        "Hà Nội",
        "Hải Phòng",
        "Huế",
        "Đà Nẵng",
        "Hồ Chí Minh",
        "Cần Thơ",
    )
    city_prefixes = (
        "Thành phố",
        "thành phố",
        "TP.",
    )
    city_suffixes = (
        "Thành phố",
        "Quận",
        "Huyện",
        "Thị xã",
        "Xã",
        "Phường",
    )
    city_formats = ("{{city_prefix}} {{city_name}}",)
    provinces = (
        "Cao Bằng",
        "Tuyên Quang",
        "Điện Biên",
        "Lai Châu",
        "Sơn La",
        "Lào Cai",
        "Thái Nguyên",
        "Lạng Sơn",
        "Quảng Ninh",
        "Bắc Ninh",
        "Phú Thọ",
        "Hưng Yên",
        "Ninh Bình",
        "Thanh Hóa",
        "Nghệ An",
        "Hà Tĩnh",
        "Quảng Trị",
        "Quảng Ngãi",
        "Gia Lai",
        "Đắk Lắk",
        "Khánh Hòa",
        "Lâm Đồng",
        "Đồng Nai",
        "Tây Ninh",
        "Đồng Tháp",
        "Vĩnh Long",
        "An Giang",
        "Cà Mau",
    )
    province_prefixes = (
        "Tỉnh",
        "tỉnh",
    )
    province_formats = (
        "{{province_prefix}} {{province_name}}",
        "{{province_name}}",
    )

    # Address
    address_formats = (
        "{{street_address}}, {{commune}}, {{province}}",
        "{{street_address}} {{commune}} {{province}}",
        "{{street_address}} {{commune}} {{province}} {{postcode}}",
        "{{street_address}}, {{commune}}, {{city}}",
        "{{street_address}} {{commune}} {{city}}",
        "{{street_address}} {{commune}} {{city}} {{postcode}}",
    )

    postcode_formats = ("#####",)

    provinces_abbr = (
        "AG",
        "BN",
        "CM",
        "CB",
        "CT",
        "ĐNa",
        "ĐL",
        "ĐB",
        "ĐN",
        "ĐT",
        "GL",
        "HN",
        "HT",
        "HP",
        "SG",
        "HUE",
        "HY",
        "KH",
        "LC",
        "LS",
        "LCa",
        "LĐ",
        "NA",
        "NB",
        "PT",
        "QNg",
        "QN",
        "QT",
        "SL",
        "TN",
        "TNg",
        "TH",
        "TQ",
        "VL",
    )

    provinces_postcode = {
        "AG": ((90000, 90999), (91000, 91999), (92000, 92999)),
        "BN": ((16000, 16999), (26000, 26999)),
        "CM": ((97000, 97999), (98000, 98999)),
        "CB": ((21000, 21999),),
        "CT": ((94000, 94999), (95000, 95999), (96000, 96999)),
        "ĐNa": ((50000, 50999), (51000, 51999), (52000, 52999)),
        "ĐL": ((56000, 56999), (63000, 63999), (64000, 64999)),
        "ĐB": ((32000, 32999),),
        "ĐN": ((67000, 67999), (76000, 76999)),
        "ĐT": ((81000, 81999), (84000, 84999)),
        "GL": ((55000, 55999), (61000, 61999), (62000, 62999)),
        "HN": (
            (10000, 10999),
            (11000, 11999),
            (12000, 12999),
            (13000, 13999),
            (14000, 14999),
        ),
        "HT": ((45000, 45999), (46000, 46999)),
        "HP": ((3000, 3999), (4000, 4999), (5000, 5999)),
        "SG": (
            (70000, 70999),
            (71000, 71999),
            (72000, 72999),
            (73000, 73999),
            (74000, 74999),
            (75000, 75999),
            (78000, 78999),
        ),
        "HUE": ((49000, 49999),),
        "HY": ((6000, 6999), (17000, 17999)),
        "KH": ((57000, 57999), (59000, 59999)),
        "LC": ((30000, 30999),),
        "LS": ((25000, 25999),),
        "LCa": ((31000, 31999), (33000, 33999)),
        "LĐ": ((65000, 65999), (66000, 66999), (77000, 77999)),
        "NA": ((43000, 43999), (44000, 44999)),
        "NB": ((7000, 7999), (8000, 8999), (18000, 18999)),
        "PT": ((15000, 15999), (35000, 35999), (36000, 36999)),
        "QNg": ((53000, 53999), (54000, 54999), (60000, 60999)),
        "QN": ((1000, 1999), (2000, 2999)),
        "QT": ((47000, 47999), (48000, 48999)),
        "SL": ((34000, 34999),),
        "TN": ((80000, 80999), (82000, 82999), (83000, 83999)),
        "TNg": ((23000, 23999), (24000, 24999)),
        "TH": ((40000, 40999), (41000, 41999), (42000, 42999)),
        "TQ": ((20000, 20999), (22000, 22999)),
        "VL": ((85000, 85999), (86000, 86999), (87000, 87999)),
    }

    def city_prefix(self) -> str:
        """Returns a random city prefix."""
        return self.random_element(self.city_prefixes)

    def administrative_unit(self) -> str:
        """Returns a random administrative unit (province)."""
        return self.random_element(self.provinces + self.cities)

    state = administrative_unit

    def state_abbr(self) -> str:
        """
        Returns a random two-letter abbreviation for Vietnamese provinces.

        """
        abbreviations: Tuple[str, ...] = self.provinces_abbr
        return self.random_element(abbreviations)

    def postcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        """
        Returns a random postcode within the provided province abbreviation.

        :param state_abbr: A province abbreviation.
        :returns: A random postcode within the provided province abbreviation.
        """
        if state_abbr is None:
            state_abbr = self.random_element(self.provinces_abbr)

        if state_abbr in self.provinces_abbr:
            postcode_range = self.random_element(self.provinces_postcode[state_abbr])
            postcode = self.generator.random.randint(*postcode_range)
            return f"{postcode:05d}"

        raise ValueError("Province Abbreviation not found in list")

    def postcode(self) -> str:
        """Returns a random postcode from an allocated province range."""
        return self.postcode_in_state()

    def vi_building_number_format(self) -> str:
        return self.random_element(self.vi_building_number_formats)

    def building_number(self) -> str:
        pattern = self.generator.parse(self.random_element(self.building_number_formats))
        return self.numerify(pattern)

    def sub_street_prefix(self) -> str:
        return self.random_element(self.sub_street_prefixes)

    def sub_street(self) -> str:
        pattern = self.random_element(self.sub_street_formats)
        return self.bothify(self.generator.parse(pattern))

    def street_prefix(self) -> str:
        """
        :example: 'đường'
        """
        return self.random_element(self.street_prefixes)

    def numbered_street(self) -> str:
        """Returns a random street number with at most three digits."""
        pattern = self.generator.parse(self.random_element(self.numbered_street_formats))
        return self.numerify(pattern)

    def street_name(self) -> str:
        return self.random_element(self.streets)

    def street(self) -> str:
        pattern = self.random_element(self.street_formats)
        return self.generator.parse(pattern)

    def commune_name(self) -> str:
        return self.random_element(self.communes)

    def commune_prefix(self):
        return self.random_element(self.commune_prefixes)

    def commune(self) -> str:
        pattern: str = self.random_element(self.commune_formats)
        return self.generator.parse(pattern)

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def province_prefix(self) -> str:
        return self.random_element(self.province_prefixes)

    def province_name(self) -> str:
        return self.random_element(self.provinces)

    def province(self):
        pattern: str = self.random_element(self.province_formats)
        return self.generator.parse(pattern)
