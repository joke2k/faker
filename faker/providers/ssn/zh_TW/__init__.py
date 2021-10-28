from .. import Provider as SsnProvider


class Provider(SsnProvider):
    ssn_formats = ("?#########",)

    def ssn(self) -> str:
        return self.bothify(self.random_element(self.ssn_formats)).upper()
