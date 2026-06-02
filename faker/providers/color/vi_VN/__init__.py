from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    """
    Implement color provider for ``vi_VN`` locale.

    #Sources: https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_m%C3%A0u
    """

    all_colors = OrderedDict(
        (
            ("Trắng Antique", "#FAEBD7"),
            ("Aquamarine", "#7FFFD4"),
            ("Azure", "#F0FFFF"),
            ("Beige", "#F5F5DC"),
            ("Đen", "#000000"),
            ("Xanh dương", "#0000FF"),
            ("Xanh tím", "#8A2BE2"),
            ("Nâu", "#A52A2A"),
            ("Sô cô la", "#D2691E"),
            ("San hô", "#FF7F50"),
            ("Xanh hải quân", "#6495ED"),
            ("Hồng đào", "#DC143C"),
            ("Xanh đậm", "#00008B"),
            ("Xanh biển đậm", "#008B8B"),
            ("Xám đậm", "#A9A9A9"),
            ("Xanh lá đậm", "#006400"),
            ("Rêu đậm", "#BDB76B"),
            ("Cam đậm", "#FF8C00"),
            ("Đỏ đậm", "#8B0000"),
            ("Xanh ngọc đậm", "#00CED1"),
            ("Tím đậm", "#9400D3"),
            ("Hồng đậm", "#FF1493"),
            ("Xám xỉn", "#696969"),
            ("Hồng fuchsia", "#FF00FF"),
            ("Vàng", "#FFD700"),
            ("Xám", "#808080"),
            ("Xanh lá cây", "#008000"),
            ("Xanh lá cây nhạt", "#ADFF2F"),
            ("Hồng sáng", "#FF69B4"),
            ("Indigo", "#4B0082"),
            ("Ngà voi", "#FFFFF0"),
            ("Rêu", "#F0E68C"),
            ("Hồng lavender", "#FFF0F5"),
            ("Xanh dương nhạt", "#ADD8E6"),
            ("Xanh biển nhạt", "#E0FFFF"),
            ("Xám sáng", "#D3D3D3"),
            ("Xanh lá cây sáng", "#90EE90"),
            ("Hồng sáng", "#FFB6C1"),
            ("Xanh biển sáng", "#87CEFA"),
            ("Vàng sáng", "#FFFFE0"),
            ("Hạt Dẻ", "#800000"),
            ("Cam", "#FFA500"),
            ("Cam đỏ", "#FF4500"),
            ("Xanh lá cây nhạt", "#98FB98"),
            ("Xanh biển nhạt", "#AFEEEE"),
            ("Hồng", "#FFC0CB"),
            ("Tím", "#DDA0DD"),
            ("Tím đậm", "#800080"),
            ("Đỏ", "#FF0000"),
            ("Xanh biển xanh", "#2E8B57"),
            ("Bạc", "#C0C0C0"),
            ("Xanh lục bảo", "#40E0D0"),
            ("Tím violet", "#EE82EE"),
            ("Trắng", "#FFFFFF"),
            ("Vàng", "#FFFF00"),
            ("Xanh lá cây vàng", "#9ACD32"),
        )
    )

    safe_colors = (
        "đen",
        "đỏ rượu",
        "xanh lá cây",
        "rêu",
        "tím",
        "xanh biển",
        "xanh chanh",
        "xanh dương",
        "bạc",
        "xám",
        "vàng",
        "hồng fuchsia",
        "trắng",
    )
