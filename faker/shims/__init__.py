try:
    from collections import Counter
except ImportError:
    from .counter import Counter
