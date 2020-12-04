from functools import wraps
from typing import Any, Callable, Dict, Tuple

from faker.utils import text


def slugify(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> str:
        return text.slugify(fn(*args, **kwargs))
    return wrapper


def slugify_domain(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> str:
        return text.slugify(fn(*args, **kwargs), allow_dots=True)
    return wrapper


def slugify_unicode(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> str:
        return text.slugify(fn(*args, **kwargs), allow_unicode=True)
    return wrapper


def lowercase(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> str:
        return fn(*args, **kwargs).lower()
    return wrapper
