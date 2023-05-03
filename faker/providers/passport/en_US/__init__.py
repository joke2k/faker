from .. import ElementsType
from .. import Provider as PassportProvider


class Provider(PassportProvider):
    """Implement passport provider for ``en_US`` locale.

    Sources:

    - https://en.wikipedia.org/wiki/United_States_license_plate_designs_and_serial_formats
    """
    
    #given_name: ElementsType[str] = ("{{first_name}} ")
    #surname:  ElementsType[str] = ("{{last_name}} ")

    
    def nationality(self)-> str:
        return "USA"
    
    


    passport_number_formats = (
        # NGP
        "?########",
        #Pre-NGP
        "#########",
    )

    