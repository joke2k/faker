from .. import Provider as SsnProvider


class Provider(SsnProvider):

    def ssn(self) -> str:

        def _get_alphabet_weight(c) -> int:
            """ A=10, B=11, ...., H=17,
            I=34,
            J=18, K=19, ..., N=22,
            O=35,
            P=23, Q=24, ..., V=29,
            W=32,
            X=30, Y=31, Z=33
            """
            if ord(c) < 73:  # A-H
                return ord(c) - 55
            if ord(c) == 73:  # I
                return ord(c) - 39
            if ord(c) < 79:  # J-N
                return ord(c) - 56
            if ord(c) == 79:  # O
                return ord(c) - 44
            if ord(c) < 87:  # P-V
                return ord(c) - 57
            if ord(c) == 87:  # W
                return ord(c) - 55
            if ord(c) < 90:  # X, Y
                return ord(c) - 58
            return ord(c) - 57  # Z

        def _checksum(s):
            res = 0
            for i, c in enumerate(s):
                if i == 0:
                    res = _get_alphabet_weight(c) % 10 * 9 + _get_alphabet_weight(c) // 10
                else:
                    res += int(c) * (9 - i)
            return str(10 - res % 10)

        ssn_without_checksum = self.numerify(self.random_uppercase_letter() + str(self.random_int(1, 2)) + "#######")
        return ssn_without_checksum + _checksum(ssn_without_checksum)
