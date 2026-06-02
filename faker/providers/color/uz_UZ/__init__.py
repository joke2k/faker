from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    """Implement color provider for ``uz_UZ`` locale."""

    # Source: https://uz.wiktionary.org/wiki/Vikilug%E2%80%98at:Ranglar
    all_colors = OrderedDict(
        (
            ("Akvamarin", "#7FFFD4"),
            ("Anor", "#800000"),
            ("Apelsin", "#FFA000"),
            ("Bej", "#F5F5DC"),
            ("Binafsha", "#8B00FF"),
            ("Bodom", "#FFEBCD"),
            ("Bordo rang", "#800000"),
            ("Doimiy sariq", "#FFBF00"),
            ("Hantal", "#120A8F"),
            ("Havo rang", "#000080"),
            ("Indigo", "#4B0082"),
            ("Jigar rang", "#964B00"),
            ("Kul", "#808080"),
            ("Kumush", "#C0C0C0"),
            ("Koʻk", "#0000FF"),
            ("Kremi", "#FFFDD0"),
            ("Magenta", "#FF00FF"),
            ("Malina", "#DC143C"),
            ("Marjon", "#FF7F50"),
            ("Moshrang", "#C3B091"),
            ("Oq", "#FFFFFF"),
            ("Oxra", "#CC7722"),
            ("Oltin", "#FFD700"),
            ("Pushti", "#FFC0CB"),
            ("Qizil", "#FF0000"),
            ("Qizgʻish binafsharang", "#E0B0FF"),
            ("Qora", "#000000"),
            ("Qizil-sariq", "#FF8C69"),
            ("Samoviy", "#87CEFF"),
            ("Sariq", "#FFFF00"),
            ("Siyohrang", "#660099"),
            ("Sepya", "#705714"),
            ("Siena", "#FF8247"),
            ("Suv", "#00FFFF"),
            ("Terrakota", "#E2725B"),
            ("Turkuaz", "#30D5C8"),
            ("Ultramarin", "#120A8F"),
            ("Yashil", "#00FF00"),
            ("Zumrad", "#50C878"),
        )
    )

    safe_colors = (
        "Oq",
        "Qora",
        "Yashil",
        "Ko'k",
        "Qizil",
        "Sariq",
        "Pushti",
        "Olov",
        "Qaymoq",
        "Laym",
        "Kumush",
        "Kulrang",
    )
