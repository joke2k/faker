class TestFoodProvider:
    """Test food provider methods."""

    num_samples = 100

    def test_dish(self, faker, num_samples):
        for _ in range(num_samples):
            dish = faker.dish()
            assert isinstance(dish, str)
            assert len(dish) > 0

    def test_dish_in_known_list(self, faker):
        from faker.providers.food import Provider as FoodProvider

        for _ in range(50):
            assert faker.dish() in FoodProvider.dishes

    def test_ingredient(self, faker, num_samples):
        for _ in range(num_samples):
            ingredient = faker.ingredient()
            assert isinstance(ingredient, str)
            assert len(ingredient) > 0

    def test_ingredient_in_known_list(self, faker):
        from faker.providers.food import Provider as FoodProvider

        for _ in range(50):
            assert faker.ingredient() in FoodProvider.ingredients

    def test_spice(self, faker, num_samples):
        for _ in range(num_samples):
            spice = faker.spice()
            assert isinstance(spice, str)
            assert len(spice) > 0

    def test_spice_in_known_list(self, faker):
        from faker.providers.food import Provider as FoodProvider

        for _ in range(50):
            assert faker.spice() in FoodProvider.spices

    def test_fruit(self, faker, num_samples):
        for _ in range(num_samples):
            fruit = faker.fruit()
            assert isinstance(fruit, str)
            assert len(fruit) > 0

    def test_fruit_in_known_list(self, faker):
        from faker.providers.food import Provider as FoodProvider

        for _ in range(50):
            assert faker.fruit() in FoodProvider.fruits

    def test_vegetable(self, faker, num_samples):
        for _ in range(num_samples):
            vegetable = faker.vegetable()
            assert isinstance(vegetable, str)
            assert len(vegetable) > 0

    def test_vegetable_in_known_list(self, faker):
        from faker.providers.food import Provider as FoodProvider

        for _ in range(50):
            assert faker.vegetable() in FoodProvider.vegetables
