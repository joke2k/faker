import random

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for Peruvian identity numbers.

    Sources:
    - RENIEC (DNI) and SUNAT (RUC) documentation and official pages
      https://www.reniec.gob.pe, https://www.gob.pe/729-consultar-el-estado-del-ruc
    - Supplemental algorithm reference: public documentation on RUC checksum (Modulo 11)
    Accessed: 2026-02-07
    """

    def dni(self) -> str:
        return self.numerify("########")

    def ruc(self) -> str:
        ruc_type = self.random_element(["10", "20"])
        body = self.numerify("########")
        base_ruc = f"{ruc_type}{body}"
        check_digit = self._calculate_ruc_check_digit(base_ruc)
        return f"{base_ruc}{check_digit}"

    @staticmethod
    def _calculate_ruc_check_digit(base_ruc: str) -> int:
        factors = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        total = sum(int(digit) * factor for digit, factor in zip(base_ruc, factors))
        remainder = total % 11
        check_digit = 11 - remainder
        if check_digit == 10:
            return 0
        if check_digit == 11:
            return 1
        return check_digit

    def ssn(self) -> str:
        return self.dni()
