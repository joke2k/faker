from faker.utils.datetime_safe import datetime

from .. import Provider as CompanyProvider


def calculate_checksum(value):
    factors = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8][-len(value):]
    check_sum = 0
    for number, factor in zip(value, factors):
        check_sum += int(number) * factor

    return str((check_sum % 11) % 10)


class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}} «{{last_name}}»',
        '{{company_prefix}} «{{last_name}} {{last_name}}»',
        '{{company_prefix}} «{{last_name}}-{{last_name}}»',
        '{{company_prefix}} «{{last_name}}, {{last_name}} и {{last_name}}»',
        '{{last_name}}',
    )

    company_prefixes = (
        'РАО', 'АО', 'ИП', 'НПО',
    )

    def company_prefix(self):
        return self.random_element(self.company_prefixes)

    def businesses_inn(self):
        """
        Returns tax identification number for businesses (ru. идентификационный номер налогоплательщика, ИНН).
        """
        region = '%02d' % self.random_int(min=1, max=92)
        inspection = '%02d' % self.random_int(min=1, max=99)
        tail = '%05d' % self.random_int(min=1, max=99999)
        result = region + inspection + tail

        return result + calculate_checksum(result)

    def individuals_inn(self):
        """
        Returns tax identification number for individuals (ru. идентификационный номер налогоплательщика, ИНН).
        """
        region = '%02d' % self.random_int(min=1, max=92)
        inspection = '%02d' % self.random_int(min=1, max=99)
        tail = '%06d' % self.random_int(min=1, max=999999)
        result = region + inspection + tail
        result += calculate_checksum(result)

        return result + calculate_checksum(result)

    def businesses_ogrn(self):
        """
        Returns primary state registration number for businesses
        (ru. основной государственный регистрационный номер, ОГРН).
        """
        sign = self.random_element(('1', '5'))
        year = '%02d' % self.random_int(min=1, max=datetime.now().year - 2000)
        region = '%02d' % self.random_int(min=1, max=92)
        tail = '%07d' % self.random_int(min=1, max=9999999)

        result = sign + year + region + tail

        return result + str((int(result) % 11) % 10)

    def individuals_ogrn(self):
        """
        Returns primary state registration number for individuals
        (ru. основной государственный регистрационный номер, ОГРН).
        """
        year = '%02d' % self.random_int(min=1, max=datetime.now().year - 2000)
        region = '%02d' % self.random_int(min=1, max=92)
        tail = '%09d' % self.random_int(min=1, max=999999999)

        result = '3' + year + region + tail

        return result + str((int(result) % 13) % 10)

    def kpp(self):
        """
        Returns tax registration reason code (ru. код причины постановки на учет, КПП).
        """
        region = '%02d' % self.random_int(min=1, max=92)
        inspection = '%02d' % self.random_int(min=1, max=99)
        reason = self.random_element(('01', '43', '44', '45'))
        tail = '%03d' % self.random_int(min=1, max=999)

        return region + inspection + reason + tail
