from typing import Dict, List, Tuple

from .. import BaseProvider
from .isbn import ISBN10, ISBN13, MAX_LENGTH

localized = True


class Provider(BaseProvider):
    """Generates fake ISBNs.

    See https://www.isbn-international.org/content/what-isbn for the
    format of ISBNs.
    See https://www.isbn-international.org/range_file_generation for the
    list of rules pertaining to each prefix/registration group.
    """

    rules: Dict[str, Dict[str, List[Tuple[str, str, int]]]] = {}

    def _body(self) -> List[str]:
        """Generate the information required to create an ISBN-10 or
        ISBN-13.
        """
        ean: str = self.random_element(self.rules.keys())
        reg_group: str = self.random_element(self.rules[ean].keys())

        # Given the chosen ean/group, decide how long the
        #   registrant/publication string may be.
        # We must allocate for the calculated check digit, so
        #   subtract 1
        reg_pub_len: int = MAX_LENGTH - len(ean) - len(reg_group) - 1

        # Generate a registrant/publication combination
        reg_pub: str = self.numerify("#" * reg_pub_len)

        # Use rules to separate the registrant from the publication
        rules = self.rules[ean][reg_group]
        registrant, publication = self._registrant_publication(reg_pub, rules)
        return [ean, reg_group, registrant, publication]

    @staticmethod
    def _registrant_publication(reg_pub: str, rules: List[Tuple[str, str, int]]) -> Tuple[str, str]:
        """Separate the registration from the publication in a given
        string.

        :param reg_pub: A string of digits representing a registration
            and publication.
        :param rules: A list of registrant rules which designate where
            to separate the values in the string.
        :returns: A (registrant, publication) tuple of strings.
        """
        for rule in rules:
            if rule[0] <= reg_pub[:-1] <= rule[1]:
                reg_len = rule[2]
                break
        else:
            raise Exception(f"Registrant/Publication '{reg_pub}' not found in registrant rule list.")
        registrant, publication = reg_pub[:reg_len], reg_pub[reg_len:]
        return registrant, publication

    def isbn13(self, separator: str = "-") -> str:
        ean, group, registrant, publication = self._body()
        isbn = ISBN13(ean, group, registrant, publication)
        return isbn.format(separator)

    def isbn10(self, separator: str = "-") -> str:
        ean, group, registrant, publication = self._body()
        isbn = ISBN10(ean, group, registrant, publication)
        return isbn.format(separator)
