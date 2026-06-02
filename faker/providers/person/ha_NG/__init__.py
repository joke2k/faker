# Data sources:
# Hausa names: https://en.wikipedia.org/wiki/Hausa_names
# Additional references:
# - Journal of West African Languages (Hausa naming practices, 2016)

from faker.providers.person import Provider as PersonProvider


class Provider(PersonProvider):
    # Male first names
    first_names_male = [
        "Abdullahi",
        "Musa",
        "Sani",
        "Ibrahim",
        "Aliyu",
        "Bello",
        "Kabiru",
        "Shehu",
        "Yusuf",
        "Haruna",
        "Ismail",
        "Usman",
        "Nasiru",
        "Mahmud",
        "Umar",
        "Habibu",
        "Danjuma",
        "Tanimu",
        "Shamsuddeen",
        "Ahmad",
    ]

    # Female first names
    first_names_female = [
        "Zainab",
        "Aisha",
        "Hauwa",
        "Fatima",
        "Hadiza",
        "Maryam",
        "Sa’adatu",
        "Jamila",
        "Rabi",
        "Khadija",
        "Bilkisu",
        "Asma’u",
        "Halima",
        "Safiya",
        "Sumayya",
        "Habiba",
        "Ruqayya",
        "Hafsat",
        "Aminatu",
        "Gambo",
    ]

    # Combined list
    first_names = first_names_male + first_names_female

    # Prefixes
    prefixes_male = ["Alhaji", "Mallam", "Dr.", "Prof."]
    prefixes_female = ["Hajiya", "Mrs.", "Dr.", "Prof."]

    prefixes = prefixes_male + prefixes_female

    # Last names
    last_names = [
        "Abubakar",
        "Mohammed",
        "Yahaya",
        "Garba",
        "Danjuma",
        "Buhari",
        "Zubairu",
        "Jibril",
        "Suleiman",
        "Lawal",
        "Tukur",
        "Ali",
        "Shehu",
        "Mustapha",
        "Kabir",
        "Idris",
        "Sa’idu",
        "Bappa",
        "Yusuf",
        "Isah",
    ]
