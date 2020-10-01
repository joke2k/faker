from collections import OrderedDict

from .. import BaseProvider

localized = True


class CreditCard:

    def __init__(
            self,
            name,
            prefixes,
            length=16,
            security_code='CVC',
            security_code_length=3):
        self.name = name
        self.prefixes = prefixes
        self.length = length
        self.security_code = security_code
        self.security_code_length = security_code_length


class Provider(BaseProvider):
    """Implement default credit card provider for Faker.

    For all methods that take ``card_type`` as an argument, a random card type
    will be used if the supplied value is ``None``. The list of valid card types
    includes ``'amex'``, ``'diners'``, ``'discover'``, ``'jcb'``, ``'jcb15'``,
    ``'jcb16'``, ``'maestro'``, ``'mastercard'``, ``'visa'``, ``'visa13'``,
    ``'visa16'``, and ``'visa19'``.

    Sources:

    - https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29
    - https://www.regular-expressions.info/creditcard.html
    - https://creditcardjs.com/credit-card-type-detection
    """

    prefix_maestro = ['5018', '5020', '5038', '56##', '57##', '58##',
                      '6304', '6759', '6761', '6762', '6763', '0604', '6390']
    prefix_mastercard = ['51', '52', '53', '54', '55', '222%', '223', '224',
                         '225', '226', '227', '228', '229', '23', '24', '25',
                         '26', '270', '271', '2720']
    prefix_visa = ['4']
    prefix_amex = ['34', '37']
    prefix_discover = ['6011', '65']
    prefix_diners = ['300', '301', '302', '303', '304', '305', '36', '38']
    prefix_jcb16 = ['35']
    prefix_jcb15 = ['2131', '1800']

    credit_card_types = OrderedDict((
        ('maestro', CreditCard('Maestro',
                                    prefix_maestro, 12, security_code='CVV')),
        ('mastercard', CreditCard('Mastercard',
                                  prefix_mastercard, 16, security_code='CVV')),
        ('visa16', CreditCard('VISA 16 digit', prefix_visa)),
        ('visa13', CreditCard('VISA 13 digit', prefix_visa, 13)),
        ('visa19', CreditCard('VISA 19 digit', prefix_visa, 19)),
        ('amex', CreditCard('American Express', prefix_amex,
                            15, security_code='CID', security_code_length=4)),
        ('discover', CreditCard('Discover', prefix_discover)),
        ('diners', CreditCard('Diners Club / Carte Blanche', prefix_diners, 14)),
        ('jcb15', CreditCard('JCB 15 digit', prefix_jcb15, 15)),
        ('jcb16', CreditCard('JCB 16 digit', prefix_jcb16)),
    ))
    credit_card_types['visa'] = credit_card_types['visa16']
    credit_card_types['jcb'] = credit_card_types['jcb16']

    luhn_lookup = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8,
                   '5': 1, '6': 3, '7': 5, '8': 7, '9': 9}

    def credit_card_provider(self, card_type=None):
        """Generate a credit card provider name."""
        if card_type is None:
            card_type = self.random_element(self.credit_card_types.keys())
        return self._credit_card_type(card_type).name

    def credit_card_number(self, card_type=None):
        """Generate a valid credit card number."""
        card = self._credit_card_type(card_type)
        prefix = self.random_element(card.prefixes)
        number = self._generate_number(self.numerify(prefix), card.length)
        return number

    def credit_card_expire(self, start='now', end='+10y', date_format='%m/%y'):
        """Generate a credit card expiry date.

        This method uses |date_time_between| under the hood to generate the
        expiry date, so the ``start`` and ``end`` arguments work in the same way
        here as it would in that method. For the actual formatting of the expiry
        date, |strftime| is used and ``date_format`` is simply passed
        to that method.
        """
        expire_date = self.generator.date_time_between(start, end)
        return expire_date.strftime(date_format)

    def credit_card_full(self, card_type=None):
        """Generate a set of credit card details."""
        card = self._credit_card_type(card_type)

        tpl = ('{provider}\n'
               '{owner}\n'
               '{number} {expire_date}\n'
               '{security}: {security_nb}\n')

        tpl = tpl.format(provider=card.name,
                         owner=self.generator.parse(
                             "{{first_name}} {{last_name}}"),
                         number=self.credit_card_number(card),
                         expire_date=self.credit_card_expire(),
                         security=card.security_code,
                         security_nb=self.credit_card_security_code(card))

        return self.generator.parse(tpl)

    def credit_card_security_code(self, card_type=None):
        """Generate a credit card security code."""
        sec_len = self._credit_card_type(card_type).security_code_length
        return self.numerify('#' * sec_len)

    def _credit_card_type(self, card_type=None):
        """Generate a random CreditCard instance of the specified card type."""
        if card_type is None:
            card_type = self.random_element(self.credit_card_types.keys())
        elif isinstance(card_type, CreditCard):
            return card_type
        return self.credit_card_types[card_type]

    def _generate_number(self, prefix, length):
        """Generate a credit card number.

        The ``prefix`` argument is the start of the CC number as a string which
         may contain any number of digits. The ``length`` argument is the length
         of the CC number to generate which is typically 13 or 16.
        """
        number = prefix
        # Generate random char digits
        number += '#' * (length - len(prefix) - 1)
        number = self.numerify(number)
        reverse = number[::-1]
        # Calculate sum
        tot = 0
        pos = 0
        while pos < length - 1:
            tot += Provider.luhn_lookup[reverse[pos]]
            if pos != (length - 2):
                tot += int(reverse[pos + 1])
            pos += 2
        # Calculate check digit
        check_digit = (10 - (tot % 10)) % 10
        number += str(check_digit)
        return number
