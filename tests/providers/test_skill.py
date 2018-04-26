import unittest
from faker.providers.skill.en_US import Provider as EnUsProvider
from faker import Faker


class TestSkill(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('en_US')

    def test_skill_provider_grabs_soft_skill(self):
        skill = self.factory.soft_skill()

        assert skill in EnUsProvider.soft_skills

    def test_skill_provider_grabs_hard_skill(self):
        skill = self.factory.hard_skill()

        assert skill in EnUsProvider.hard_skills

