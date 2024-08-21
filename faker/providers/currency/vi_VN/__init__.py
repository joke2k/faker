from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # Source: https://vi.wikipedia.org/wiki/%C4%90%E1%BB%93ng_(%C4%91%C6%A1n_v%E1%BB%8B_ti%E1%BB%81n_t%E1%BB%87)#Ti%E1%BB%81n_gi%E1%BA%A5y_-_Ti%E1%BB%81n_polymer  # NOQA
    price_formats = ["#.##", "%#.##", "%##.##", "%,###.##", "%#,###.##"]

    def pricetag(self) -> str:
        return "₫" + self.numerify(self.random_element(self.price_formats))
