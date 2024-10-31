from faker.providers import BaseProvider
from .constants import animals
from random import choice

class Provider(BaseProvider):

    def animal(self,animal_class=None):
        if animal_class:
            filtered_animals = [animal for animal in animals if animal['class'] == animal_class]
            animal = choice(filtered_animals)
        else:
            animal = choice(animals)
        return animal

    def animal_name(self):
        animal = self.animal()
        name = animal.get('common_name')
        return name

    def animal_name_scientific(self):
        animal = self.animal()
        scientific = animal.get('scientific_name')
        return scientific

    def bird(self):
        animal = self.animal(animal_class='birds')
        return animal

    def fish(self):
        animal = self.animal(animal_class='fish')
        return animal

    def mammal(self):
        animal = self.animal(animal_class='mammals')
        return animal

    def reptile(self):
        animal = self.animal(animal_class='reptiles')
        return animal

    def amphibian(self):
        animal = self.animal(animal_class='amphibians')
        return animal

