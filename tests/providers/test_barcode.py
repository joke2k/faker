import re

import pytest


class TestBarcodeProvider:
    """Test barcode provider methods"""
    num_samples = 1000
    ean8_pattern = re.compile(r'\d{8}')
    ean13_pattern = re.compile(r'\d{13}')

    def test_ean(self, faker, num_samples):
        for _ in range(num_samples):
            ean8 = faker.ean(8)
            ean13 = faker.ean(13)
            assert self.ean8_pattern.fullmatch(ean8)
            assert self.ean13_pattern.fullmatch(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean_bad_length(self, faker):
        bad_lengths = [size for size in range(1, 15) if size not in (8, 13)]
        for length in bad_lengths:
            with pytest.raises(AssertionError):
                faker.ean(length)

    def test_ean8(self, faker, num_samples):
        for _ in range(num_samples):
            ean8 = faker.ean8()
            assert self.ean8_pattern.fullmatch(ean8)

            # Included check digit must be correct
            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

    def test_ean13(self, faker, num_samples):
        for _ in range(num_samples):
            ean13 = faker.ean13()
            assert self.ean13_pattern.fullmatch(ean13)

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_no_leading_zero(self, faker, num_samples):
        for _ in range(num_samples):
            ean13 = faker.ean13(leading_zero=False)
            assert self.ean13_pattern.fullmatch(ean13)
            assert ean13[0] != '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_leading_zero(self, faker, num_samples):
        for _ in range(num_samples):
            ean13 = faker.ean13(leading_zero=True)
            assert self.ean13_pattern.fullmatch(ean13)
            assert ean13[0] == '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0


@pytest.fixture(scope='class')
def provider_class(request):
    if hasattr(request.cls, 'get_provider_class') and callable(request.cls.get_provider_class):
        _provider_class = request.cls.get_provider_class()
        if isinstance(_provider_class, type):
            return _provider_class
    raise NotImplementedError(f'Using the provider_class requires {request.cls.__name__}.get_provider_class() '
                              'to be present, which has to return the Provider class it uses.')


@pytest.fixture()
def provider(faker, provider_class):
    return provider_class(faker)


class _LocaleCommonMixin:
    ean8_pattern = re.compile(r'\d{8}')
    ean13_pattern = re.compile(r'\d{13}')

    @staticmethod
    def assert_prefix(barcode_digits, prefixes):
        for prefix in prefixes:
            if all(a == b for a, b in zip(barcode_digits, map(int, prefix))):
                return
        str_barc = ''.join(str(x) for x in barcode_digits)
        str_pref = ', '.join(map(lambda _prefix: ''.join(str(x) for x in _prefix)), prefixes)
        raise AssertionError(f"{str_barc} doesn't match any of the prefixes: {str_pref}")

    def test_localized_ean(self, faker, num_samples, provider):
        for _ in range(num_samples):
            ean8 = faker.localized_ean(8)
            ean13 = faker.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            self.assert_prefix(ean8_digits, provider.local_prefixes)
            self.assert_prefix(ean13_digits, provider.local_prefixes)

    def test_localized_ean8(self, faker, num_samples, provider):
        for _ in range(num_samples):
            ean8 = faker.localized_ean8()
            assert self.ean8_pattern.match(ean8)

            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

            self.assert_prefix(ean8_digits, provider.local_prefixes)

    def test_localized_ean13(self, faker, num_samples, provider):
        for _ in range(num_samples):
            ean13 = faker.localized_ean13()
            assert self.ean13_pattern.match(ean13)

            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            self.assert_prefix(ean13_digits, provider.local_prefixes)


class _LocaleNorthAmericaMixin(_LocaleCommonMixin):
    upc_a_pattern = re.compile(r'\d{12}')
    upc_e_pattern = re.compile(r'[01]\d{7}')

    def test_upc_a(self, faker, num_samples):
        for _ in range(num_samples):
            upc_a = faker.upc_a()
            assert self.upc_a_pattern.fullmatch(upc_a)

            # Included check digit must be correct
            upc_a_digits = [int(digit) for digit in upc_a]
            assert (sum(upc_a_digits) + 2 * sum(upc_a_digits[::2])) % 10 == 0

    def test_upc_ae_mode(self, faker, num_samples):
        for _ in range(num_samples):
            upc_ae = faker.upc_a(upc_ae_mode=True)
            assert self.upc_a_pattern.fullmatch(upc_ae)

            # Included check digit must be correct
            upc_ae_digits = [int(digit) for digit in upc_ae]
            assert (sum(upc_ae_digits) + 2 * sum(upc_ae_digits[::2])) % 10 == 0

    def test_upc_e_explicit_number_system(self, faker, num_samples):
        for _ in range(num_samples):
            upc_e_0 = faker.upc_e(number_system_digit=0)
            upc_e_1 = faker.upc_e(number_system_digit=1)
            assert self.upc_e_pattern.fullmatch(upc_e_0)
            assert self.upc_e_pattern.fullmatch(upc_e_1)
            assert upc_e_0[0] == '0'
            assert upc_e_1[0] == '1'

    def test_upc_e_safe_mode(self, faker):
        # For this test, we explicitly specify a base and a number system digit
        # so we do not have to wait for RNG to produce the right combinations.
        for _ in range(100):
            # Be aware that there are other unsafe combinations
            unsafe_base = f'{faker.random_int(0, 99):02}000{faker.random_int(3, 4)}'
            safe_base = unsafe_base[:2] + '0000'
            number_system_digit = faker.random_int(0, 1)

            # Safe mode will create a UPC-E barcode with the safe base
            # even if an unsafe base was supplied
            upc_e_safe = faker.upc_e(base=unsafe_base,
                                     number_system_digit=number_system_digit,
                                     safe_mode=True)
            assert upc_e_safe[1:-1] == safe_base
            assert upc_e_safe[1:-1] != unsafe_base

            # Unsafe mode will force create a UPC-E barcode with unsafe base
            upc_e_unsafe = faker.upc_e(base=unsafe_base,
                                       number_system_digit=number_system_digit,
                                       safe_mode=False)
            assert upc_e_unsafe[1:-1] != safe_base
            assert upc_e_unsafe[1:-1] == unsafe_base

            # What will be the same are their number system and check digits
            assert upc_e_safe[0] == upc_e_unsafe[0]
            assert upc_e_safe[-1] == upc_e_unsafe[-1]

    def test_upc_a2e_bad_values(self, faker, provider):
        # Invalid data type
        with pytest.raises(TypeError):
            provider._convert_upc_a2e(12345678)

        # Invalid string
        with pytest.raises(ValueError):
            provider._convert_upc_a2e('abcdef')

    def test_upc_a2e2a(self, faker, num_samples, provider):
        for _ in range(num_samples):
            upc_a = faker.upc_a(upc_ae_mode=True)
            assert self.upc_a_pattern.fullmatch(upc_a)

            # Convert UPC-A to UPC-E
            upc_e = provider._convert_upc_a2e(upc_a)

            # Number system and check digits must be the same
            assert int(upc_a[0]) == int(upc_e[0])
            assert int(upc_a[-1]) == int(upc_e[-1])

            # Create a new UPC-A barcode based on the UPC-E barcode
            new_upc_a = faker.upc_a(upc_ae_mode=True,
                                    base=upc_e[1:-1],
                                    number_system_digit=int(upc_e[0]))

            # New UPC-A barcode must be the same as the original
            assert upc_a == new_upc_a

    def test_upc_e2a2e(self, faker, num_samples, provider):
        for _ in range(num_samples):
            upc_e = faker.upc_e()
            assert self.upc_e_pattern.fullmatch(upc_e)

            # Create a new UPC-A barcode based on the UPC-E barcode
            upc_a = faker.upc_a(upc_ae_mode=True,
                                base=upc_e[1:-1],
                                number_system_digit=int(upc_e[0]))

            # Number system and check digits must be the same
            assert int(upc_a[0]) == int(upc_e[0])
            assert int(upc_a[-1]) == int(upc_e[-1])

            # Convert UPC-A to UPC-E
            new_upc_e = provider._convert_upc_a2e(upc_a)

            # New UPC-E barcode must be the same as the original
            assert new_upc_e == upc_e


class TestEnUs(_LocaleNorthAmericaMixin):
    """ Tests en_US barcode provider """
    num_samples = 1000

    @staticmethod
    def get_provider_class():
        from faker.providers.barcode.en_US import Provider
        return Provider


class TestEnCa(_LocaleNorthAmericaMixin):
    """ Tests en_CA barcode provider """
    num_samples = 1000

    @staticmethod
    def get_provider_class():
        from faker.providers.barcode.en_CA import Provider
        return Provider


class TestFrCa(_LocaleNorthAmericaMixin):
    """ Tests fr_CA barcode provider """
    num_samples = 1000

    @staticmethod
    def get_provider_class():
        from faker.providers.barcode.fr_CA import Provider
        return Provider


class TestJaJp(_LocaleCommonMixin):
    """ Tests ja_JP barcode provider """
    num_samples = 1000

    @staticmethod
    def get_provider_class():
        from faker.providers.barcode.ja_JP import Provider
        return Provider

    def test_jan(self, faker, num_samples, provider):
        for _ in range(num_samples):
            jan8 = faker.jan(8)
            jan13 = faker.jan(13)
            assert self.ean8_pattern.match(jan8)
            assert self.ean13_pattern.match(jan13)

            jan8_digits = [int(digit) for digit in jan8]
            jan13_digits = [int(digit) for digit in jan13]
            assert (sum(jan8_digits) + 2 * sum(jan8_digits[::2])) % 10 == 0
            assert (sum(jan13_digits) + 2 * sum(jan13_digits[1::2])) % 10 == 0

            self.assert_prefix(jan8_digits, provider.local_prefixes)
            self.assert_prefix(jan13_digits, provider.local_prefixes)

    def test_jan8(self, faker, num_samples, provider):
        for _ in range(num_samples):
            jan8 = faker.jan(8)
            assert self.ean8_pattern.match(jan8)

            jan8_digits = [int(digit) for digit in jan8]
            assert (sum(jan8_digits) + 2 * sum(jan8_digits[::2])) % 10 == 0

            self.assert_prefix(jan8_digits, provider.local_prefixes)

    def test_jan13(self, faker, num_samples, provider):
        for _ in range(num_samples):
            jan13 = faker.jan(13)
            assert self.ean13_pattern.match(jan13)

            jan13_digits = [int(digit) for digit in jan13]
            assert (sum(jan13_digits) + 2 * sum(jan13_digits[1::2])) % 10 == 0

            self.assert_prefix(jan13_digits, provider.local_prefixes)


class TestEsEs(_LocaleCommonMixin):
    """ Tests es_ES barcode provider """
    num_samples = 1000

    @staticmethod
    def get_provider_class():
        from faker.providers.barcode.es_ES import Provider
        return Provider

    def test_localized_ean(self, faker, num_samples, provider):
        for _ in range(num_samples):
            ean8 = faker.localized_ean(8)
            ean13 = faker.localized_ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

            self.assert_prefix(ean8_digits, provider.local_prefixes)
            self.assert_prefix(ean13_digits, provider.local_prefixes)
