import random

from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    """Implement barcode provider for Afghanistan (en_AF)"""

    local_prefixes = (
        (0, 1),
        (9, 1),
    )

    def ean13(self, prefix: str = "622") -> str:
        if not prefix.isdigit():
            raise ValueError("Prefix must be numeric")

        length = 12 - len(prefix)
        body = "".join(str(random.randint(0, 9)) for _ in range(length))
        partial_code = prefix + body
        check_digit = self._calculate_check_digit(partial_code)

        return partial_code + str(check_digit)

    def _calculate_check_digit(self, code: str) -> int:
        if len(code) != 12:
            raise ValueError("Code must be 12 digits for check digit calculation")

        sum_odd = sum(int(code[i]) for i in range(0, 12, 2))
        sum_even = sum(int(code[i]) for i in range(1, 12, 2))
        total = sum_odd + sum_even * 3

        return (10 - (total % 10)) % 10

    def upc_a(self, prefix: str = "622") -> str:
        return self.ean13(prefix)[1:]
