from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "055# ### ###",
        "066# ### ###",
        "077# ### ###",
    )
