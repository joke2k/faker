from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Bulgarian VAT IDs
    """

    vat_id_formats = (
        "########",  # 8 digits + check digit: legal entities (BULSTAT)
        "#########",  # 9 digits + check digit: physical persons, EGN-based
    )

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random Bulgarian VAT ID with a valid check digit: 9
        digits for legal entities or 10 digits for physical persons,
        mirroring the check digit algorithms of ``stdnum.bg.vat``
        (python-stdnum), which accepts either length.
        """
        vat_format = self.random_element(self.vat_id_formats)
        base = self.numerify(vat_format)
        if len(base) == 8:
            # the 9-digit numbers are for legal entities
            return f"BG{base}{self._vat_check_digit_legal(base)}"
        # the 10-digit numbers are for physical persons, foreigners and others
        check = self._vat_check_digit_other(base)
        while check == "10":
            # a check digit of 10 is not representable as a single digit
            base = self.numerify(vat_format)
            check = self._vat_check_digit_other(base)
        return f"BG{base}{check}"

    @staticmethod
    def _vat_check_digit_legal(number: str) -> str:
        """
        Check digit for the 9-digit (legal entity) variant, identical to
        ``stdnum.bg.vat.calc_check_digit_legal``: weighted sum modulo 11
        with weights 1..8; on a remainder of 10 the sum is recomputed
        with weights 3..10 and the result is taken modulo 10.
        """
        check = sum((i + 1) * int(n) for i, n in enumerate(number)) % 11
        if check == 10:
            check = sum((i + 3) * int(n) for i, n in enumerate(number)) % 11
        return str(check % 10)

    @staticmethod
    def _vat_check_digit_other(number: str) -> str:
        """
        Check digit for the 10-digit (physical person) variant,
        identical to ``stdnum.bg.vat.calc_check_digit_other``: weights
        (4, 3, 2, 7, 6, 5, 4, 3, 2) and ``(11 - weighted sum) % 11``.
        The result can be ``"10"``, which is not a valid single check
        digit, so callers must regenerate the base number in that case.
        """
        weights = (4, 3, 2, 7, 6, 5, 4, 3, 2)
        return str((11 - sum(w * int(n) for w, n in zip(weights, number))) % 11)
