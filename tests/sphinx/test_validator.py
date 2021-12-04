# coding=utf-8
import sys

from unittest import mock

from faker.sphinx.validator import SampleCodeValidator


class TestSampleCodeValidator:
    @mock.patch("faker.sphinx.validator.ast.parse")
    def test_ast_parser_called_in_eval_mode(self, mock_ast_parse):
        command = "variable.method()"
        mock_ast_parse.assert_not_called()
        SampleCodeValidator(command)
        mock_ast_parse.assert_called_with(command, mode="eval")

    def test_invalid_syntax(self):
        validator = SampleCodeValidator("[T___T)")
        assert validator.errors

    def test_single_instance_of_variable_access(self):
        validator = SampleCodeValidator("variable1")
        assert not validator.errors

        validator = SampleCodeValidator("[variable2]")
        assert not validator.errors

        validator = SampleCodeValidator("[variable1, variable1]")
        assert validator.errors

        validator = SampleCodeValidator("[variable1, variable2]")
        assert validator.errors

    def test_ordereddict_variable_access_exception(self):
        validator = SampleCodeValidator("[OrderedDict]")
        assert not validator.errors

        validator = SampleCodeValidator("[OrderedDict, variable1]")
        assert not validator.errors

        validator = SampleCodeValidator("[OrderedDict, OrderedDict, OrderedDict, OrderedDict]")
        assert not validator.errors

        validator = SampleCodeValidator("[OrderedDict, OrderedDict, OrderedDict, OrderedDict, variable1]")
        assert not validator.errors

        validator = SampleCodeValidator("[OrderedDict, variable1, variable2]")
        assert validator.errors

        validator = SampleCodeValidator("[OrderedDict2, variable1]")
        assert validator.errors

    def test_single_instance_of_attribute_access(self):
        validator = SampleCodeValidator("variable.attr1")
        assert not validator.errors

        validator = SampleCodeValidator("variable.attr1.attr2")
        assert validator.errors

    def test_single_instance_of_method_or_function_call(self):
        validator = SampleCodeValidator("variable.method1()")
        assert not validator.errors

        validator = SampleCodeValidator("variable.method1().method2()")
        assert validator.errors

    def test_ordereddict_constructor_exception(self):
        validator = SampleCodeValidator("OrderedDict()")
        assert not validator.errors

        validator = SampleCodeValidator("variable.method1(OrderedDict())")
        assert not validator.errors

        validator = SampleCodeValidator("variable.method1(OrderedDict2())")
        assert validator.errors

        validator = SampleCodeValidator("variable.method1(OrderedDict(), OrderedDict(), OrderedDict())")
        assert not validator.errors

        validator = SampleCodeValidator("variable.method1().method2(OrderedDict())")
        assert validator.errors

    def test_allowed_literal_types(self):
        commands = [
            "variable.method(12345)",
            'variable.method("12345")',
            'variable.method(b"12345")',
            "variable.method([1, 2, 3, 4, 5])",
            "variable.method((1, 2, 3, 4, 5))",
            "variable.method({1, 2, 3, 4, 5})",
            'variable.method({"value": 12345})',
            "variable.method(True)",
            "variable.method(False)",
            "variable.method(None)",
        ]

        for command in commands:
            validator = SampleCodeValidator(command)
            assert not validator.errors

    def test_prohibited_literal_types(self):
        commands = ["variable.method(...)"]
        if sys.version_info[0] == 3 and sys.version_info[1] >= 6:
            commands.append('f"{variable}"')

        for command in commands:
            validator = SampleCodeValidator(command)
            assert validator.errors

    def test_prohibited_operations(self):
        commands = [
            # Unary Operations
            "+variable",
            "-variable",
            "not variable",
            "~variable",
            # Mathematical Operations
            "variable + 5",
            "variable - 5",
            "variable * 5",
            "variable / 5",
            "variable // 5",
            "variable % 5",
            "variable ** 5",
            # Bitwise Operations
            "variable << 5",
            "variable >> 5",
            "variable | 5",
            "variable ^ 5",
            "variable & 5",
            # Boolean Operations
            "variable and True",
            "variable or True",
            # Comparisons
            "variable is None",
            "variable is not None",
            "variable in [1, 2, 3, 4, 5]",
            "variable not in [1, 2, 3, 4, 5]",
            "variable == 5",
            "variable != 5",
            "variable < 5",
            "variable <= 5",
            "variable > 5",
            "variable >= 5",
        ]

        for command in commands:
            validator = SampleCodeValidator(command)
            assert validator.errors

    def test_other_prohibited_expressions(self):
        commands = [
            "variable if True else 1",
            "variable[1]",
            "variable[1:3]",
            "variable[1:3, 2]",
            "[True for _ in [1, 2, 3]]",
            "(True for _ in [1, 2, 3])",
            "{True for _ in [1, 2, 3]}",
            "{str(_): _ for _ in [1, 2, 3]}",
            "lambda x: x",
        ]

        for command in commands:
            validator = SampleCodeValidator(command)
            assert validator.errors
