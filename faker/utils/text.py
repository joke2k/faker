import re
import unicodedata


def slugify(value, allow_dots=False):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace. Modified to optionally allow dots.

    Copied from Django 1.7
    """
    if allow_dots:
        pattern = '[^\.\w\s-]'
    else:
        pattern = '[^\w\s-]'
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(pattern, '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)
