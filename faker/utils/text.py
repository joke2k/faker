# coding=utf-8

import re
import unicodedata


_re_pattern = re.compile('[^\w\s-]')
_re_pattern_allow_dots = re.compile('[^\.\w\s-]')
_re_spaces = re.compile('[-\s]+')


def slugify(value, allow_dots=False):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace. Modified to optionally allow dots.

    Copied from Django 1.7
    """
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = value.strip().lower()
    if allow_dots:
        value = _re_pattern_allow_dots.sub('', value)
    else:
        value = _re_pattern.sub('', value)
    return _re_spaces.sub('-', value)
