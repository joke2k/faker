from functools import wraps

from faker.utils import text


def slugify(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return text.slugify(fn(*args, **kwargs))
    return wrapper
