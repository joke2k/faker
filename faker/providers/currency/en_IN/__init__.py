from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    """Implement currency provider for ``en_IN`` locale.

    Amounts use the Indian numbering system, which groups digits after the
    first thousand in twos (lakh and crore), e.g. ₹12,34,567.89.
    """

    price_formats = [
        "#.##",
        "%#.##",
        "%##.##",
        "%,###.##",
        "%#,###.##",
        "%,##,###.##",
        "%#,##,###.##",
    ]

    def pricetag(self) -> str:
        return "\N{INDIAN RUPEE SIGN}" + self.numerify(self.random_element(self.price_formats))
