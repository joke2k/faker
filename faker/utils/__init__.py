def is_string(var):
    try:
        return isinstance(var, basestring)
    except NameError:
        return isinstance(var, str)
