from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    price_formats = ["#.##", "%#.##", "%##.##", "%,###.##"]

    def pricetag(self) -> str:
        return "\N{NAIRA SIGN}" + "\N{NO-BREAK SPACE}" + self.numerify(self.random_element(self.price_formats))
