from .. import Provider as SsnProvider


class Provider(SsnProvider):
    def ssn(self) -> str:
        """
        Returns a 9 digits Dutch SSN called "burgerservicenummer (BSN)".

        the Dutch "burgerservicenummer (BSN)" needs to pass the "11-proef",
        which is a check digit approach; this function essentially reverses
        the checksum steps to create a random valid BSN (which is 9 digits).
        """

        # see http://nl.wikipedia.org/wiki/Burgerservicenummer (in Dutch)
        def _checksum(digits):
            factors = (9, 8, 7, 6, 5, 4, 3, 2, -1)
            s = 0
            for i in range(len(digits)):
                s += digits[i] * factors[i]
            return s

        while True:
            # Draw the first 8 digits independently (with replacement), since
            # a BSN has no requirement that they be distinct. An 8-digit BSN
            # is written with one leading zero to reach 9 digits, so a second
            # leading zero would represent a number shorter than any real
            # BSN and has to be excluded.
            first_digit = self.generator.random.randint(0, 9)
            second_digit_choices = range(1, 10) if first_digit == 0 else range(0, 10)
            digits = [first_digit, self.generator.random.choice(second_digit_choices)]
            digits += self.generator.random.choices(range(10), k=6)
            # sum those 8 digits according to (part of) the "11-proef"
            s = _checksum(digits)
            # determine the last digit to make it qualify the test
            digits.append((s % 11) % 10)
            # repeat steps until it does qualify the test
            if 0 == (_checksum(digits) % 11):
                break

        # build the resulting BSN
        bsn = "".join([str(e) for e in digits])
        # finally return our random but valid BSN
        return bsn

    vat_id_formats = ("NL#########B##",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random Dutch VAT ID
        """
        return self.bothify(self.random_element(self.vat_id_formats))
