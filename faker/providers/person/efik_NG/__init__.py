# Data sources:
# Efik Names: https://efikeburutu.org/efik%20naming%20system.html
# Additional references:
# - https://en.wikipedia.org/wiki/Efik_name
# Compiled by: https://x.com/mb_awak
# programming help: https://github.com/ifeoluwaoladeji

from faker.providers.person import Provider as PersonProvider

class Provider(PersonProvider):
    # Male first names
    first_names_male = [
        "Etim", "Antigha", "Bassey", "Nyong", "Nkese", "Edet",
        "Odionka", "Efefiom", "Andem", "Henshaw", "Ndiyo", "Duke",
        "Orok", "Mesembe", "Namondo", "Efiwat", "Asikpo", "Archibong",
        "Ekpe",
    ]

    # Female first names
    first_names_female = [
        "Okoho", "Edemanwan", "Ansa", "Asari", "Efioanwan", "Ekanem",
        "Orokanwan", "Eyoanwan", "Itamanwan", "Efiokanwan", "Eke", "Atim",
        "Inyang", "Nsikak", "Ekerette", "Ekanem", "Udobong", "Ankwa", "Minika"
    ]

    # Combined list
    first_names = first_names_male + first_names_female

    # Prefixes
    prefixes_male = ["Mr", "Dr.", "Prof."]
    prefixes_female = ["Miss", "Mrs.", "Dr.", "Prof."]

    prefixes = prefixes_male + prefixes_female

    # Last names
    last_names = [
        "Oku", "Aye", "Ewa", "Ibok", "Efiok",
        "Itam", "Essien", "Eyonsa", "Okokon", "Cobham", "Offiong",
        "Ekeng", "Efa", "Otu", "Itam", "Orok", "Eyo",
        "Nsa", "Ita", "Hogan", "Esu", "Ekpenyong", "Otu",
        "Etetim", "Inyang", "Effiong",
    ]

