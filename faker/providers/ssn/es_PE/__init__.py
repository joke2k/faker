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
        """
        Generates a random DNI (Documento Nacional de Identidad).
        It's an 8-digit number.
        :return: A random 8-digit DNI.
        """
        return self.numerify("########")

    def ruc(self) -> str:
        """
        Generates a valid RUC (Registro Único de Contribuyentes).
        It's an 11-digit number.
        https://www.gob.pe/729-consultar-el-estado-del-ruc
        :return: A random 11-digit RUC.
        """
        # RUC can start with 10 (person), 15/17 (non-domiciled), or 20 (company)
        # We will generate the most common ones: 10 and 20.
        ruc_type = self.random_element(["10", "20"])
        if ruc_type == "10":
            # For natural persons, the next 8 digits are often the DNI
            body = self.numerify("########")
        else:  # ruc_type == '20'
            # For companies, the next 8 digits are correlative
            body = self.numerify("########")
    """

    def dni(self) -> str:
        """
        Generates a random DNI (Documento Nacional de Identidad).
        It's an 8-digit number.
        :return: A random 8-digit DNI.
        """
        return self.numerify("########")

    def ruc(self) -> str:
        """
        Generates a valid RUC (Registro Único de Contribuyentes).
        It's an 11-digit number.
        https://www.gob.pe/729-consultar-el-estado-del-ruc
        :return: A random 11-digit RUC.
        """
        # RUC can start with 10 (person), 15/17 (non-domiciled), or 20 (company)
        # We will generate the most common ones: 10 and 20.
        ruc_type = self.random_element(["10", "20"])
        if ruc_type == "10":
            # For natural persons, the next 8 digits are often the DNI
            body = self.numerify("########")
        else:  # ruc_type == '20'
            # For companies, the next 8 digits are correlative
            body = self.numerify("########")

>>>>>>> origin/feature/add-es_PE-locale
        base_ruc = f"{ruc_type}{body}"
        check_digit = self._calculate_ruc_check_digit(base_ruc)
        return f"{base_ruc}{check_digit}"

    @staticmethod
    def _calculate_ruc_check_digit(base_ruc: str) -> int:
        """
        Calculates the check digit for a Peruvian RUC.
        The algorithm is weighted sum modulo 11 (Módulo 11).
        """
>>>>>>> origin/feature/add-es_PE-locale
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
        """
        Alias for DNI.
        """
        return self.dni()
