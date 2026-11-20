from faker.providers.currency.en_AF import Provider as EnAfCurrencyProvider


class Provider(EnAfCurrencyProvider):
    """Currency provider for Pashto Afghanistan locale."""

    def pricetag(self) -> str:
        price = self.numerify(self.random_element(self.price_formats))
        return f"{price} ؋"
