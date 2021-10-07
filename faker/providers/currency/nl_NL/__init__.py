from faker.providers.currency import Provider as CurrencyProvider


class Provider(CurrencyProvider):

    price_formats = ["#,##", "%#,##", "%##,##", "%.###,##", "%#.###,##"]

    def pricetag(self):
        return "\N{euro sign}" + self.numerify(self.random_element(self.price_formats))
