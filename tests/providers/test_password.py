import unittest
from faker import Faker
import string
class TestPasswordProvider(unittest.TestCase):
    """Test password generation provider"""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider("path.to.your.module.Provider")  # Ex: 'faker_password.provider.Provider'
        Faker.seed(0)

    def test_generate_password_size(self):
        for size in [8, 12, 20, 32]:
            password = self.fake.generate_password(size=size)
            self.assertEqual(len(password), size, f"Password length should be {size}")

    
    def test_password_has_uppercase(self):
        password = self.fake.generate_password(size=16)
        has_upper = any(char.isupper() for char in password)
        self.assertTrue(has_upper, "Password should contain at least one uppercase letter")
    

    def test_password_has_upper_and_lowercase(self):
        password = self.fake.generate_password(size=16)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        self.assertTrue(has_upper, "Password should contain at least one uppercase letter")
        self.assertTrue(has_lower, "Password should contain at least one lowercase letter")
    
    def test_password_has_symbol(self):
        password = self.fake.generate_password(size=16)
        has_symbol = any(char in string.punctuation for char in password)
        self.assertTrue(has_symbol, "Password should contain at least one symbol")


    def test_password_has_number(self):
        password = self.fake.generate_password(size=16)
        has_digit = any(char in string.digits for char in password)
        self.assertTrue(has_digit, "Password should contain at least one number")