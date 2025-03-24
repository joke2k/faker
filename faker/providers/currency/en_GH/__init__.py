from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    price_formats = ["#.##", "%#.##", "%##.##", "%,###.##", "%#,###.##"]

    def pricetag(self) -> str:
        return "GH₵\N{NO-BREAK SPACE}" + self.numerify(self.random_element(self.price_formats))
