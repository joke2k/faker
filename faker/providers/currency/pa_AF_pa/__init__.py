from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    """Currency provider for Pashto Afghanistan locale."""

    price_formats = ["###,###", "#,###,###", "##,###,###", "%,###,###,###"]

    def pricetag(self) -> str:
        price = self.numerify(self.random_element(self.price_formats))
        return f"{price} ؋"  # Afghan Afghani symbol after the number (common in RTL)