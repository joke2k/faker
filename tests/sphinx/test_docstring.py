# coding=utf-8
import inspect

from unittest import mock
from unittest.mock import MagicMock

from faker.config import DEFAULT_LOCALE
from faker.sphinx.docstring import DEFAULT_SAMPLE_SIZE, DEFAULT_SEED, ProviderMethodDocstring, Sample


class TestProviderMethodDocstring:
    def test_what_is_not_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="not_a_method",
            name="name",
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        assert docstring.skipped

    def test_name_is_not_dotted_path_to_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.sphinx.docstring.ProviderMethodDocString._parse",
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        assert docstring.skipped

    def test_name_is_dotted_path_to_base_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == "bothify"
        assert docstring._locale == DEFAULT_LOCALE

    def test_name_is_dotted_path_to_standard_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.barcode.Provider.upc_a",
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == "upc_a"
        assert docstring._locale == DEFAULT_LOCALE

    def test_name_is_dotted_path_to_localized_provider_method(self):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.automotive.en_PH.Provider.protocol_license_plate",
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        assert not docstring.skipped
        assert docstring._method == "protocol_license_plate"
        assert docstring._locale == "en_PH"

    @mock.patch("faker.sphinx.docstring.logger.warning")
    def test_log_warning(self, mock_logger_warning):
        path = inspect.getfile(MagicMock)
        name = "faker.providers.color.Provider"
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name=name,
            obj=MagicMock,
            options=MagicMock(),
            lines=MagicMock(),
        )
        docstring._log_warning("Test Warning 1")
        docstring._log_warning("Test Warning 2")

        assert docstring._log_prefix == f"{path}:docstring of {name}: WARNING:"

        calls = mock_logger_warning.call_args_list
        assert len(calls) == 2

        # 1st call to logger.warning
        args, kwargs = calls[0]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == f"{path}:docstring of {name}: WARNING: Test Warning 1"

        # 2nd call to logger.warning
        args, kwargs = calls[1]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == f"{path}:docstring of {name}: WARNING: Test Warning 2"

    def test_stringify_results(self, faker):
        class TestObject:
            def __repr__(self):
                return "abcdefg"

        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=[],
        )
        results = [
            "",  # Empty string
            "'",  # Single quote literal (escaped)
            "'",  # Single quote literal (unescaped)
            '"',  # Double quote literal (unescaped)
            '"',  # Double quote literal (escaped)
            "aa\taaaaa\r\n",  # String containing \t, \r, \n
            b"abcdef",  # Bytes object
            True,  # Booleans
            False,
            None,  # None types
            [1, 2, 3, 4, 5],  # Other non-primitives
            (1, 2, 3, 4, 5),
            {1: 2, 2: 3, 3: 4, 4: 5},
            faker.uuid4(cast_to=None),
            TestObject(),
        ]
        output = [docstring._stringify_result(result) for result in results]
        assert output == [
            "''",  # Ends up as '' when printed
            '"\'"',  # Ends up as "'" when printed
            '"\'"',  # Ends up as "'" when printed
            "'\"'",  # Ends up as '"' when printed
            "'\"'",  # Ends up as '"' when printed
            "'aa\\taaaaa\\r\\n'",  # Ends up as 'aa\\taaaaa\\r\\n' when printed
            "b'abcdef'",  # Ends up as b'abcdef' when printed
            "True",  # Ends up as True when printed
            "False",  # Ends up as False when printed
            "None",  # Ends up as None when printed
            "[1, 2, 3, 4, 5]",  # Ends up using object's __repr__
            "(1, 2, 3, 4, 5)",
            "{1: 2, 2: 3, 3: 4, 4: 5}",
            "UUID('e3e70682-c209-4cac-a29f-6fbed82c07cd')",
            "abcdefg",
        ]

    @mock.patch.object(ProviderMethodDocstring, "_log_warning")
    def test_parsing_empty_lines(self, mock_log_warning):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=[],
        )
        assert not docstring.skipped
        assert len(docstring._samples) == 1
        assert docstring._samples[0] == Sample(DEFAULT_SAMPLE_SIZE, DEFAULT_SEED, "")

    @mock.patch.object(ProviderMethodDocstring, "_log_warning")
    def test_parsing_single_line_non_sample(self, mock_log_warning):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=["lorem"],
        )
        assert not docstring.skipped
        assert len(docstring._samples) == 1
        assert docstring._samples[0] == Sample(DEFAULT_SAMPLE_SIZE, DEFAULT_SEED, "")

    @mock.patch.object(ProviderMethodDocstring, "_log_warning")
    def test_parsing_single_line_valid_sample(self, mock_log_warning):
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=[":sample: a=1"],
        )
        assert not docstring.skipped
        assert docstring._samples == [Sample(5, 0, "a=1")]

    @mock.patch.object(ProviderMethodDocstring, "_log_warning")
    def test_parsing_multiple_lines(self, mock_log_warning):
        lines = [
            "lorem",  # No-op, not a sample line
            ":sample:",  # Valid, default sample count, default seed, empty kwargs, 1st in expected
            ":sample 10 2000:",  # Invalid, size and seed must be specified as "keyword arguments"
            ":sample 10 seed=1000:",  # Invalid, size and seed must be specified as "keyword arguments"
            ":sample size=10 1000:",  # Invalid, size and seed must be specified as "keyword arguments"
            ":sample size=0:",  # Invalid, sample count cannot be zero
            ":sample size=100:",  # Valid, 100 samples, default seed, empty kwargs, 2nd in expected
            ":sample size=0100:",  # Invalid, leading zeroes are not allowed
            ":sampler",  # Invalid, starts with ":sample" but will not pass validation
            ":sample :",  # No-op, must be ":sample:" verbatim
            ":sample seed=4761:",  # Valid, default sample count, seed value of 4761
            "",  # but line break was detected, so sample parsing stops here
            "ipsum",  # No-op, not a sample line
            ":sample sede=123",  # Invalid, seed misspelled
            ":sample size=4 seed=100:",  # Valid, will reset to 5 samples, seed value of 100, empty kwargs, the 4th
            ":sample seed=103 size=104:",  # Invalid, "seed" kwarg must come after "size" kwarg
            ":sample: a=1, b=2",  # Valid, default count and seed with kwargs, the 5th
            ":sample size=2222: a=2, b=1",  # Valid, 2222 samples, default seed, and with kwargs, the 6th
            ":sample 11 12:",  # Invalid, seed value must be set with "seed=" prefix
            ":sample seed=3333: d=3",  # Valid, default count, seed value of 3333, with kwargs, the 7th
            ":sample size=3333 seed=2222: c=1",  # Valid, 3333 samples, seed value of 2222, with kwargs, the 8th
            ":sample size=10 seed=10:",  # Valid 9th, 10 samples, seed value of 10, with kwargs
            "   arg1=1,",  # and will continue reading the next few lines
            '   arg2="val2",arg3="val3",',  # and will prettify (missing whitespace after comma)
            " arg4=4   ,    arg5=5,",  # and will remove excess whitespaces here
            ' arg6="ar  g6",',  # but not if whitespaces are within double quotes
            "       arg7='   ar  g 7',",  # or within single quotes
            '    arg8="aaa,aaa"',  # and will not prettify commas within quotes
            ":sample size=20 seed=3456:",  # Valid 10th, 20 samples, seed value of 3456, with kwargs
            'arg1="val1,val1,val1",',  # and this is very similar to previous sample
            'arg2="val2",',  # and it is ok not to have leading whitespaces in continuation lines
            'arg3="val3    val3",',  # and it is ok to have a trailing comma after the last kwarg
        ]

        expected_output = [
            Sample(DEFAULT_SAMPLE_SIZE, DEFAULT_SEED, ""),  # 1st sample parsed
            Sample(100, DEFAULT_SEED, ""),  # 2nd sample parsed
            Sample(DEFAULT_SAMPLE_SIZE, 4761, ""),  # 3rd sample parsed
            Sample(5, 100, ""),  # 4th sample parsed
            Sample(DEFAULT_SAMPLE_SIZE, DEFAULT_SEED, "a=1, b=2"),  # 5th sample parsed
            Sample(2222, DEFAULT_SEED, "a=2, b=1"),  # 6th sample parsed
            Sample(DEFAULT_SAMPLE_SIZE, 3333, "d=3"),  # 7th sample parsed
            Sample(3333, 2222, "c=1"),  # 8th sample parsed
            Sample(  # 9th sample parsed
                10,
                10,
                'arg1=1, arg2="val2", arg3="val3", arg4=4, arg5=5, arg6="ar  g6", arg7=\'   ar  g 7\', arg8="aaa,aaa"',
            ),
            Sample(  # 10th sample parsed
                20,
                3456,
                'arg1="val1,val1,val1", arg2="val2", arg3="val3    val3",',
            ),
        ]
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=lines,
        )
        assert not docstring.skipped
        assert docstring._samples == expected_output

    @mock.patch.object(ProviderMethodDocstring, "_log_warning")
    def test_end_to_end_sample_generation(self, mock_warning, faker):
        non_sample_lines = ["lorem", "ipsum", "dolor", "sit", "amet"]
        valid_sample_lines = [
            ":sample 1234jdbvhjdbygdvbhxjhx",  # Will fail during sample section processing, 1st log warning
            ":sample: invalid_arg='value'",  # Will fail during sample generation, 2nd log warning
            ":sample size=3 seed=1000: text='???###'",  # 1st sample generation
            ":sample: number=100**100**100",  # Will fail SampleCodeValidator validation, 3rd log warning
            ":sample seed=3210: letters='abcde'",  # 2nd sample generation
            ":sample size=10 seed=1: abcd='abcd'",  # Will fail during sample generation, 4th log warning
            ":sample size=20 seed=1234: text='???###', ",  # 3rd sample generation
            "         letters='abcde'",
        ]
        lines = non_sample_lines + valid_sample_lines
        docstring = ProviderMethodDocstring(
            app=MagicMock(),
            what="method",
            name="faker.providers.BaseProvider.bothify",
            obj=MagicMock,
            options=MagicMock(),
            lines=lines,
        )

        output = docstring.lines[len(non_sample_lines) :]
        assert output[0] == ":examples:"

        # 1st sample generation
        faker.seed_instance(1000)
        assert output[1] == ""
        assert output[2] == ">>> Faker.seed(1000)"
        assert output[3] == ">>> for _ in range(5):"
        assert output[4] == "...     fake.bothify(text='???###')"
        assert output[5] == "..."
        for i in range(6, 11):
            assert output[i] == docstring._stringify_result(faker.bothify(text="???###"))

        # 2nd sample generation
        faker.seed_instance(3210)
        assert output[11] == ""
        assert output[12] == ">>> Faker.seed(3210)"
        assert output[13] == ">>> for _ in range(5):"
        assert output[14] == "...     fake.bothify(letters='abcde')"
        assert output[15] == "..."
        for i in range(16, 21):
            assert output[i] == docstring._stringify_result(faker.bothify(letters="abcde"))

        # 3rd sample generation
        faker.seed_instance(1234)
        assert output[21] == ""
        assert output[22] == ">>> Faker.seed(1234)"
        assert output[23] == ">>> for _ in range(20):"
        assert output[24] == "...     fake.bothify(text='???###', letters='abcde')"
        assert output[25] == "..."
        for i in range(26, 46):
            assert output[i] == docstring._stringify_result(faker.bothify(text="???###", letters="abcde"))

        calls = mock_warning.call_args_list
        assert len(calls) == 4

        # 1st call to _log_warning
        args, kwargs = calls[0]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == "The section `:sample 1234jdbvhjdbygdvbhxjhx` is malformed and will be discarded."

        # 2nd call to _log_warning
        args, kwargs = calls[1]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == "Sample generation failed for method `bothify` with arguments `invalid_arg='value'`."

        # 3rd call to _log_warning
        args, kwargs = calls[2]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == (
            "Invalid code elements detected. Sample generation will be skipped for "
            "method `bothify` with arguments `number=100**100**100`."
        )

        # 4th call to _log_warning
        args, kwargs = calls[3]
        assert len(args) == 1
        assert not kwargs
        assert args[0] == "Sample generation failed for method `bothify` with arguments `abcd='abcd'`."
