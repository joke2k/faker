import random

from datetime import date, datetime
from typing import Optional

from ....typing import SexLiteral
from .. import Provider as SsnProvider


def select_gender(gender: SexLiteral) -> int:
    """Choose an even number for Female and odd number for Male."""
    gender = 0 if gender.lower() == "f" else 1
    return random.choice(range(gender, 10, 2))


def calculate_day_count(birthday: date) -> int:
    """Calculate the day count from reference date '31 December 1899'."""
    ref_date = date(1899, 12, 31)
    return (birthday - ref_date).days


def calculate_check_sum(val: str) -> int:
    """Calculate checksum using INN calculation method."""
    weights = [-1, 5, 7, 9, 4, 6, 10, 5, 7]
    checksum = sum(int(v) * w for v, w in zip(val, weights))

    return checksum % 11 % 10


class Provider(SsnProvider):
    def ssn(self, birthday: Optional[str] = None, gender: Optional[SexLiteral] = None) -> str:
        """
        Ukrainian "Реєстраційний номер облікової картки платника податків"
        also known as "Ідентифікаційний номер фізичної особи".
        @params: birthday: "DD-MM-YYYY" format, default random date
        @params: gender: "M" or "F" default: random gender

        :sample:
        :sample: birthday='22-06-1990', gender='F'
        """

        try:
            # generate day of birthday date object
            if birthday:
                dob = datetime.strptime(birthday, "%d-%m-%Y").date()
            else:
                dob = self.generator.date_object()
        except Exception:
            raise ValueError("Birthday format must be DD-MM-YYYY")

        if gender and gender not in ("M", "F"):
            raise ValueError('Gender must be "m" or "f" or None')

        day_count = calculate_day_count(dob)
        people_num = self.random_number(3, fix_len=True)
        gender_ = select_gender(gender) if gender else random.randint(0, 1)
        ssn_without_checksum = f"{day_count}{people_num}{gender_}"
        checksum = calculate_check_sum(ssn_without_checksum)
        return f"{ssn_without_checksum}{checksum}"
