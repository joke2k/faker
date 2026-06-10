from collections import OrderedDict
from .. import Provider as ColorProvider

class Provider(ColorProvider):
    """Implement color provider for Pashto locale."""

    all_colors = OrderedDict((
        ("شین محو", "#F0F8FF"),   # Alice Blue
        ("بېژ تیره", "#FAEBD7"),  # Antique White
        ("فیروزي", "#00FFFF"),    # Aqua
        ("آبی فیروزي", "#7FFFD4"),  # Aquamarine
        ("لاجوردي", "#F0FFFF"),   # Azure
        ("بېژ", "#F5F5DC"),       # Beige
        ("کرم", "#FFE4C4"),       # Bisque
        ("تور", "#000000"),       # Black
        ("کاهگلي", "#FFEBCD"),   # Blanched Almond
        ("آسماني", "#0000FF"),    # Blue
        ("بنفش تیره", "#8A2BE2"), # Blue Violet
        ("قهوه‌اي", "#A52A2A"),   # Brown
        ("خاکي", "#DEB887"),      # Burly Wood
        ("آبی فولادي", "#5F9EA0"), # Cadet Blue
        ("شین روشن", "#7FFF00"), # Chartreuse
        ("شوکو لاتي", "#D2691E"), # Chocolate
        ("مرجاني", "#FF7F50"),    # Coral
        ("آبی ذرتي", "#6495ED"),  # Cornflower Blue
        ("کاهي", "#FFF8DC"),      # Cornsilk
        ("زرشکي", "#DC143C"),     # Crimson
        ("فیروزي تیره", "#00CED1"), # Dark Cyan
        ("سرمه‌اي", "#00008B"),   # Dark Blue
        ("سبز کبریتي تیره", "#008B8B"), # Dark Cyan
        ("ماشي تیره", "#B8860B"), # Dark Goldenrod
        ("خاکستري تیره", "#A9A9A9"), # Dark Gray
        ("سبز تیره", "#006400"),  # Dark Green
        ("ماشي", "#BDB76B"),      # Dark Khaki
        ("بنفش تیره", "#8B008B"), # Dark Magenta
        ("زیتوني تیره", "#556B2F"), # Dark Olive Green
        ("نارنجي تیره", "#FF8C00"), # Dark Orange
        ("ارکیده بنفش", "#9932CC"), # Dark Orchid
        ("سور تیره", "#8B0000"),  # Dark Red
        ("قهوه‌اي حنايي", "#E9967A"), # Dark Salmon
        ("سبز دریایي تیره", "#8FBC8F"), # Dark Sea Green
        ("آبی دودي", "#483D8B"),  # Dark Slate Blue
        ("لجنی تیره", "#2F4F4F"), # Dark Slate Gray
        ("بنفش باز", "#9400D3"),   # Dark Violet
        ("شفقي", "#FF1493"),      # Deep Pink
        ("آبی کمرنگ", "#00BFFF"), # Deep Sky Blue
        ("دودي", "#696969"),      # Dim Gray
        ("آبی", "#1E90FF"),       # Dodger Blue
        ("شرابي", "#B22222"),     # Firebrick
        ("پوست پیازي", "#FFFAF0"), # Floral White
        ("شویدي", "#228B22"),     # Forest Green
        ("سرخابي", "#FF00FF"),    # Fuchsia
        ("خاکستري مات", "#DCDCDC"), # Gainsboro
        ("سفید بنفشه", "#F8F8FF"), # Ghost White
        ("کهربایي", "#FFD700"),   # Gold
        ("خردلي", "#DAA520"),     # Goldenrod
        ("خاکستري", "#808080"),   # Gray
        ("سبز", "#008000"),       # Green
        ("شین پستې", "#ADFF2F"),  # Green Yellow
        ("شین محو", "#F0FFF0"),   # Honeydew
        ("سرخابي روشن", "#FF69B4"), # Hot Pink
        ("جگري", "#CD5C5C"),      # Indian Red
        ("نیلي تیره", "#4B0082"), # Indigo
        ("استخواني", "#FFFFF0"),  # Ivory
        ("خاکي روشن", "#F0E68C"), # Khaki
        ("نیلي کمرنگ", "#E6E6FA"), # Lavender
        ("صورتي مات", "#FFF0F5"), # Lavender Blush
        ("شین چمني", "#7CFC00"),  # Lawn Green
        ("شیرشکري", "#FFFACD"),   # Lemon Chiffon
        ("آبی کبریتي", "#ADD8E6"), # Light Blue
        ("بېژ تیره روشن", "#F08080"), # Light Coral
        ("آبی آسماني", "#E0FFFF"), # Light Cyan
        ("لیمویي روشن", "#FAFAD2"), # Light Goldenrod Yellow
        ("خاکستري روشن", "#D3D3D3"), # Light Gray
        ("سبز روشن", "#90EE90"),  # Light Green
        ("صورتي روشن", "#FFB6C1"), # Light Pink
        ("نارنجي کرم", "#FFA07A"), # Light Salmon
        ("سبز کبریتي روشن", "#20B2AA"), # Light Sea Green
        ("آبی آسماني روشن", "#87CEFA"), # Light Sky Blue
        ("سربي", "#778899"),      # Light Slate Gray
        ("بنفش مایل به آبی", "#B0C4DE"), # Light Steel Blue
        ("شیري", "#FFFFE0"),      # Light Yellow
        ("شین روشن", "#00FF00"), # Lime
        ("سبز چمني", "#32CD32"),  # Lime Green
        ("کتانی", "#FAF0E6"),     # Linen
        ("بنفش", "#FF00FF"),      # Magenta
        ("عنابي", "#800000"),     # Maroon
        ("سبز دریایي", "#66CDAA"), # Medium Aquamarine
        ("آبی تیره", "#0000CD"),  # Medium Blue
        ("ارکیده", "#BA55D3"),    # Medium Orchid
        ("بنفش تیره متوسط", "#9370DB"), # Medium Purple
        ("خزه‌اي", "#3CB371"),    # Medium Sea Green
        ("آبی متالیک", "#7B68EE"), # Medium Slate Blue
        ("شین دریایي", "#00FA9A"), # Medium Spring Green
        ("فیروزي تیره متوسط", "#48D1CC"), # Medium Turquoise
        ("ارغواني", "#C71585"),   # Medium Violet Red
        ("آبی نفتي", "#191970"),  # Midnight Blue
        ("سفید نعناعي", "#F5FFFA"), # Mint Cream
        ("بېژ صورتي", "#FFE4E1"), # Misty Rose
        ("هلويي", "#FFE4B5"),     # Moccasin
        ("کرم تیره", "#FFDEAD"),  # Navajo White
        ("سرمه‌اي", "#000080"),   # Navy
        ("بېژ روشن", "#FDF5E6"),  # Old Lace
        ("زیتوني", "#808000"),    # Olive
        ("سبز ارتشي", "#6B8E23"), # Olive Drab
        ("نارنجي", "#FFA500"),    # Orange
        ("قرمز نارنجي", "#FF4500"), # Orange Red
        ("ارکیده روشن", "#DA70D6"), # Orchid
        ("نخودي", "#EEE8AA"),     # Pale Goldenrod
        ("سبز کمرنگ", "#98FB98"), # Pale Green
        ("فیروزي کمرنگ", "#AFEEEE"), # Pale Turquoise
        ("شرابي روشن", "#DB7093"), # Pale Violet Red
        ("هلويي روشن", "#FFEFD5"), # Papaya Whip
        ("هلويي", "#FFDAB9"),     # Peach Puff
        ("بادامي تیره", "#CD853F"), # Peru
        ("صورتي", "#FFC0CB"),     # Pink
        ("بنفش کمرنگ", "#DDA0DD"), # Plum
        ("آبی کبریتي روشن", "#B0E0E6"), # Powder Blue
        ("بنفش متوسط", "#800080"), # Purple
        ("سور", "#FF0000"),       # Red
        ("بادمجاني", "#BC8F8F"),  # Rosy Brown
        ("آبی سلطنتي", "#4169E1"), # Royal Blue
        ("کاکائويي", "#8B4513"),  # Saddle Brown
        ("سالمون روشن", "#FA8072"), # Salmon
        ("هلويي تیره", "#F4A460"), # Sandy Brown
        ("خزه‌اي تیره", "#2E8B57"), # Sea Green
        ("صدفي", "#FFF5EE"),      # Seashell
        ("قهوه‌اي متوسط", "#A0522D"), # Sienna
        ("طوسي", "#C0C0C0"),      # Silver
        ("آبی آسماني", "#87CEEB"), # Sky Blue
        ("آبی فولادي تیره", "#6A5ACD"), # Slate Blue
        ("سربي تیره", "#708090"), # Slate Gray
        ("صورتي محو", "#FFFAFA"), # Snow
        ("شین بهاري", "#00FF7F"), # Spring Green
        ("آبی فولادي", "#4682B4"), # Steel Blue
        ("برنزه", "#D2B48C"),    # Tan
        ("سبز دودي", "#008080"),  # Teal
        ("بادمجاني روشن", "#D8BFD8"), # Thistle
        ("قرمز گوجه‌اي", "#FF6347"), # Tomato
        ("فیروزي روشن", "#40E0D0"), # Turquoise
        ("بنفش روشن", "#EE82EE"), # Violet
        ("گندمي", "#F5DEB3"),     # Wheat
        ("سپین", "#FFFFFF"),      # White
        ("خاکستري محو", "#F5F5F5"), # White Smoke
        ("ژېړ", "#FFFF00"),       # Yellow
        ("شین زیتوني", "#9ACD32"), # Yellow Green
    ))

    safe_colors = (
        "تور", "عنابي", "سبز", "آسماني", "زیتوني", "بنفش", "سبز دودي", "آهکي", "آبی", "نقره‌اي", "خاکستري", "ژېړ", "ارغواني", "فیروزي", "سپین",
    )