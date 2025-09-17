from __future__ import annotations

from typing import Iterable, List

from .. import BaseProvider

AMBIGUOUS = set("O0oIl1|`'\"")
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"


class Provider(BaseProvider):
    """Strong password generator"""

    def strong_password(
        self,
        *,
        length: int = 16,
        min_upper: int = 1,
        min_lower: int = 1,
        min_digits: int = 1,
        min_symbols: int = 1,
        allow_ambiguous: bool = False,
    ) -> str:
        """Generate a strong password base on policy provided
        Parameters:
        - length : Total length of the generated password
        - min_upper : Minimum number of uppercase letters
        - min_lower : Minimum number of lowercase letters
        - min_digits : Minimum number of digits
        - min_symbols : Minimum number of symbols (from a curated set)
        - allow_ambiguous : If False, characters that are commonly confused (e.g., 'O', '0', 'l', '1', '|') are excluded
        """
        min = [min_upper, min_lower, min_digits, min_symbols]
        if any(m < 0 for m in min):
            raise ValueError("Minimum counts must be non-negative")
        required = sum(min)
        if required > length:
            raise ValueError(f"length ({length}) is less than the sum of minimums ({required})")

        # Build character pools
        uppercase = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        lowercase = [c for c in "abcdefghijklmnopqrstuvwxyz"]
        digits = [c for c in "0123456789"]
        symbols = list(SYMBOLS)

        if not allow_ambiguous:

            def filter(pool: Iterable[str]) -> List[str]:
                return [c for c in pool if c not in AMBIGUOUS]

            uppercase = filter(uppercase)
            lowercase = filter(lowercase)
            digits = filter(digits)

        # Guarantee minimum requirements
        password_chars: List[str] = []
        password_chars.extend(self.random_choices(uppercase, length=min_upper))
        password_chars.extend(self.random_choices(lowercase, length=min_lower))
        password_chars.extend(self.random_choices(digits, length=min_digits))
        password_chars.extend(self.random_choices(symbols, length=min_symbols))

        # Fill remaining characters from the union pool
        characters_pool = uppercase + lowercase + digits + symbols
        remaining = length - len(password_chars)
        if remaining > 0:
            password_chars.extend(self.random_choices(characters_pool, length=remaining))

        # Shuffle
        rng = getattr(self.generator, "random", None)
        if rng is None:
            import random as _random

            rng = _random
        rng.shuffle(password_chars)

        return "".join(password_chars)
