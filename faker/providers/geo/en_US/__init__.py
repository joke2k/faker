from .. import Provider as GeoProvider


class Provider(GeoProvider):
    
    nationalities = (
        "Afghan", "Albanian", "Algerian", "Argentine, Argentinian", "Australian", "Austrian", "Bangladeshi", "Belgian",
        "Bolivian", "Batswana", "Brazilian", "Bulgarian", "Cambodian", "Cameroonian", "Canadian", "Chilean", "Chinese",
        "Colombian", "Costa Rican", "Croatian", "Cuban", "Czech", "Danish", "Dominican", "Ecuadorian", "Egyptian",
        "Salvadorian", "English", "Estonian", "Ethiopian", "Fijian", "Finnish", "French", "German", "Ghanaian", "Greek",
        "Guatemalan", "Haitian", "Honduran", "Hungarian", "Icelandic", "Indian", "Indonesian", "Iranian", "Iraqi",
        "Irish", "Israeli", "Italian", "Jamaican", "Japanese", "Jordanian", "Kenyan", "Kuwaiti", "Lao", "Latvian",
        "Lebanese", "Libyan", "Lithuanian", "Malagasy", "Malaysian", "Malian", "Maltese", "Mexican", "Mongolian",
        "Moroccan", "Mozambican", "Namibian", "Nepalese", "Dutch", "New Zealand", "Nicaraguan", "Nigerian", "Norwegian",
        "Pakistani", "Panamanian", "Paraguayan", "Peruvian", "Philippine", "Polish", "Portuguese", "Romanian",
        "Russian", "Saudi", "Scottish", "Senegalese", "Serbian", "Singaporean", "Slovak", "South African", "Korean",
        "Spanish", "Sri Lankan", "Sudanese", "Swedish", "Swiss", "Syrian", "Taiwanese", "Tajikistani", "Thai", "Tongan",
        "Tunisian", "Turkish", "Ukrainian", "Emirati", "British", "American", "Uruguayan", "Venezuelan", "Vietnamese",
        "Welsh", "Zambian", "Zimbabwean",
    )
        
        
    def nationality(self):
        """
        :example 'American'
        """
        return self.random_element(self.nationalities)
