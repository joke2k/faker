import os

import pytest

EXCLUSIVE_SESSION_FLAG = '--exclusive-faker-session'
SKIP_REASON = (
    'This test is skipped by default since it depends on changes in the behavior of session-scoped fixtures. '
    'Use a separate pytest run for tests like this with the "{flag}" flag specified.'
).format(flag=EXCLUSIVE_SESSION_FLAG)


def pytest_addoption(parser):
    parser.addoption(
        EXCLUSIVE_SESSION_FLAG, action='store_true', default=False,
        help='Allows tests that require an exclusive session to run',
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption(EXCLUSIVE_SESSION_FLAG):
        return
    skip_lacks_exclusive_session = pytest.mark.skip(reason=SKIP_REASON)
    session_overrides_dir = os.path.abspath(os.path.join(__file__, '..'))
    for item in items:
        if str(item.fspath).startswith(session_overrides_dir):
            item.add_marker(skip_lacks_exclusive_session)
