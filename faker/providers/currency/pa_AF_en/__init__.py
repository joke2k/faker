from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    """Currency provider for English Afghanistan locale (en_AF)."""

    price_formats = ["###,###", "#,###,###", "##,###,###", "%,###,###,###"]

    def pricetag(self) -> str:
        price = self.numerify(self.random_element(self.price_formats))
        return f"AFN {price}"  # Common English-style format used in Afghanistan