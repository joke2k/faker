from ..de import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # source: https://de.wikipedia.org/wiki/Schreibweise_von_Zahlen#Dezimaltrennzeichen_2
    price_formats = ["\N{figure dash}.##", "%.##", "%#.##", "%##.##", "% ###.##", "%# ###.##"]

    def pricetag(self):
        return "Fr.\N{no-break space}" + self.numerify(self.random_element(self.price_formats))
