import pytest
import unittest

from importlib import import_module
from pathlib import Path

from faker.cli import execute_from_command_line


class TestingCli(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_using_no_command(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            execute_from_command_line(['faker'])


