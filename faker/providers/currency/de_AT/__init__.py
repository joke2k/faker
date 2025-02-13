from ..de import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    price_formats = ["#,##", "%#,##", "%##,##", "%.###,##", "%#.###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats)) + "\N{NO-BREAK SPACE}\N{EURO SIGN}"
