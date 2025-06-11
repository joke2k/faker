from collections import OrderedDict
from typing import Optional

from faker.providers.credit_card import Provider as CreditCardProvider
from faker.typing import CardType, CreditCard


class Provider(CreditCardProvider):
    """Custom credit card provider for the zh_CN locale."""

    prefix_unionpay = ["62"]  # UnionPay cards typically start with 62
    prefix_visa = ["4"]
    prefix_mastercard = ["51", "52", "53", "54", "55"]

    credit_card_types = OrderedDict(
        (
            ("unionpay", CreditCard("UnionPay", prefix_unionpay, security_code="CVN2")),
            ("visa", CreditCard("Visa", prefix_visa, security_code="CVV2")),
            ("mastercard", CreditCard("Mastercard", prefix_mastercard, security_code="CVC2")),
        )
    )

    def credit_card_full(self, card_type: Optional[CardType] = None) -> str:
        """Generate a full Chinese credit card with details."""
        card = self._credit_card_type(card_type)
        tpl = "{provider}\n{owner}\n{number} {expire_date}\n{security}: {security_nb}\n{issuer}"
        tpl = tpl.format(
            provider=card.name,
            owner=self.generator.parse("{{first_name}}{{last_name}}"),
            number=self.credit_card_number(card),
            expire_date=self.credit_card_expire(),
            security=card.security_code,
            security_nb=self.credit_card_security_code(card),
            issuer=self.generator.parse("{{bank}}"),
        )
        return self.generator.parse(tpl)
