from collections import OrderedDict
from typing import Optional

from faker.providers.person.uk_UA import translit
from faker.typing import CardType, CreditCard

from .. import Provider as CreditCardProvider


class Provider(CreditCardProvider):
    """Implement credit card provider for ``uk_UA`` locale.
    https://blog.ipay.ua/uk/sekrety-bankovskix-kart-kak-identificirovat-bank-po-nomeru-karty/
    """

    prefix_visa = ["4"]
    prefix_mastercard = ["51", "52", "53", "54"]
    prefix_prostir = ["9"]
    prefix_maestro = ["6762"]

    credit_card_types = OrderedDict(
        (
            ("visa", CreditCard("Visa", prefix_visa, security_code="CVV2")),
            ("mastercard", CreditCard("Mastercard", prefix_mastercard, security_code="CVC2")),
            ("prostir", CreditCard("ПРОСТІР", prefix_prostir, security_code="CVC2")),
            ("maestro", CreditCard("Maestro", prefix_maestro, security_code="CVV")),
        )
    )

    def credit_card_full(self, card_type: Optional[CardType] = None) -> str:
        """Generate UA Credit Card:
        Supported card types 'visa', 'mastercard', 'prostir', 'maestro'

        :sample:
        :sample: card_type="prostir"
        :sample: card_type="mastercard"
        """
        card = self._credit_card_type(card_type)
        tpl = "{provider}\n{owner}\n{number} {expire_date}\n{security}: {security_nb}\n{issuer}"
        tpl = tpl.format(
            provider=card.name,
            owner=translit(
                self.generator.parse(
                    self.random_element(
                        [
                            "{{first_name_male}} {{last_name_male}}",
                            "{{first_name_female}} {{last_name_female}}",
                        ]
                    )
                )
            ),
            number=self.credit_card_number(card),
            expire_date=self.credit_card_expire(),
            security=card.security_code,
            security_nb=self.credit_card_security_code(card),
            issuer=self.generator.parse("{{bank}}"),
        )

        return self.generator.parse(tpl)
