from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source (https://tr.wikipedia.org/wiki/T.C._Kimlik_Numaras%C4%B1)
    # Turkey Republic National Number (TCKN) is an 11-digit identity number.
    # Rules:
    # 1. The number consists of 11 digits.
    # 2. The first digit cannot be zero.
    # 3. The 10th digit is calculated as:
    #    ((sum of digits in odd positions (1st, 3rd, 5th, 7th, 9th) * 7)
    #    - sum of digits in even positions (2nd, 4th, 6th, 8th)) mod 10.
    # 4. The 11th digit is the modulo 10 of the sum of the first 10 digits.
    # 5. The number must satisfy these rules to be considered valid.

    def ssn(self) -> str:
        """
        :example: '85420031070'
        """
        digits = [self.random_int(1, 9)]

        for _ in range(8):
            digits.append(self.random_int(0, 9))

        odd_sum = sum(digits[i] for i in [0, 2, 4, 6, 8])
        even_sum = sum(digits[i] for i in [1, 3, 5, 7])
        tenth = ((odd_sum * 7) - even_sum) % 10
        digits.append(tenth)

        total_sum = sum(digits)
        eleventh = total_sum % 10
        digits.append(eleventh)

        return "".join(str(d) for d in digits)
