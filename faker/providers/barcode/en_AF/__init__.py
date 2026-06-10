import random
from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    """Implement barcode provider for Afghanistan (en_AF)"""

    # Example Afghanistan prefixes (just illustrative)
    local_prefixes = (
        (0, 1),  # could represent Afghan local products
        (9, 1),
    )

    def ean13(self, prefix: str = "622") -> str:
        """Generate a 13-digit EAN barcode with optional prefix for Afghanistan."""
        if not prefix.isdigit():
            raise ValueError("Prefix must be numeric")
        length = 12 - len(prefix)
        body = "".join(str(random.randint(0, 9)) for _ in range(length))
        partial_code = prefix + body
        check_digit = self._calculate_check_digit(partial_code)
        return partial_code + str(check_digit)

    def _calculate_check_digit(self, code: str) -> int:
        """Calculate the EAN-13 check digit"""
        if len(code) != 12:
            raise ValueError("Code must be 12 digits for check digit calculation")
        sum_odd = sum(int(code[i]) for i in range(0, 12, 2))
        sum_even = sum(int(code[i]) for i in range(1, 12, 2))
        total = sum_odd + sum_even * 3
        return (10 - (total % 10)) % 10

    def upc_a(self, prefix: str = "622") -> str:
        """Generate a 12-digit UPC-A barcode using the same prefix"""
        ean = self.ean13(prefix)
        return ean[1:]  # UPC-A is 12 digits, drop the first digit

