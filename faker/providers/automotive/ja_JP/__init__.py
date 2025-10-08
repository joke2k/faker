from .. import Provider as AutomotiveProvider

# flake8: noqa: E501


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``ja_JP`` locale.

    Sources (retrieved on 2025-09-15):

    - https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%8A%E3%83%B3%E3%83%90%E3%83%BC%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E4%B8%80%E8%A6%A7
    - http://nplate.cloudfree.jp/misc/m50_bango.html
    """

    license_plate_area_names = (
        "品川",
        "足立",
        "練馬",
        "横浜",
        "川崎",
        "名古屋",
        "大阪",
        "神戸",
        "福岡",
        "札幌",
        "尾張小牧",
        "伊勢志摩",
    )

    classification_numbers = (
        "###",
        "##",
    )

    license_plate_kana = (
        "あ",
        "い",
        "う",
        "え",
        "か",
        "き",
        "く",
        "け",
        "こ",
        "さ",
        "す",
        "せ",
        "そ",
        "た",
        "ち",
        "つ",
        "て",
        "と",
        "な",
        "に",
        "ぬ",
        "ね",
        "の",
        "は",
        "ひ",
        "ふ",
        "ほ",
        "ま",
        "み",
        "む",
        "め",
        "も",
        "や",
        "ゆ",
        "よ",
        "ら",
        "り",
        "る",
        "れ",
        "ろ",
        "わ",
        "を",
    )

    serial_number_formats = ("#", "##", "###", "####")

    MIDDLE_DOT = "・"
    DELIMITER = "-"

    license_plate_formats = ("{{area_name}} {{classification_number}} {{kana}} {{serial_number}}",)

    def license_plate(self) -> str:
        """Generate a Japanese license plate."""
        pattern = self.random_element(self.license_plate_formats)
        return self.generator.parse(pattern)

    def area_name(self) -> str:
        return self.random_element(self.license_plate_area_names)

    def classification_number(self) -> str:
        return self.numerify(self.random_element(self.classification_numbers))

    def kana(self) -> str:
        return self.random_element(self.license_plate_kana)

    def serial_number(self) -> str:
        """
        Generate the vehicle’s serial number (the last four digits on a Japanese license plate).
        - For 4 digits: insert a hyphen between the second and third digits (e.g., 12-34).
        - For 1 to 3 digits: pad the left side with middle dots (・) so the total width is four
          characters (e.g., ・123, ・・12, ・・・1). Do not use a hyphen in these cases.
        """

        raw_digits = self.numerify(self.random_element(self.serial_number_formats))
        n = len(raw_digits)

        if n == 4:
            v = f"{raw_digits[:2]}{self.DELIMITER}{raw_digits[2:]}"
            return v
        else:
            return raw_digits.rjust(4, self.MIDDLE_DOT)
