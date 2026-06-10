from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """ Afghan mobile and phone number provider """

    formats = (
        # Mobile numbers with Afghan country code +93
        "+93 70# ### ###",
        "070# ### ###",
        "+93 71# ### ###",
        "071# ### ###",
        "+93 72# ### ###",
        "072# ### ###",
        "+93 73# ### ###",
        "073# ### ###",
        "+93 74# ### ###",
        "074# ### ###",
        "+93 75# ### ###",
        "075# ### ###",
        "+93 76# ### ###",
        "076# ### ###",
        "+93 77# ### ###",
        "077# ### ###",
        "+93 78# ### ###",
        "078# ### ###",
        "+93 79# ### ###",
        "079# ### ###",
        # Landlines (example for Kabul and other provinces)
        "+93 20 ### ###",
        "020 ### ###",
        "+93 40 ### ###",
        "040 ### ###",
        "+93 50 ### ###",
        "050 ### ###",
    )

    def mobile_number(self):
        pattern = self.random_element(self.formats)
        return self.numerify(pattern)
