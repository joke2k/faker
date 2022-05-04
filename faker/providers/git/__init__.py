import random

from .. import BaseProvider

localized = False


class Provider(BaseProvider):
    def git_short_sha(self) -> str:
        return '%07x' % random.randrange(16**7)

    def git_commit_sha(self) -> str:
        return '%040x' % random.randrange(16**40)

    # TODO: Random git commit message (name + date + commit sha)
