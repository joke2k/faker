from typing import Tuple

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source:
    # https://en.wikipedia.org/wiki/National_Insurance_number
    # UK National Insurance numbers (NINO) follow a specific format
    # To avoid generating real NINOs, the prefix and suffix letters
    # remain static using values reserved by HMRC (never to be used).
    # Example format: "QR 12 34 56 C" or "QR123456C" - only alphanumeric
    # and whitespace characters are permitted. Whitespace is for readability
    # only and is generally included as per the above examples, but a
    # few 'styles' have been included below for the sake of realism.

    nino_formats: Tuple[str, ...] = (
        "ZZ ## ## ## T",
        "ZZ######T",
        "ZZ ###### T",
    )

    def ssn(self) -> str:
        pattern: str = self.random_element(self.nino_formats)
        return self.numerify(self.generator.parse(pattern))

    vat_id_formats: Tuple[str, ...] = (
        "GB### #### ##",
        "GB### #### ## ###",
        "GBGD###",
        "GBHA###",
    )

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random British VAT ID
        """
        pattern = self.random_element(self.vat_id_formats)

        if pattern == "GBGD###":
            return f"GBGD{self.random_int(min=0, max=499):03d}"

        if pattern == "GBHA###":
            return f"GBHA{self.random_int(min=500, max=999):03d}"

        body = self.numerify("#######")
        total = sum(int(digit) * weight for digit, weight in zip(body, range(8, 1, -1)))
        check_digits = (-total) % 97

        number = f"GB{body[:3]} {body[3:]} {check_digits:02d}"

        if pattern == "GB### #### ## ###":
            number += " " + self.numerify("###")

        return number
