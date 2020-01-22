from .. import Provider as BaseProvider


class Provider(BaseProvider):
    vat_id_formats = (
        'CZ########',
        'CZ#########',
        'CZ##########',
    )

    national_id_months = ['%.2d' % i for i in range(1, 13)] + ['%.2d' % i for i in range(51, 63)]

    def vat_id(self):
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random Czech VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def birth_number(self):
        """
        Birth Number (Czech/Slovak: rodné číslo (RČ))
        https://en.wikipedia.org/wiki/National_identification_number#Czech_Republic_and_Slovakia
        """
        birthdate = self.generator.date_of_birth()
        year = '%.2d' % (birthdate.year % 100)
        month = self.random_element(self.national_id_months)
        day = '%.2d' % birthdate.day
        if birthdate.year > 1953:
            sn = self.random_number(4, True)
        else:
            sn = self.random_number(3, True)
        number = int('{}{}{}{}'.format(year, month, day, sn))
        while number % 11 != 0:
            number += 1
        else:
            number = str(number)
            if year == '00':
                number = '00' + number
            elif year[0] == '0':
                number = '0' + number
            return '{}/{}'.format(number[:6], number[6::])
