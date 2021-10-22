from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Greek VAT IDs and Greek police IDs
    """

    vat_id_formats = ("EL#########",)

    police_id_formats = (
        "?######",
        "??######",
        "? ######",
        "?? ######",
    )

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Greek VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def police_id(self) -> str:
        """
        :return: a random Greek police ID
        """

        return self.bothify(
            self.random_element(self.police_id_formats),
            letters="ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
        )
