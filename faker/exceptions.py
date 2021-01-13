class BaseFakerException(Exception):
    """The base exception for all Faker exceptions."""


class UniquenessException(BaseFakerException):
    """To avoid infinite loops, after a certain number of attempts,
    the "unique" attribute of the Proxy will throw this exception.
    """
