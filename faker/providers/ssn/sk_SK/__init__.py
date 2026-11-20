from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Slovakian VAT IDs
    """

    vat_id_formats = ("SK##########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Slovakian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def birth_number(self) -> str:
        """
        Birth Number (Czech/Slovak: rodné číslo (RČ))
        https://en.wikipedia.org/wiki/National_identification_number#Czech_Republic_and_Slovakia
        """
        birthdate = self.generator.date_of_birth()
        year = f"{birthdate:%y}"
        month = "%.2d" % (birthdate.month + self.random_element((0, 50)))
        day = f"{birthdate:%d}"
        if birthdate.year > 1953:
            sn = self.random_int(11, 9999)
        else:
            sn = self.random_int(11, 999)
        number = f"{year}{month}{day}{sn:0{4 if birthdate.year > 1953 else 3}d}"
        birth_number = str(int(number) // 11 * 11).zfill(len(number))
        return f"{birth_number[:6]}/{birth_number[6::]}"
