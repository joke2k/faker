"""This module provides address-related functionalities for Vietnamese addresses."""

from collections import OrderedDict
from typing import Optional, Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """Provider for generating Vietnamese addresses.
    Sources:

    # https://vi.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:K%C3%BD_hi%E1%BB%87u_quy_%C6%B0%E1%BB%9Bc_c%C3%A1c_t%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam
    """

    city_prefixes = ("Thành phố", "Quận", "Huyện", "Thị xã")

    city_suffixes = (
        "Thành phố",
        "Quận",
        "Huyện",
        "Thị xã",
        "Xã",
        "Phường",
    )

    building_number_formats = ("###", "##", "#")

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

    postcode_formats = ("######",)

    provinces = (
        "An Giang",
        "Bà Rịa – Vũng Tàu",
        "Bạc Liêu",
        "Bắc Kạn",
        "Bắc Giang",
        "Bắc Ninh",
        "Bến Tre",
        "Bình Dương",
        "Bình Định",
        "Bình Phước",
        "Bình Thuận",
        "Cà Mau",
        "Cao Bằng",
        "Cần Thơ",
        "Đà Nẵng",
        "Đắk Lắk",
        "Đắk Nông",
        "Điện Biên",
        "Đồng Nai",
        "Đồng Tháp",
        "Gia Lai",
        "Hà Giang",
        "Hà Nam",
        "Hà Nội",
        "Hà Tĩnh",
        "Hải Dương",
        "Hải Phòng",
        "Hậu Giang",
        "Hòa Bình",
        "Thành phố Hồ Chí Minh",
        "Hưng Yên",
        "Khánh Hòa",
        "Kiên Giang",
        "Kon Tum",
        "Lai Châu",
        "Lạng Sơn",
        "Lào Cai",
        "Lâm Đồng",
        "Long An",
        "Nam Định",
        "Nghệ An",
        "Ninh Bình",
        "Ninh Thuận",
        "Phú Thọ",
        "Phú Yên",
        "Quảng Bình",
        "Quảng Nam",
        "Quảng Ngãi",
        "Quảng Ninh",
        "Quảng Trị",
        "Sóc Trăng",
        "Sơn La",
        "Tây Ninh",
        "Thái Bình",
        "Thái Nguyên",
        "Thanh Hóa",
        "Thừa Thiên Huế",
        "Tiền Giang",
        "Trà Vinh",
        "Tuyên Quang",
        "Vĩnh Long",
        "Vĩnh Phúc",
        "Yên Bái",
    )

    provinces_abbr = (
        "AG",
        "BV",
        "BL",
        "BK",
        "BG",
        "BN",
        "BT",
        "BD",
        "BĐ",
        "BP",
        "BTh",
        "CM",
        "CB",
        "CT",
        "ĐNa",
        "ĐL",
        "ĐNo",
        "ĐB",
        "ĐN",
        "ĐT",
        "GL",
        "HG",
        "HNa",
        "HN",
        "HT",
        "HD",
        "HP",
        "HGi",
        "HB",
        "SG",
        "HY",
        "KH",
        "KG",
        "KT",
        "LC",
        "LS",
        "LCa",
        "LĐ",
        "LA",
        "NĐ",
        "NA",
        "NB",
        "NT",
        "PT",
        "PY",
        "QB",
        "QNa",
        "QNg",
        "QN",
        "QT",
        "ST",
        "SL",
        "TN",
        "TB",
        "TNg",
        "TH",
        "TTH",
        "TG",
        "TV",
        "TQ",
        "VL",
        "VP",
        "YB",
    )

    provinces_postcode = {
        "AG": (88000, 88999),
        "BV": (79000, 79999),
        "BL": (96000, 96999),
        "BK": (26000, 26999),
        "BG": (23000, 23999),
        "BN": (22000, 22999),
        "BT": (93000, 93999),
        "BD": (82000, 82999),
        "BĐ": (59000, 59999),
        "BP": (83000, 83999),
        "BTh": (80000, 80999),
        "CM": (97000, 97999),
        "CB": (27000, 27999),
        "CT": (92000, 92999),
        "ĐNa": (55000, 55999),
        "ĐL": (63000, 63999),
        "ĐNo": (64000, 64999),
        "ĐB": (38000, 38999),
        "ĐN": (81000, 81999),
        "ĐT": (87000, 87999),
        "GL": (60000, 60999),
        "HG": (31000, 31999),
        "HNa": (40000, 40999),
        "HN": (10000, 15999),
        "HT": (48000, 48999),
        "HD": (17000, 17999),
        "HP": (18000, 18999),
        "HGi": (91000, 91999),
        "HB": (35000, 35999),
        "SG": (70000, 76999),
        "HY": (16000, 16999),
        "KH": (65000, 65999),
        "KG": (92000, 92999),
        "KT": (58000, 58999),
        "LC": (39000, 39999),
        "LS": (24000, 24999),
        "LCa": (33000, 33999),
        "LĐ": (67000, 67999),
        "LA": (85000, 85999),
        "NĐ": (42000, 42999),
        "NA": (46000, 47999),
        "NB": (43000, 43999),
        "NT": (66000, 66999),
        "PT": (29000, 29999),
        "PY": (62000, 62999),
        "QB": (51000, 51999),
        "QNa": (56000, 56999),
        "QNg": (57000, 57999),
        "QN": (20000, 20999),
        "QT": (52000, 52999),
        "ST": (95000, 95999),
        "SL": (36000, 36999),
        "TN": (84000, 84999),
        "TB": (41000, 41999),
        "TNg": (25000, 25999),
        "TH": (44000, 45999),
        "TTH": (53000, 53999),
        "TG": (86000, 86999),
        "TV": (94000, 94999),
        "TQ": (30000, 30999),
        "VL": (89000, 89999),
        "VP": (28000, 28999),
        "YB": (32000, 32999),
    }

    address_formats = OrderedDict(
        (
            ("{{street_address}}\n{{city}}, {{postcode}}", 25.0),
            ("{{city}}\n{{street_address}}, {{postcode}}", 1.0),
        )
    )

    city_formats = (
        "{{city_prefix}} {{first_name}}{{city_suffix}}",
        "{{first_name}}{{city_suffix}}",
    )

    street_name_formats = (
        "{{first_name}} {{street_suffix}}",
        "{{last_name}} {{street_suffix}}",
    )

    street_address_formats = ("{{building_number}} {{street_name}}",)

    def city_prefix(self) -> str:
        """Returns a random city prefix."""
        return self.random_element(self.city_prefixes)

    def administrative_unit(self) -> str:
        """Returns a random administrative unit (province)."""
        return self.random_element(self.provinces)

    state = administrative_unit

    def state_abbr(self) -> str:
        """
        Returns a random two-letter abbreviation for Vietnamese provinces.

        """
        abbreviations: Tuple[str, ...] = self.provinces_abbr
        return self.random_element(abbreviations)

    def postcode(self) -> str:
        """Returns a random postcode."""
        return f"{self.generator.random.randint(100000, 999999):06d}"

    def postcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        """
        Returns a random postcode within the provided province abbreviation.

        :param state_abbr: A province abbreviation.
        :returns: A random postcode within the provided province abbreviation.
        """
        if state_abbr is None:
            state_abbr = self.random_element(self.provinces_abbr)

        if state_abbr in self.provinces_abbr:
            postcode = str(
                self.generator.random.randint(
                    self.provinces_postcode[state_abbr][0], self.provinces_postcode[state_abbr][1]
                )
            )

            # zero left pad up until desired length (length is 6)
            target_postcode_len = 6
            current_postcode_len = len(postcode)
            if current_postcode_len < target_postcode_len:
                pad = target_postcode_len - current_postcode_len
                postcode = f"{'0' * pad}{postcode}"

            return postcode

        raise ValueError("Province Abbreviation not found in list")
