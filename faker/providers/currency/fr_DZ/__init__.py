from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # source: https://fr.wikipedia.org/wiki/Dinar_alg%C3%A9rien
    price_formats = ["#,##", "%#,##", "%##,##", "% ###,##", "%# ###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats)) + "\N{NO-BREAK SPACE}DA"
