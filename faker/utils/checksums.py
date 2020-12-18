from typing import List


def luhn_checksum(number: float) -> int:
    def digits_of(n: float) -> List[int]:
        return [int(d) for d in str(n)]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def calculate_luhn(partial_number: float) -> int:
    """
    Generates the Checksum using Luhn's algorithm
    """
    check_digit = luhn_checksum(int(partial_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit
