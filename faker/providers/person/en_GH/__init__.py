from faker.providers.person import Provider as PersonProvider


class Provider(PersonProvider):
    """
    Implement person provider for ` en_GH` locale.
    """

    first_names_male = (
        "Kwame",
        "Kofi",
        "Yaw",
        "Fiifi",
        "Kojo",
        "Ekow",
        "Yoa",
        "Selasie",
    )

    first_names_female = (
        "Akosua",
        "Afia",
        "Abena",
        "Adwoa",
        "Ama",
        "Esi",
        "Yaa",
        "Akua",
        "Efua",
        "Aba",
    )

    last_names = (
        "Mensah",
        "Owusu",
        "Osei",
        "Boateng",
        "Agyeman",
        "Asante",
        "Acheampong",
        "Appiah",
        "Boadu",
        "Amponsah",
        "Darko",
        "Yeboah",
        "Nkrumah",
        "Amoah",
        "Gyasi",
        "Frimpong",
        "Adu",
        "Quartey",
    )

    formats_female = ("{{first_name_female}} {{last_name}}",)

    formats_male = ("{{first_name_male}} {{last_name}}",)

    formats = formats_male + formats_female
