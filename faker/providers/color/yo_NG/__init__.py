from collections import OrderedDict
from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    """Implement color provider for ``hr_HR`` locale."""

    all_colors = OrderedDict(
        (
            ("Dúdú", "#000000"),
            ("Fùnfùn", "#FFFFFF"),
            ("Púpà", "#FF0000"),
            ("Dúdú ātì púpà", "#964B00"),
            ("Ārò", "#000080"),
            ("Áláwò ēwē", "#32CD32"),
            ("Awọ ēwē púpà", "#FF4500"),
            ("Awọ ēwē ósàn", "#90EE90")
        )
    )

    safe_colors = (
        "Dúdú",
        "Dúdú ātì púpà",
        "Áláwò ēwē",
        "Ārò",
        "Púpà",
        "Fùnfùn"
    )
