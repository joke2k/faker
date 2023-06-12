from .. import Provider as BaseProvider
import datetime
from faker.utils.checksums import calculate_luhn

class Provider(BaseProvider):
    """
    A Faker provider for Austrian Identification Numbers
    """

    def ssn(self) -> str:
        """
        https://learn.microsoft.com/en-us/microsoft-365/compliance/sit-defn-austria-social-security-number?view=o365-worldwide
        10 digits:
            - three digits that correspond to a serial number
            - one check digit
            - six digits that correspond to the birth month (DDMMYY)
        :return: a random Austrian SSN
        """


        age = datetime.timedelta(days=self.generator.random.randrange(0, 100))
        birthday = datetime.date.today() - age
        birthdate = "%02d%02d%s" % (
            birthday.day,
            birthday.month,
            str(birthday.year)[-2:],
        )

        serial = self.bothify("###")
        check = str(calculate_luhn(float(serial + birthdate)))

        ssn = serial + check + birthdate

        return ssn

    tin_formats = ("##-###/####",)

    def tin(self) -> str:
        """
        https://learn.microsoft.com/en-us/microsoft-365/compliance/sit-defn-austria-tax-identification-number?view=o365-worldwide
        :return: a random Austrian TIN
        """

        return self.bothify(self.random_element(self.tin_formats))

    vat_id_formats = ("ATU########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Austrian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
