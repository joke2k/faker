from typing import List, Tuple

from faker.providers.sbn.rules import RegistrantRule

from .. import BaseProvider
from .rules import RULES
from .sbn import SBN, SBN9


class Provider(BaseProvider):
    """Generates fake SBNs. These are the precursor to the ISBN and are
    largely similar to ISBN-10.

    See https://www.isbn-international.org/content/what-isbn for the
    format of ISBNs. SBNs have no EAN prefix or Registration Group.
    """

    def _body(self) -> List[str]:
        """Generate the information required to create an SBN"""

        reg_pub_len: int = SBN.MAX_LENGTH - 1

        # Generate a registrant/publication combination
        reg_pub: str = self.numerify("#" * reg_pub_len)

        # Use rules to separate the registrant from the publication
        rules: List[RegistrantRule] = RULES
        registrant, publication = self._registrant_publication(reg_pub, rules)
        return [registrant, publication]

    @staticmethod
    def _registrant_publication(reg_pub: str, rules: List[RegistrantRule]) -> Tuple[str, str]:
        """Separate the registration from the publication in a given
        string.
        :param reg_pub: A string of digits representing a registration
            and publication.
        :param rules: A list of RegistrantRules which designate where
            to separate the values in the string.
        :returns: A (registrant, publication) tuple of strings.
        """
        for rule in rules:
            if rule.min <= reg_pub[:-1] <= rule.max:
                reg_len = rule.registrant_length
                break
        else:
            raise Exception("Registrant/Publication not found in registrant rule list.")
        registrant, publication = reg_pub[:reg_len], reg_pub[reg_len:]
        return registrant, publication

    def sbn9(self, separator: str = "-") -> str:
        registrant, publication = self._body()
        sbn = SBN9(registrant, publication)
        return sbn.format(separator)
