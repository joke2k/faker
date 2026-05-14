from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # source: https://ar.wikipedia.org/wiki/دينار_جزائري
    price_formats = ["#,##", "%#,##", "%##,##", "% ###,##", "%# ###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats)) + "\N{NO-BREAK SPACE}دج"
