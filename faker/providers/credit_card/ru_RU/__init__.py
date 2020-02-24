from collections import OrderedDict

from faker.providers.person.ru_RU import translit

from .. import CreditCard
from .. import Provider as CreditCardProvider


class Provider(CreditCardProvider):
    # Prefixes from: https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    prefix_visa = ['4']
    prefix_mastercard = ['51', '52', '53', '54', '55', '222%', '223', '224', '225', '226',
                         '227', '228', '229', '23', '24', '25', '26', '270', '271', '2720']
    prefix_mir = ['2200', '2201', '2202', '2203', '2204']
    prefix_maestro = ['50', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69']
    prefix_amex = ['34', '37']
    prefix_unionpay = ['62', '81']

    credit_card_types = OrderedDict((
        ('visa', CreditCard('Visa', prefix_visa, security_code='CVV2')),
        ('mastercard', CreditCard('Mastercard', prefix_mastercard, security_code='CVC2')),
        ('mir', CreditCard('МИР', prefix_mir)),
        ('maestro', CreditCard('Maestro', prefix_maestro, security_code='CVV2')),
        ('amex', CreditCard('American Express', prefix_amex, 15, security_code='CID', security_code_length=4)),
        ('unionpay', CreditCard('Union Pay', prefix_unionpay)),
    ))

    def credit_card_expire(self, start='now', end='+4y', date_format='%m/%y'):
        expire_date = self.generator.date_time_between(start, end)
        return expire_date.strftime(date_format)

    def credit_card_full(self, card_type=None):
        card = self._credit_card_type(card_type)

        tpl = ('{provider}\n'
               '{owner}\n'
               '{number} {expire_date}\n'
               '{security}: {security_nb}\n'
               '{issuer}')

        tpl = tpl.format(provider=card.name,
                         owner=translit(
                             self.generator.parse(self.random_element(["{{first_name_male}} {{last_name_male}}",
                                                                       "{{first_name_female}} {{last_name_female}}"]))),
                         number=self.credit_card_number(card),
                         expire_date=self.credit_card_expire(),
                         security=card.security_code,
                         security_nb=self.credit_card_security_code(card),
                         issuer=self.generator.parse("{{bank}}"))

        return self.generator.parse(tpl)
