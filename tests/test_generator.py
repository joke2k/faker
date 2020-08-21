from unittest.mock import patch

import pytest

from faker import Faker, Generator


class BarProvider:

    def foo_formatter(self):
        return 'barfoo'


class FooProvider:

    def foo_formatter(self):
        return 'foobar'

    def foo_formatter_with_arguments(self, param='', append=''):
        return 'baz' + str(param) + str(append)


@pytest.fixture(autouse=True)
def generator():
    generator = Generator()
    generator.add_provider(FooProvider())
    return generator


class TestGenerator:
    """Test Generator class"""
    def test_get_formatter_returns_correct_formatter(self, generator):
        foo_provider = generator.providers[0]
        formatter = generator.get_formatter('foo_formatter')
        assert callable(formatter) and formatter == foo_provider.foo_formatter

    def test_get_formatter_with_unknown_formatter(self, generator):
        with pytest.raises(AttributeError) as excinfo:
            generator.get_formatter('barFormatter')
        assert str(excinfo.value) == 'Unknown formatter "barFormatter"'

        fake = Faker('it_IT')
        with pytest.raises(AttributeError) as excinfo:
            fake.get_formatter('barFormatter')
        assert str(excinfo.value) == 'Unknown formatter "barFormatter" with locale "it_IT"'

    def test_format_calls_formatter_on_provider(self, generator):
        assert generator.format('foo_formatter') == 'foobar'

    def test_format_passes_arguments_to_formatter(self, generator):
        result = generator.format('foo_formatter_with_arguments', 'foo', append='!')
        assert result == 'bazfoo!'

    def test_add_provider_overrides_old_provider(self, generator):
        assert generator.format('foo_formatter') == 'foobar'
        generator.add_provider(BarProvider())
        assert generator.format('foo_formatter') == 'barfoo'

    def test_parse_without_formatter_tokens(self, generator):
        assert generator.parse('fooBar#?') == 'fooBar#?'

    def test_parse_with_valid_formatter_tokens(self, generator):
        result = generator.parse('This is {{foo_formatter}} a text with "{{ foo_formatter }}"')
        assert result == 'This is foobar a text with "foobar"'

    def test_arguments_group_with_values(self, generator):
        generator.set_arguments('group1', 'argument1', 1)
        generator.set_arguments('group1', 'argument2', 2)
        assert generator.get_arguments('group1', 'argument1') == 1
        assert generator.del_arguments('group1', 'argument2') == 2
        assert generator.get_arguments('group1', 'argument2') is None
        assert generator.get_arguments('group1') == {'argument1': 1}

    def test_arguments_group_with_dictionaries(self, generator):
        generator.set_arguments('group2', {'argument1': 3, 'argument2': 4})
        assert generator.get_arguments('group2') == {'argument1': 3, 'argument2': 4}
        assert generator.del_arguments('group2') == {'argument1': 3, 'argument2': 4}
        assert generator.get_arguments('group2') is None

    def test_arguments_group_with_invalid_name(self, generator):
        assert generator.get_arguments('group3') is None
        assert generator.del_arguments('group3') is None

    def test_arguments_group_with_invalid_argument_type(self, generator):
        with pytest.raises(ValueError) as excinfo:
            generator.set_arguments('group', ['foo', 'bar'])
        assert str(excinfo.value) == "Arguments must be either a string or dictionary"

    def test_parse_with_valid_formatter_arguments(self, generator):
        generator.set_arguments('format_name', {"param": "foo", "append": "bar"})
        result = generator.parse('This is "{{foo_formatter_with_arguments:format_name}}"')
        generator.del_arguments('format_name')
        assert result == 'This is "bazfoobar"'

    def test_parse_with_unknown_arguments_group(self, generator):
        with pytest.raises(AttributeError) as excinfo:
            generator.parse('This is "{{foo_formatter_with_arguments:unknown}}"')
        assert str(excinfo.value) == 'Unknown argument group "unknown"'

    def test_parse_with_unknown_formatter_token(self, generator):
        with pytest.raises(AttributeError) as excinfo:
            generator.parse('{{barFormatter}}')
        assert str(excinfo.value) == 'Unknown formatter "barFormatter"'

    def test_magic_call_calls_format(self, generator):
        assert generator.foo_formatter() == 'foobar'

    def test_magic_call_calls_format_with_arguments(self, generator):
        assert generator.foo_formatter_with_arguments('foo') == 'bazfoo'

    @patch('faker.generator.random_module.getstate')
    def test_get_random(self, mock_system_random, generator):
        random_instance = generator.random
        random_instance.getstate()
        mock_system_random.assert_not_called()

    @patch('faker.generator.random_module.seed')
    def test_random_seed_doesnt_seed_system_random(self, mock_system_random, generator):
        # Save original state of shared random instance to avoid affecting other tests
        state = generator.random.getstate()

        generator.seed(0)
        mock_system_random.assert_not_called()

        # Restore state of shared random instance
        generator.random.setstate(state)
