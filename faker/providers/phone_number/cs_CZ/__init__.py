from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):

    # Phone numbers
    # https://cs.wikipedia.org/wiki/Telefonn%C3%AD_%C4%8D%C3%ADslo

    formats = (
        # 601-608
        "601 ### ###",
        "602 ### ###",
        "603 ### ###",
        "604 ### ###",
        "605 ### ###",
        "606 ### ###",
        "607 ### ###",
        "608 ### ###",
        # 702-705
        "702 ### ###",
        "703 ### ###",
        "704 ### ###",
        "705 ### ###",
        # 720-739
        "72# ### ###",
        "73# ### ###",
        # 770-779
        "77# ### ###",
        # 790-799
        "79# ### ###",
    )
