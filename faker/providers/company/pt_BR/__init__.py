import string

from typing import List

from .. import Provider as CompanyProvider

# Characters allowed in the base of an alphanumeric CNPJ (digits and A-Z).
CNPJ_ALPHANUMERIC_CHARS = string.digits + string.ascii_uppercase

_CNPJ_WEIGHTS = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def company_id_checksum(digits: List[int]) -> List[int]:
    digits = list(digits)
    weights = _CNPJ_WEIGHTS

    dv = sum(w * d for w, d in zip(weights[1:], digits))
    dv = (11 - dv) % 11
    dv = 0 if dv >= 10 else dv
    digits.append(dv)

    dv2 = sum(w * d for w, d in zip(weights, digits))
    dv2 = (11 - dv2) % 11
    dv2 = 0 if dv2 >= 10 else dv2
    digits.append(dv2)

    return digits[-2:]


def alphanumeric_company_id_checksum(base: str) -> str:
    """Return the two numeric check digits for a 12-character CNPJ base.

    Supports the alphanumeric CNPJ (Serpro): each base character contributes
    the value ``ord(char) - ord("0")``, so digits keep their value and letters
    map ``A`` -> 17 ... ``Z`` -> 42. The check digits themselves stay numeric.
    """
    values = [ord(char) - ord("0") for char in base]

    dv1 = (11 - sum(w * v for w, v in zip(_CNPJ_WEIGHTS[1:], values))) % 11
    dv1 = 0 if dv1 >= 10 else dv1
    values.append(dv1)

    dv2 = (11 - sum(w * v for w, v in zip(_CNPJ_WEIGHTS, values))) % 11
    dv2 = 0 if dv2 >= 10 else dv2

    return f"{dv1}{dv2}"


class Provider(CompanyProvider):
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}}",
        "{{last_name}}",
    )

    catch_phrase_formats = ("{{catch_phrase_noun}} {{catch_phrase_verb}} {{catch_phrase_attribute}}",)

    nouns = (
        "a segurança",
        "o prazer",
        "o conforto",
        "a simplicidade",
        "a certeza",
        "a arte",
        "o poder",
        "o direito",
        "a possibilidade",
        "a vantagem",
        "a liberdade",
    )

    verbs = (
        "de conseguir",
        "de avançar",
        "de evoluir",
        "de mudar",
        "de inovar",
        "de ganhar",
        "de atingir seus objetivos",
        "de concretizar seus projetos",
        "de realizar seus sonhos",
    )

    attributes = (
        "de maneira eficaz",
        "mais rapidamente",
        "mais facilmente",
        "simplesmente",
        "com toda a tranquilidade",
        "antes de tudo",
        "naturalmente",
        "sem preocupação",
        "em estado puro",
        "com força total",
        "direto da fonte",
        "com confiança",
    )

    company_suffixes = ("S/A", "S.A.", "Ltda.", "- ME", "- EI", "e Filhos")

    def catch_phrase_noun(self) -> str:
        """
        Returns a random catch phrase noun.
        """
        return self.random_element(self.nouns)

    def catch_phrase_attribute(self) -> str:
        """
        Returns a random catch phrase attribute.
        """
        return self.random_element(self.attributes)

    def catch_phrase_verb(self) -> str:
        """
        Returns a random catch phrase verb.
        """
        return self.random_element(self.verbs)

    def catch_phrase(self) -> str:
        """
        :example: 'a segurança de evoluir sem preocupação'
        """
        pattern: str = self.random_element(self.catch_phrase_formats)
        catch_phrase = self.generator.parse(pattern)
        catch_phrase = catch_phrase[0].upper() + catch_phrase[1:]
        return catch_phrase

    def company_id(self, alphanumeric: bool = False) -> str:
        """Generate a Brazilian CNPJ as a 14-character string (no punctuation).

        When ``alphanumeric`` is ``True`` the 12-character base may contain
        letters (the new Serpro format); the two check digits stay numeric.
        """
        if alphanumeric:
            base = "".join(self.random_element(CNPJ_ALPHANUMERIC_CHARS) for _ in range(12))
            return base + alphanumeric_company_id_checksum(base)

        digits: List[int] = list(self.random_sample(range(10), 8))
        digits += [0, 0, 0, 1]
        digits += company_id_checksum(digits)
        return "".join(str(d) for d in digits)

    def cnpj(self, alphanumeric: bool = False) -> str:
        """Generate a formatted Brazilian CNPJ (e.g. ``12.345.678/0001-95``).

        Pass ``alphanumeric=True`` for the new alphanumeric format, e.g.
        ``12.ABC.345/01DE-35``.
        """
        company_id = self.company_id(alphanumeric=alphanumeric)
        return f"{company_id[:2]}.{company_id[2:5]}.{company_id[5:8]}/{company_id[8:12]}-{company_id[12:]}"
