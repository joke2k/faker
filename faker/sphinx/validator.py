# coding=utf-8
import ast
import traceback

from collections import OrderedDict


class SampleCodeValidator(ast.NodeVisitor):
    """
    Class that checks if a string is a valid and "safe" Python expression

    What is considered "safe" for this class is limited to the context of generating
    provider method sample code and output for documentation purposes. The end goal
    is to pass a command string to `eval()` should the string pass the validation
    performed by this class.

    The main assumption this class will make is that the command string passed during
    class instantiation will always be in the form "{generator}.{method}({arguments})".
    In said form, {generator} is a `Generator` object variable that already exists
    within the scope where `eval()` will be called, {method} will be the provider
    method name which is also available within the `eval()` scope, and {arguments}
    will be sample arguments parsed from docstrings. This means that {arguments} can
    potentially be used as a vector for code injection.

    In order to neuter the impact of code injection, the following validation steps
    will be applied:

    - The command string is parsed using 'eval' mode, meaning expressions only.
    - The command string can only have whitelisted code elements. See `_whitelisted_nodes`.
    - The command string can only have one instance of variable access.
    - The command string can only have one instance of attribute access.
    - The command string can only have one instance of a function/method call.
    - The argument values in the command string can only be literals.
    - The only literals allowed are numbers (integers, floats, or complex numbers),
      strings (but not f-strings), bytes, lists, tuples, sets, dictionaries, True,
      False, and None.

    There is, however, an exception. In order to accommodate sample code with custom
    probability distribution, variable access to `OrderedDict` will not count against
    the maximum limit of variable access, and invoking `OrderedDict` constructor calls
    will not count against the maximum limit of function/method calls. In order to
    neuter the impact of code injection, please ensure that `OrderedDict` refers to
    the standard library's `collections.OrderedDict` within the `eval()` scope before
    passing the command string to `eval()` for execution. This can be done in code review.
    """

    _whitelisted_nodes = (
        # Code elements related to function calls and variable and attribute access
        ast.Expression,
        ast.Call,
        ast.Attribute,
        ast.Name,
        ast.Load,
        ast.keyword,
        # Code elements representing whitelisted literals
        ast.Num,
        ast.Str,
        ast.Bytes,
        ast.List,
        ast.Tuple,
        ast.Set,
        ast.Dict,
        ast.NameConstant,
    )

    _max_function_call_count = 1
    _max_attribute_access_count = 1
    _max_variable_access_count = 1

    def __init__(self, command):
        self._errors = set()
        self._function_call_count = 0
        self._attribute_access_count = 0
        self._variable_access_count = 0
        self._command = command

        try:
            self._tree = ast.parse(command, mode="eval")
        except (SyntaxError, ValueError):
            self._log_error(traceback.format_exc())
        else:
            self._validate()

    @property
    def errors(self):
        return self._errors

    def _is_whitelisted(self, node):
        return isinstance(node, self._whitelisted_nodes)

    def _log_error(self, msg):
        self._errors.add(msg)

    def _validate(self):
        self.visit(self._tree)

    def _is_node_using_ordereddict(self, node):
        is_valid = False

        # If instance of function call, check if it is a call to the OrderedDict constructor
        if isinstance(node, ast.Call):
            is_valid = self._is_node_using_ordereddict(node.func)

        # If instance of variable access, check if it is
        elif isinstance(node, ast.Name) and node.id == OrderedDict.__name__:
            is_valid = True

        return is_valid

    def visit(self, node):
        # Check if code element type is allowed
        if not self._is_whitelisted(node):
            msg = "Code element `%s` is not allowed." % node.__class__.__name__
            self._log_error(msg)

        return super().visit(node)

    def visit_Call(self, node):
        if not self._is_node_using_ordereddict(node):
            # There can only be one instance of a function call
            if self._function_call_count < self._max_function_call_count:
                self._function_call_count += 1
            else:
                msg = "There can only be one instance of a function/method call."
                self._log_error(msg)

        # Proceed to child nodes
        self.generic_visit(node)

    def visit_Attribute(self, node):
        # There can only be one instance of attribute access
        if self._attribute_access_count < self._max_attribute_access_count:
            self._attribute_access_count += 1
        else:
            msg = "There can only be one instance of attribute access."
            self._log_error(msg)

        # Proceed to child nodes
        self.generic_visit(node)

    def visit_Name(self, node):
        if not self._is_node_using_ordereddict(node):
            # There can only be one instance of variable access
            if self._variable_access_count < self._max_variable_access_count:
                self._variable_access_count += 1
            else:
                msg = "There can only be one instance of variable access."
                self._log_error(msg)

        # Proceed to child nodes
        self.generic_visit(node)
