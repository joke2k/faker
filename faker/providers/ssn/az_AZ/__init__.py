from .. import Provider as SsnProvider


class Provider(SsnProvider):
    # The FIN code consists of 7 characters (letters and numbers of the English alphabet,
    # except for the letters "I" and "O").

    characters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    all_characters = characters + numbers

    def ssn(self) -> str:
        ssn = "".join(self.random_elements(elements=self.all_characters, length=7))
        return ssn
