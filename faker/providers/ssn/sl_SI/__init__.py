from .. import Provider as BaseProvider
from faker.utils.checksums import calculate_luhn

class Provider(BaseProvider):
    """
    A Faker provider for the Slovenian Identification Numbers
    """

    tin_formats = ("%######",)

    def tin(self) -> str:
        """
        https://learn.microsoft.com/en-us/microsoft-365/compliance/sit-defn-slovenia-tax-identification-number?view=o365-worldwide
        :return: a random Slovenian TIN
        """
        tin = self.bothify(self.random_element(self.tin_formats))

        return tin + str(calculate_luhn(float(tin)))


    vat_id_formats = ("SI########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Slovenian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
