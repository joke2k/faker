from .. import Provider as SsnProvider


def checksum(s: str) -> int:
    def _get_alphabet_weight(c: str) -> int:
        """A=10, B=11, ...., H=17,
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

    res = 0
    for i, c in enumerate(s):
        if i == 0:
            res = _get_alphabet_weight(c) % 10 * 9 + _get_alphabet_weight(c) // 10
        elif i < 9:
            res += int(c) * (9 - i)
        else:
            res += int(c)
    return res


class Provider(SsnProvider):
    def ssn(self) -> str:
        ssn_without_last_char = self.numerify(self.random_uppercase_letter() + str(self.random_int(1, 2)) + "#######")
        last_char = str((10 - checksum(ssn_without_last_char) % 10) % 10)
        return ssn_without_last_char + last_char
