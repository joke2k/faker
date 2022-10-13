from collections import OrderedDict

from .. import Provider as ColorProvider


class Provider(ColorProvider):
    """Implement color provider for ``tr_TR`` locale.
    Sources:
    - https://tr.wikipedia.org/wiki/Renkler_listesi
    """

    all_colors = OrderedDict(
        (
            ("Açık galibarda", "#FF77FF")
            ("Açık mavi", "#ADD8E6")
            ("Açık mor", "#E0B0FF"),
            ("Açık turkuaz", "#08E8DE"),
            ("Açık yeşil", "#66FF00"),
            ("Bakır rengi", "#B87333"),
            ("Barut rengi", "#3D2B1F"),
            ("Bebek mavisi", "#E0FFFF"),
            ("Bordo", "#800000"),
            ("Camgöbeği","#00FFFF"),
            ("Siyah", "#000000"),
            ("Beyaz", "#FFFFFF"),
            ("Sarı", "#FFFF00"),
            ("Orman yeşili", "#228B22"),
            ("Turuncu", "#FF7F00")
            ("Mavi", "#0000FF"),
            ("Kırmızı", "#FF0000")
        )
    )
    
    safe_colors = (
        "Siyah",
        "Mavi",
        "Camgöbeği",
        "Sarı",
        "Beyaz",
        "Kırmızı"
    )
