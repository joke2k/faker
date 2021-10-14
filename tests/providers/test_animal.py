from faker.providers.animal import Provider as AnimalProvider


class TestAnimalProvider:
    """Test animal provider methods"""

    def test_animal(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.animal_name() in AnimalProvider.animals

    def test_animal_scientific(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.animal_scientific_name() in AnimalProvider.animals_latin
