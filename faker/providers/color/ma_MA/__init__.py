from collections import OrderedDict

from deasciiify import deasciiify

from ..en_US import Provider as ColorProvider


class Provider(ColorProvider):
    all_colors = OrderedDict((deasciiify(name), code)
                             for name, code
                             in ColorProvider.all_colors.iteritems())
