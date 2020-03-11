# coding=utf-8
import inspect
import unittest
from unittest import mock
from unittest.mock import MagicMock

from faker import Faker
from faker.config import DEFAULT_LOCALE
from faker.sphinx.docstring import ProviderMethodDocstring


class TestProviderMethodDocstring(unittest.TestCase):

    def test_what_is_not_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='not_a_method', name=MagicMock(),
            obj=MagicMock(), options=MagicMock(), lines=MagicMock(),
        )
        assert docstring.skipped

    def test_name_is_not_dotted_path_to_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',  name='faker.sphinx.docstring.ProviderMethodDocString._parse',
            obj=MagicMock(), options=MagicMock(), lines=MagicMock(),
        )
        assert docstring.skipped

    def test_name_is_dotted_path_to_base_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',  name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == 'bothify'
        assert docstring._locale == DEFAULT_LOCALE

    def test_name_is_dotted_path_to_standard_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method', name='faker.providers.barcode.Provider.upc_a',
            obj=MagicMock(), options=MagicMock(), lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == 'upc_a'
        assert docstring._locale == DEFAULT_LOCALE

    def test_name_is_dotted_path_to_localized_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.automotive.en_PH.Provider.protocol_license_plate',
            obj=MagicMock(), options=MagicMock(), lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == 'protocol_license_plate'
        assert docstring._locale == 'en_PH'

    @mock.patch.object(ProviderMethodDocstring, '_generate_samples')
    def test_parsing_empty_lines(self, mock_generate_samples):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=[],
        )
        assert not docstring.skipped
        assert not docstring._samples

    @mock.patch.object(ProviderMethodDocstring, '_generate_samples')
    def test_parsing_single_line_non_sample(self, mock_generate_samples):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=['lorem'],
        )
        assert not docstring.skipped
        assert not docstring._samples

    @mock.patch.object(ProviderMethodDocstring, '_generate_samples')
    def test_parsing_single_line_valid_sample(self, mock_generate_samples):
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=[':sample: a=1'],
        )
        assert not docstring.skipped
        assert docstring._samples == ['a=1']

    @mock.patch.object(ProviderMethodDocstring, '_generate_samples')
    def test_parsing_multiple_lines(self, mock_generate_samples):
        lines = [
            'lorem',
            'ipsum',
            '',
            ':sample: a=1, b=2',            # This becomes 1st sample line
            ':sample: a=2, b=1, c=3',       # This becomes 2nd sample line
            '',                             # Since empty, 2nd sample line will not include this
            'sit',
            ':sample: c=3, a=5,',           # This becomes 3rd sample line
            '         b=1    ',             # and continues to this line
            ':sample: a=1, b=5',            # This becomes 4th sample line
            '   c="abc  def"     d=1  '     # and continues to this line
        ]
        expected_output = [
            'a=1, b=2',
            'a=2, b=1, c=3',
            'c=3, a=5, b=1',                # Multiple whitespaces not inside quotes will
            'a=1, b=5 c="abc  def" d=1',    # be replaced by single whitespace
        ]
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=lines,
        )
        assert not docstring.skipped
        assert docstring._samples == expected_output

    def test_generate_samples(self):
        fake = Faker(DEFAULT_LOCALE)
        non_sample_lines = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
        sample_lines = [
            ":sample: text='???###'",
            ":sample: letters='abcde'",
            ":sample: abcd='abcd'",         # Will be ignored due to failed sample generation
            ":sample: text='???###', ",
            "         letters='abcde'",
            ":sample: default",
        ]
        lines = non_sample_lines + sample_lines
        docstring = ProviderMethodDocstring(
            app=MagicMock(), what='method',
            name='faker.providers.BaseProvider.bothify',
            obj=MagicMock(), options=MagicMock(), lines=lines,
        )

        output = docstring.lines[len(non_sample_lines):]
        assert output[0] == ":examples:"
        assert output[1] == ""

        Faker.seed(0)
        assert output[2] == ">>> fake.bothify(text='???###')"
        assert output[3] == fake.bothify(text='???###')

        Faker.seed(0)
        assert output[4] == ">>> fake.bothify(letters='abcde')"
        assert output[5] == fake.bothify(letters='abcde')

        Faker.seed(0)
        assert output[6] == ">>> fake.bothify(text='???###', letters='abcde')"
        assert output[7] == fake.bothify(text='???###', letters='abcde')

        Faker.seed(0)
        assert output[8] == '>>> fake.bothify()'
        assert output[9] == fake.bothify()
        assert output[10] == ''
