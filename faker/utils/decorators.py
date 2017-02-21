# coding=utf-8

import collections
from functools import wraps

from deasciiify import deasciiify

from faker.utils import text


def slugify(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return text.slugify(fn(*args, **kwargs))
    return wrapper


def slugify_domain(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return text.slugify(fn(*args, **kwargs), allow_dots=True)
    return wrapper


def slugify_unicode(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return text.slugify(fn(*args, **kwargs), allow_unicode=True)
    return wrapper


def martianify(*fields):
    """Returns a class decorator that "martianifies" the specified fields.

    The act of martianifying a string involves replacing the ASCII letters in
    the string with non-ASCII characters that look similar to the original
    character. This is very useful for adding non-ASCII characters to your test
    suite while maintaining the readability of the strings.

    For example, a string like "cooperative", when "martianified" looks like
    "ḉȍöᶈᶒṙẳʈḯṿę"; yet useful for testing, yet readable.

    :param fields: list of fields to be "martianified", represented as a list
        of strings. Each of these strings must be the name of a field
        containing a list of strings.
    """
    def transform(item):
        if isinstance(item, basestring):
            return deasciiify(item)
        elif isinstance(item, collections.OrderedDict):
            return collections.OrderedDict((transform(key), transform(value))
                                           for key, value in item.iteritems())
        elif isinstance(item, dict):
            return {transform(key): transform(value)
                    for key, value in item.iteritems()}
        elif isinstance(item, collections.Iterable):
            return item.__class__(transform(x) for x in item)
        else:
            return item

    def decorator(cls):
        for field in fields:
            try:
                value = getattr(cls, field)
            except AttributeError:
                raise KeyError('%s is not a field on %s' % (field,
                                                            cls.__name__))
            setattr(cls, field, transform(value))
        return cls

    return decorator
