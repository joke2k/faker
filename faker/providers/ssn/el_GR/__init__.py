import random

from faker.utils.checksums import calculate_luhn

from .. import Provider as BaseProvider


def tin_checksum(tin: str) -> int:
    """
    Calculates the checksum (last) digit of Greek TINs given the rest
    :param tin: first 8 digits of a Greek TIN
    :return: calculated checksum digit
    """

    tin_list = [int(i) for i in list(tin)]
    return (
        (
            (tin_list[0] * 256)
            + (tin_list[1] * 128)
            + (tin_list[2] * 64)
            + (tin_list[3] * 32)
            + (tin_list[4] * 16)
            + (tin_list[5] * 8)
            + (tin_list[6] * 4)
            + (tin_list[7] * 2)
        )
        % 11
    ) % 10


class Provider(BaseProvider):
    """
    A Faker provider for Greek identification numbers
    """

    police_id_format = "??######"

    # TIN checksum algo sourced from here
    # http://epixeirisi.gr/%CE%9A%CE%A1%CE%99%CE%A3%CE%99%CE%9C%CE%91-%CE%98%CE%95%CE%9C%CE%91%CE%A4%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%9A%CE%91%CE%99-%CE%9B%CE%9F%CE%93%CE%99%CE%A3%CE%A4%CE%99%CE%9A%CE%97%CE%A3/23791/%CE%91%CF%81%CE%B9%CE%B8%CE%BC%CF%8C%CF%82-%CE%A6%CE%BF%CF%81%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CE%BA%CE%BF%CF%8D-%CE%9C%CE%B7%CF%84%CF%81%CF%8E%CE%BF%CF%85
    def vat_id(self, prefix: bool = True) -> str:
        """
        Generates random Greek VAT IDs (business TINs)
        :param prefix: boolean option to use EU format ("EL") prefix
        :return: a random Greek VAT ID
        """

        vat_id = "EL" if prefix else ""
        vat_id_starting_numbers = ("7", "8", "9", "0")
        vat_id = (
            vat_id + random.choice(vat_id_starting_numbers) + self.numerify("#######")
        )
        return vat_id + str(tin_checksum(vat_id[2:] if prefix else vat_id))

    def tin(self) -> str:
        """
        Generates random Greek personal TINs
        :return: a random Greek personal TIN
        """

        vat_id_starting_numbers = ("1", "2", "3", "4")
        vat_id = random.choice(vat_id_starting_numbers) + self.numerify("#######")
        return vat_id + str(tin_checksum(vat_id))

    # Uses Luhn checksum according to this
    # https://dotnetadventures.wordpress.com/2012/12/13/c-%CE%AD%CE%BB%CE%B5%CE%B3%CF%87%CE%BF%CF%82-%CE%BF%CF%81%CE%B8%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82-%CE%B1-%CE%BC-%CE%BA-%CE%B1-includes-python-version/
    def ssn(self) -> str:
        """
        Generates random Greek social security number (AMKA)
        :return: a random Greek social security number
        """

        ssn = self.generator.date(pattern="%d%m%y") + self.numerify("####")
        return ssn + str(calculate_luhn(ssn))

    # Valid format accd to ΥΑ 3021/19/53/2005 - FΕΚ 1440/Β'/18.10.2005
    # http://www.dsanet.gr/Epikairothta/Nomothesia/ya3021_19_05.htm
    def police_id(self) -> str:
        """
        Generates random Greek identity card (aka police-issued identification card) numbers
        :return: a random Greek identity card number
        """

        return self.bothify(
            self.police_id_format,
            letters="ΑΒΕΖΗΙΚΜΝΟΡΤΥΧ",
        )
