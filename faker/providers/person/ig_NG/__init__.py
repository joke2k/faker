# Data sources:
# Igbo names: https://en.wikipedia.org/wiki/Igbo_names
# Additional references:
# - Behind the Name (Igbo, Yoruba): https://www.behindthename.com
# - Journal of West African Languages (Hausa naming practices, 2016)
from faker.providers.person import Provider as PersonProvider


class Provider(PersonProvider):
    # Male first names
    first_names_male = [
        "Chinedu",
        "Obinna",
        "Ifeanyi",
        "Emeka",
        "Uche",
        "Chukwudi",
        "Nnamdi",
        "Ikenna",
        "Ekene",
        "Chibuzo",
        "Ebuka",
        "Nonso",
        "Chukwuemeka",
        "Somtochukwu",
        "Uchenna",
        "Ifechukwu",
        "Chigozie",
        "Okechukwu",
        "Kelechi",
        "Chijioke",
    ]

    # Female first names
    first_names_female = [
        "Adaeze",
        "Chiamaka",
        "Oluchi",
        "Ngozi",
        "Amarachi",
        "Ifunanya",
        "Chinelo",
        "Ogechi",
        "Nneka",
        "Obianuju",
        "Ujunwa",
        "Ifeoma",
        "Chidimma",
        "Nkiruka",
        "Onyinye",
        "Chizoba",
        "Chinyere",
        "Kosisochukwu",
        "Ozioma",
        "Somadina",
    ]

    # Combined list
    first_names = first_names_male + first_names_female

    # Prefixes
    prefixes_male = ["Mr.", "Chief", "Dr.", "Engr.", "Prof."]
    prefixes_female = ["Mrs.", "Miss", "Dr.", "Prof.", "Lady"]

    prefixes = prefixes_male + prefixes_female

    # Last names
    last_names = [
        "Okafor",
        "Eze",
        "Obi",
        "Nwosu",
        "Okeke",
        "Nwachukwu",
        "Onoh",
        "Ogbuehi",
        "Iwu",
        "Chukwu",
        "Onwuka",
        "Anyanwu",
        "Udeh",
        "Ihejirika",
        "Madu",
        "Njoku",
        "Ezeugo",
        "Ojukwu",
        "Iroha",
        "Okoro",
    ]
