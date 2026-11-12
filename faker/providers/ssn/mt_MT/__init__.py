from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Maltese VAT IDs
    """

    vat_id_formats = ("MT%#####",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11

        The last two digits are a check value: the weighted sum of all
        eight digits with weights (3, 4, 6, 7, 8, 9, 10, 1) must be a
        multiple of 37.

        :return: A random Maltese VAT ID
        """

        vat_id = self.numerify(self.random_element(self.vat_id_formats))
        total = sum(w * int(d) for w, d in zip((3, 4, 6, 7, 8, 9), vat_id[2:]))
        check = (37 - total % 37) % 37
        return f"{vat_id}{check:02d}"
