from .. import BaseProvider, ElementsType


class Provider(BaseProvider):
    """Implement default food provider for Faker.

    Sources:
    - Dish names: https://en.wikipedia.org/wiki/List_of_dishes (checked 2025-01-01)
    - Ingredients: https://en.wikipedia.org/wiki/List_of_culinary_fruits,
      https://en.wikipedia.org/wiki/List_of_vegetables (checked 2025-01-01)
    - Spices: https://en.wikipedia.org/wiki/List_of_culinary_herbs_and_spices (checked 2025-01-01)
    """

    dishes: ElementsType[str] = (
        "Aloo Gobi",
        "Baba Ganoush",
        "Baingan Bharta",
        "Black Bean Soup",
        "Black Bean Tacos",
        "Buddha Bowl",
        "Chana Masala",
        "Chickpea Shawarma",
        "Congee with Shiitake",
        "Dal Tadka",
        "Falafel",
        "French Onion Soup",
        "Ful Medames",
        "Gazpacho",
        "Harira",
        "Hummus",
        "Injera with Misir Wot",
        "Jackfruit Tacos",
        "Jollof Rice",
        "Khichdi",
        "Kimchi Fried Rice",
        "Lentil Bolognese",
        "Lentil Soup",
        "Miso Ramen",
        "Mujaddara",
        "Mushroom Risotto",
        "Palak Tofu",
        "Pasta e Fagioli",
        "Pasta Primavera",
        "Pesto Pasta",
        "Ratatouille",
        "Red Lentil Dal",
        "Ribollita",
        "Roasted Cauliflower Tagine",
        "Smoky Black Bean Stew",
        "Tamarind Chickpeas",
        "Tofu Larb",
        "Tofu Tikka Masala",
        "Tom Yum",
        "Truffle Pasta",
        "Udon Noodle Soup",
        "Ugali with Sukuma Wiki",
        "Vegetable Bibimbap",
        "Vegetable Curry",
        "Vegetable Pho",
        "White Bean Stew",
        "Yellow Split Pea Soup",
    )

    ingredients: ElementsType[str] = (
        "Arborio Rice",
        "Avocado",
        "Baby Spinach",
        "Black Beans",
        "Brown Lentils",
        "Button Mushrooms",
        "Cannellini Beans",
        "Cashews",
        "Chickpeas",
        "Coconut Milk",
        "Edamame",
        "Firm Tofu",
        "Fresh Basil",
        "Fresh Ginger",
        "Garlic",
        "Green Onions",
        "Jasmine Rice",
        "Kalamata Olives",
        "Kale",
        "Kidney Beans",
        "Leeks",
        "Nutritional Yeast",
        "Pinto Beans",
        "Portobello Mushrooms",
        "Pumpkin",
        "Quinoa",
        "Red Bell Pepper",
        "Red Kidney Beans",
        "Roasted Chickpeas",
        "Roma Tomatoes",
        "Seitan",
        "Shiitake Mushrooms",
        "Silken Tofu",
        "Smoked Paprika",
        "Soba Noodles",
        "Sun-Dried Tomatoes",
        "Sweet Potato",
        "Tahini",
        "Tempeh",
        "Udon Noodles",
        "Walnuts",
        "White Miso",
        "Whole Wheat Pasta",
        "Yellow Onion",
        "Zucchini",
    )

    spices: ElementsType[str] = (
        "Allspice",
        "Anise",
        "Black Pepper",
        "Cardamom",
        "Cayenne",
        "Chili Flakes",
        "Cilantro",
        "Cinnamon",
        "Cloves",
        "Coriander",
        "Cumin",
        "Dill",
        "Fennel Seeds",
        "Fenugreek",
        "Garam Masala",
        "Ground Ginger",
        "Mustard Seeds",
        "Nutmeg",
        "Oregano",
        "Paprika",
        "Rosemary",
        "Saffron",
        "Sumac",
        "Thyme",
        "Turmeric",
        "Za'atar",
    )

    fruits: ElementsType[str] = (
        "Apricot",
        "Avocado",
        "Banana",
        "Blackberry",
        "Blood Orange",
        "Blueberry",
        "Cherry",
        "Clementine",
        "Coconut",
        "Dragon Fruit",
        "Durian",
        "Fig",
        "Grapefruit",
        "Guava",
        "Jackfruit",
        "Kiwi",
        "Lemon",
        "Lime",
        "Lychee",
        "Mango",
        "Melon",
        "Nectarine",
        "Papaya",
        "Passion Fruit",
        "Peach",
        "Pear",
        "Pineapple",
        "Plum",
        "Pomegranate",
        "Pomelo",
        "Raspberry",
        "Starfruit",
        "Strawberry",
        "Tamarind",
        "Watermelon",
    )

    vegetables: ElementsType[str] = (
        "Artichoke",
        "Arugula",
        "Asparagus",
        "Beet",
        "Bell Pepper",
        "Bok Choy",
        "Broccoli",
        "Brussels Sprouts",
        "Butternut Squash",
        "Cabbage",
        "Carrot",
        "Cauliflower",
        "Celeriac",
        "Celery",
        "Chard",
        "Corn",
        "Cucumber",
        "Daikon",
        "Eggplant",
        "Endive",
        "Fennel",
        "Garlic",
        "Green Beans",
        "Jalapeño",
        "Kale",
        "Kohlrabi",
        "Leek",
        "Lettuce",
        "Mushroom",
        "Okra",
        "Onion",
        "Parsnip",
        "Peas",
        "Potato",
        "Pumpkin",
        "Radish",
        "Shallot",
        "Spinach",
        "Sweet Potato",
        "Tomato",
        "Turnip",
        "Watercress",
        "Yam",
        "Zucchini",
    )

    def dish(self) -> str:
        """Generate a random dish name.

        :return: A dish name string.
        :rtype: str
        :sample:
        """
        return self.random_element(self.dishes)

    def ingredient(self) -> str:
        """Generate a random cooking ingredient.

        :return: An ingredient string.
        :rtype: str
        :sample:
        """
        return self.random_element(self.ingredients)

    def spice(self) -> str:
        """Generate a random spice or herb.

        :return: A spice or herb string.
        :rtype: str
        :sample:
        """
        return self.random_element(self.spices)

    def fruit(self) -> str:
        """Generate a random fruit name.

        :return: A fruit name string.
        :rtype: str
        :sample:
        """
        return self.random_element(self.fruits)

    def vegetable(self) -> str:
        """Generate a random vegetable name.

        :return: A vegetable name string.
        :rtype: str
        :sample:
        """
        return self.random_element(self.vegetables)
