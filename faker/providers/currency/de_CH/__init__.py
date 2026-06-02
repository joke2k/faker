from ..de import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # source: https://de.wikipedia.org/wiki/Schreibweise_von_Zahlen#Dezimaltrennzeichen_2
    price_formats = ["\N{FIGURE DASH}.##", "%.##", "%#.##", "%##.##", "% ###.##", "%# ###.##"]

    def pricetag(self):
        return "Fr.\N{NO-BREAK SPACE}" + self.numerify(self.random_element(self.price_formats))
