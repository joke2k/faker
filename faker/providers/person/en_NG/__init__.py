# Data sources:
# Yoruba names: https://en.wikipedia.org/wiki/List_of_Yoruba_given_names
# Igbo names: https://en.wikipedia.org/wiki/Igbo_names
# Hausa names: https://en.wikipedia.org/wiki/Hausa_names
# Nigerian English names: https://en.wikipedia.org/wiki/Nigerian_name
# Additional references:
# - Behind the Name (Igbo, Yoruba): https://www.behindthename.com
# - Journal of West African Languages (Hausa naming practices, 2016)

from faker.providers.person import Provider as PersonProvider


class Provider(PersonProvider):
    # Male first names
    first_names_male = [
        "John",
        "Emmanuel",
        "Peter",
        "Samuel",
        "David",
        "Michael",
        "Joseph",
        "Daniel",
        "James",
        "Paul",
        "Gabriel",
        "Joshua",
        "Philip",
        "Andrew",
        "Stephen",
        "Benjamin",
        "Mark",
        "Nathaniel",
        "Simon",
        "Cornelius",
    ]

    # Female first names
    first_names_female = [
        "Mary",
        "Grace",
        "Joy",
        "Patience",
        "Elizabeth",
        "Victoria",
        "Sarah",
        "Deborah",
        "Esther",
        "Blessing",
        "Charity",
        "Hope",
        "Gloria",
        "Agnes",
        "Peace",
        "Comfort",
        "Juliet",
        "Ruth",
        "Angela",
        "Faith",
    ]

    # Combined list
    first_names = first_names_male + first_names_female

    # Prefixes
    prefixes_male = ["Mr.", "Chief", "Dr.", "Prof.", "Engr."]
    prefixes_female = ["Mrs.", "Miss", "Dr.", "Prof.", "Lady"]

    prefixes = prefixes_male + prefixes_female

    # Last names
    last_names = [
        "Okonkwo",
        "Adeyemi",
        "Olawale",
        "Chukwu",
        "Eze",
        "Obi",
        "Abiola",
        "Okafor",
        "Balogun",
        "Uche",
        "Ogunleye",
        "Nnamani",
        "Adetokunbo",
        "Ojo",
        "Ekwueme",
        "Oshodi",
        "Ibrahim",
        "Akinwale",
        "Obasanjo",
        "Oyekan",
    ]
