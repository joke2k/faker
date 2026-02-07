from ..es import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    """
    Currency provider for es_PE — localizes price formats.

    Source: Central Reserve Bank of Peru (BCRP) and local conventions.
    Accessed: 2026-02-07
    """

    price_formats = ["#,##", "%#,##", "%##,##", "%.###,##", "%#.###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats))
