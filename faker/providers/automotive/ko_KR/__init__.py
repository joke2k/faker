from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """
    Implement automotive provider for ``ko_KR`` locale.
    """

    license_formats = (
        "##?####",
        "###?####",
    )

    letter_codes = (
        "가",
        "나",
        "다",
        "라",
        "마",
        "거",
        "너",
        "더",
        "러",
        "머",
        "버",
        "서",
        "어",
        "저",
        "고",
        "노",
        "도",
        "로",
        "모",
        "보",
        "소",
        "오",
        "조",
        "구",
        "누",
        "두",
        "루",
        "무",
        "부",
        "수",
        "우",
        "주",
    )

    def license_plate(self) -> str:
        pattern = self.random_element(self.license_formats)
        letters = "".join(self.letter_codes)
        return self.numerify(self.lexify(pattern, letters=letters))
