from .. import Provider as BaseProvider
from ... import date_time
from faker.utils.checksums import calculate_luhn

class Provider(BaseProvider):
    """
    A Faker provider for the Austrian Identification Numbers
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
        date = date_time.Provider.date_time_between(start_date='-100y', end_date='now')

        day = str(date.day) if date.day > 10 else '0' + str(date.day)
        month = str(date.month) if date.month > 10 else '0' + str(date.month)
        year = str(date.year)[-2:]

        serial = self.bothify("###")
        birth = day + month + year
        check = str(calculate_luhn(int(serial + birth)))

        return serial + check + birth

    vat_id_formats = ("ATU########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Austrian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
