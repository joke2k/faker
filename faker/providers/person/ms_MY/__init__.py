from .. import Provider as PersonProvider

localized = True


class Provider(PersonProvider):
    """Person provider for ms_MY locale (Malay, Malaysia)."""

    formats_male = (
        "{{first_name_male}}{{last_name}}",
        "{{prefix_male}}{{first_name_male}}{{last_name}}",
    )

    formats_female = (
        "{{first_name_female}}{{last_name}}",
        "{{prefix_female}}{{first_name_female}}{{last_name}}",
    )

    formats = formats_male + formats_female

    first_names_male = (
        "Ahmad",
        "Muhammad",
        "Abdul",
        "Mohd",
        "Azizan",
        "Zainal",
        "Ismail",
        "Hafiz",
        "Azizul",
        "Fahmi",
        "Haziq",
        "Shahrul",
        "Azman",
        "Sulaiman",
        "Yusof",
        "Shafiq",
        "Zaki",
        "Faris",
        "Hafizul",
        "Azizan",
        "Shahril",
        "Luqman",
        "Naqib",
        "Zulhilmi",
        "Arif",
        "Faiz",
        "Iman",
        "Reza",
    )

    first_names_female = (
        "Aishah",
        "Siti",
        "Nor",
        "Fatimah",
        "Zainab",
        "Amina",
        "Salmah",
        "Nur",
        "Hanim",
        "Rashidah",
        "Nurul",
        "Aisyah",
        "Amirah",
        "Hanis",
        "Liyana",
        "Syafiqah",
        "Zara",
        "Irdina",
        "Sofea",
        "Hana",
        "Insyirah",
        "Fatin",
        "Nasuhah",
        "Damia",
        "Aqilah",
        "Farah",
        "Sakinah",
        "Syazwani",
        "Hana",
        "Najma",
    )

    last_names = (
        "bin Abdullah",
        "binti Ahmad",
        "bin Hassan",
        "binti Mohd",
        "bin Ibrahim",
        "binti Ismail",
        "bin Yusof",
        "binti Razak",
        "bin Othman",
        "binti Hamid",
        "bin Nazri",
        "binti Abdullah",
        "bin Azizan",
        "binti Zainal",
        "bin Sulaiman",
        "binti Shafiq",
        "bin Zaki",
        "binti Hafiz",
        "bin Azizan",
    )

    prefixes_males = (
        "En.",
        "Tn.",
        "Dr.",
        "Hj.",
        "Ir.",
        "Prof.",
        "Dato'",
        "Datuk",
        "Tan Sri",
        "Tun",
    )
    prefixes_females = (
        "Pn.",
        "Cik.",
        "Dr.",
        "Hjh.",
        "Ir.",
        "Prof.",
        "Datuk",
        "Puan Sri",
        "Tun",
    )

    def first_name_male(self):
        return self.random_element(self.first_names_male)

    def first_name_female(self):
        return self.random_element(self.first_names_female)

    def last_name(self):
        return self.random_element(self.last_names)

    def prefix_male(self):
        return self.random_element(self.prefixes_males)

    def prefix_female(self):
        return self.random_element(self.prefixes_females)
