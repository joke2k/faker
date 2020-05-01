import re
import unittest

from faker import Faker
from faker.providers.barcode.en_US import Provider as EnUSProvider
from faker.providers.barcode.en_CA import Provider as EnCAProvider
from faker.providers.barcode.fr_CA import Provider as FrCAProvider
from faker.providers.barcode.ja_JP import Provider as JaJPProvider


class TestBaseProvider(unittest.TestCase):
    """ Tests barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.fake = Faker('')
        Faker.seed(0)

    def test_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.ean(8)
            ean13 = self.fake.ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean_bad_length(self):
        bad_lengths = [l for l in range(1, 15) if l not in (8, 13)]
        for length in bad_lengths:
            with self.assertRaises(AssertionError):
                self.fake.ean(length)

    def test_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.ean8()
            assert self.ean8_pattern.match(ean8)

            # Included check digit must be correct
            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

    def test_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.ean13()
            assert self.ean13_pattern.match(ean13)

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0


class TestEnUS(unittest.TestCase):
    """ Tests en_US barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.upc_a_pattern = re.compile(r'^\d{12}$')
        self.upc_e_pattern = re.compile(r'^[01]\d{7}$')
        self.fake = Faker('en_US')
        Faker.seed(0)

    def test_ean13_no_leading_zero(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.ean13(leading_zero=False)
            assert self.ean13_pattern.match(ean13)
            assert ean13[0] != '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_leading_zero(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.ean13(leading_zero=True)
            assert self.ean13_pattern.match(ean13)
            assert ean13[0] == '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_localized_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean(8)
            ean13 = self.fake.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in EnUSProvider.local_prefixes
            )
            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in EnUSProvider.local_prefixes
            )

    def test_localized_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean8()
            assert self.ean8_pattern.match(ean8)

            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in EnUSProvider.local_prefixes
            )

    def test_localized_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.localized_ean13()
            assert self.ean13_pattern.match(ean13)

            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in EnUSProvider.local_prefixes
            )

    def test_upc_a(self):
        for _ in range(self.num_sample_runs):
            upc_a = self.fake.upc_a()
            assert self.upc_a_pattern.match(upc_a)

            # Included check digit must be correct
            upc_a_digits = [int(digit) for digit in upc_a]
            assert (sum(upc_a_digits) + 2 * sum(upc_a_digits[::2])) % 10 == 0

    def test_upc_ae_mode(self):
        for _ in range(self.num_sample_runs):
            upc_ae = self.fake.upc_a(upc_ae_mode=True)
            assert self.upc_a_pattern.match(upc_ae)

            # Included check digit must be correct
            upc_ae_digits = [int(digit) for digit in upc_ae]
            assert (sum(upc_ae_digits) + 2 * sum(upc_ae_digits[::2])) % 10 == 0

    def test_upc_e_explicit_number_system(self):
        for _ in range(self.num_sample_runs):
            upc_e_0 = self.fake.upc_e(number_system_digit=0)
            upc_e_1 = self.fake.upc_e(number_system_digit=1)
            assert self.upc_e_pattern.match(upc_e_0)
            assert self.upc_e_pattern.match(upc_e_1)
            assert upc_e_0[0] == '0'
            assert upc_e_1[0] == '1'

    def test_upc_e_safe_mode(self):
        # For this test, we explicitly specify a base and a number system digit
        # so we do not have to wait for RNG to produce the right combinations.
        for _ in range(100):
            # Be aware that there are other unsafe combinations
            unsafe_base = '{:02}000{}'.format(self.fake.random_int(0, 99), self.fake.random_int(3, 4))
            safe_base = unsafe_base[:2] + '0000'
            number_system_digit = self.fake.random_int(0, 1)

            # Safe mode will create a UPC-E barcode with the safe base
            # even if an unsafe base was supplied
            upc_e_safe = self.fake.upc_e(base=unsafe_base,
                                         number_system_digit=number_system_digit,
                                         safe_mode=True)
            assert upc_e_safe[1:-1] == safe_base
            assert upc_e_safe[1:-1] != unsafe_base

            # Unsafe mode will force create a UPC-E barcode with unsafe base
            upc_e_unsafe = self.fake.upc_e(base=unsafe_base,
                                           number_system_digit=number_system_digit,
                                           safe_mode=False)
            assert upc_e_unsafe[1:-1] != safe_base
            assert upc_e_unsafe[1:-1] == unsafe_base

            # What will be the same are their number system and check digits
            assert upc_e_safe[0] == upc_e_unsafe[0]
            assert upc_e_safe[-1] == upc_e_unsafe[-1]

    def test_upc_a2e_bad_values(self):
        provider = EnUSProvider(self.fake)

        # Invalid data type
        with self.assertRaises(TypeError):
            provider._convert_upc_a2e(12345678)

        # Invalid string
        with self.assertRaises(ValueError):
            provider._convert_upc_a2e('abcdef')

    def test_upc_a2e2a(self):
        provider = EnUSProvider(self.fake)

        for _ in range(self.num_sample_runs):
            upc_a = self.fake.upc_a(upc_ae_mode=True)
            assert self.upc_a_pattern.match(upc_a)

            # Convert UPC-A to UPC-E
            upc_e = provider._convert_upc_a2e(upc_a)

            # Number system and check digits must be the same
            assert int(upc_a[0]) == int(upc_e[0])
            assert int(upc_a[-1]) == int(upc_e[-1])

            # Create a new UPC-A barcode based on the UPC-E barcode
            new_upc_a = self.fake.upc_a(upc_ae_mode=True,
                                        base=upc_e[1:-1],
                                        number_system_digit=int(upc_e[0]))

            # New UPC-A barcode must be the same as the original
            assert upc_a == new_upc_a

    def test_upc_e2a2e(self):
        provider = EnUSProvider(self.fake)

        for _ in range(self.num_sample_runs):
            upc_e = self.fake.upc_e()
            assert self.upc_e_pattern.match(upc_e)

            # Create a new UPC-A barcode based on the UPC-E barcode
            upc_a = self.fake.upc_a(upc_ae_mode=True,
                                    base=upc_e[1:-1],
                                    number_system_digit=int(upc_e[0]))

            # Number system and check digits must be the same
            assert int(upc_a[0]) == int(upc_e[0])
            assert int(upc_a[-1]) == int(upc_e[-1])

            # Convert UPC-A to UPC-E
            new_upc_e = provider._convert_upc_a2e(upc_a)

            # New UPC-E barcode must be the same as the original
            assert new_upc_e == upc_e


class TestEnCA(unittest.TestCase):
    """ Tests en_CA barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.fake = Faker('en_CA')
        Faker.seed(0)

    def test_localized_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean(8)
            ean13 = self.fake.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in EnCAProvider.local_prefixes
            )
            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in EnCAProvider.local_prefixes
            )

    def test_localized_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean8()
            assert self.ean8_pattern.match(ean8)

            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in EnCAProvider.local_prefixes
            )

    def test_localized_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.localized_ean13()
            assert self.ean13_pattern.match(ean13)

            ean13_digits = [int(digit) for digit in ean13]
            if not ((sum(ean13_digits) + 2 * sum(ean13_digits[::2])) % 10 == 0):
                print(ean13_digits)
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in EnCAProvider.local_prefixes
            )


class TestFrCA(unittest.TestCase):
    """ Tests fr_CA barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.fake = Faker('fr_CA')
        Faker.seed(0)

    def test_localized_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean(8)
            ean13 = self.fake.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in FrCAProvider.local_prefixes
            )
            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in FrCAProvider.local_prefixes
            )

    def test_localized_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean8()
            assert self.ean8_pattern.match(ean8)

            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in FrCAProvider.local_prefixes
            )

    def test_localized_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.localized_ean13()
            assert self.ean13_pattern.match(ean13)

            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in FrCAProvider.local_prefixes
            )


class TestJaCA(unittest.TestCase):
    """ Tests ja_JP barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.fake = Faker('ja_JP')
        Faker.seed(0)

    def test_localized_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean(8)
            ean13 = self.fake.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in JaJPProvider.local_prefixes
            )
            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in JaJPProvider.local_prefixes
            )

    def test_localized_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.fake.localized_ean8()
            assert self.ean8_pattern.match(ean8)

            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean8_digits, prefix))
                for prefix in JaJPProvider.local_prefixes
            )

    def test_localized_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.fake.localized_ean13()
            assert self.ean13_pattern.match(ean13)

            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            assert any(
                all(a == b for a, b in zip(ean13_digits, prefix))
                for prefix in JaJPProvider.local_prefixes
            )
