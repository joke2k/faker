from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    ssn_formats: ElementsType[str] = ("###-##-####",)

    def ssn(self) -> str:
        return self.bothify(self.random_element(self.ssn_formats))
