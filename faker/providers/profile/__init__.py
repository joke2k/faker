import itertools

from datetime import date
from decimal import Decimal
from typing import Dict, List, Optional, Tuple, Union

from ...typing import SexLiteral
from .. import BaseProvider


class Provider(BaseProvider):
    """
    This provider is a collection of functions to generate personal profiles and identities.

    """

    def simple_profile(self, sex: Optional[SexLiteral] = None) -> Dict[str, Union[str, date, SexLiteral]]:
        """
        Generates a basic profile with personal information
        """
        sex_ = self.random_element(["F", "M"]) if sex is None else sex
        if sex_ == "F":
            name = self.generator.name_female()
        elif sex_ == "M":
            name = self.generator.name_male()
        return {
            "username": self.generator.user_name(),
            "name": name,
            "sex": sex_,
            "address": self.generator.address(),
            "mail": self.generator.free_email(),
            "birthdate": self.generator.date_of_birth(),
        }

    def profile(
        self, fields: Optional[List[str]] = None, sex: Optional[SexLiteral] = None
    ) -> Dict[str, Union[str, Tuple[Decimal, Decimal], List[str], date]]:
        """
        Generates a complete profile.
        If "fields" is not empty, only the fields in the list will be returned
        """
        if fields is None:
            fields = []

        d = {
            "job": self.generator.job(),
            "company": self.generator.company(),
            "ssn": self.generator.ssn(),
            "residence": self.generator.address(),
            "current_location": (self.generator.latitude(), self.generator.longitude()),
            "blood_group": "".join(self.random_element(list(itertools.product(["A", "B", "AB", "O"], ["+", "-"])))),
            "website": [self.generator.url() for _ in range(1, self.random_int(2, 5))],
        }

        d = dict(d, **self.generator.simple_profile(sex))
        # field selection
        if len(fields) > 0:
            d = {k: v for k, v in d.items() if k in fields}

        return d
