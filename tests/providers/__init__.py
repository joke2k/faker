import re
import string

from collections import OrderedDict

import pytest

from faker.providers import BaseProvider


class TestBaseProvider:
    """Test base provider methods"""

    def test_locale(self, faker, num_samples):
        locales = [
            '{}_{}'.format(language, region)
            for language, regions in BaseProvider.language_locale_codes.items()
            for region in regions
        ]
        for _ in range(num_samples):
            locale = faker.locale()
            assert locale in locales

    def test_language_code(self, faker, num_samples):
        language_codes = list(BaseProvider.language_locale_codes)
        for _ in range(num_samples):
            language_code = faker.language_code()
            assert language_code in language_codes

    def test_random_digit(self, faker, num_samples):
        samples = [faker.random_digit() for _ in range(num_samples * 10)]
        assert set(samples) == set(range(10))

    def test_random_digit_not_null(self, faker, num_samples):
        samples = [faker.random_digit_not_null() for _ in range(num_samples * 10)]
        assert set(samples) == set(range(1, 10))

    def test_random_digit_or_empty(self, faker, num_samples):
        expected = set(range(10))
        expected.add('')
        samples = [faker.random_digit_or_empty() for _ in range(num_samples * 10)]
        assert set(samples) == expected

    def test_random_digit_not_null_or_empty(self, faker, num_samples):
        expected = set(range(1, 10))
        expected.add('')
        samples = [faker.random_digit_not_null_or_empty() for _ in range(num_samples * 10)]
        assert set(samples) == expected

    def test_random_number(self, faker):
        number = faker.random_number(10, True)
        assert len(str(number)) == 10

        # Digits parameter < 0
        with pytest.raises(ValueError):
            number = faker.random_number(-1, True)

        # Digits parameter < 1 with fix_len=True
        with pytest.raises(ValueError):
            number = faker.random_number(0, True)

    @pytest.mark.parametrize('text,pattern', [
        ('', r''),
        ('abcd', r'abcd'),
        ('#' * 100, r'[0-9]{100}'),
        ('%' * 100, r'[1-9]{100}'),
        ('!' * 100, r'[0-9]{,100}'),
        ('@' * 100, r'[0-9]{,100}'),
        ('##!abc %%@def##!' * 100, r'(?:[0-9]{2,3}abc [1-9]{2,3}def[0-9]{2,3}){100}'),
        ('#@@#^?あ5漢!!%%@' * 100, r'(?:\d[1-9]{,2}\d\^\?あ5漢\d{,2}[1-9]{2}[1-9]*){100}'),
    ], ids=[
        'empty_string',
        'no_valid_placeholders',
        'only_number_signs',
        'only_percent_signs',
        'only_exclamation_marks',
        'only_at_symbols',
        'with_ascii_characters',
        'with_other_symbols_and_non_ascii',
    ])
    def test_numerify(self, faker, num_samples, text, pattern):
        for _ in range(num_samples):
            numerified = faker.numerify(text)
            assert re.fullmatch(pattern, numerified)

    @pytest.mark.parametrize('text,letters,pattern', [
        ('', string.ascii_letters, r''),
        ('abcd', string.ascii_letters, r'abcd'),
        ('???', string.ascii_letters, r'[0-9a-zA-Z]{3}'),
        ('???', 'aBcDeFgHiJ12345', r'[1-5aBcDeFgHiJ]{3}'),
        ('??Xr^#7p??', 'AbCdخあ5漢7Я', r'[AbCdخあ5漢7Я]{2}Xr\^#7p[AbCdخあ5漢7Я]{2}'),
    ], ids=[
        'empty_string',
        'no_valid_placeholders',
        'letters_using_whole_ascii',
        'letters_using_ascii_subset',
        'pattern_with_other_symbols_and_letters_using_non_ascii',
    ])
    def test_lexify(self, faker, num_samples, text, letters, pattern):
        for _ in range(num_samples):
            lexified = faker.lexify(text, letters=letters)
            assert re.fullmatch(pattern, lexified)

    @pytest.mark.parametrize('text,letters,pattern', [
        ('', string.ascii_letters, r''),
        ('abcd', string.ascii_letters, r'abcd'),
        ('???', string.ascii_letters, r'[0-9a-zA-Z]{3}'),
        ('???', 'aBcDeFgHiJ12345', r'[1-5aBcDeFgHiJ]{3}'),
        ('#%!@???', string.ascii_letters, r'\d[1-9]\d*[1-9]*[0-9a-zA-Z]{3}'),
        ('#%!@???', 'aBcDeFgHiJ12345', r'\d[1-9]\d*[1-9]*[1-5aBcDeFgHiJ]{3}'),
        ('#%!@??Xr7p??', 'AbCdخあ5漢7Я', r'\d[1-9]\d*[1-9]*[AbCdخあ5漢7Я]{2}Xr7p[AbCdخあ5漢7Я]{2}'),
    ], ids=[
        'empty_string',
        'no_valid_placeholders',
        'simple_pattern_and_letters_using_whole_ascii',
        'simple_pattern_and_letters_using_ascii_subset',
        'more_complex_pattern_and_letters_using_whole_ascii',
        'more_complex_pattern_and_letters_using_ascii_subset',
        'more_complex_pattern_with_other_symbols_and_letters_using_non_ascii',
    ])
    def test_bothify(self, faker, num_samples, text, letters, pattern):
        for _ in range(num_samples):
            bothified = faker.bothify(text, letters=letters)
            assert re.fullmatch(pattern, bothified)

    @pytest.mark.parametrize('text,upper,pattern', [
        ('', False, r''),
        ('', True, r''),
        ('abcd', False, r'abcd'),
        ('abcd', True, r'abcd'),
        ('^^^^', False, r'[0-9a-f]{4}'),
        ('^^^^', True, r'[0-9A-F]{4}'),
        ('Abc ^^^ %^^^?あ5漢!#^^', False, r'Abc [0-9a-f]{3} %[0-9a-f]{3}\?あ5漢!#[0-9a-f]{2}'),
        ('Abc ^^^ %^^^?あ5漢!#^^', True, r'Abc [0-9A-F]{3} %[0-9A-F]{3}\?あ5漢!#[0-9A-F]{2}'),
    ], ids=[
        'empty_string_lowercase',
        'empty_string_uppercase',
        'no_circumflex_lowercase',
        'no_circumflex_uppercase',
        'simple_pattern_lowercase',
        'simple_pattern_uppercase',
        'complex_pattern_lowercase',
        'complex_pattern_uppercase',
    ])
    def test_hexify(self, faker, num_samples, text, upper, pattern):
        for _ in range(num_samples):
            hexified = faker.hexify(text, upper=upper)
            assert re.fullmatch(pattern, hexified)

    def test_random_letter(self, faker, num_samples):
        for _ in range(num_samples):
            letter = faker.random_letter()
            assert letter.isalpha()

    def test_random_lowercase_letter(self, faker, num_samples):
        for _ in range(num_samples):
            letter = faker.random_lowercase_letter()
            assert letter.isalpha() and letter.lower() == letter

    def test_random_uppercase_letter(self, faker, num_samples):
        for _ in range(num_samples):
            letter = faker.random_uppercase_letter()
            assert letter.isalpha() and letter.upper() == letter

    def test_random_element(self, faker, num_samples):
        # dicts not allowed because they introduce dependency on PYTHONHASHSEED
        with pytest.raises(ValueError):
            faker.random_element({})

        choices = ('a', 'b', 'c', 'd')
        for _ in range(num_samples):
            assert faker.random_element(choices) in choices

        choices = OrderedDict([('a', 5), ('b', 2), ('c', 2), ('d', 1)])
        for _ in range(num_samples):
            assert faker.random_element(choices) in choices

        choices = OrderedDict([('a', 0.5), ('b', 0.2), ('c', 0.2), ('d', 0.1)])
        for _ in range(num_samples):
            assert faker.random_element(choices) in choices

    def test_random_sample(self, faker):
        # Too many items requested
        with pytest.raises(ValueError):
            faker.random_sample('abcde', 6)

        # Same length
        sample = faker.random_sample('abcd', 4)
        assert sorted(sample) == list('abcd')

        sample = faker.random_sample('abcde', 5)
        assert sorted(sample) == list('abcde')

        # Length = 3
        sample = faker.random_sample('abcde', 3)
        assert len(sample) == 3
        assert set(sample).issubset(set('abcde'))

        # Length = 1
        sample = faker.random_sample('abcde', 1)
        assert len(sample) == 1
        assert set(sample).issubset(set('abcde'))

        # Length = 0
        sample = faker.random_sample('abcde', 0)
        assert sample == []

    def test_randomize_nb_elements(self, faker, num_samples):
        assert faker.randomize_nb_elements(number=1, le=True, ge=True) == 1
        assert faker.randomize_nb_elements(le=True, ge=True) == 10
        assert faker.randomize_nb_elements(min=42) == 42
        assert faker.randomize_nb_elements(max=1) == 1

        number = 9999
        lower_bound = int(number * 0.6)
        upper_bound = int(number * 1.4)

        for _ in range(num_samples):
            res = faker.randomize_nb_elements(number=number, le=True)
            assert res >= lower_bound
            assert res <= number, "'{}' is not <= than '{}'".format(res, number)

        for _ in range(num_samples):
            res = faker.randomize_nb_elements(number=number, ge=True)
            assert number <= res <= upper_bound

        for _ in range(num_samples):
            res = faker.randomize_nb_elements(number=number)
            assert lower_bound <= res <= upper_bound
