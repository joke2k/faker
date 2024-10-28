from collections import OrderedDict

from ..de import Provider as BaseProvider


class Provider(BaseProvider):
    all_colors: OrderedDict[str, str] = OrderedDict(
        (color_name.replace("ß", "ss"), color_hexcode) for color_name, color_hexcode in BaseProvider.all_colors.items()
    )
