from .. import Provider as BaseProvider
from faker.utils.checksums import calculate_luhn

class Provider(BaseProvider):
    """
    A Faker provider for German Identification Numbers
    """

    tin_formats = ("##########",)

    def tin(self) -> str:
        """
        https://learn.microsoft.com/en-us/microsoft-365/compliance/sit-defn-germany-tax-identification-number?view=o365-worldwide
        :return: A random German TIN
        """
        id = self.bothify(self.random_element(self.tin_formats))
        check = str(calculate_luhn(int(id)))

        return id + check


    vat_id_formats = ("DE#########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random German VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
