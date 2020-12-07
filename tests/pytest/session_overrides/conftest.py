from pathlib import Path

import pytest

EXCLUSIVE_SESSION_FLAG = '--exclusive-faker-session'
SKIP_REASON = (
    f'This test is skipped by default since it depends on changes in the behavior of session-scoped fixtures. '
    f'Use a separate pytest run for tests like this with the "{EXCLUSIVE_SESSION_FLAG}" flag specified.'
)


def pytest_addoption(parser):
    parser.addoption(
        EXCLUSIVE_SESSION_FLAG, action='store_true', default=False,
        help='Allows tests that require an exclusive session to run',
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption(EXCLUSIVE_SESSION_FLAG):
        return
    skip_lacks_exclusive_session = pytest.mark.skip(reason=SKIP_REASON)
    session_overrides_dir = Path(__file__).resolve().parent
    for item in items:
        if str(item.fspath).startswith(str(session_overrides_dir)):
            item.add_marker(skip_lacks_exclusive_session)
