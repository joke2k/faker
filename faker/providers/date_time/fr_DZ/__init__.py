from typing import Any

from ..fr_FR import Provider as fr_FRProvider


class Provider(fr_FRProvider):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
