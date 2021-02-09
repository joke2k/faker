import warnings

from ..fr_CA import Provider as FRCAProvider


class Provider(FRCAProvider):
    def __init__(self, *args, **kwargs):
        warnings.warn("fr_QC locale is deprecated. Please use fr_CA.")
        super().__init__(*args, **kwargs)
