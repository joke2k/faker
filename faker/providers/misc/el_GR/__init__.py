from .. import Provider as MiscProvider


class Provider(MiscProvider):
    """
    Provider for miscellaneous data for el_GR locale

    This class also houses all other provider methods that would have otherwise been weird to place in another provider.
    """

    gemstone_names = (
        "Αλεξανδρίτης",
        "Αμέθυστος",
        "Αχάτης ",
        "Διαμάντι",
        "Ρουμπίνι ",
        "Ζαφείρι ",
        "Σμαράγδι",
        "Τιρκουάζ",
        "Στρας",
        "Ρόδι",
        "Μαργαριτάρι",
        "Νεφρίτης",
        "Τοπάζι",
        "Τουρμαλίνη",
        "Κιτρίνη",
        "Κεχριμπάρι",
    )
    mountain_names = (
        "Αιγάλεω",	
        "Άθως",	
        "Αίνος",	
        "Αίτνα",	
        "Άλπεις",	
        "Αππένινα",
        "Αροανία",
        "Βεργίνα",
        "Γερανεία",	
        "Δίβρη",	
        "Δίρφυς",
        "Έλικον",
        "Ζήρια",	
        "Κυλλήνη",	
        "Λυκαβηττός",
        "Μαίναλον",
        "Μίνθη",	
        "Οινόη",	
        "Οίτη",	
        "Όλυμπος",	
        "Όλυμπος", 
        "Κίσσαβος",	
        "Παντωκράτορ",
        "Παρνασσός",	
        "Πάρνηθα",
        "Πεννίοες",	
        "Πεντέλη",	
        "Πήλιον",
        "Πίνδος",	
        "Σκόλλις",	
        "Ταΰγετος",	
        "Υμηττός",	
        "Φολόη",	
        "Χελμός",
    )    
    plant_names = (
        "Αγγούρια",
        "Αγκινάρες",
        "Αρακάς",
        "Καρότα",
        "Κολοκυθάκια - Κολοκύθια",
        "Κουκιά",
        "Κουνουπίδια",
        "Κρεμμύδια",
        "Λάχανα",
        "Μαρούλια",
        "Μελιτζάνες",
        "Μπάμιες",
        "Μπρόκολα",
        "Ντομάτες",
        "Παντζάρια",
        "Πατάτες",
        "Πιπεριές",
        "Πράσα",
        "Ραπανάκια",
        "Σκόρδα",
        "Σπανάκι",
        "Φασολάκια",
        "Αμαρύλλις",
        "Αστήρ",	
        "Καμπανούλα",	
        "Ανεμώνη",	
        "Περγαμότο",
        "Χρυσάνθεμο",	
        "Μαργαρίτα",
        "Τριφύλλι",	
        "Ασφόδελο",
        "Κρόκος",	
        "Γαρύφαλλο",	
        "Ηελοχάρης",
        "Δακτυλίς",
        "Υάκινθος",
        "Πρίνος",
        "Ίρις",
        "Κρίνος",
        "Πασχαλιά",
        "Λεβάντα",
        "Μαντζουράνα",	
        "Ορχιδέα",
        "Μιμόζα",	
        "Ηράνθεμο",	
        "Δενδρολίβανο",
        "Τριαντάφυλλο",
        "Πετούνια",	
        "Παιωνία",	
        "Φασκόμηλο",	
        "Θυμάρι",
        "Αντίρριο",	
        "Γαϊδουράγκαθο",
        "Ηλιοτρόπιο",	
        "Θηρανθεμίς",
        "Τουλίπα",
        "Ζίννια",	
        "Μπιγκόνια",        
    )
    space_object_names = (
        "Αφροδίτη",
        "Άρης",
        "Δίας",
        "Ερμής",
        "Κρόνος",
        "Ουρανός",
        "Ποσειδώνας",
        "Πλούτωνας",        
    )
    random_object_names = gemstone_names + mountain_names + plant_names + space_object_names

    def gemstone_name(self) -> str:
        return self.random_element(self.gemstone_names)

    def mountain_name(self) -> str:
        return self.random_element(self.mountain_names)

    def plant_name(self) -> str:
        return self.random_element(self.plant_names)

    def space_object_name(self) -> str:
        return self.random_element(self.space_object_names)

    def random_object_name(self) -> str:
        return self.random_element(self.random_object_names)
